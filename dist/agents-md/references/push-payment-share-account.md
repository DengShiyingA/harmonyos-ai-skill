# Push, Notification, Payment, Share, and Account Kit

## Contents
- Notification Kit (notificationManager)
- Account Kit — Huawei ID login
- Configure Client ID in `module.json5`
- One-click login (enterprise developers, non-game apps)
- Huawei Account login (all developers)
- Silent login
- Common error codes
- Key concepts
- Push Kit — push notifications
- Get Push Token
- Receive push messages (module.json5)
- Payment Kit — Huawei Pay (physical goods & services)
- Share Kit — cross-app content sharing

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `Notification Kit, Push Kit, Account Kit, Huawei ID login, Payment Kit, Share Kit`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

## Notification Kit (notificationManager)

```ts
import { notificationManager } from '@kit.NotificationKit'

// 1. Create slot (call once at app init)
await notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION)

// 2. Check and request notification enable
const enabled = await notificationManager.isNotificationEnabled()
if (!enabled) await notificationManager.requestEnableNotification()  // deprecated but functional

// 3. Publish
const request: notificationManager.NotificationRequest = {
  id: 1001,
  // OMIT slotType — see API 21 type mismatch note above
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: { title: '标题', text: '正文', additionalText: '副文本' }
  },
  deliveryTime: Date.now(),
  showDeliveryTime: true,
  tapDismissed: true
}
await notificationManager.publish(request)

// 4. Cancel
await notificationManager.cancel(1001)
```


## Account Kit — Huawei ID login


### Configure Client ID in `module.json5`

```json5
{
  "module": {
    "name": "entry",
    "type": "entry",
    "metadata": [{
      "name": "client_id",
      "value": "YOUR_CLIENT_ID"  // from AGC console
    }]
  }
}
```


### One-click login (enterprise developers, non-game apps)

Retrieves phone number + UnionID in a single tap. Requires manual signing + AGC permission approval.

```ts
import { authentication } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

// Step 1: Get anonymous phone number (for display on login page)
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
authRequest.scopes = ['quickLoginAnonymousPhone'];
authRequest.state = util.generateRandomUUID();
authRequest.forceAuthorization = false;  // must be false for one-click login

const controller = new authentication.AuthenticationController();
const response = await controller.executeRequest(authRequest);
const anonymousPhone = response.data?.extraInfo?.quickLoginAnonymousPhone as string;
// Display anonymousPhone on login page, e.g. "188****1234"
```

```ts
// Step 2: Show LoginWithHuaweiIDButton — user taps to get Authorization Code
import { loginComponentManager, LoginWithHuaweiIDButton } from '@kit.AccountKit';

LoginWithHuaweiIDButton({
  params: {
    style: loginComponentManager.Style.BUTTON_RED,
    borderRadius: 24,
    loginType: loginComponentManager.LoginType.QUICK_LOGIN,  // one-click login
    supportDarkMode: true
  },
  controller: this.controller  // LoginWithHuaweiIDButtonController
})

// In controller callback: response.authorizationCode → send to server
// Server calls /oauth2/v6/quickLogin/getPhoneNumber to get full phone + UnionID
```

**Obfuscation whitelist** — if property obfuscation is enabled, add to `obfuscation-rules.txt`:
```
-keep-property-name
quickLoginAnonymousPhone
```


### Huawei Account login (all developers)

Retrieves UnionID/OpenID via `LoginWithHuaweiIDButton` or API. Supports enterprise + individual developers.

```ts
// Using LoginWithHuaweiIDButton component (recommended)
LoginWithHuaweiIDButton({
  params: {
    style: loginComponentManager.Style.BUTTON_RED,
    borderRadius: 24,
    loginType: loginComponentManager.LoginType.ID,  // standard login
    supportDarkMode: true
  },
  controller: this.controller
})
// callback returns authorizationCode → server exchanges for UnionID/OpenID
```

```ts
// Using custom button with API
import { authentication } from '@kit.AccountKit';

const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
loginRequest.forceLogin = true;  // true = show login page if not logged in
loginRequest.state = util.generateRandomUUID();

const controller = new authentication.AuthenticationController(getContext(this));
const response = await controller.executeRequest(loginRequest);
const authCode = response.data?.authorizationCode;
// Send authCode to server → server gets UnionID/OpenID via Access Token
```


### Silent login

No user interaction — retrieves UnionID for returning users (reinstall, device switch).

```ts
const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
loginRequest.forceLogin = false;  // false = silent, no UI if not logged in
loginRequest.state = util.generateRandomUUID();

const controller = new authentication.AuthenticationController();
const response = await controller.executeRequest(loginRequest);
const authCode = response.data?.authorizationCode;
// If error.code === 1001502001 → user not logged in, show other login methods
```


### Common error codes

| Code | Meaning | Action |
|---|---|---|
| `1001502001` | Huawei Account not logged in | Show other login methods |
| `1001502005` | Network error | Retry or show other methods |
| `1001502012` | User cancelled | No action needed |
| `1001500001` | Certificate fingerprint check failed | Check signing config |
| `1001502014` | Missing scopes/permissions | Check AGC permission approval |
| `1005300001` | User did not agree to protocol | Show agreement dialog |


### Key concepts

| ID type | Scope | Use case |
|---|---|---|
| **OpenID** | Per-app unique | Identify user within one app |
| **UnionID** | Per-developer unique | Identify user across multiple apps by same developer |
| **GroupUnionID** | Per-account-group unique | Identify user across affiliated developers |

For cross-platform user data continuity, prefer **UnionID** over OpenID.


## Push Kit — push notifications


### Get Push Token

Call in `onCreate()` of your UIAbility. Token identifies device+app for push messages.

```ts
import { pushService } from '@kit.PushKit';

// In EntryAbility.onCreate()
pushService.getToken().then((token: string) => {
  console.info('Push token:', token);
  // Upload token to your app server for sending push messages
}).catch((err: BusinessError) => {
  console.error('Failed to get push token:', err.code, err.message);
});
```

**Prerequisites**: Enable Push Service in AGC console first, otherwise `getToken()` returns error 1000900010.

Token changes on: app reinstall, factory reset, `deleteToken()` + re-`getToken()`. Always call `getToken()` on each app launch to keep server-side token fresh.


### Receive push messages (module.json5)

Configure a UIAbility with `action.ohos.push.listener` to receive token updates and push data:

```json5
"skills": [{ "actions": ["action.ohos.push.listener"] }]
```

Push Kit supports: notification messages, voice broadcast, card refresh, background messages, live view, in-app call messages.


## Payment Kit — Huawei Pay (physical goods & services)

For physical goods/services only (hotels, rides, bills). Virtual goods use IAP Kit instead.

```ts
import { paymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

// orderStr is built by your server after calling Huawei Pay pre-order API
// Contains: app_id, merc_no, prepay_id, timestamp, noncestr, sign
const orderStr = '{"app_id":"...","merc_no":"...","prepay_id":"...","timestamp":"...","noncestr":"...","sign":"..."}';

const context = getContext(this) as common.UIAbilityContext;
paymentService.requestPayment(context, orderStr)
  .then(() => { console.info('Payment succeeded'); })
  .catch((err: BusinessError) => { console.error('Payment failed:', err.code, err.message); });
```

Server flow: your server calls `/api/v2/aggr/preorder/create/app` → gets `prepayId` → builds signed `orderStr` → returns to client.

Supports: Phone, Tablet, PC/2in1. China mainland only.


## Share Kit — cross-app content sharing

```ts
import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

// Share a hyperlink
const shareData = new systemShare.SharedData({
  utd: uniformTypeDescriptor.UniformDataType.HYPERLINK,
  content: 'https://example.com/article/123',
  title: 'Article Title',
  description: 'Article preview text',
});
const controller = new systemShare.ShareController(shareData);
controller.show(this.context, {
  previewMode: systemShare.SharePreviewMode.DEFAULT,
  selectionMode: systemShare.SelectionMode.SINGLE,
});
```

Supported UTD types: `HYPERLINK`, `PLAIN_TEXT`, `HTML`, `IMAGE` (pass `uri` from file), `FILE`.

# Forms, Service Cards, Atomic Services, and Distributed Features

## Contents
- Atomic Services / Meta-Services (原子化服务 / 元服务)
- Distributed features
- Form Kit — ArkTS service cards (服务卡片)
- FormExtensionAbility lifecycle
- Card UI (`EntryFormAbility/pages/Card.ets`)
- `module.json5` — declare the form
- `resources/base/profile/form_config.json`

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `Atomic Service, Meta Service, Form Kit, service card, FormExtensionAbility, distributed capability`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

## Atomic Services / Meta-Services (原子化服务 / 元服务)

Installation-free, small (≤10MB) apps launched from:
- Service cards (home-screen widgets built with `FormExtensionAbility`)
- Search, scan, NFC, cross-device continuation

Configured via `module.json5` with `"installationFree": true`. Build-time they produce `.app` packages containing multiple HAPs.


## Distributed features

- **Cross-device continuation** (流转) — `continueAbility` / `onContinue`/`onNewWant` lifecycle
- **Distributed data object** — synced state across devices
- **Distributed file system** — shared sandbox
- **Device manager** — discover trusted devices


## Form Kit — ArkTS service cards (服务卡片)

Service cards run in a sandboxed FormExtensionAbility process; they use a subset of ArkUI.


### FormExtensionAbility lifecycle

```ts
// entry/src/main/ets/formextensionability/EntryFormAbility.ets
import { FormExtensionAbility, formBindingData, FormInfo, formProvider } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class EntryFormAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    // Called when user adds card to home screen
    const formData = { title: 'Hello', count: 0 };
    return formBindingData.createFormBindingData(formData);
  }

  onCastToNormalForm(formId: string) { }

  onUpdateForm(formId: string) {
    // Periodic/requested update
    const data = formBindingData.createFormBindingData({ count: Date.now() });
    formProvider.updateForm(formId, data);
  }

  onRemoveForm(formId: string) { }

  onFormEvent(formId: string, message: string) {
    // Triggered by postCardAction in the card UI
    console.log('card event:', formId, message);
  }
}
```


### Card UI (`EntryFormAbility/pages/Card.ets`)

```ts
// Cards are ArkUI components but with restricted APIs (no @State mutation from events)
// Use postCardAction to route events back to FormExtensionAbility
@Entry
@Component
struct CardPage {
  @LocalStorageProp('title') title: string = '';
  @LocalStorageProp('count') count: number = 0;

  build() {
    Column({ space: 8 }) {
      Text(this.title).fontSize(16).fontWeight(FontWeight.Bold)
      Text(`Count: ${this.count}`).fontSize(14)
      Button('+1')
        .onClick(() => {
          postCardAction(this, {
            action: 'message',
            params: { event: 'increment' }
          });
        })
    }.padding(12)
  }
}
```


### `module.json5` — declare the form

```json5
{
  "extensionAbilities": [{
    "name": "EntryFormAbility",
    "srcEntry": "./ets/formextensionability/EntryFormAbility.ets",
    "type": "form",
    "metadata": [{
      "name": "ohos.extension.form",
      "resource": "$profile:form_config"
    }]
  }]
}
```


### `resources/base/profile/form_config.json`

```json
{
  "forms": [{
    "name": "widget",
    "displayName": "$string:widget_display_name",
    "description": "$string:widget_desc",
    "src": "./ets/formextensionability/pages/Card.ets",
    "uiSyntax": "arkts",
    "window": { "designWidth": 720, "autoDesignWidth": true },
    "colorMode": "auto",
    "isDynamic": true,
    "updateEnabled": true,
    "scheduledUpdateTime": "10:30",
    "updateDuration": 1,
    "defaultDimension": "2*2",
    "supportDimensions": ["1*2", "2*2", "2*4"]
  }]
}
```

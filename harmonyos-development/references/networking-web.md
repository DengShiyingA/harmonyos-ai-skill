# Networking, ArkWeb, and Background Transfers

## Contents
- HTTP request example
- Network connectivity monitoring
- WebSocket
- ArkWeb — Web component
- JS ↔ ArkTS bridge (`javaScriptProxy`)
- Custom User-Agent and cookies
- Intercept resource requests
- Background upload & download (request.agent)
- Background upload (supports pause/resume)
- Background download (auto breakpoint resume)

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `HTTP request, WebSocket, Network Kit, connectivity, ArkWeb, Web component, javaScriptProxy, cookies, request.agent upload download`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

### HTTP request example

```ts
import { http } from '@kit.NetworkKit';

async function fetchJson(url: string): Promise<string> {
  const req = http.createHttp();
  try {
    const res = await req.request(url, {
      method: http.RequestMethod.GET,
      header: { 'Content-Type': 'application/json' },
      connectTimeout: 5000, readTimeout: 10000
    });
    return res.result as string;
  } finally {
    req.destroy();
  }
}
```


### Network connectivity monitoring

```ts
import { connection } from '@kit.NetworkKit';

// Check current network state
const hasNet = connection.hasDefaultNetSync();

// Monitor network changes
const netCon = connection.createNetConnection();
netCon.on('netAvailable', () => { /* network restored */ });
netCon.on('netLost', () => { /* network lost */ });
netCon.on('netCapabilitiesChange', (info: connection.NetCapabilityInfo) => {
  const isWifi = info.netCap.bearerTypes.includes(connection.NetBearType.BEARER_WIFI);
  const isCellular = info.netCap.bearerTypes.includes(connection.NetBearType.BEARER_CELLULAR);
});
netCon.register(() => {});  // activate subscriptions

// Cleanup
netCon.unregister(() => {});
```


### WebSocket

```ts
import { webSocket } from '@kit.NetworkKit';

const ws = webSocket.createWebSocket();
ws.on('open', () => { ws.send('hello'); });
ws.on('message', (err, data: string | ArrayBuffer) => {
  console.info('received:', typeof data === 'string' ? data : 'binary');
});
ws.on('close', (err, { code, reason }) => { /* closed */ });
ws.on('error', (err) => { /* handle */ });

ws.connect('wss://example.com/ws', { header: { 'Authorization': 'Bearer xxx' } });

// Send
ws.send(JSON.stringify({ type: 'chat', text: 'hi' }));

// Close
ws.close();
```


## ArkWeb — Web component

Embed web content in ArkTS via the `Web` component from `@kit.ArkWeb`.

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct BrowserPage {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'https://example.com', controller: this.controller })
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .fileAccess(true)
        .onPageBegin((event) => { console.log('loading:', event?.url); })
        .onPageEnd((event) => { console.log('loaded:', event?.url); })
        .onErrorReceive((event) => { console.error('web error:', event?.error.getErrorInfo()); })
        .darkMode(WebDarkMode.Auto)   // follow system dark mode
        .forceDarkAccess(true)
    }
  }
}
```


### JS ↔ ArkTS bridge (`javaScriptProxy`)

```ts
// Register ArkTS object callable from JS
Web({ src: 'https://example.com', controller: this.controller })
  .javaScriptProxy({
    object: {
      callNative: (msg: string) => {
        console.log('from JS:', msg);
        return 'ArkTS received: ' + msg;
      }
    },
    name: 'NativeBridge',
    methodList: ['callNative'],
    controller: this.controller
  })
// In the web page: window.NativeBridge.callNative('hello');

// Call JS from ArkTS
this.controller.runJavaScript('window.updateUI("data")', (err, result) => {
  console.log('JS result:', result);
});
```


### Custom User-Agent and cookies

```ts
// Append to default UA
webview.WebviewController.setCustomUserAgent(
  webview.WebviewController.getDefaultUserAgent() + ' MyApp/1.0'
);

// Manage cookies
import { webCookie } from '@kit.ArkWeb';
webCookie.setCookie('https://example.com', 'token=abc; path=/');
webCookie.saveCookieAsync();   // persist to disk
```


### Intercept resource requests

```ts
Web({ src: '...', controller: this.controller })
  .onInterceptRequest((event) => {
    if (event?.request.getRequestUrl().includes('/api/')) {
      // Return custom response
      const resp = new WebResourceResponse();
      resp.setResponseData('{"intercepted":true}');
      resp.setResponseMimeType('application/json');
      resp.setResponseEncoding('utf-8');
      resp.setResponseCode(200);
      resp.setReasonMessage('OK');
      return resp;
    }
    return null;  // null = load normally
  })
```


## Background upload & download (request.agent)

```ts
import { request } from '@kit.BasicServicesKit';
```


### Background upload (supports pause/resume)

```ts
const config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'https://example.com/upload',
  mode: request.agent.Mode.BACKGROUND,
  method: 'POST',
  data: formItems,                       // Array of FormItem
};
const task = await request.agent.create(context, config);
task.on('progress', (progress) => { /* track */ });
task.on('completed', (progress) => { /* done */ });
await task.start();
await task.pause();    // pause
await task.resume();   // resume with breakpoint
```


### Background download (auto breakpoint resume)

```ts
const config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'https://example.com/file.zip',
  mode: request.agent.Mode.BACKGROUND,
  saveas: `./downloads/file.zip`,
  overwrite: true,
  gauge: true,
};
const task = await request.agent.create(context, config);
task.on('progress', (progress) => { /* track */ });
await task.start();
```

# Data Storage, Resources, and File Access

## Contents
- File/document picker
- relationalStore (SQLite)
- preferences (key-value settings)
- Resource access — `$r()` and `$rawfile()`
- Resource directory structure
- Accessing resources
- Programmatic access via ResourceManager
- Application file paths (Context properties)
- fileIo — application file read/write
- Read file from Picker URI
- Cross-module resource access (跨模块资源访问)
- Access HAR resources (same as local)
- Access HSP resources (prefix with module name)

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `relationalStore, preferences, fileIo, ResourceManager, rawfile, picker, application sandbox, HAR resources, HSP resources`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

### File/document picker

```ts
import { picker } from '@kit.CoreFileKit';

// Pick document files (PDF, DOCX, etc.)
const documentPicker = new picker.DocumentViewPicker(context);
const result = await documentPicker.select({
  maxSelectNumber: 5,
  fileSuffixFilters: ['.pdf', '.docx', '.xlsx'],  // optional filter
});
const uris: string[] = result;  // file URIs with temporary read permission

// Save file to user-chosen location
const savePicker = new picker.DocumentViewPicker(context);
const saveResult = await savePicker.save({
  newFileNames: ['export.pdf'],
});
const destUri: string = saveResult[0];
```


## relationalStore (SQLite)

```ts
import { relationalStore } from '@kit.ArkData'
import { common } from '@kit.AbilityKit'

// Init (call in aboutToAppear / UIAbility.onCreate)
const store = await relationalStore.getRdbStore(ctx, {
  name: 'my_db.db',
  securityLevel: relationalStore.SecurityLevel.S1
})
await store.executeSql('CREATE TABLE IF NOT EXISTS records (...)')

// Insert
const values: relationalStore.ValuesBucket = { id: '1', title: 'Hello' }
await store.insert('records', values)

// Query (ordered)
const predicates = new relationalStore.RdbPredicates('records')
predicates.orderByDesc('timestamp')
const rs = await store.query(predicates, ['id', 'title', 'timestamp'])
while (rs.goToNextRow()) {
  const id = rs.getString(rs.getColumnIndex('id'))
}
rs.close()

// Update
const predicates2 = new relationalStore.RdbPredicates('records')
predicates2.equalTo('id', '1')
await store.update({ title: 'Updated' }, predicates2)

// Delete
const predicates3 = new relationalStore.RdbPredicates('records')
predicates3.equalTo('id', '1')
await store.delete(predicates3)
```


## preferences (key-value settings)

```ts
import { preferences } from '@kit.ArkData'

const store = await preferences.getPreferences(ctx, 'user_settings')
// Read (with default)
const val = (await store.get('sort_order', 'time_desc')) as string
// Write + flush
await store.put('sort_order', 'time_asc')
await store.flush()
```


## Resource access — `$r()` and `$rawfile()`


### Resource directory structure

```
resources/
├─ base/                    # default resources (always matched)
│  ├─ element/              # string.json, color.json, float.json, etc.
│  ├─ media/                # images, audio, video
│  └─ profile/              # custom JSON config files
├─ zh_CN/element/           # Chinese locale override
├─ en_US/element/           # English locale override
├─ dark/element/            # dark mode override
├─ rawfile/                 # raw files (not compiled, accessed by path)
└─ resfile/                 # installed to sandbox, read-only access
```

Qualifier order: MCC_MNC → language_script_region → orientation → device → colorMode → density.


### Accessing resources

```ts
// App resources: $r('app.type.name')
Text($r('app.string.hello_world'))
  .fontSize($r('app.float.text_size_body'))
  .fontColor($r('app.color.primary'))
Image($r('app.media.app_icon'))

// With format args: $r('app.string.greeting', 'Alice', 5)
// For string "Hello, %1$s! You have %2$d messages."
Text($r('app.string.greeting', 'Alice', 5))

// Plural: $r('app.plural.item_count', count, count)
Text($r('app.plural.item_count', 2, 2))  // "2 items"

// Raw files: $rawfile('path/relative/to/rawfile/')
Image($rawfile('images/banner.png'))

// System resources: $r('sys.type.name')
Text('Hello')
  .fontColor($r('sys.color.ohos_id_color_emphasize'))
  .fontSize($r('sys.float.ohos_id_text_size_headline1'))

// Cross-HSP module resources: $r('[moduleName].type.name')
Text($r('[library].string.shared_text'))
```


### Programmatic access via ResourceManager

```ts
const resMgr = getContext(this).resourceManager;
const str = resMgr.getStringByNameSync('hello_world');
const rawFd = resMgr.getRawFd('data.json');  // returns {fd, offset, length}
```


### Application file paths (Context properties)

| Context property | Path | Purpose |
|---|---|---|
| `filesDir` | `base/files/` | Persistent app data (survives app updates) |
| `cacheDir` | `base/cache/` | Cache (system may auto-clean when space low) |
| `tempDir` | `base/temp/` | Temp files (cleaned on app exit) |
| `databaseDir` | `database/` | Database files (relationalStore, etc.) |
| `preferencesDir` | `base/preferences/` | Preferences KV store |
| `bundleCodeDir` | `bundle/` | Installed HAP resources (read-only) |
| `distributedFilesDir` | `distributedfiles/` | Cross-device shared files |


## fileIo — application file read/write

Core file operations via `@kit.CoreFileKit`. All paths should come from Context properties (filesDir, cacheDir, etc.).

```ts
import { fileIo as fs } from '@kit.CoreFileKit';

const context = getContext(this);

// Write a file
const filePath = context.filesDir + '/data.json';
const file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
fs.writeSync(file.fd, JSON.stringify({ key: 'value' }));
fs.closeSync(file);

// Read a file
const readFile = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
const buf = new ArrayBuffer(4096);
const readLen = fs.readSync(readFile.fd, buf);
const content = String.fromCharCode(...new Uint8Array(buf.slice(0, readLen)));
fs.closeSync(readFile);

// Check existence
const exists = fs.accessSync(filePath);

// List directory
const entries = fs.listFileSync(context.filesDir);

// Copy file
fs.copyFileSync(filePath, context.cacheDir + '/data_backup.json');

// Delete file
fs.unlinkSync(filePath);

// Stat file (size, mtime)
const stat = fs.statSync(filePath);
console.info(`size: ${stat.size}, mtime: ${stat.mtime}`);
```


### Read file from Picker URI

```ts
// After picker returns a URI (temporary read-only permission)
const file = fs.openSync(uri, fs.OpenMode.READ_ONLY);
const buf = new ArrayBuffer(4096);
const len = fs.readSync(file.fd, buf);
fs.closeSync(file);
```


## Cross-module resource access (跨模块资源访问)


### Access HAR resources (same as local)

```ts
Text($r('app.string.string_in_har'))
Image($r('app.media.image_in_har'))
// Better performance with .id for resourceManager:
this.context.resourceManager.getStringSync($r('app.string.string_in_har').id);
```


### Access HSP resources (prefix with module name)

```ts
Text($r('[hsp1].string.string_in_hsp'))
Image($r('[hsp1].media.image_in_hsp'))
```

Or via `createModuleContext`:

```ts
import { common } from '@kit.AbilityKit';
const hspContext = await common.application.createModuleContext(this.context, 'hsp1');
const str = hspContext.resourceManager.getStringByNameSync('string_in_hsp');
```

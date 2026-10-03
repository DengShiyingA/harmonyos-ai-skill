# Official References and Sample Projects

## Contents
- Key references
- Official sample projects (GitCode)
- Audio & Video
- Camera & Image
- UI Components & Layout
- App Architecture & Navigation
- Data & Storage
- Network & Communication
- Security & Auth
- AI & ML
- Multi-Device & Wearable
- Concurrency & Performance
- System & Platform
- Graphics & 3D
- Web & Hybrid

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `HarmonyOS samples, GitCode sample project, official sample code, Huawei developer sample catalog`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

## Key references

- Official docs: https://developer.huawei.com/consumer/cn/doc/
- Best practices: https://developer.huawei.com/consumer/cn/best-practices
- Samples: https://developer.huawei.com/consumer/cn/samples/
- Codelabs: https://developer.huawei.com/consumer/cn/codelabsPortal/serviceTypes
- ArkTS guide: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts
- ArkUI guide: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui
- State management: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview
- Navigation: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-set-navigation-routing
- Concurrency: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-concurrency
- SDK / Kits: https://developer.huawei.com/consumer/cn/sdk
- OHPM registry: https://developer.huawei.com/consumer/cn/deveco-service
- DevEco Studio: https://developer.huawei.com/consumer/cn/deveco-studio/
- Symbol icons: https://developer.huawei.com/consumer/cn/design/harmonyos-symbol
- AppGallery Connect: https://developer.huawei.com/consumer/cn/agconnect
- StateStore: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-global-state-management-state-store
- GitCode samples: https://gitcode.com/HarmonyOS_Samples


## Official sample projects (GitCode)

430+ open-source HarmonyOS samples at `https://gitcode.com/HarmonyOS_Samples/<name>`. Key projects by category:


### Audio & Video
- **AVCodecVideo** — Video playback/recording via AVCodec (H.264/H.265, AudioVivid)
- **AdaptiveVideo** — Short video immersive & rotation playback
- **AudioCast** — Audio casting to external devices
- **AudioToVideoSync** — Audio-video synchronization
- **DecodePlayControl** — Surface-mode video playback control
- **PlayShortVideosBasedOnVideoComponent** — Short video player (progress bar, fullscreen, speed, autoplay)
- **SmoothSwitchShortVideos** — Smooth short video switching with preloading
- **MusicHome** — Adaptive music album app (one-time dev, multi-device)
- **MusicCard** — Music service widget via Form Kit
- **NetAdaptiveVideoStream** — Adaptive bitrate video streaming
- **HMOS_LiveStream** — Live streaming (broadcaster + viewer)
- **UseAVTranscoderVideo** — Video transcoding
- **SwipePlayer** — Swipe-to-switch video player
- **VideoCast** — Video casting to external devices


### Camera & Image
- **CustomCamera** — Camera Kit: preview, flash, focus, exposure, front/back switch
- **ImageGetAndSave** — Image acquisition and saving
- **PicturePreview** — Image preview with zoom and swipe
- **PixelMapImageEdit** — Image editing via PixelMap encode/decode
- **SmartPhotoPicker** — Photo recommendation via PhotoPicker
- **MultiPictureBeautification** — Multi-device image beautification
- **LongSnapshotPractice** — Long screenshot implementation
- **MultipleImage** — Multi-image carousel with Swiper
- **ImageToVideo** — Compositing images into video
- **CoreVisionKitOCR** — OCR-based text auto-fill


### UI Components & Layout
- **CommonListFlows** — Common list scenarios with List component
- **ListScrollComponent** — Scrollable list with lazy loading
- **GridScrollComponent** — Grid scroll with performance optimization
- **WaterFlowScrollComponent** — Waterfall flow layout
- **SwiperPerformance** — Swiper performance optimization
- **ComponentEncapsulation** — Component encapsulation patterns
- **CommentReply** — Comment reply with RichEditor (text, emoji, @mention)
- **DialogHub** — Universal dialog library
- **CustomizeKeyboard** — Custom keyboard implementation
- **DragFramework** — Drag-and-drop for images, rich text, lists
- **TextExpand** — Expandable/collapsible text
- **PureTabs** — Tab-based navigation UI
- **FoldedHover** — Foldable device hover mode
- **CardInfoRefresh** — Service widget creation, interaction & refresh (Form Kit)
- **PageFlip** — Page turning effects
- **ResponsiveLayout** — Responsive layout for multiple device types
- **Immersive** — Immersive full-screen UI


### App Architecture & Navigation
- **AppLifecycleManagement** — App lifecycle state management
- **AppStartUp** — Startup task initialization (AppStartup)
- **StageModelContext** — Stage model context usage
- **HMRouter** — HMRouter-based page navigation
- **NavigationSettings** — Settings app with Navigation (small/large window)
- **JumpBetweenApps** — App-to-app jumping via App Linking
- **CrossModuleReference** — Native HAR/HSP module cross-reference
- **CrossModuleResourceAccess** — Cross-module resource access ($r, resourceManager)
- **DynamicComponent** — Dynamic component creation
- **DesktopShortcut** — Desktop shortcut entry via module.json5
- **EmebedAbility** — Embedded atomic service via FullScreenLaunchComponent


### Data & Storage
- **KVStore** — Key-value database read/write
- **DatabaseReadWrite** — Relational database via C-API
- **DataCache** — Cold start acceleration with data caching
- **BackupRestore** — Data migration via backup/restore framework
- **GenerateSandboxFile** — Sandbox file generation
- **NativeFileIO** — Native-side file read/write
- **NativeFileAccess** — Native-side file access
- **TurboTransJSON** — High-performance JSON serialization (turbo_trans)


### Network & Communication
- **NetworkReconnection** — App network reconnection
- **NetBoost** — Multi-network concurrency for acceleration
- **RcpFileTransfer** — File upload/download via Remote Communication Kit
- **RemoteCommunicationPlatform** — RCP network requests (forms, certificates, DNS)
- **WebCrossDomain** — Web cross-domain via ArkWeb interceptor & cookies
- **MultiWeb** — Responsive multi-Web layout
- **OnlineEditorCollaboration** — Online document editing with cross-device collaboration


### Security & Auth
- **UserAuth** — Face/fingerprint auth + password vault auto-fill
- **PermissionApplication** — Permission request flow
- **AntiPeep** — Sensitive information anti-peep protection
- **UniversalKeystoreCollection** — HUKS key management (encrypt/decrypt, sign/verify)
- **DigitalShield** — Biometric authentication for transactions
- **DeviceSecurityKit_sampleCode_SafetyDetectDemo_ArkTS** — Device environment & URL safety detection


### AI & ML
- **MindSporeLiteArkTS** — On-device image classification (MindSpore Lite ArkTS API)
- **MindSporeLiteCpp** — On-device image classification (MindSpore Lite C++ API)
- **MSLiteHumanSegmentation** — On-device human segmentation
- **MSLiteSceneRecognition** — On-device scene detection
- **MSLiteStyleTransform** — On-device image style transfer
- **RAG_QA** — RAG-based Q&A with on-device knowledge processing


### Multi-Device & Wearable
- **MultiDeviceCamera** — Camera on phone, foldable, tablet with preview rotation
- **MultiDeviceCommunication** — One-time dev, multi-device IM app
- **Phone_Connection** — Phone-watch communication & heart rate monitoring
- **SmartWatchCarControl** — Watch car control app
- **SmartWatchMap** — Watch map app
- **SmartWatchTakeTaxi** — Watch taxi app
- **WearableBus** — Watch bus transit app
- **WearableMusic** — Watch music app
- **APILevelAdapt** — Multi-API version compatibility (ArkTS + Native)


### Concurrency & Performance
- **UseTaskPool** — Multi-threaded tasks via TaskPool
- **UseSendable** — Sendable cross-thread communication & UI refresh
- **MultiThreadIO** — Database & file I/O with TaskPool + @Sendable
- **NativeSubMainThreadCommunication** — Native sub-thread to UI main-thread communication
- **FunctionFlowRuntimeKit-SampleCode-ConcurrentQueue** — FFRT concurrent queue
- **FunctionFlowRuntimeKit-SampleCode-TaskGraph** — FFRT task graph dependencies
- **UtilizeHWCEfficiently** — Low-power HWC composition


### System & Platform
- **BackTaskImplement** — Background tasks for app continuity
- **LiveViewLockScreen** — Lock screen live view
- **IntentsKitGameRevisit** — Intent-based game revisit recommendations
- **ContinuePublish** — Cross-device content publishing (app continuation)
- **HiTraceMeterPrefTag** — Performance tracing with HiTraceMeter
- **ObtainingDeviceID** — Device identifier retrieval
- **BluetoothLowEnergy** — BLE device connection & communication
- **NFCTag** — NFC-based app launch
- **QueryAppPackageInfo** — App package info query
- **SystemEnvVarSubscriber** — System environment variable subscription
- **DesktopExtensionKit-samplecode** — Status bar integration via Desktop Extension Kit


### Graphics & 3D
- **Graphics3D** — 3D engine API usage
- **DocsSample_XComponent** — XComponent self-rendering & AI analysis
- **DocsSample_Graphics** — Graphics subsystem samples


### Web & Hybrid
- **H5Launch** — H5 cold start acceleration
- **ExecutingJSWithJSVM** — JSVM-API: create engines, execute JS, destroy
- **DocsSample_ArkWeb** — ArkWeb component samples
- **SmallWindowScene** — Small window (floating) scenario

> Full catalog: `https://gitcode.com/HarmonyOS_Samples` — clone any sample with `git clone https://gitcode.com/HarmonyOS_Samples/<name>.git`

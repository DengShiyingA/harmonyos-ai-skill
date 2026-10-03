# Media, Camera, Audio, Image, Scan, and Vision Kits

## Contents
- Photo/video picker (correct API — `picker.PhotoViewPicker` is deprecated)
- CoreSpeechKit — ASR audio format requirements
- Camera Kit
- CameraPicker — no-permission photo/video capture
- Full camera session (preview + photo capture)
- XComponent for camera preview
- Audio Kit — playback & recording
- AudioRenderer (ArkTS) — PCM playback
- Audio focus (InterruptEvent)
- StreamUsage → volume type mapping
- AudioSession — custom focus strategy
- Background playback requirements
- Scan Kit — barcode scanning & generation
- Default UI scan (no camera permission needed)
- Image decode (detect barcode in photo)
- Custom UI scan (requires `ohos.permission.CAMERA`)
- Barcode generation
- AVSession Kit — media playback control (required for background audio)
- Create and activate session
- Background playback requirements
- Unsupported commands
- Core Vision Kit — OCR, face detection, subject segmentation
- Text recognition (OCR)
- Face detection
- Subject segmentation
- AVPlayer — unified audio/video playback
- AVPlayer with video surface (XComponent)
- AVPlayer controls
- AVRecorder — audio/video recording
- Image Kit — decode, transform, encode
- Decode image to PixelMap
- PixelMap transforms
- Encode PixelMap to file
- Release resources

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `Camera Kit, CameraPicker, Audio Kit, AVPlayer, AVSession, Image Kit, PixelMap, Scan Kit, Core Vision Kit, CoreSpeechKit`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

### Photo/video picker (correct API — `picker.PhotoViewPicker` is deprecated)

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';

const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
const picker = new photoAccessHelper.PhotoViewPicker();
const result = await picker.select({
  MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
  maxSelectNumber: 9
});
const uris: string[] = result.photoUris;
```


### CoreSpeechKit — ASR audio format requirements

```ts
import { speechRecognizer } from '@kit.CoreSpeechKit';

const engine = await speechRecognizer.createEngine({
  language: 'zh-CN',
  online: 0   // 0=on-device, 1=cloud
});
// Audio MUST be: PCM, 16kHz, mono, 16-bit
// Chunk size: 640 or 1280 bytes, write every 20ms or 40ms
engine.startListening({
  sessionId: `asr_${Date.now()}`,
  audioInfo: {
    audioType: 'pcm',
    sampleRate: 16000,
    soundChannel: 1,
    sampleBit: 16
  }
});
```


## Camera Kit


### CameraPicker — no-permission photo/video capture

Simplest way to capture a photo or video — launches the system camera UI. **No camera permission required.**

```ts
import { camera, cameraPicker as picker } from '@kit.CameraKit';
import { fileIo, fileUri } from '@kit.CoreFileKit';

// Create a temp file to receive the capture result
const pathDir = getContext(this).filesDir;
const filePath = pathDir + `/${Date.now()}.tmp`;
fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE);

const pickerProfile: picker.PickerProfile = {
  cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK,
  saveUri: fileUri.getUriFromPath(filePath)   // omit to save to media library
};

// Launch system camera — user takes photo/video and confirms
const result = await picker.pick(
  getContext(this),
  [picker.PickerMediaType.PHOTO, picker.PickerMediaType.VIDEO],
  pickerProfile
);

if (result.resultCode === 0) {
  const uri = result.resultUri;               // file URI of captured media
  const isPhoto = result.mediaType === picker.PickerMediaType.PHOTO;
}
```


### Full camera session (preview + photo capture)

Requires `ohos.permission.CAMERA`. Flow: CameraManager → CameraInput → Session → PreviewOutput/PhotoOutput.

```ts
import { camera } from '@kit.CameraKit';

// 1. Get camera manager and device
const cameraManager = camera.getCameraManager(context);
const cameras = cameraManager.getSupportedCameras();
const cameraDevice = cameras[0];

// 2. Create input and open
const cameraInput = cameraManager.createCameraInput(cameraDevice);
await cameraInput.open();

// 3. Get output capabilities
const capability = cameraManager.getSupportedOutputCapability(
  cameraDevice, camera.SceneMode.NORMAL_PHOTO
);

// 4. Create preview output (surfaceId from XComponent)
const previewOutput = cameraManager.createPreviewOutput(
  capability.previewProfiles[0], surfaceId
);

// 5. Create photo output
const photoOutput = cameraManager.createPhotoOutput(capability.photoProfiles[0]);

// 6. Build and start session
const session = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
session.beginConfig();
session.addInput(cameraInput);
session.addOutput(previewOutput);
session.addOutput(photoOutput);
await session.commitConfig();
await session.start();

// 7. Capture photo
photoOutput.on('photoAvailable', (err, photo) => {
  const imageObj = photo.main;
  imageObj.getComponent(image.ComponentType.JPEG, (err, component) => {
    const buffer: ArrayBuffer = component.byteBuffer!;
    // Save buffer to file, then release
    imageObj.release();
  });
});
photoOutput.capture({ quality: camera.QualityLevel.QUALITY_LEVEL_HIGH });

// 8. Cleanup: session.stop() → cameraInput.close() → previewOutput.release() → session.release()
```


### XComponent for camera preview

```ts
@Entry @Component
struct CameraPreview {
  private ctrl = new XComponentController();
  private surfaceId = '';

  build() {
    XComponent({ type: XComponentType.SURFACE, controller: this.ctrl })
      .onLoad(() => {
        this.surfaceId = this.ctrl.getXComponentSurfaceId();
        // Use this.surfaceId to create previewOutput
      })
      .width('100%').height('100%')
  }
}
```

Key permissions: `ohos.permission.CAMERA` (photo/video), `ohos.permission.MICROPHONE` (audio recording).


## Audio Kit — playback & recording


### AudioRenderer (ArkTS) — PCM playback

```ts
import { audio } from '@kit.AudioKit';

const rendererOptions: audio.AudioRendererOptions = {
  streamInfo: {
    samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
    channels: audio.AudioChannel.CHANNEL_2,
    sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
    encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
  },
  rendererInfo: {
    usage: audio.StreamUsage.STREAM_USAGE_MUSIC,  // determines volume type & focus
    rendererFlags: 0
  }
};

const renderer = await audio.createAudioRenderer(rendererOptions);
renderer.on('writeData', (buffer: ArrayBuffer) => {
  // Fill buffer with PCM data
  return audio.AudioDataCallbackResult.VALID;
});
await renderer.start();
// ... renderer.pause() / renderer.stop() / renderer.release()
```


### Audio focus (InterruptEvent)

System manages audio focus automatically based on `StreamUsage`. Listen for focus changes:

```ts
renderer.on('audioInterrupt', (event: audio.InterruptEvent) => {
  if (event.forceType === audio.InterruptForceType.INTERRUPT_FORCE) {
    switch (event.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
        // System paused us — update UI to paused state
        break;
      case audio.InterruptHint.INTERRUPT_HINT_STOP:
        // Permanently lost focus — stop playback
        break;
      case audio.InterruptHint.INTERRUPT_HINT_DUCK:
        // Volume lowered to 20% — optional UI update
        break;
      case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
        // Volume restored
        break;
    }
  } else if (event.hintType === audio.InterruptHint.INTERRUPT_HINT_RESUME) {
    // Can resume playback (SHARE type — app decides)
    await renderer.start();
  }
});
```


### StreamUsage → volume type mapping

| StreamUsage | Volume type | Typical use |
|---|---|---|
| `MUSIC` / `MOVIE` / `AUDIOBOOK` / `GAME` | Media | Music, video, audiobook, game BGM |
| `VOICE_COMMUNICATION` | Voice call | VoIP calls |
| `RINGTONE` / `NOTIFICATION` | Ringtone | Incoming call, notifications |
| `ALARM` | Alarm | Alarms (plays on speaker even with BT) |
| `NAVIGATION` | — | Nav voice (ducks music, doesn't pause) |


### AudioSession — custom focus strategy

```ts
const audioManager = audio.getAudioManager();
const sessionManager = audioManager.getSessionManager();

// Activate session with custom concurrency mode
const strategy: audio.AudioSessionStrategy = {
  concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_PAUSE_OTHERS
};
await sessionManager.activateAudioSession(strategy);

// Monitor deactivation
sessionManager.on('audioSessionDeactivated', (event) => {
  console.info('Session deactivated:', event.reason);
});

// When done
await sessionManager.deactivateAudioSession();
```

Concurrency modes: `CONCURRENCY_DEFAULT`, `CONCURRENCY_MIX_WITH_OTHERS`, `CONCURRENCY_DUCK_OTHERS`, `CONCURRENCY_PAUSE_OTHERS`.


### Background playback requirements

Apps playing audio in background **must**:
- For media/game streams (`MUSIC`/`MOVIE`/`AUDIOBOOK`/`GAME`): integrate **AVSession** AND request **long-running task** (`AUDIO_PLAYBACK`)
- For other audible streams: request `AUDIO_PLAYBACK` long-running task only
- Without these, system will mute and freeze the app when backgrounded


## Scan Kit — barcode scanning & generation


### Default UI scan (no camera permission needed)

Launches the system scan UI. Camera is pre-authorized — no permission request required.

```ts
import { scanCore, scanBarcode } from '@kit.ScanKit';

const options: scanBarcode.ScanOptions = {
  scanTypes: [scanCore.ScanType.ALL],
  enableMultiMode: true,
  enableAlbum: true
};

try {
  const result = await scanBarcode.startScanForResult(
    getContext(this),   // or this.getUIContext().getHostContext()
    options
  );
  // result.originalValue — decoded string
  // result.scanType — code type (QR, EAN-13, etc.)
  console.info('Scan result:', result.originalValue);
} catch (err) {
  console.error('Scan failed:', err.code, err.message);
}
```

Supported code types: QR Code, Data Matrix, PDF417, Aztec, EAN-8, EAN-13, UPC-A, UPC-E, Codabar, Code 39/93/128, ITF-14.


### Image decode (detect barcode in photo)

```ts
import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

// Pick an image from gallery
const picker = new photoAccessHelper.PhotoViewPicker();
const pickerResult = await picker.select({
  MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
  maxSelectNumber: 1
});

// Decode barcode from selected image
const inputImage: detectBarcode.InputImage = { uri: pickerResult.photoUris[0] };
const results = await detectBarcode.decode(inputImage, {
  scanTypes: [scanCore.ScanType.ALL],
  enableMultiMode: true
});
// results is Array<scanBarcode.ScanResult>
```


### Custom UI scan (requires `ohos.permission.CAMERA`)

Use `customScan` from `@kit.ScanKit` for full control over the scan UI:

```ts
import { scanCore, scanBarcode, customScan } from '@kit.ScanKit';

// 1. Init
customScan.init({ scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true });

// 2. Start with XComponent surfaceId
const viewControl: customScan.ViewControl = { width, height, surfaceId };
const results = await customScan.start(viewControl);

// 3. Control: customScan.openFlashLight() / closeFlashLight()
//             customScan.setZoom(2.0) / getZoom()
//             customScan.setFocusPoint({x, y}) / resetFocus()
//             customScan.stop() / rescan()

// 4. Release when done
await customScan.release();
```


### Barcode generation

```ts
import { scanCore, generateBarcode } from '@kit.ScanKit';
import { image } from '@kit.ImageKit';

const pixelMap: image.PixelMap = await generateBarcode.createBarcode('https://example.com', {
  scanType: scanCore.ScanType.QR_CODE,
  height: 400,
  width: 400
});
// Use pixelMap directly in Image component: Image(this.pixelMap)
```

Supports generating: QR Code, EAN-8, EAN-13, UPC-A, UPC-E, Codabar, Code 39/93/128, ITF-14, Data Matrix, PDF417, Aztec.


## AVSession Kit — media playback control (required for background audio)

**Critical**: All apps playing audio/video in background **must** create an AVSession. Without it, the system will **force-pause** your audio when the app goes to background.


### Create and activate session

```ts
import { avSession as AVSessionManager } from '@kit.AVSessionKit';

// Create session — type: 'audio' | 'video' | 'voice_call'
const session = await AVSessionManager.createAVSession(context, 'MyPlayer', 'audio');

// Set metadata (required — without it, playback controls won't appear)
await session.setAVMetadata({
  assetId: 'song_001',
  title: 'Song Title',
  artist: 'Artist Name',
  mediaImage: 'https://example.com/cover.jpg',
  duration: 240000   // ms
});

// Set playback state
await session.setAVPlaybackState({
  state: AVSessionManager.PlaybackState.PLAYBACK_STATE_PLAY,
  position: { elapsedTime: 0, updateTime: Date.now() },
  speed: 1.0
});

// Register control commands BEFORE activating
session.on('play', () => { /* resume playback */ });
session.on('pause', () => { /* pause playback */ });
session.on('playNext', () => { /* next track */ });
session.on('playPrevious', () => { /* previous track */ });
session.on('seek', (position: number) => { /* seek to position ms */ });

// Activate — must be called AFTER metadata + commands are set
await session.activate();
```


### Background playback requirements

For media streams (`MUSIC`/`MOVIE`/`AUDIOBOOK`/`GAME`):
1. Create AVSession (as above)
2. Request `AUDIO_PLAYBACK` long-running task via Background Tasks Kit
3. Both are **mandatory** — missing either one causes background audio to be silenced


### Unsupported commands

Use `session.off()` to unregister commands your app doesn't support. The system playback center will gray out corresponding buttons.

```ts
session.off('playPrevious');  // no "previous" button
session.off('toggleFavorite'); // no favorite button
```


## Core Vision Kit — OCR, face detection, subject segmentation

On-device AI capabilities from `@kit.CoreVisionKit`. China mainland only, no simulator support.


### Text recognition (OCR)

```ts
import { textRecognition } from '@kit.CoreVisionKit';

// Initialize once (e.g., in aboutToAppear)
await textRecognition.init();

// Recognize text from PixelMap
const visionInfo: textRecognition.VisionInfo = { pixelMap: myPixelMap };
const result = await textRecognition.recognizeText(visionInfo, {
  isDirectionDetectionSupported: false
});
console.info('OCR result:', result.value);  // full recognized text string

// Release when done (e.g., in aboutToDisappear)
await textRecognition.release();
```

Supports: Chinese (simplified/traditional), English, Japanese, Korean. Input: JPEG/PNG, 720p+ recommended.


### Face detection

```ts
import { faceDetector } from '@kit.CoreVisionKit';

await faceDetector.init();
const faces: faceDetector.Face[] = await faceDetector.detect({ pixelMap: myPixelMap });
// Each face: faceRectangle, landmark positions, euler angles, confidence
await faceDetector.release();
```


### Subject segmentation

```ts
import { subjectSegmentation } from '@kit.CoreVisionKit';

await subjectSegmentation.init();
const result = await subjectSegmentation.doSegmentation(
  { pixelMap: myPixelMap },
  { maxCount: 5, enableSubjectDetails: true, enableSubjectForegroundImage: true }
);
// result.fullSubject.foregroundImage — PixelMap with background removed
// result.subjectCount, result.subjectDetails[i].subjectRectangle
await subjectSegmentation.release();
```


## AVPlayer — unified audio/video playback

`AVPlayer` from `@kit.MediaKit` handles mp4/mp3/mkv/mpeg-ts etc. — just provide the source, no manual decode needed.

```ts
import { media } from '@kit.MediaKit';

// Create player
const avPlayer = await media.createAVPlayer();

// Set callbacks
avPlayer.on('stateChange', (state: string) => {
  switch (state) {
    case 'initialized':    // source set, prepare now
      avPlayer.prepare();
      break;
    case 'prepared':       // ready to play
      avPlayer.play();
      break;
    case 'completed':      // playback finished
      avPlayer.release();
      break;
  }
});

avPlayer.on('error', (err) => {
  console.error('AVPlayer error:', err.message);
  avPlayer.release();
});

// Set source — local file (fd)
const file = fs.openSync(context.filesDir + '/video.mp4', fs.OpenMode.READ_ONLY);
avPlayer.fdSrc = { fd: file.fd, offset: 0, length: fs.statSync(file.fd).size };

// Or network URL
avPlayer.url = 'https://example.com/audio.mp3';
```


### AVPlayer with video surface (XComponent)

```ts
avPlayer.on('stateChange', (state: string) => {
  if (state === 'initialized') {
    avPlayer.surfaceId = xComponentSurfaceId;  // from XComponent.onLoad
    avPlayer.prepare();
  } else if (state === 'prepared') {
    avPlayer.play();
  }
});
avPlayer.url = 'https://example.com/video.mp4';
```


### AVPlayer controls

```ts
avPlayer.pause();
avPlayer.play();
avPlayer.seek(30000);              // seek to 30s (ms)
avPlayer.setSpeed(media.PlaybackSpeed.SPEED_FORWARD_2_00_X);
avPlayer.setVolume(0.5);           // 0.0 ~ 1.0
avPlayer.stop();                   // stop → can prepare() again
avPlayer.release();                // release all resources
```


### AVRecorder — audio/video recording

```ts
import { media } from '@kit.MediaKit';

const recorder = await media.createAVRecorder();

const config: media.AVRecorderConfig = {
  audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType: media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile: {
    audioBitrate: 48000,
    audioChannels: 2,
    audioCodec: media.CodecMimeType.AUDIO_AAC,
    audioSampleRate: 48000,
    fileFormat: media.ContainerFormatType.CFT_MPEG_4,
    videoBitrate: 2000000,
    videoCodec: media.CodecMimeType.VIDEO_AVC,
    videoFrameWidth: 1920,
    videoFrameHeight: 1080,
    videoFrameRate: 30
  },
  url: `fd://${file.fd}`,       // file descriptor for output
  rotation: 0
};

await recorder.prepare(config);
// For video: const surfaceId = await recorder.getInputSurface();
await recorder.start();
// ... recording ...
await recorder.stop();
await recorder.release();
```

For background playback: must create AVSession + request AUDIO_PLAYBACK long-running task (see AVSession Kit section).


## Image Kit — decode, transform, encode


### Decode image to PixelMap

```ts
import { image } from '@kit.ImageKit';
import { fileIo as fs } from '@kit.CoreFileKit';

// From file path
const imageSource = image.createImageSource(context.filesDir + '/photo.jpg');
const pixelMap = await imageSource.createPixelMap({
  editable: true,
  desiredPixelFormat: image.PixelMapFormat.RGBA_8888
});

// From file descriptor
const file = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
const imageSource2 = image.createImageSource(file.fd);

// From ArrayBuffer (e.g., from network response)
const imageSource3 = image.createImageSource(arrayBuffer);

// From rawfile
const rawFd = context.resourceManager.getRawFd('image.png');
const imageSource4 = image.createImageSource(rawFd);

// Get image info
const info = await pixelMap.getImageInfo();
console.info(`${info.size.width} x ${info.size.height}`);
```


### PixelMap transforms

```ts
pixelMap.crop({ x: 0, y: 0, size: { width: 400, height: 400 } });  // crop
pixelMap.scale(0.5, 0.5);                                           // scale to 50%
pixelMap.rotate(90);                                                 // rotate 90° clockwise
pixelMap.flip(true, false);                                          // horizontal flip
pixelMap.flip(false, true);                                          // vertical flip
pixelMap.opacity(0.5);                                               // set 50% opacity
pixelMap.translate(100, 100);                                        // offset by 100px
```


### Encode PixelMap to file

```ts
import { image } from '@kit.ImageKit';

const packer = image.createImagePacker();
const packOpts: image.PackingOption = { format: 'image/jpeg', quality: 90 };
const data: ArrayBuffer = await packer.packing(pixelMap, packOpts);
// Write data to file via fs.writeSync
packer.release();
```


### Release resources

```ts
pixelMap.release();
imageSource.release();
```

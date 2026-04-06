# HarmonyOS_Samples 官方示例代码


---
## APILevelAdapt
源码: https://gitcode.com/HarmonyOS_Samples/APILevelAdapt

# 实现多API版本兼容

## 项目简介
本项目演示在 HarmonyOS 多版本环境下，如何在同一套代码中实现 API 能力探测与优雅降级，进而实现优雅的 API 兼容策略，覆盖 ArkTS层与Native层两类典型场景：

1. **ArkTS（UI 层）**：通过 `deviceInfo.sdkApiVersion` / `deviceInfo.distributionOSApiVersion` 判断系统版本，选择高版本新特性或低版本替代实现。
2. **Native（NAPI/C++ 层）**：
   - 通过 `dlopen + dlsym` 对动态库符号进行探测，判断某个系统 API 是否存在，从而避免低版本调用导致崩溃。
   - 通过OH_GetDistributionOSApiVersion()获取ISV发行版系统api版本并判断系统版本，选择高版本新特性或低版本特性替代实现。

## 效果预览
|                     首页                     |                   滚动场景                   |                 音频音量场景                 |
| :------------------------------------------: | :------------------------------------------: | :------------------------------------------: |
| <img src='./screenshots/pic1.png' width=320> | <img src='./screenshots/pic2.png' width=320> | <img src='./screenshots/pic3.png' width=320> |

## 使用说明

1. 使用git clone下载该项目代码，并将整个应用示例工程导入DevEco Studio。

2. 打开Terminal终端，使用下面的命令初始化并更新引用的所有子模块：

   ```
   git submodule update --init --recursive
   ```

3. 执行编译构建，安装运行后，即可在设备上查看应用示例运行效果，以及进行相关调试。

## 工程目录

```
├──entry/src/main/cpp
│  ├──classdef
│  │  ├──include
│  │  │  ├──ArkUIBaseNode.h                      // 组件树操作的基类
│  │  │  ├──ArkUINode.h                          // 通用组件的封装
│  │  │  ├──ArkUIButtonNode.h                    // 实现按钮组件的封装类
│  │  │  └──NativeModuleInstance.h               // ArkUI在Native侧模块的封装接口
│  │  └──src
│  │     ├──ArkUIBaseNode.cpp                    // 组件树操作的基类
│  │     ├──ArkUINode.cpp                        // 通用组件的封装
│  │     


---
## AVCodecVideo
> 本实例基于AVCodec能力，提供基于视频编解码的视频播放和录制的功能。

源码: https://gitcode.com/HarmonyOS_Samples/AVCodecVideo

# 基于AVCodec能力的视频编解码

### 介绍

本实例基于AVCodec能力，实现了基于视频编解码的视频播放和录制的功能。通过调用Native侧的编码器，解码器，以及封装和解封装功能，完成从相机录制流到mp4文件的转换，以及对封装好的视频进行解封装，并解码送显。基于本示例可帮助应用开发需要编解码进行视频播放和录制的场景。

- 视频播放的主要流程是将视频文件通过解封装->解码->送显/播放。
- 视频录制的主要流程是相机采集->编码->封装成mp4文件。

### 播放支持的原子能力规格

| 媒体格式 | 封装格式    | 码流格式                                |
|------|:--------|:------------------------------------|
| 视频   | mp4     | 视频码流：H.264/H.265, 音频码流:AudioVivid   |
| 视频   | mkv     | 视频码流：H.264/H.265, 音频码流：aac/mp3/opus |
| 视频   | mpeg-ts | 视频码流：H.264, 音频码流：AudioVivid         |

### 录制支持的原子能力规格

| 封装格式 | 视频编解码类型     | 
|------|-------------|
| mp4  | H.264/H.265 |

### 效果预览

| 应用主界面                                              | 录制页面                                                |
|----------------------------------------------------|-----------------------------------------------------|
| ![AVCodec_Index.png](screenshots/device/Index.png) | ![AVCodecSample.gif](screenshots/device/record.png) | 

### 使用说明

1. 在弹出是否允许“AVCodecVideo”使用相机后，点击“允许”。

#### 录制

1. 点击“录制”。

2. 确认允许录制文件保存到图库。

3. 录制完成后点击“停止录制”。

#### 播放

1. 推送视频文件至图库下或点击下方“开始录制”，录制一个视频文件。

2. 点击播放按钮，选择文件，开始播放。

### 工程目录

```       
├──entry/src/main/cpp                 // Native层
│  ├──capbilities                     // 能力接口和实现
│  │  ├──include                      // 能力接口
│  │  ├──AudioCapturer.cpp            // 音频采集实现
│  │  ├──AudioDecoder.cpp             // 音频解码实现
│  │  ├──AudioEncoder.cpp             // 音频编码实现
│  │  ├──Demuxer.cpp                  // 解封装实现
│  


---
## AdaptiveVideo
源码: https://gitcode.com/HarmonyOS_Samples/AdaptiveVideo

# 实现短视频沉浸和旋转播放功能

#### 介绍

根据提供的adaptive_video库实现短视频的沉浸、旋转播放，同时提供一个高阶组件库方便开发者实现功能，降低开发成本，提高开发效率。

#### 效果预览

<img src="./screenshots/screenshots.gif" width="320">

#### 功能描述

1. 非高阶场景支持视频沉浸播放，手机横向视频支持全屏播放，上下切换视频等功能
2. 高阶场景支持视频沉浸播放，手机横向视频支持全屏播放，双击点赞动画，长按2倍速播放，PC/2in1设备支持键盘操作进度等功能

#### 工程目录

```
├──commons
│  ├──base/src/main/ets
│  │  ├──constants
│  │  │  ├──BreakpointConstants.ets                 // 断点常量类
│  │  │  └──CommonConstants.ets                     // 常量类
│  │  └──model
│  │     ├──BreakpointType.ets                      // 根据断点获取不同断点的值
│  │     └──VideoDataSource.ets                     // 懒加载数据源
│  └──base/src/main/resources                       // 应用静态资源目录
├──features
│  ├──adaptive_video_component/src/main/ets
│  │  ├──components
│  │  │  ├──AdaptiveAVPlayer.ets                    // 沉浸和旋转库实现类
│  │  │  ├──CustomAdaptiveVideoComponent.ets        // 高阶组件实现类
│  │  │  ├──PCVideoControl.ets                      // PC端播放控制栏
│  │  │  └──VideoControl.ets                        // 全屏播放播放控制栏
│  │  ├──pages
│  │  │  ├──Home.ets                                // 底部TAB所在类
│  │  │  └──Recommend.ets                           // 顶部TAB所在类
│  │  └──utils
│  │     └──AVPlayerUtil.ets                        // 播放工具类
│  └──adaptive_video_component/src/main/resources   // 应用静态资源目录
└──products
   ├──entry/src/main/ets
   │  ├──entryability
   │  │  └──EntryAbility.ets
   │  ├──entrybackupability
   │  │  └──EntryBackupAbility.ets
   │  └──pages
   │     └──Index.ets                  


---
## AdjustBrightness
源码: https://gitcode.com/HarmonyOS_Samples/AdjustBrightness

## 实现页面亮度调节的功能

### 介绍

在“视频播放”和“付款码展示”这两种典型场景下，应用需要在不同的页面分别设置不同的屏幕亮度，用户也可以自定义调节屏幕亮度，并且随着页面跳转而自动恢复系统亮度设置。
本示例通过窗口能力提供的[setWindowBrightness](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowbrightness9)和[setWindowKeepScreenOn](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowkeepscreenon9)实现这两种典型场景，帮助开发者理解并掌握页面亮度设置开发的流程与细节，当开发者业务需要“调节页面亮度”的情况，可直接复用本示例代码。

### 预览效果
![image](screenshots/device/SetBrightness.gif)

【备注】录屏无法录制亮度变化，具体实现已真机为准

### 使用说明

1. 点击“视频播放”按钮，进入视频播放页面，点击播放，手指触摸视频左侧上下滑动调节页面亮度，视频自动循环播放，播放过程中不会熄屏，保持常亮；
暂停视频，静置，屏幕跟随系统设置熄屏时间自动熄屏。
2. 点击“付款码”按钮，进入付款码页面，页面自动高亮。
3. 从“视频播放页”或“付款码页”返回首页，页面恢复在系统设置的屏幕亮度。
4. 在“视频播放页”调节完亮度后，返回主页，再次进入“视频播放页”，页面恢复之前设置的“视频播放页”亮度。

### 工程目录

``` 
├──entry/src/main/ets                          
│  ├──common
│  │  ├──Constants.ets                  // 公共常量
│  │  └──GlobalBuilderContext.ets       // 缓存全局@Builder
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets         // 自定义应用数据转换和迁移模板类
│  ├──model                              
│  │  ├──CommentModel.ets               // “视频播放页”视频评论数据结构 model
│  │  └──SystemAreaModel.ets            // 缓存系统状态栏和导航栏高度 model
│  ├──pages
│  │  ├──Index.ets                      // 首页
│  │  ├──PayCodePage.ets                // 付款码页面结构
│  │  └──VideoPage.ets                  // 视频播放页面结构
│  ├──util
│  │  └──BrightnessUtil.ets             // 亮度调节工具类
│


---
## AntiPeep
源码: https://gitcode.com/HarmonyOS_Samples/AntiPeep

# 基于防窥保护能力实现敏感信息防窥功能

## 简介

本示例基于敏感信息的防窥场景，通过系统的防窥保护能力，同时搭配ArkUI的状态管理，帮助开发者解决在有陌生人窥视屏幕的情况下， 达到隐藏敏感信息的功能。

## 效果预览：

| 非窥视状态                                                                                                   | 窥视状态                                               |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <img src="screenshots/phone/show.png" width="320"/>| <img src="screenshots/phone/hide.png" width="320"/> <img src="screenshots/phone/system_layer.png" width="320"/>|

## 使用说明：

1. 下载本示例代码导入到IDE，打开AppScope->app.json文件，修改bundleName为您自己的应用名称。

2. 参考[签名配置指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing)为第一步对应的bundleName的应用，申请带有"ohos.permission.DLP_GET_HIDE_STATUS"权限的profile文件，并在工程中配置相应的签名信息。<br>
   ![image](screenshots/common/acl_permission.png)

3. 编译安装应用后，找到系统的设置->隐私和安全->防窥保护->打开对应应用的开关。

4. 当机主和非机主共同查看屏幕的时候，页面上的数字信息会隐藏显示；其他情况会直接显示内容。

5. 如果开启了"防窥蒙层"选项，则触发窥视状态的时候也会弹出一次"系统防窥蒙层"的页面，后续直到再次进入该页面之前"系统防窥蒙层"不再触发。


## 工程目录

```
├──entry/src/main/ets
│  ├──common
│  │  ├──models
│  │  │  └──ItemInfo.ets                // 业务数据类
│  │  ├──utils
│  │  │  └──AntiPeepUtils.ets           // 防窥保护工具类
│  │  └──CommonConstants.ets            // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets         // 备份恢复类
│  ├──pages
│  │  └──Index.ets                


---
## AppLifecycleManagement
源码: https://gitcode.com/HarmonyOS_Samples/AppLifecycleManagement

# 实现应用生命周期状态管理切换功能

### 介绍

本示例详细介绍了应用如何实现主动退出、重启和切换至后台功能，同时展示了订阅应用前后台状态变化的方法。通过这些机制，开发者可以更好地控制应用生命周期，优化用户体验，并响应不同的运行时需求。

### 效果预览
![preview.png](screenshots/devices/preview.png)

### 目录结构

```
├──entry/src/main/ets/
│  ├──common
│  │  ├──ToastUtils.ets                   // 提示弹窗工具类
│  │  └──Logger.ets                       // 日志打印工具类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets           // 数据备份恢复类
│  └──pages
│     └──Index.ets                        // 应用入口页
└──entry/src/main/resources               // 应用静态资源目录
```
### 具体实现

* 应用前后台切换变化通过[ApplicationContext.on('applicationStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextonapplicationstatechange10)方法进行监听。
* UIAbility的关闭通过[UIAbilityContext.terminateSelf()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#terminateself)方法来实现。
* 应用程序的关闭通过[ApplicationContext.killAllProcesses()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextkillallprocesses)方法实现。
* 应用重启通过[ApplicationContext.restartApp()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextrestartapp12)方法实现。
* 应用切换到后台通过Window模块的[minimize()](https://developer.huawei.com/consumer/cn/doc/harmo


---
## AppStartUp
源码: https://gitcode.com/HarmonyOS_Samples/AppStartUp

## 基于AppStartup初始化启动任务

### 介绍

本示例通过系统能力[StartupConfigEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupconfig)、[StartupTask](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startuptask)和[startupManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupmanager)
实现当应用启动时，同步或异步地做一些初始化任务，加快应用启动速度。 帮助开发者掌握ArkUI启动框架AppStartup，让执行启动任务的代码变得更加简洁清晰、容易维护。

### 预览效果
![image](screenshots/device/startWork.gif)

### 使用说明

1. 启动应用，进入应用主界面，检索日志“AutoMode Task execute complete”，表示自动初始化任务执行完成。
2. 点击“自动模式”按钮，进入二级页面查看自动初始化任务的结果。
3. 点击“手动模式”按钮，执行并手动初始化任务的结果，可检索日志“Manual Task execute success”。

### 工程目录

``` 
├──entry/src/main/ets                          
│  ├──common
│  │  ├──Constants.ets                  // 公共常量
│  │  └──GlobalBuilderContext.ets       // 缓存全局@Builder
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets         // 自定义应用数据转换和迁移模板类
│  ├──pages
│  │  ├──AutoModePage.ets               // 自动模式页面
│  │  ├──Index.ets                      // 首页
│  │  └──ManualModePage.ets             // 手动模式页面
│  ├──startup
│  │  ├──FileTask.ets                   // 文件读写任务
│  │  ├──ImageKinfeTask.ets             // 图片框架Imagekinfe初始化任务
│  │  ├──KvManagerUtilTask.ets          // 分布式数据库初始化任务
│  │  ├──KVStoreTask.ets                // 分布式数据库写入脏数据任务
│  │  ├──RdbStoreTask.ets               // 关系型数据库初


---
## ArkTSComponentsTest
> 本示例基于自动化测试框架，对已有的示例代码实现了单元测试和UI测试。开发者可以结合业务场景对应用进行自动化测试，提升开发效率。

源码: https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest

# 基于自动化测试框架实现单元测试和UI测试

## 项目简介

本示例基于自动化测试框架，对已有的示例代码实现了单元测试和UI测试。开发者可以结合业务场景对应用进行自动化测试，提升开发效率。

## 效果预览

![image](screenshots/device/uiTest.cn.gif)

## 相关概念

- 单元测试框架： 提供测试脚本识别、调度、执行和结果汇总的能力。开发者可在测试脚本中调用UI测试框架和白盒性能测试框架接口编写测试用例。
- UI测试框架：提供UI界面查找和模拟操作能力，可覆盖UI自动化测试的关键场景，包括界面控件精准查找、UI交互操作（如点击、滑动、文本输入等）、外设行为模拟（如键盘输入、鼠标操作、触控板手势、手写笔动作等），助力开发者开发高效可靠的界面自动化测试用例。

## 使用说明

- 运行以下命令安装@ohos/hypium。

```shell
ohpm install @ohos/hypium@1.0.24 --save-dev
```

- 打开entry/src/ohosTest/ets/test目录，右键test目录运行自动化测试。

## 工程目录

```text
├──AppScope
│  ├──resources
│  └──app.json5
├──entry
│  ├──src
│  │  ├──main
│  │  │  ├──ets
│  │  │  │  ├──constants
│  │  │  │  │  └──CommonConstants.ets
│  │  │  │  ├──entryability
│  │  │  │  │  └──EntryAbility.ets
│  │  │  │  ├──model
│  │  │  │  │  └──ItemData.ets
│  │  │  │  ├──pages
│  │  │  │  │  ├──LoginPage.ets
│  │  │  │  │  └──MainPage.ets
│  │  │  │  ├──view
│  │  │  │  │  ├──Home.ets
│  │  │  │  │  └──Setting.ets
│  │  │  │  └──viewmodel
│  │  │  │     └──MainViewModel.ets
│  │  │  ├──resources  
│  │  │  └──module.json5
│  │  └──ohosTest
│  │     ├──ets
│  │     │  ├──test
│  │     │  │  ├──ui
│  │     │  │  │  └──UITest.test.ets
│  │     │  │  ├──unit
│  │     │  │  │  ├──CommonConstants.test.ets
│  │     │  │  │  └──MainViewModel.test.ets
│  │     │  │  ├──data.json
│  │     │  │  └──List.test.ets
│  │     │  ├──testability
│  │     │  │  ├──pages
│  │     │  │  │  └──Index.ets
│  │     │  │  └──TestAbility.ets
│  │     │  └──testrunner
│  │     │ 


---
## AudioCast
源码: https://gitcode.com/HarmonyOS_Samples/AudioCast

# 实现音频投播功能

## 项目简介

本实例基于播控中心和系统投播实现完整的音频投播功能，包含投播和播控中心基础控制：设备切换、歌曲切换、音量增减、进度切换、播放模式切换。

## 效果预览
| 歌曲选择                                                 | 本端播放                                                 | 歌词页                                                  |
|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| <img src='./screenshots/device/page1.png' width=320> | <img src='./screenshots/device/page2.png' width=320> | <img src='./screenshots/device/page3.png' width=320> |

## 使用说明

1. 本端设备播放音频，进度/音量/歌曲控制/音质切换/播放模式切换。
2. 播控中心控制本端设备，进度/音量/歌曲控制。
3. 建立投播，本端控制远端设备进度/音量/歌曲控制。

## 工程目录

```
├───entry/src/main/ets
│   ├───common                              
│   │   ├───contants                        
│   │   │   ├───BreakpointConstants.ets    // 断点常量
│   │   │   ├───LyricConst.ets             // 歌词常量
│   │   │   ├───PlayerConstants.ets        // 播放页常量
│   │   │   └───RouterConstants.ets        // 路由常量
│   │   └───utils                           
│   │       ├───BackgroundUtil.ets         // 后台任务工具类
│   │       ├───BreakpointSystem.ets       // 断点工具类
│   │       ├───ColorConversion.ets        // 颜色转换工具类
│   │       ├───LrcUtils.ets               // 歌词通用方法
│   │       ├───MediaTools.ets             // 媒体数据转换工具类
│   │       ├───ResourceConversion.ets     // 资源转换工具类
│   │       ├───SecondBufferWalk.ets       // 字节读取工具类
│   │       └───SongItemBuilder.ets        // 音


---
## AudioToVideoSync
源码: https://gitcode.com/HarmonyOS_Samples/AudioToVideoSync

# 实现音画同步播放效果

## 介绍
本示例基于视频解码，通过计算音视频帧的延时进行音画同步适配，解决在本地视频播放、网络视频播放和录制视频播放等场景的音画不同步问题。开发者在实现解码播放视频功能时，加入音画同步模块，保持视频画面和音频同步播放，让用户在高时延场景下观看视频有更好的体验。

## 效果预览
| 应用首页                                       | 网络视频播放页面                                       | 录制页面                                          | 音画同步播放页面                                    |
|--------------------------------------------|------------------------------------------------|-----------------------------------------------|---------------------------------------------|
| <img src="screenshots/device/index.png" width=320> | <img src="screenshots/device/network.png" width=320> | <img src="screenshots/device/record.png" width=320> | <img src="screenshots/device/sync.png" width=320> |

## 使用说明
1. 打开应用，有三个场景供选择：本地视频音画同步场景、网络视频音画同步场景、录制视频音画同步场景。
2. 点击进入本地视频音画同步场景，从图库选择指定视频。
3. 进入音画同步页面，播放页面有x1、x2和x3快进功能选择。
4. 点击进入网络视频音画同步场景，提供了固定的网络视频，点击可以播放。
5. 点击进入音画同步页面，后续操作同步骤3。
6. 点击进入录制视频音画同步场景。
7. 进入录制页面，录制视频后，视频将保存在图库，并且拉起图库，选择指定视频，后续操作同步骤3。

## 工程目录
```       
├──entry/src/main/cpp                 // Native层
│  ├──capbilities                     // 能力接口和实现
│  │  ├──include                      // 能力接口
│  │  ├──AudioDecoder.cpp             // 音频解码实现
│  │  ├──AudioEncoder.cpp             // 音频编码实现
│  │  ├──Demuxer.cpp                  // 解封装实现
│  │  ├──Muxer.cpp                    // 封装实现
│  │  ├──VideoDecoder.cpp             // 视频解码实现
│  │  └──VideoEcoder.cpp              // 视频编码实现
│  ├──common                          // 公共模块
│  


---
## BackTaskImplement
源码: https://gitcode.com/HarmonyOS_Samples/BackTaskImplement

# 基于后台任务实现应用流畅体验

### 简介
基于后台任务开发服务实现应用后台保活，本示例分为短时与长时任务模式。短时任务模式使用onApplicationForeground()/onApplicationBackground()监听前后台切换，转后台时申请短时任务。长时模式以位置服务为例，申请长时任务并订阅位置变化，应用切后台时系统仍能自动获取位置信息。
### 效果预览
|                     **主页面**                     |                     **后台申请短时任务页面**                     |                 **后台申请长时任务页面**                  |
|:-----------------------------------------------:|:------------------------------------------------------:|:-----------------------------------------------:|
| ![](screenshots/device/Home_CN.png) |    ![](screenshots/device/ShortTermTaskPage_CN.png)     | ![](screenshots/device/LongTermTaskPage_CN.png) |
### 工程目录 
```
├──entry/src/main/ets                           // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets                       // 本地启动ability      
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                     
│  ├──pages
│  │  └──Index.ets                              // 主页面    
│  ├──utils
│  │  └──SuspendTaskUtils.ets                   // 工具类
│  ├──view
│  │  ├──LongTermTaskPage.ets                   // 后台申请长时任务页面
│  │  └──ShortTermTaskPage.ets                  // 后台申请短时任务页面        
│  └──viewModel
│     ├──LongTermTaskModel.ets                  // 长时任务页面接口
│     ├──ShortTermTaskModel.ets                 // 短时任务页面接口
│     └──SuspendTaskInfo.ets                    // 短时任务实体类
└──entry/src/main/resources                     // 资源文件目录
```

### 使用说明
1. 主页面，点击“后台申请短时任务页面”按钮，进入短时任务页面，查看控制台日志，每隔2s自动发送：“already 


---
## BackupRestore
源码: https://gitcode.com/HarmonyOS_Samples/BackupRestore

# 基于备份恢复框架的数据迁移

### 介绍
本示例通过备份恢复框架实现终端设备从HarmonyOS 4.0升级到HarmonyOS 5.0.0后，应用如何将关系型数据库、文件、XML数据迁移到HarmonyOS NEXT上并恢复，开发者可以利用备份恢复框架里的[EntryBackupAbility.ets](entry/src/main/ets/entrybackupability/EntryBackupAbility.ets)，通过实现onRestore()方法来进行数据恢复。

### 效果预览

|                    主页                     |
|:-----------------------------------------:|
| ![home](screenshots/devices/phone_zh.gif) |

使用说明
1. 参考[设备升级应用数据迁移适配指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/adaptation-process)下适配流程文章中开发者自验证章节获取迁移工具。
2. 运行hdc file send com.example.backuprestore.zip /storage/media/100/local/files/Docs/Download 将同级目录中[com.example.backuprestore.zip](com.example.backuprestore.zip)发送到设备上。
3. 参考[HarmonyOS NEXT上模拟验证应用数据迁移](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/self-verification)进行数据迁移。
4. 点击数据库、文件、XML数据查看迁移后的数据。

### 工程目录

```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets                    // 入口类
│  ├──entryability
│  │  └──EntryBackupAbility.ets              // 备份恢复框架
│  ├──pages
│  │  └──Index.ets                           // 主页
│  ├──restore
│  │  ├──db
│  │  │  └──DbTransferManager.ets            // 恢复数据库数据
│  │  ├──fileMigrate
│  │  │  └──FileTransferManager.ets          // 恢复文件数据
│  │  └──sp
│  │     └──SpTransferManager.ets            // 恢复XML数据
│  └──view
│     ├──FileShow.ets                        // 展示文件数据
│     ├──RdbDataShow.ets                     // 展示数据库数据
│     └──XMLDataShow.ets                     // 展示xml数据
└──en


---
## BestPracticeSnippets
源码: https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets

# BestPracticeSnippets

## 目录

* [DealStrideSolution： 处理stride解决相机预览花屏问题](DealStrideSolution)
* [AppDataSecurity： 应用数据安全](AppDataSecurity)
* [AppPrivacyProtection：应用隐私保护](AppPrivacyProtection)
* [AvoidTimeComsume：主线程耗时操作优化指导](AvoidTimeComsume)
* [ComponentReuse：组件复用开发实践](ComponentReuse)
* [FramedRendering：高负载分帧渲染开发实践](FramedRendering)
* [FuzzySceneOptimization：图像模糊动效优化](FuzzySceneOptimization)
* [NdkQoS：基于QoS设置线程优先级](NdkQoS)
* [PreHttpRequestUseFiles：Image白块解决指导](PreHttpRequestUseFiles)
* [ImageEditTaskPool：基于TaskPool实现图片编辑功能](ImageEditTaskPool)
* [SegmentedPhotograph：实现相机分段式拍照功能](SegmentedPhotograph)
* [ScreenFlickerSolution：解决应用动效闪屏的方案](ScreenFlickerSolution)
* [CustomTitleBarWindowDrag：自定义标题栏的应用窗口拖动](CustomTitleBarWindowDrag)
* [SubwindowAdaptWhenRotate：应用子窗旋转场景开发实践](SubwindowAdaptWhenRotate)

## 使用说明

1. 将独立的应用示例工程导入DevEco Studio进行编译构建及运行调试。
2. 安装运行后，即可在设备上查看应用示例运行效果，以及进行相关调试。




---
## BluetoothLowEnergy
源码: https://gitcode.com/HarmonyOS_Samples/BluetoothLowEnergy

# 基于低功耗蓝牙实现设备间连接通信的能力

## 项目介绍
低功耗蓝牙（简称BLE）它是一种能够在低功耗情况下进行通信的蓝牙技术，与传统蓝牙相比，BLE的功耗更低，适用于需要长时间运行的低功耗设备，如智能手表、健康监测设备、智能家具等。
本示例主要介绍了设备之间通过蓝牙进行连接和通信的能力，BLE服务端开启广播后可传递数据、BLE客户端搜索可连接设备并在连接后接收广播数据。

## 效果图预览
|                客户端搜索设备                 |                客户端心率检测                 |                服务端心率广播                 |
| :-------------------------------------------: | :-------------------------------------------: | :-------------------------------------------: |
| <img src='./screenshots/pic_1.png' width=320> | <img src='./screenshots/pic_2.png' width=320> | <img src='./screenshots/pic_3.png' width=320> |

## 使用说明
需要两台设备，一台作为BLE服务端，一台作为BLE客户端。
* BLE服务端

  点击开启心率广播按钮后，进行数据传送。
* BLE客户端

  搜索可连接蓝牙设备，连接成功后，接收数据，并通过折线图展示。

## 工程目录

``` 
├──entry/src/main/ets                                   
│  ├──contants
│  │  └──CommonConstants.ets                            // 常量
│  ├──entryability
│  │  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                         // 备份恢复类
│  ├──model
│  │  └──BluetoothDevice.ets                            // 蓝牙设备
│  ├──pages
│  │  ├──client
│  │  │  ├──model
│  │  │  │  └──BluetoothClientModel.ets                 // 蓝牙客户端model层(业务逻辑层)
│  │  │  ├──view
│  │  │  │  ├──BluetoothClientView.ets                  // Bluetooth客户端页面
│  │  │  │  └──HeartRateView.ets                        // 心率折线图页面
│  │  │  └──BluetoothClientViewModel.ets                // 蓝牙客户端ViewModel层(UI驱动层)
│  │  


---
## CardInfoRefresh
> 服务卡片给用户提供一目了然的信息内容，具有易用可见、智能可选和多段可变的特点。本示例通过卡片开发服务（Form Kit），介绍卡片的创建、交互、更新与管理等功能的实现，使开发者能够高效完成个性化服务卡片的开发。

源码: https://gitcode.com/HarmonyOS_Samples/CardInfoRefresh

# 实现卡片更新与数据交互功能

### 介绍

服务卡片给用户提供一目了然的信息内容，具有易用可见、智能可选和多段可变的特点。本示例通过卡片开发服务（Form Kit），介绍卡片的创建、交互、更新与管理等功能的实现，使开发者能够高效完成个性化服务卡片的开发。

### 效果预览
| 卡片一                              | 卡片二                                     |
|----------------------------------|-----------------------------------------|
| ![](screenshots/device/form.png) | ![](screenshots/device/form_second.png) |


### 使用说明

**卡片一**
1. 安装应用后，长按应用图标，添加服务卡片。
2. 点击“router事件”按钮进入应用页面，返回桌面时可见卡片信息刷新。
3. 点击“call事件”，可见卡片信息刷新。
4. 点击“message事件”可见卡片信息刷新。
5. 配置“src/main/resources/base/profile/form_config.json”文件中的“scheduledUpdateTime”字段为某个时间，卡片信息即可在相应时间刷新。

**卡片二**
1. 安装应用后，应用首页展示图文列表，右上角心形支持点击。
2. 长按应用图片选择创建卡片二，点击卡片拉起应用。
3. 应用内选择卡片展示的同一条数据，点击心形按钮，返回桌面，心形状态更新至卡片。
4. 配置“src/main/resources/base/profile/form_config.json”文件中的“updateDuration”字段。卡片定时刷新的更新周期单位为30分钟。示例配置为1，表示卡片任意更新后，30分钟后定时刷新。

### 工程目录

```
├──entry/src/main/ets                     // 代码区
│  ├──common
│  │  ├──utils
│  │  │  ├──Logger.ets                    // 日志工具类
│  │  │  └──PreferencesUtil.ets           // 首选项工具类
│  │  ├──CommonConstants.ets              // 卡片数据
│  │  └──CommonData.ets                   // 卡片数据工具类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──entryformability
│  │  └──EntryFormAbility.ets             // 卡片生命周期类
│  ├──pages
│  │  └──Index.ets                        // 首页
│  └──widget
│     ├──pages
│     │  ├──WidgetCard.ets                // 卡片一页面
│     │  └──


---
## CommentReply
源码: https://gitcode.com/HarmonyOS_Samples/CommentReply

## 实现评论回复弹窗模块

### 介绍

本示例实现在视频应用中，使用Navigation Dialog在评论列表上层弹出评论回复模块，在该模块中使用RichEditor组件实现输入文字、表情、@好友功能。为开发者提供评论回复模块的开发实践。

### 效果预览

| 首页                                  | 评论列表                                        | 评论回复弹窗（软键盘）                             | 评论回复弹窗（表情面板）                                  |
|-------------------------------------|---------------------------------------------|-----------------------------------------|-----------------------------------------------|
| ![](./screenshots/devices/home.png) | ![](./screenshots/devices/comment-list.png) | ![](./screenshots/devices/keyboard.png) | ![](./screenshots/devices/emoji-keyboard.png) |

使用说明：

1. 打开应用，在首页点击消息图标，弹出评论列表弹窗。
2. 点击评论列表下方写评论输入框，弹出评论回复模块弹窗。
3. 评论模块默认是软键盘输入，点击编辑区域表情按钮，可切换到表情面板输入表情。
4. 点击@按钮，或通过软键盘输入@符号，显示好友列表，点击好友头像在编辑区域添加@好友内容。
5. 点击删除按钮，@好友内容先整体选中高亮，再点击删除，@好友内容整体删除。

### 工程目录

```
├──commons
│  ├──commons/src/main/ets
│  │  └──utils
│  │     ├──FileUtils.ets                  // 文件工具类     
│  │     └──Logger.ets                     // 日志工具类
│  └──commons/src/main/resources           // 应用静态资源目录
├──features
│  ├──home/src/main/ets
│  │  ├──constants
│  │  │  └──HomeConstants.ets              // 常量类	
│  │  └──view	                    
│  │     ├──CommentKeyboard.ets            // 评论回复模块
│  │  	 ├──CommentList.ets				   // 评论列表
│  │     ├──CommentSendDialog.ets          // 评论发送弹窗
│  │     ├──Home.ets                       // 首页
│  │     ├──HomeContent.ets                // 视频页
│  │     └──NavigationD


---
## CommonLinksSkip
源码: https://gitcode.com/HarmonyOS_Samples/CommonLinksSkip

# **基于enableDataDetector属性实现特殊文本识别的能力**
## 介绍
本示例通过Text组件的enableDataDetector属性，实现对一段文本中的特殊文字识别，比如包含链接、电话号码、日期、地址和邮箱的文本中，能自动识别出哪些文本是这些特殊文字。
特殊文字会变蓝并增加下划线。当识别出链接、电话号码、日历、地址和邮箱时，用户点击这些文本，弹出对应的操作菜单，点击菜单中的操作选项后会进行相应的跳转。
## 预览效果
![](screenshots/device/image.png)
## 工程目录
``` 
├──entry/src/main/ets                                   // 代码区
│  ├──entryability
│  |  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  |  └──EntryBackupAbility.ets
│  ├──pages
│  |  ├──Index.ets                                      // 首页
│  |  └──LinksPage.ets                                  // 特殊文本识别页面
|  └──uiComponent.ets
│     └──TextLink.ets                                   // 文字UI组件
└──entry/src/main/resources                             // 应用资源目录
``` 

## 使用说明

* 标准HTTP/HTTPS链接：用户点击后，弹出操作菜单，点击“打开”后，跳转至系统默认浏览器打开链接。
* AppLinking链接：用户点击后，弹出操作菜单，点击“打开”后，若系统已安装对应的应用，则直接拉起该应用；若未安装，则拉起应用市场或者跳转到浏览器中的Web页面。
* 日期链接：用户点击后，弹出操作菜单，点击“新建日程提醒”后，拉起系统新建日程的页面。
* 电话号码链接：用户点击后，弹出操作菜单，可选择进行呼叫、发生短信、新建联系人等操作。
* 地址链接：用户点击后，弹出操作菜单，点击“导航至该位置”后，拉起系统弹窗，可选择已安装的地图应用进行导航。当前系统规格不支持对英文地址的识别跳转。
* 邮箱链接：用户点击后，弹出操作菜单，点击“新建邮件”后，拉起系统弹窗，点击“电子邮件”后，拉起电子邮件应用。

## 相关权限

不涉及。
## 约束与限制
* 本示例仅支持标准系统上运行，支持设备：华为手机。

* HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

* DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
  
* HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## CommonListFlows
源码: https://gitcode.com/HarmonyOS_Samples/CommonListFlows

# 基于List组件实现常见列表流场景

## 介绍
列表流是采用以“行”为单位进行内容排列的布局形式，每“行”列表项通过文本、图片等不同形式的组合，高效地显示结构化的信息。
列表流具有排版整齐、重点突出、对比方便、浏览速度快等特点。列表流主要使用List组件，按垂直方向线性排列子组件ListItemGroup或ListItem，混合渲染任意数量的图文视图，从而构建列表内容。

本示例包含以下四个常见的列表流场景：
* 多类型列表项场景
* Tab吸顶场景
* 分组吸顶场景
* 二级联动场景

## 预览效果
|  多类型列表项场景 | Tab吸顶场景  |
|---|---|
|  ![](screenshots/divice/homePage.gif) |  ![](screenshots/divice/managerPage.gif) |
| 分组吸顶场景  | 二级联动场景  |
| ![](screenshots/divice/cityList.gif)  |  ![](screenshots/divice/categoryPage.gif) |


## 工程目录
```
├──entry/src/main/ets                                   // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages                              
│  │  ├──Index.ets                                      // 首页
│  │  ├──CategoryPage.ets                               // 二级联动场景页面
│  │  ├──CityList.ets                                   // 分组吸顶场景页面
│  │  ├──CustomListItem.ets                             // Tab吸顶场景列表内容
│  │  ├──HomePage.ets                                   // 多类型列表项场景页面
│  │  └──ManagerPage.ets                                // Tab吸顶场景页面
│  └──model 
│     └──LinkDataModel.ets                              // 二级联动场景数据
└──entry/src/main/resources                             // 应用资源目录
```

## 使用说明
示例代码包含四个场景：
* 多类型列表项场景：进入页面，下拉刷新模拟网络请求；向下滑动页面内容，景区分类标题吸顶；滑动到页面底部，上滑模拟请求添加列表数据。
* Tab吸顶场景：下滑页面内容，“关注”、“推荐”、“热搜”、“更多”实现吸顶效果。
* 分组吸顶场景：滑动左侧城市列表数据，城市列表标题实现吸顶效果，城市字母标题对应右侧字母导航列表内容高亮显示；点击右侧字母导


---
## ComplexTypePass
> 本示例介绍如何通过Native-API，在ArkTS与Native之间传递数据。

源码: https://gitcode.com/HarmonyOS_Samples/ComplexTypePass

# 实现复杂参数的跨语言交互功能

### 介绍

本示例介绍了复杂数据类型在ArkTS与C++两种语言间的交互能力。主要包含Array、Object、HashMap、PixelMap、Class五种类型。五种类型分别设计了五个小案例来帮助开发者了解不同数据交互时需要调用的Node-API接口。通过该案例开发者可以学到Node-API数据交互相关接口能力的使用，并且可以在应用开发过程中熟练的进行数据跨语言传递。

### 效果图预览

| 应用首页                                 | Uint8Array                           | Object                               |
|--------------------------------------|--------------------------------------|--------------------------------------|
| ![](screenshots/device/Preview1.png) | ![](screenshots/device/Preview2.png) | ![](screenshots/device/Preview3.png) |

| HashMap                              | PixelMap                             | Class                                |
|--------------------------------------|--------------------------------------|--------------------------------------|
| ![](screenshots/device/Preview4.png) | ![](screenshots/device/Preview5.png) | ![](screenshots/device/Preview6.png) |

**使用说明**

1. 进入应用后，下方按钮，分别对应五种数据类型的示例。
2. Uint8Array，uint8Array类型示例。在上部输入框内可以输入0-255的数字。点击“执行”后，程序会将数组从ArkTS传递至C++再返回，之后显示在下方输出框中。
3. Object，object类型示例。在上部输入框内可以输入合理年龄和姓名。点击“执行”后，程序会将包含输入信息的object从ArkTS传递至C++，C++会判断其为成人与否，并分组排序，再返回包含输出信息的object，之后显示在下方输出框中。
4. HashMap，hashMap类型示例。在上部输入框内可以输入0-9的数字。点击“执行”后，程序会将包含输入信息的hashMap从ArkTS传递至C++，C++会累加每个对象每次的输入值，再返回包含输出信息的hashMap，之后显示在下方输出框中。
5. PixelMap，pixelMap类型示例。点击“执行”后，程序会将图片的pixelMap从ArkTS传递至C++，C++将其处理为黑白图片，再返回ArkTS，之后刷新图片。
6. Class，class类型示例。点击“ArkTS class pass to Napi”后，程序会将ArkTS的Class传递至C++，C++调用其方法后，将结果显示至


---
## ComponentEncapsulation
源码: https://gitcode.com/HarmonyOS_Samples/ComponentEncapsulation

# 实现组件的封装

### 介绍

本示例通过系统组件的attributeModifier属性、PromptAction对象、wrapBuilder函数等，实现组件公共样式封装、自定义组件的封装、弹窗组件的封装、全局@Builder。帮助开发者掌握如何优化重复性的组件、布局，使代码简洁，易维护。

### 效果图预览

| 首页                                                 | 组件公共样式封装                                           | 自定义组件封装场景                               | 组件工厂类封装场景                                | 弹窗组件封装场景                                |
|----------------------------------------------------|----------------------------------------------------|-----------------------------------------|------------------------------------------|-----------------------------------------|
| <img src="screenshots/device/index.png" width=320> | <img src="screenshots/device/style.png" width=320> | ![image](screenshots/device/common.png) | ![image](screenshots/device/factory.png) | ![image](screenshots/device/dialog.png) |

##### 使用说明

进入首面，会看到各封装场景的按钮，点击按钮会进入对应的封装场景实现的页面，查看效果。

### 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  └──CommonConstants.ets         // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets            // 程序入口类
│  ├──model
│  │  ├──GetResourceString.ets       // Resource转换String函数
│  │  └──PopViewUtils.ets            // 自定义弹窗类
│  ├──pages
│  │  ├──AttributeStylePage.ets      // 组件公共样式封装
│  │  ├──CommonComponent.ets         // 自定义组件封装
│  │  ├──ComponentFactory.ets        // 组件工厂类封装
│  │  ├──DialogComponent.ets         // 弹窗组件封装        
│  │  └──Index.ets                   // 首页
│  └──view
│     ├──CustomImageText.ets   


---
## ContinuePublish
源码: https://gitcode.com/HarmonyOS_Samples/ContinuePublish

# 基于应用接续及跨设备互通功能实现内容发布功能

## 介绍

本示例基于应用接续、分布式数据对象、分布式文件系统、跨设备互通等功能，实现文本图片数据跨设备交互及接续。
通过分布式数据对象跨设备传输数据；点击系统Dock栏，使应用接续并进行数据传输，使用系统能力，使应用跨设备获取图片、拖拽图片文字、复制粘贴图片文字。开发者可学会应用接续、分布式数据使用、跨设备交互等能力。

## 效果图预览

|                    **主页**                     |                    **图片获取**                     |                     **拖拽**                      |                   **剪贴**                    |
|:---------------------------------------------:|:-----------------------------------------------:|:-----------------------------------------------:|:-------------------------------------------:|
|    ![Index](screenshots/device/Index.png)     |    ![Get](screenshots/device/fromOther.png)     |    ![OnDrop](screenshots/device/onDrop.png)     |    ![Copy](screenshots/device/copy.png)     |
| ![Index](screenshots/device/Index_tablet.png) | ![Get](screenshots/device/fromOther_tablet.png) | ![OnDrop](screenshots/device/onDrop_tablet.png) | ![Copy](screenshots/device/copy_tablet.png) |



## 使用说明

1. 进入应用首页，点击“添加优质首图”，弹出图片来源弹窗，选择拉取本地图库后，弹出本地图库弹窗，选择图片后，图片横向显示在列表中。
2. 选择拉取远端后，可选择同一华为账号下的其他设备的拍照、图库、文档扫描功能，可调用其他设备的相机、图库、文档扫描页面（注：PC/2in1可调用平板和手机，平板只能调用手机，手机无法调用其他设备且同设备无法调用），拍摄图片并保存，或选择图库图片后点击完成，回传图片至当前设备应用的列表中。
3. 在本端应用中点击列表中的图片，出现复制按钮，点击后可将图片复制到系统剪贴板，也可复制图库内的图片。在对端设备的图片列表上，点击空白区域，显示粘贴按钮，点击按钮可粘贴并显示系统剪贴板的图片。（复制数据只存在在跨设备剪贴板中2分钟）。
4. 在本端应用中长按列表中的图片，触发拖拽场景，可将本端图片拖拽至对端图片列表区域，松开鼠标，图片显示在列表中（注：需连接同一华为账号的设备打开键鼠共享，并且必须包含一台PC/2in1）。
5. 点击“标题”/“正文”输入框，可以输入相应内容。
6. 在本端应用中选择编辑区域的文字，触发系统菜单后，点击复制按钮可将文字复制到系统剪贴板，也可


---
## CoreVisionKitOCR
源码: https://gitcode.com/HarmonyOS_Samples/CoreVisionKitOCR

# 基于拍照识别能力实现文字自动填充

## 介绍

本示例基于基础视觉服务，使用`@kit.CoreVisionKit`提供的通用文字识别能力，通过拍照（CameraPicker）或者相册（PhotoViewPicker）方式，将印刷品文字（如：收货信息）转化为图像信息，再利用文字识别技术将图像信息转化为设备可以使用的文本字符，最后可以根据实际业务规则提取结构化数据。

## 效果预览

| 主页                                     | 拍照                                     | 识别                                          | 保存                                      |
|----------------------------------------|----------------------------------------|---------------------------------------------|-----------------------------------------|
| ![主页](screenshots/device/1.png "主页") | ![拍照](screenshots/device/2.png "拍照") | ![识别](screenshots/device/3.png "识别") | ![保存](screenshots/device/4.png "保存") |

使用说明：
1. 点击`图片识别`按钮，拉起`选择图片获取方式`的弹窗，选择`拍照`方式，通过对要识别的文字进行拍照获得要识别的图片。也可以选择`相册`方式，在图库中直接选择需要识别的图片。
2. 识别出图片包含的文本信息后，会自动将文本内容填充到文本输入框。
3. 点击`识别`按钮，会将文本框中的信息提取为结构化数据，显示到按钮下方的列表中。
4. 点击`保存地址`按钮，提示保存成功，文本框旧的内容会自动清空。

## 工程目录

```
entry/src/main/
├──ets
|  ├──common
|  |  ├──constants
|  |  |  └──CommonConstants.ets                               // 公共常量类
|  |  └──utils
|  |     ├──AddressParse.ets                                  // 收货信息解析类
|  |     ├──OCRManager.ets                                    // 视觉识别类
|  |     ├──PromptActionManager.ets                           // 弹窗管理类
|  |     └──Logger.ets                                        // 日志类
|  ├──entryability
|  |  └──EntryAbility.ets                                     // 入口Ability
|  ├──viewmodel
|  |  └──DataModel.ets                    


---
## CrossModuleReference
源码: https://gitcode.com/HarmonyOS_Samples/CrossModuleReference

# Native侧调用HAR/HSP模块接口

## 介绍

本示例展示了Native侧跨HAR/HSP模块调用接口，用于大型应用开发过程中，Native侧代码直接调用其他HAR/HSP模块提供的接口。通过该案例，开发者可以了解Native侧跨HAR/HSP模块调用Native方法和ArkTS方法的文件配置以及调用逻辑。

## 效果预览

![](screenshots/device/nativeCall_cn.png) 


## 使用说明

1、点击【调用Native方法】按钮，调用Native方法。

2、点击【调用HarNative方法】按钮，调用staticModule模块的Native方法。

3、点击【通过Native方法调用HarArkTS方法】按钮，通过staticModule模块的Native方法调用Har模块的ArkTS方法。

4、点击【调用HspNative方法】按钮，调用sharedModule模块的Native方法。

5、点击【通过Native方法调用HspArkTS方法】按钮，通过sharedModule模块的Native方法调用sharedModule模块的ArkTS方法。

注意：在运行应用时，需要设置Deploy Multi Hap。点击Edit Configuration -> 选择entry -> 点击Deploy Multi Hap -> 勾选Deploy Multi Hap Packages。

## 工程目录
```
├──entry/src/main                     // Native层
│  ├──cpp
│  │  ├──types                        // Native层暴露上来的接口
│  │  │  └──libentry            
│  │  │     ├──index.d.ts             // 暴露给UI层的接口
│  │  │     └──oh-package.json5
│  │  ├──CMakeLists.txt               // 编译入口
│  │  └──napi_init.cpp                // Native文件操作方法       
│  └──ets                             // UI层
│     ├──entryability                 // 应用的入口
│     │  └──EntryAbility.ets            
│     ├──entrybackupability            
│     │  └──EntryBackupAbility.ets          
│     ├──model            
│     │  └──FileNameModel.ets            
│     └──pages                        // EntryAbility 包含的页面
│        └──Index.ets                 // 应用主页面
├──staticModule/src/main              // har模块
│  ├──cpp
│  │  ├──types                        // Native层暴露上来的接口
│  │  │  └


---
## CrossModuleResourceAccess
> 本示例实现了跨模块访问HAP/HSP资源，分别使用"$r"直接引用和resourceManager模块的相关API，访问所依赖HAP/HSP模块中的文本和图片资源。

源码: https://gitcode.com/HarmonyOS_Samples/CrossModuleResourceAccess

# 实现跨模块访问HAR/HSP资源文件功能

### 介绍

在HarmonyOS应用模块化设计中，一般使用HAR和HSP模块来共享资源，可以减少重复定义，简化资源管理，提升开发效率。
本示例实现了跨模块访问HAP/HSP资源，分别使用"$r"直接引用和[resourceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager)模块的相关API，访问所依赖HAP/HSP模块中的文本和图片资源。

### 效果预览

| HAP访问HSP/HAR资源                    | HAR访问HSP/HAR资源                       | HSP访问HSP/HAR资源                       |
|-----------------------------------|--------------------------------------|--------------------------------------|
| ![](screenshots/device/index.png) | ![](screenshots/device/har1page.png) | ![](screenshots/device/hsp1page.png) |

### 工程目录

```
├──entry
│  ├──src/main/ets/
│  │  ├──common
│  │  │  └──Logger.ets                       // 日志打印工具类
│  │  ├──entryability
│  │  │  └──EntryAbility.ets                 // 程序入口类
│  │  ├──entrybackupability
│  │  │  └──EntryBackupAbility.ets           // 数据备份恢复类
│  │  └──pages
│  │     │──GetHspResource.ets               // 获取HSP中资源页面
│  │     └──Index.ets                        // 应用入口页
│  └──src/main/resources                     // 应用静态资源目录
├──har1                                      // har1模块
│  ├──src/main/ets/components                                
│  │  └──Har1Page.ets                        // 模块业务页面  
│  ├──src/main/resources                     // 应用静态资源目录   
│  └──Index.ets                              // 入口文件，对外暴露模块方法  
├──har2                                      // har2模块
│  ├──src/main/resources                     // 应用静态资源目录


---
## CustomCamera
源码: https://gitcode.com/HarmonyOS_Samples/CustomCamera

## 实现自定义相机功能

### 介绍

本示例基于Camera Kit相机服务，使用ArkTS API实现基础预览、预览画面调整（前后置镜头切换、闪光灯、对焦、调焦、设置曝光中心点等）、预览进阶功能（网格线、水平仪、人脸检测、超时暂停等）、双路预览（获取预览帧数据）、拍照（动图拍摄、延迟拍摄、音量键拍照等）、录像等核心功能。为开发者提供自定义相机开发的完整参考与实践指导。

### 效果预览

![](./screenshots/devices/camera.png)   &emsp;  ![](./screenshots/devices/camera_people.png)

使用说明：
1. 打开应用，授权后展示预览界面。
2. 上方从左至右按钮功能依次为：预览帧率设置、闪光灯设置、延迟拍照模式设置、动态拍照模式设置、单双段拍照模式设置（单段拍照模式不支持动态拍摄）。
3. 切换录像模式，上方按钮依次为：预览帧率设置、闪关灯设置、防抖模式设置（模式不支持变焦）。
4. 右侧按钮依次为：网格线、水平仪、双路预览（获取预览帧数据）。
5. 下方按钮可拍照，录像，切换前后置摄像头。

### 工程目录

```
├──camera/src/           
│  ├──main/ets/  
│  │  ├──components             
│  │  │  ├──GridLine.ets                            // 网格线组件
│  │  │  └──LevelIndicator.ets                      // 水平仪组件
│  │  ├──constants
│  │  │  └──CameraConstants.ets                     // 常量文件
│  │  └──cameraManagers             
│  │     ├──CamaraManager.ets                       // 相机会话管理类
│  │     ├──ImageReceiverManager.ets                // ImageReceiver预览流管理类
│  │     ├──MetadataManager.ets                     // 元数据输出流管理类
│  │     ├──OutputManager.ets                       // 输出流管理类抽象接口
│  │     ├──PhotoManager.ets                        // 拍照流管理类
│  │     ├──VideoManager.ets                        // 视频流管理类
│  │     └──PreviewManager.ets                      // 预览流管理类 
│  └──Index.ets                                     // 相机模块导出文件
├──commons/src/main/ets/                               
│  └──utils           
│     └──Logger.ets                                 // 日志类  
├──entry/s


---
## CustomizeKeyboard
源码: https://gitcode.com/HarmonyOS_Samples/CustomizeKeyboard

# 实现自定义键盘功能

## 介绍

本示例介绍自定义键盘的实现，通过绑定系统键盘，实现自定义键盘和系统键盘的切换；通过onAreaChange获取自定义键盘高度，设置布局避让；为开发者讲解键盘切换、自定义键盘光标处理、自定义键盘布局避让等技术场景案例。

## 效果预览
|               自定义键盘布局避让                |              自定义键盘和系统键盘切换               |              自定义键盘通用功能               |
|:--------------------------------------:|:---------------------------------------:|:------------------------------------:|
| ![image](screenshots/device/avoid.gif) | ![image](screenshots/device/switch.gif) | ![image](screenshots/device/use.gif) |


## 使用说明

1. 首页点击“绑定自定义键盘”输入框，拉起自定义键盘，布局会向上避让。

2. 分别点击键盘上“123”、“ABC”、“中文”tab页签，切换数字键盘、英文键盘、系统键盘，实现一个输入框同时绑定自定义键盘和系统键盘。

3. 支持键盘通用操作，包括内容输入、光标设置、大小写切换、复制、粘贴、删除等功能。


## 工程目录

```
├──entry/src/main/ets	                 // 代码区
│  ├──constants
│  │  └──Constants.ets                   // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets                // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets          // 数据备份
│  ├──model
│  │  └──KeyboardController.ets          // 自定义键盘控制类
│  ├──pages
│  │  └──MainPage.ets                    // 主页面
│  ├──view
│  │  ├──CustomKeyboard.ets              // 自定义键盘入口
│  │  ├──CustomKeyboardComponent.ets     // 自定义键盘组件
│  │  ├──EnglishKeyboard.ets             // 英文键盘组件
│  │  ├──InputTextComponent.ets          // 绑定的TextInput组件
│  │  ├──NumberKeyboard.ets              // 数字键盘组件
│  │  ├──TabButton.ets                   // 键盘上方Tab组件Button按钮
│  │  ├──TabView.ets                     // 键盘上方Tab组件
│  │  └──TextInputComponent.ets       


---
## DataCache
> 本示例是基于ArkTS的声明式开发范式实现的样例，主要介绍了首页数据缓存来加速应用冷启动的使用。

源码: https://gitcode.com/HarmonyOS_Samples/DataCache

# 基于DataCache提升应用冷启动速度

### 介绍

本示例展示了基于DataCache库的数据缓存能力，提升HarmonyOS应用冷启动速度的功能，以优化应用使用体验。

### 效果预览

<img src="screenshots/device/20240806_141226.gif" width="254" />

### 工程目录

```markdown
├──entry/src/main/ets/
│  ├──common
│  │  ├──constant                  
│  │  │  └──CommonConstants.ets               // 公共常量
│  │  ├──types  
│  │  │  └──CommonTypes.ets                   // 公共类型
│  │  └──utils 
│  │     └──Refresh.ets                       // 刷新工具类
│  ├──entryability
│  │  └──EntryAbility.ets                     // 程序入口类
│  ├──model
│  │  └──ListModel.ets                        // 模型文件
│  ├──pages                 
│  │  └──Index.ets                            // 首页
│  └──view     
│     ├──ListPage.ets                         // List列表页     
│     ├──NewsItem.ets                         // 列表item项         
│     └──TabBar.ets                           // TabBar
└──entry/src/main/resources                   // 应用资源目录
```

### 使用说明

本示例通过使用库`@hadss/datacache`的数据读取能力，在应用启动过程中的整体缓存读取流程如下：

![](screenshots/device/flowchart.png)

### 具体实现

1. 点击应用进入主页面前，首先会获取本地缓存数据，如果没有缓存则请求网络数据，请求网络数据后，会将数据缓存起来，数据有效期设为2天。源码参考：[EntryAbility.ets](entry/src/main/ets/entryability/EntryAbility.ets)
   - 使用DataCache的get方法获取缓存，DataCache的put方法缓存数据，设置有效期，接口参考：[@hadss/datacache](https://ohpm.openharmony.cn/#/cn/detail/@hadss%2Fdatacache)
2. 页面展示新闻列表，点击页签或左右滑动页面，切换标签并展示对应新闻类型的数据。源码参考：[TabBar.ets](entry/src/main/ets/view/TabBar.ets)
   - 使用Tabs组件实现左右滑动页签
3. 新闻列表页面，滑动到新闻列表首项数据，接着往下滑动会触发下拉刷新操作，页面更新初始5条新闻数据


---
## DatabaseReadWrite
源码: https://gitcode.com/HarmonyOS_Samples/DatabaseReadWrite

# 使用C-API读写关系型数据库

### 介绍

本示例展示了使用了C-API接口对关系型数据库进行增删改查的场景。

### 效果预览



|                             主页                              |                           增加/编辑商品                           |                            筛选商品                             |
|:-----------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| <img src=./screenshots/pic1.png align="center" width=320 /> | <img src=./screenshots/pic2.png align="center" width=320 /> | <img src=./screenshots/pic3.png align="center" width=320 /> |

### 使用说明

1. 点击**新增**按钮可以添加一个商品，点击**提交**按钮后商品信息的增加会展示在主页面。
2. 点击编辑按钮可以修改当前列表一个商品的信息，点击**提交**按钮后商品信息的修改会展示在主页面。
3. 点击**删除**按钮可以删除当前列表的一个商品信息，删除后剩下的商品信息会展示在主页面。
4. 点击**商品**选择项用来筛选商品类别，可以筛选 Mate60/Mate40 系列产品并展示在商品列表。
5. 点击**售价**选择项用来筛选商品价格，可以根据价格筛选产品并展示在主页面。
6. 点击**刷新**按钮，清除筛选条件，展示全部商品。

### 具体实现

本示例分为NDK封装RDB数据库、ArkUI和NDK数据交互两个部分

- NDK封装RDB数据库：

  (1) 通过NDK能力封装RDB数据库。

  (2) 参考文件：RDB.h，RDB.cpp。

  (3) 指南参考：[RelationalStore开发指导 (C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/native-relational-store-guidelines-V5)，[NDK开发导读](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/ndk-development-overview-V5)。

- ArkUI和NDK数据交互：

  (1) 将NDK封装后的数据与ArkUI界面交互。

  (2) 参考文件：napi_init.cpp，index.ets，oh_modules/libentry.so/index.d.ts。

  (3) 指南参考：[NDK开发导读](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/ndk-de


---
## DecodePlayControl
源码: https://gitcode.com/HarmonyOS_Samples/DecodePlayControl

# 基于Surface模式进行视频播放控制

## 项目介绍
本实例基于AVCodec能力实现Surface模式下的视频播控功能，通过调用Native侧解码器与解封装能力，完成视频播放、暂停、进度调整、资源切换及倍速播放等核心操作；可帮助开发者理解并掌握Surface模式下视频解码能力及解码流程的开发方法。
## 效果预览

| 应用主界面                                              |
|----------------------------------------------------|
| ![AVCodec_Index.png](screenshots/device/Index.png) |

## 使用说明

1. 进入首页后，点击下方的选集按钮进行播放，播放中点击不同的选集可切换视频播放。
2. 播放界面中，点击左侧播放和暂停按钮可控制视频播放状态。
3. 滑动进度条可调整视频播放进度。
4. 点击倍速按钮可进行视频播放速度切换。
5. 点击全屏播放按钮可进行视频横向全屏播放。

## 工程目录

```       
├──entry/src/main/cpp                 // Native层
│  ├──capabilities                  // 系统解码能力
│  │  ├──include                
│  │  │  ├──AudioDecoder.h         // 音频解码能力接口
│  │  │  ├──CodecCallback.h        // 解码回调接口
│  │  │  ├──Demuxer.h              // 解封装能力接口       
│  │  │  └──VideoDecoder.h         // 视频解码能力接口
│  │  └──src
│  │     ├──AudioDecoder.cpp       // 音频解码能力实现
│  │     ├──CodecCallback.cpp      // 解码回调实现
│  │     ├──Demuxer.cpp            // 解封装能力实现       
│  │     └──VideoDecoder.cpp       // 视频解码能力实现
│  ├──common                       // 解码公共工具
│  │  └──include      
│  │     ├──AudioSampleInfo.h      // 音频解码数据信息   
│  │     ├──MediaError.h           // 异常转态枚举
│  │     ├──MediaLog.h             // 宏定义日志
│  │     ├──SampleInfo.h           // 解码数据信息
│  │     └──VideoSampleInfo.h      // 视频解码数据信息
│  ├──player                       // 视频解码业务
│  │  ├──include
│  │  │  ├──Player.h               // 视频解码播放和控制接口       
│  │  │  └──playerNative.h         // Native交互接口          



---
## DesktopExtensionKit-samplecode
> 本示例展示了应用通过Desktop Extension Kit接口接入状态栏的能力。

源码: https://gitcode.com/HarmonyOS_Samples/DesktopExtensionKit-samplecode

# DesktopExtensionKit-samplecode

本示例展示了应用通过Desktop Extension Kit接口接入状态栏的能力。


---
## DesktopShortcut
源码: https://gitcode.com/HarmonyOS_Samples/DesktopShortcut

# 通过module.json5文件配置应用快捷打开方式入口
## 介绍
桌面快捷方式能让用户快速访问应用的核心功能，有效提高操作效率，同时增加用户对应用的依赖性。

以导航场景为例，为常去的地点（例如家、公司等）创建导航方式，点击即可启动地图应用并开始导航。
## 预览效果
![](/screenshots/image.gif)
## 工程目录
````
├──entry/src/main/ets                                   // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages                              
│  │  ├──GoCompany.ets                                  // 我的公司页
│  │  ├──GoHouse.ets                                    // 我的家页
│  │  └──Index.ets                                      // 首页
│  └──util
│     └──CommonFunction.ets                             // 公共方法
└──entry/src/main/resources                             // 应用资源目录
````
## 使用说明
长按应用图标，即可出现快捷方式列表。点击对应图标，即可快速打开应用中对应的页面。
## 实现说明
* 在/resources/base/profile/目录下配置shortcuts_config.json配置文件。

* 在module.json5配置文件的abilities标签中，针对需要添加快捷方式的UIAbility进行配置metadata标签，使shortcut配置文件对该UIAbility生效。

## 相关权限
无
## 约束与限制
* 本示例仅支持标准系统上运行，支持设备：华为手机。

* HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

* DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

* HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## DeviceSecurityKit_sampleCode_SafetyDetectDemo_ArkTS
> 本示例基于Device Security Kit（设备安全服务）的安全检测功能，对应用设备所处环境、URL链接做检测，以支撑业务识别风险。

源码: https://gitcode.com/HarmonyOS_Samples/DeviceSecurityKit_sampleCode_SafetyDetectDemo_ArkTS

# 实现安全检测（ArKTS）

## 介绍

本示例向您介绍如何在应用中获取系统完整性检测、系统完整性本地检测、系统完整性增强检测和URL检测的结果。

需要使用设备安全服务接口 **@kit.DeviceSecurityKit**。

## 效果预览
![效果图](screenshots/device/home_page.png)

## Sample工程的配置与使用

### 在DevEco中配置Sample工程的步骤如下

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
2. 打开Sample应用，使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)配置的应用包名替换app.json5文件中的bundleName属性值。
3. 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)开通安全检测服务，具体请参考[Device Security Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)。

#### Sample工程使用说明
1. 运行该 Sample 应用前，先对设备进行联网。
2. 运行该 Sample 应用，点击"SysIntegrity"按钮获取系统完整性检测结果，点击"SysIntegrityOnLocal"按钮获取系统完整性本地检测结果，点击"SysIntegrityEnhanced"按钮获取系统完整性增强检测结果，点击"UrlThreat"按钮获取URL检测结果，如果获取成功，页面会显示检测结果，如果获取失败，页面会显示相应的错误码。

## 工程目录

```
├─entry/src/main/ets       // 代码区。
│ ├─entryability
│ │ └─EntryAbility.ets     // 程序入口类。
│ ├─model
│ │ └─SafetyDetectModel.ts // 系统完整性检测、系统完整性本地检测、系统完整性增强检测和URL检测结果获取类。
│ ├─pages
│ │ └─Index.ets            // 首页，获取系统完整性检测、系统完整性本地检测、系统完整性增强检测和URL检测结果的页面。
```
## 具体实现

本示例展示系统完整性检测、系统完整性本地检测、系统完整性增强检测和URL检测的功能在页面中直接调用，使用safetyDetect.checkSysIntegrity()方法获取当前设备的系统完整性检测结果，使用safetyDetect.checkSysIntegrityOnLocal()方法获取当前设备的系统完整性本地检测结果，使用safetyDetect.checkSy


---
## DialogHub
源码: https://gitcode.com/HarmonyOS_Samples/DialogHub

# 基于DialogHub实现通用弹窗库案例
## 简介
本案例演示了如何利用[DialogHub](https://gitcode.com/openharmony-sig/dialoghub)弹窗框架实现多样化的弹窗需求。
涵盖了常见弹窗类型展示、弹窗与页面及用户的交互模式、弹窗组件的复用技巧，以及在同一页面中有效管理多个弹窗的解决方案。
通过这些实例，您可以快速掌握DialogHub的灵活应用，提升用户界面的交互体验与功能丰富性。

## 效果图预览

| 自定义弹窗                                                      | 跟手弹窗                                                      | 半模态弹窗                                                     | Toast弹窗                                                   |
|------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| <img src="./screenshots/device/zh/custom.png" width="320"> | <img src="./screenshots/device/zh/popup.png" width="320"> | <img src="./screenshots/device/zh/sheet.png" width="320"> | <img src="./screenshots/device/zh/toast.png" width="320"> |

## 使用说明
[查看详情](https://gitcode.com/openharmony-sig/dialoghub)

## 工程目录
```text
├─entry/src/main/ets                         // 代码区
├── components                               // UI组件
│   ├── ActiveCloseBuilder.ets               // 可主动关闭的弹窗Builder
│   ├── AutoDismissBuilder.ets               // 点击蒙层自动关闭的弹窗Builder
│   ├── IconToastBuilder.ets                 // 可透传手势的弹窗Builder
│   ├── ImagePopupBuilder.ets                // 指向选定组件的带箭头弹窗Builder
│   ├── InputBuilder.ets                     // 避让键盘的弹窗Builder
│   ├── InputCallbackBuilder.


---
## DigitalShield
源码: https://gitcode.com/HarmonyOS_Samples/DigitalShield

# 金融数字盾服务

## 介绍
本示例利用Device Security Kit的数字盾服务，开发一个银行转账的数字盾。
通过在可信执行环境(TEE)中开放固定的接口，帮助用户直接调用接口进行身份认证，密钥管理，统一可信UI界面展示，关键资产存储等能力共同构建数字盾能力

## 效果预览
| 数字盾预览                                         | 
|-----------------------------------------------|
| <img src='./screenshots/index.png' width=320> | 

## 使用说明
### 数字盾服务签名申请
1. 完成应用开发准备 (https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview)
2. 开通Device Security服务中的数字盾服务 (https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)
3. 基于服务账号生成鉴权令牌 (https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-token)
4. 将签名补充在build-profile.json5的signingConfigs中

### 编译安装
使用DevEco Studio打开工程，并进行编译安装。

### 生物认证
> 数字盾的生物认证能力依赖于系统录入的指纹和人脸信息，在进行生物信息交易认证前，需要用户在系统设置页面对指纹和人脸信息进行录入

### 应用使用
1. 用户打开应用首先进行数字盾的开通，根据用户需要设置纯数字或数字+英文的格式的初始PIN码开通数字盾
2. 用户根据需要对数字盾PIN码进行修改，同样可选纯数字或数字+英文的格式
3. 根据设备支持能力类型及个人诉求在应用内绑定指纹或者人脸
4. 进入转账页面，输入转账信息，选择密码(PIN)，人脸(绑定后按钮可见)，指纹(绑定后按钮可见)其中任一方式进行交易认证
5. 根据用户需要，选择需认证或无认证关闭数字盾

## 工程目录

```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets                // Ability的生命周期回调内容
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets          // EntryBackupAbility的生命周期回调内容
│  ├──model                
│  │  └──TrustedAuthentication.ets       // Device Security Kit数字盾能力实现
│  ├──pages                
│  │  ├──Index.ets                       // Navigation导航入口界面
│  │  ├──MainPage.ets                    // 


---
## DocsSample_ArkWeb
源码: https://gitcode.com/HarmonyOS_Samples/DocsSample_ArkWeb

# DocsSample_Arkweb

## 目录

* [ArkWebSchemeHandler: 拦截Web组件发起的网络请求](ArkWebSchemeHandler)

## 使用说明

1. 将独立的应用示例工程导入DevEco Studio进行编译构建及运行调试。
2. 安装运行后，即可在设备上查看应用示例运行效果，以及进行相关调试。


---
## DocsSample_Graphics
源码: https://gitcode.com/HarmonyOS_Samples/DocsSample_Graphics

# DocsSample_Graphics

## 目录

* [ArkTSDrawing： 使用Drawing实现图形绘制与显示的示例（ArkTS）](ArkTSDrawing)
* [ArkTSGraphicsDraw： 图形绘制与显示的示例（ArkTS）](ArkTSGraphicsDraw)
* [NDKAPIDrawing： Drawing API示例（C/C++）](NDKAPIDrawing)
* [NDKDrawing： 使用Drawing实现图形绘制与显示的示例（C/C++）](NDKDrawing)
* [NDKGraphicsDraw： 图形绘制与显示的示例（drawing C/C++）](NDKGraphicsDraw)


## 使用说明

1. 将独立的应用示例工程导入DevEco Studio进行编译构建及运行调试。
2. 安装运行后，即可在设备上查看应用示例运行效果，以及进行相关调试。



---
## DocsSample_MultiMedia
源码: https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia

# DocsSample_MultiMedia

## 目录

* [UsingImageProcessingToProcessImages: 基于ImageProcessing处理图片](UsingImageProcessingToProcessImages)

## 使用说明

1. 将独立的应用示例工程导入DevEco Studio进行编译构建及运行调试。
2. 安装运行后，即可在设备上查看应用示例运行效果，以及进行相关调试。


---
## DocsSample_XComponent
> 本示例主要介绍开发者如何使用ArkTS XComponent组件进行自绘制以及AI分析能力。

源码: https://gitcode.com/HarmonyOS_Samples/DocsSample_XComponent

# DocsSample_XComponent

## 目录

* [ArkTS XComponent组件进行自绘制以及AI分析能力](XComponent)


## 使用说明

1. 将独立的应用示例工程导入DevEco Studio进行编译构建及运行调试。
2. 安装运行后，即可在设备上查看应用示例运行效果，以及进行相关调试。



---
## DragFramework
> 本示例设置组件响应拖拽事件，实现图片、富文本、文本、输入框、列表等组件的拖拽功能。

源码: https://gitcode.com/HarmonyOS_Samples/DragFramework

# 实现组件的自定义拖拽功能

## 介绍

本示例基于ArkUI的拖拽框架，实现图片、富文本、文本、输入框、列表等组件的拖拽功能，通过设置拖拽事件中的接口信息自定义拖拽响应，实现拖拽图像增加水印、自定义拖拽背板图、AI识别拖拽内容等拖拽场景。针对文件类型数据的拖拽，本示例实现了在线图片资源拖拽和本地视频文件拖拽。针对图文混排内容的拖拽，本示例分别基于Text组件、RichEditor组件和手动构造多Entry数据三种方式实现。

## 效果预览

### 效果预览

|                               Image                               |
|:--------------------------------------------------------------:|
| <img src='./screenshots/start.png' width='320'> |

## 使用说明

1.首页展示拖拽功能入口。

2.点击ImageDrag、HyperLinkDrag、RichEditorDrag、TextInputDrag、TextAreaDrag按钮跳转到对应组件的拖拽页面，选中内容后长按可以将组件拖拽到释放区内。

3.点击ListDrag按钮跳转到List组件拖拽页面，选择其中一列要拖拽的内容后，将选中的内容拖拽到另一列。

4.点击BackgroundCustomization按钮跳转到自定义拖拽背板页面，在拖拽图片的过程中显示自定义的背板图。

5.点击WatermarkAdded按钮跳转到拖拽图片增加水印页面，拖拽释放后，在结果图中增加水印。

6.点击AIRecognition按钮跳转到AI识别拖拽内容页面，拖拽释放后，在释放区域内显示文字识别的结果。

7.点击OnlineImage按钮跳转到在线图片拖拽页面，拖拽释放后，在释放区域内显示图片并且将图片保存到本地。

8.点击LocalVideo按钮跳转到本地视频拖拽页面，拖拽释放后，在释放区域内显示视频，同时将视频保存到沙箱路径。

9.点击TextAndImageIndex按钮跳转到图文混排拖拽目录页面。

10.在图文混排拖拽目录页面点击Text按钮跳转到Text组件图文混排内容页面，在拖出方选择图文混排内容，拖拽释放后，在落入方显示图片和文字。

11.在图文混排拖拽目录页面点击RichEditor按钮跳转到RichEditor组件图文混排内容页面，在拖出方选择图文混排内容，拖拽释放后，在落入方显示图片和文字。

12.在图文混排拖拽目录页面点击MultiEntry按钮跳转到MultiEnty图文混排内容页面，在拖出方选择图文混排内容，拖拽释放后，不同接收格式的落入方落入图片和文字内容。

13.点击SpliceScreenDrag按钮创建一个UIAbility，通过手势触发进入待分屏状态且进入任一拖拽页面后，再次点击桌面上的应用图标打开新窗口进入拖拽页面即可实现分屏拖拽。

14.本示例支持跨设备拖拽。

## 工程目录

```
 ├─entry/src/main/ets/                       // 应用首页
 │   ├──common
 │   │  ├──Constants.ets                     // 常量类
 │   │  ├──ResoureUtil.ets                   // 链接工具函数
 │   │  └─


---
## DynamicComponent
> 本示例介绍了在声明式UI中实现组件动态创建的方法.

源码: https://gitcode.com/HarmonyOS_Samples/DynamicComponent

# 实现组件的动态创建功能

### 介绍

本示例通过NodeController绑定自定义节点BuilderNode和布局组件NodeContainer实现组件的动态创建，可以节省组件的创建时间，提升用户体验，同时还可以将独立的逻辑进行封装，有助于应用的模块化开发。

### 效果图预览
| 主页面                                                       | 列表流广告页面                                                 | 动态生成页面                                                                    |
|-----------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------------------------|
| <img src="screenshots/device/MainPage.png" width="300px"> | <img src="screenshots/device/Dialog.png" width="300px"> | <img src="screenshots/device/DynamicallyGeneratePages.png" width="300px"> |

**使用说明**

1. 进入列表流广告组件实践案例后，广告组件随即被动态创建。其分为两种，分别为图片广告与视频广告。
2. 进入动态生成页面实践案例后，点击刷新，即可更换主题图片。

### 实现思路

1. 构建广告组件。源码参考[AdBuilder.ets](./entry/src/main/ets/components/AdBuilder.ets)。
2. 模拟从云端初始化卡片列表，根据云端数据生成普通卡片对象和广告卡片对象。源码参考代码可参考[MainPage.ets](./entry/src/main/ets/pages/MainPage.ets)中的aboutToAppear()。
3. 在布局中，需要判断节点是否是广告节点，若是则预埋NodeContainer节点。当NodeContainer节点要进行渲染时，会调用getAdNodeController方法获取对应的NodeController，通过NodeController中的makeNode接口完成组件上树。源码参考代码可参考[MainPage.ets](./entry/src/main/ets/pages/MainPage.ets)中的build()。
4. 在getAdNodeController中通过queryAdById(adId)模拟了广告信息/布局获取，并在完成信息获取后构建了相应NodeController，并实现makeNode接口。 AdNodeController继承自NodeController，目的是为了给广告模块提供Controller，其中initAd方法通过 this.adNode.build(…)将广告组件添加到rootNode上。
   当NodeContrainer进行绘制时，会调用AdNode


---
## EmebedAbility
> 本示例展示了使用 FullScreenLaunchComponent 全屏启动元服务组件实现嵌入式拉起元服务的能力。

源码: https://gitcode.com/HarmonyOS_Samples/EmebedAbility

# 实现嵌入式拉起元服务功能

### 介绍

本示例使用了FullScreenLaunchComponent组件，当被拉起方元服务授权使用方元服务嵌入式运行时，使用方可以通过FullScreenLaunchComponent组件将被拉起方元服务以全屏方式展示出来。通过全屏显示，可以让用户更加沉浸在元服务的界面中，享受更好的视觉效果和交互体验。

### 效果预览

![phone.gif](screenshots/device/phone.gif)

### 工程目录

```
├──entry/src/main/ets/                         
│  ├──entryability
│  │  └──EntryAbility.ets                           // 程序入口类
│  └──pages
│     └──mainPage.ets                               // 主页入口                                                   
└──entry/src/main/resource                          // 应用静态资源目录
```

### 具体实现

使用 FullScreenLaunchComponent 全屏启动元服务组件实现嵌入式拉起元服务。

### 相关权限

不涉及。

### 使用说明

1. 分别手机、折叠屏安装并打开元服务，同时在开发者选项中开启元服务豁免管控。
2. 点击界面上图标，已安装对应元服务的场景下可实现全屏嵌入式运行元服务。
3. 点击界面上图标，未安装对应元服务的场景下跳出式拉起元服务。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS 系统：HarmonyOS 5.0.0 Release及以上。
3. DevEco Studio 版本：DevEco Studio 5.0.0 Release及以上。
4. HarmonyOS SDK 版本：HarmonyOS 5.0.0 Release SDK及以上。


---
## ExecutingJSWithJSVM
源码: https://gitcode.com/HarmonyOS_Samples/ExecutingJSWithJSVM

# 使用JSVM-API接口创建多个引擎执行JS代码并销毁
### 简介
本示例展示了如何使用JSVM-API在ArkTS环境中，动态传入JavaScript或自定义的Native函数代码字符串到Native侧执行，并在执行完成后获取执行结果，同时销毁Native侧执行环境，通过在Native侧执行ArkTS代码可以加快代码执行效率，提高程序性能表现。

### 效果预览

![image](screenshots/device/phone.png)

### 使用说明
本项目提供高效的JavaScript代码执行方案，开发者可通过底部按钮将预设代码或自定义函数传递至Native侧执行，以优化特定代码段的运行效率。支持灵活修改测试代码，并可参考项目实现进行二次开发。

### 工程目录

```  
├──entry/src/main
│  ├──cpp                             // Native层
│  │  ├──types/libentry
│  │  │  └──index.d.ts                // 暴露给ArkTS侧的接口  
│  │  ├──CMakeLists.txt               // 编译入口  
│  │  ├──common.h                     // 头文件  
│  │  └──create_jsvm_runtime.cpp      // 创建jsvm的Native方法封装     
│  └──ets                             // UI层  
│     ├──entryability
│     │  └──EntryAbility.ets          // 应用入口
│     ├──entrybackupability  
│     │  └──EntryBackupAbility.ets  
│     └──pages                        
│        └──Index.ets                 // 应用主页面  
└──entry/src/main/resources           // 应用资源目录  
```  

### 具体实现

通过在Native侧自定义创建JS执行环境，传入要执行的JS代码或自定义函数的字符，即可在Native侧进行函数执行，执行完成后自行实现并调用释放执行环境的releaseJsCore()方法。

### 相关权限

不涉及

### 约束与限制
1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## FoldedHover
> 本示例基于折叠屏提供的手持操作体验“悬停态”，即可将设备半折后立在桌面上，适用于不需要频繁进行交互的场景。

源码: https://gitcode.com/HarmonyOS_Samples/FoldedHover

# 实现折叠屏悬停态

### 简介

本示例基于折叠屏提供的手持操作体验“悬停态”，即可将设备半折后立在桌面上，适用于不需要频繁进行交互的场景，例如视频通话，视频播放等，折叠屏进入悬停态时，中间弯折的区域难以操作且内容会变形，需要进行避让。本示例提供实现折叠屏悬停态的三种实现方式：FolderStack组件，FoldSplitContainer组件以及自定义组件。

### 效果预览：

| FolderStack组件实现悬停态              | FoldSplitContainer组件实现悬停态       | 自定义组件实现悬停态                      |
|---------------------------------|---------------------------------|---------------------------------|
| ![image](screenshots/page1.png) | ![image](screenshots/page2.png) | ![image](screenshots/page3.png) |

### 使用说明：

1. 打开应用进入主页面后，会有三种实现悬停态页面的按钮，在此页面横屏半折设备直接进入自定义实现悬停态的页面，并展现悬停态（注意：只有在半折叠横屏状态下能上下开合的折叠屏设备才可实现悬停态效果）。

2. 点击第一个按钮，进入FolderStack组件实现悬停态页面，可对页面内的视频进行操作，横屏半折状态可进入悬停态，此时页面可自由旋转。

3. 点击第二个按钮，进入FoldSplitContainer组件实现悬停态页面，页面是仿照游戏页面进行布局，未实现操作功能，且只能保持二分栏状态，横屏半折状态可进入悬停态，此时页面可自由旋转。

4. 点击第三个按钮，进入自定义组件实现悬停态页面，可对页面内的视频进行操作，横屏展开状态下半折叠可进入悬停态，此时页面仅可横向旋转。

5. 本示例全量功能支持双折叠，三折叠仅M态下仅支持FoldSplitContainer组件和自定义组件实现悬停态，FolderStack组件不支持悬停态。

### 工程目录

```
├──entry/src/main/ets
│  ├──common
│  │  ├──utils      
│  │  │  ├──AVPlayerUtil.ets            // 媒体工具类   
│  │  │  ├──DisplayUtil.ets             // 显示工具类   
│  │  │  └──WindowUtil.ets              // 窗口工具类
│  │  └──CommonConstants.ets            // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets        
│  ├──pages                  
│  │  └──Index.ets                      // 首页
│  └──view
│     ├──basicview                      
│     │  ├──BackTitleView.


---
## FunctionFlowRuntimeKit-SampleCode-ConcurrentQueue
> 本示例基于FFRT提供的并发队列特性，通过银行服务系统样例的简易实现向开发者展示具体的特性使用方式

源码: https://gitcode.com/HarmonyOS_Samples/FunctionFlowRuntimeKit-SampleCode-ConcurrentQueue

# FunctionFlowRuntimeKit-SampleCode-ConcurrentQueue

本示例基于FFRT提供的并发队列特性，通过银行服务系统样例的简易实现向开发者展示具体的特性使用方式


---
## FunctionFlowRuntimeKit-SampleCode-SerialQueue
> 本示例基于FFRT提供的串行队列特性，通过异步日志系统样例的简易实现向开发者展示具体的特性使用方式

源码: https://gitcode.com/HarmonyOS_Samples/FunctionFlowRuntimeKit-SampleCode-SerialQueue

# FunctionFlowRuntimeKit-SampleCode-SerialQueue

本示例基于FFRT提供的串行队列特性，通过异步日志系统样例的简易实现向开发者展示具体的特性使用方式


---
## FunctionFlowRuntimeKit-SampleCode-TaskGraph
> 本示例基于FFRT提供的图依赖并发特性，通过斐波那契与流媒体视频处理的简易样例实现向开发者展示具体的特性使用方式。

源码: https://gitcode.com/HarmonyOS_Samples/FunctionFlowRuntimeKit-SampleCode-TaskGraph

# FunctionFlowRuntimeKit-SampleCode-TaskGraph

本示例基于FFRT提供的图依赖并发特性，通过斐波那契与流媒体视频处理的简易样例实现向开发者展示具体的特性使用方式。


---
## GenerateSandboxFile
源码: https://gitcode.com/HarmonyOS_Samples/GenerateSandboxFile

# 实现一键生成沙箱文件功能

## 介绍

本示例基于文件I/O接口和不同的数据库distributedKVStore,preferences,relationalStore接口，实现了一键在终端内生成沙箱文件、用户首选项、kv数据库、
关系型数据库文件功能，便于用户调试终端与电脑间的文件传输。


## 效果预览
| **主页**                                          | **文件列表**                                       |
|-------------------------------------------------|------------------------------------------------|
| <img src="screenshots/Main.png" width="240px"> | <img src="screenshots/File.png" width="240px"> |


## 使用说明

1.点击生成文件，即可在终端内生成应用文件和数据库文件。

2.点击文件列表，即可查看终端内生成的文件名称和类型。

### 具体实现

1.通过fileIo，distributedKVStore，preferences，relationalStore接口在终端沙箱目录生成文件与数据库文件。

2.通过在终端沙箱目录搜寻对应的文件名来验证文件是否生成。

## 工程目录
```
├──entry/src/main/ets
│  ├──common
│  │  └──Logger.ets                            // 日志类  
│  ├──entryability
│  │  └──EntryAbility.ets                      // 程序入口类 
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                // 数据备份恢复类
│  ├──pages
│  │  └──Index.ets                             // 主页页面  
│  └──view
│     └──File.ets                              // 文件列表页面
└──entry/src/main/resources                    // 应用资源目录
```

## 相关权限

ohos.permission.INTERNET：允许使用Internet网络。

## 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## GeneratingUserDirectoryEnvironmentFile
源码: https://gitcode.com/HarmonyOS_Samples/GeneratingUserDirectoryEnvironmentFile

# 实现生成用户目录文件功能

## 介绍

本示例基于文件I/O接口和Environment接口，实现了一键在PC/2in1设备内生成Document目录、Download目录、Desktop目录文件功能，便于用户理解在
Document目录、Download目录、Desktop目录的文件交互。


## 效果预览
| **主页**                                          |
|-------------------------------------------------|
| <img src="screenshots/image.png" width="800px"> |


## 使用说明

输入文件名字和信息，点击目标目录插入文件，即可在对应目录生成目标文件。


### 具体实现

通过fileIo和Environment接口在PC/2in1设备生成用户目录文件。

## 工程目录
```
├──entry/src/main/ets 
│  ├──common
│  │  └──Logger.ets                            // 日志类 
│  ├──entryability
│  │  └──EntryAbility.ets                      // 程序入口类 
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                // 程序出口类
│  └──pages
│     └──Index.ets                             // 主页面
└──entry/src/main/resources                   // 应用资源目录
```

## 相关权限

- ohos.permission.READ_WRITE_DOCUMENTS_DIRECTORY：允许应用访问公共目录下的Documents目录及子目录。Allows an application to access the Documents directory and its subdirectories in the user directory.
- ohos.permission.READ_WRITE_DOWNLOAD_DIRECTORY：允许应用访问公共目录下Download目录及子目录。
- ohos.permission.READ_WRITE_DESKTOP_DIRECTORY：允许应用访问公共目录下Desktop目录及子目录。

- 请[采用受限权限申请方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl)申请使用以上权限。

## 约束与限制

1.本示例仅支持标准系统上运行，支持设备：PC/2in1。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## GesturesShare
源码: https://gitcode.com/HarmonyOS_Samples/GesturesShare

# 基于Share Kit实现隔空传送分享文件和链接

## 项目简介

本示例基于Share Kit实现快速跨设备分享文件，结合App Linking实现了快速跨设备分享链接并直接进入应用内视频播放页面的功能。通过harmonyShare.on('gesturesShare')方法注册隔空传送监听事件，并在回调中使用sharableTarget.share()方法分享文件或者分享App Linking链接，从而实现让用户通过“一抓一放”实现跨端传输。

## 效果预览

| 首页                                                 | 隔空传送文件分享页面                                        | 隔空传送链接分享页面                                         |
|----------------------------------------------------|---------------------------------------------------|----------------------------------------------------|
| <img src="screenshots/device/index.png" width=320> | <img src="screenshots/device/file.png" width=320> | <img src="screenshots/device/video.png" width=320> |

## 使用说明

1. 在运行项目前，需要完成App Linking的配置，以及对应用进行手动签名，具体可以参考[使用App Linking实现应用间跳转](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startup)。
2. 在完成App Linking的配置后，请前往[ShareModel.ets](feature/share/src/main/ets/model/ShareModel.ets)文件，将share()方法中的content参数替换为真实可用的链接地址，同时将[module.json5](product/entry/src/main/module.json5)文件中uris的host修改为可用的域名。
3. 设备A和设备B均安装运行示例代码，在亮屏、解锁的状态下并且都已开启华为分享服务（系统默认开启）。
4. 打开[设备侧隔空传送开关](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gestures-share-open)。
5. 设备A进入首页点击隔空传送文件按钮，进入隔空传送文件页面，勾选文件后通过隔空传送手势分享文件到设备B。
6. 设备A进入首页点击隔空传送链接按钮，进入隔空传送链接页面，在当前页面通过隔空传送手势分享链接到设备B，设备B直接拉起应用进入视频播放界面。

## 工程目录

```
├──common/src/main/ets
│  ├──constants
│  │  └──BreakpointConstants.ets                 //断点常量定义
│  ├──utils
│  │  ├──B


---
## Graphics3D
> 本实例主要介绍3D引擎提供的接口功能。

源码: https://gitcode.com/HarmonyOS_Samples/Graphics3D

# 基于3D引擎接口实现3D图形渲染功能

### 介绍

本实例主要介绍3D引擎提供的接口功能。提供了@ohos.graphics.scene中接口的功能演示。
3D引擎渲染的画面会被显示在Component3D这一控件中。点击按钮触发不同的功能，用户可以观察渲染画面的改变。

### 效果预览

| 主页                             | container                           | node_base                      | node_camera                      |
| ------------------------------ | ----------------------------------- | ------------------------------ | -------------------------------- |
| ![](screenshots/main_page.jpg) | ![](screenshots/node_container.jpg) | ![](screenshots/node_base.jpg) | ![](screenshots/node_camera.jpg) |

| node_light                                         | scene_environment                                         | scene_animation                                         | scene_shader                                         |
| -------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------- |
| <img src='./screenshots/node_light.jpg' width=320> | <img src='./screenshots/scene_environment.jpg' width=320> | <img src='./screenshots/scene_animation.jpg' width=320> | <img src='./screenshots/scene_shader.jpg' width=320> |

使用说明

1. 在主界面，可以点击按钮进入不同的子页面，每一个子页面分别测试了一类3D引擎的接口功能，在子页面点击back返回主界面。
2. 在container界面，点击按钮，可以添加、移除子节点，节点的结构信息已打印在界面上。在本示例中操作的子节点是一个头盔模型。
3. 在node_base界面，点击按钮对节点的基础属性如位置、旋转、大小、可见性等进行操作。在本示例中操作的子节点是一个头盔模型。
4. 在node_camera界面，点击按钮对相机的属性如投影、后处理等进


---
## GridScrollComponent
源码: https://gitcode.com/HarmonyOS_Samples/GridScrollComponent

# 基于ScrollComponents实现网格

## 项目简介

本示例展示了使用ScrollComponents构建网格页面，覆盖场景包括

- 网格单元格组件复用，以及跨页面的组件复用场景
- 网格加速首屏渲染的场景
- 网格数据处理场景：下拉刷新、上拉加载、长按删除
- 网格设置排列方式场景
- 网格显示数据场景
- 网格设置行列间距场景
- 网格可滚动布局场景
- 网格控制滚动位置场景
- 网格嵌套滚动场景
- 网格单元格拖拽场景
- 网格自适应和自适应列场景
- 网格以当前行最高的单元格的高度为其他单元格的高度场景
- 网格设置边缘渐隐场景
- 网格设置单元格样式场景

## 效果预览

<img src="./screenshots/img.webp" width = "320" alt="图片名称"/>

## 使用说明

1. 打开应用首页，显示场景列表。点击PhotoGridPage，实现网格单元格结构相同的组件复用场景、网格设置排列方式场景。
2. 返回首页，点击WorkGridPage，实现网格单元格结构类型不同的组件复用场景、和PhotoGridPage.ets的网格跨页面复用场景、网格下拉刷新场景、网格上拉加载更多场景、网格单元格拖拽场景、网格嵌套滚动场景、网格设置边缘渐隐场景。
3. 返回首页，点击CardGridPage，实现网格单元格内子结构可拆分组合的组件复用场景、网格加速首屏渲染场景、网格显示数据场景、网格设置行列间距场景、网格可滚动布局场景、网格设置单元格格式场景、网格长按删除单元格场景。
4. 返回首页，点击NumberGridPage，实现网格自适应场景。
5. 返回首页，点击WordGridPage，实现网格自适应列场景、网格以当前行最高的单元格高度为其他单元格高度场景

## 工程目录

```
├──entry/src/main/ets                     // 代码区
│  ├──common
│  │  ├──constants
│  │  │  └──CommonConstants.ets           // 常量
│  │  └──utils           
│  │     ├──ContextUtil.ets               // 工具
│  │     ├──Logger.ets                    // 日志
│  │     └──Utils.ets                     // 工具
│  ├──entryability
│  │  └──GridAbility.ets                  // 应用入口
│  ├──model
│  │  ├──mock.ets                         // 模拟数据
│  │  ├──types.ets                        // 数据模型
│  │  ├──PhotoModel.ets                   // 图片数据
│  │  ├──WorkModel.ets                    // 作品数据
│  │  ├──UserInfoModel.ets                // 用户信息数据
│  │  ├──NumberModel.ets                  // 数字数据
│  │  └──WordModel.ets          


---
## H5Launch
源码: https://gitcode.com/HarmonyOS_Samples/H5Launch

# 实现H5应用冷启动加速功能

## 介绍

本示例主要介绍了使用数据缓存及预解析和预连接优化、资源拦截替换加速、预编译JavaScript生成字节码缓存（Code Cache）、离线资源免拦截注入等最佳实践方案来加速H5 web应用冷启动时延，帮助用户实现H5应用冷启动达标。

## 效果预览

<img src="screenshots/device/app.gif" width="320" />

## 工程目录

```markdown
├──entry/src/main/ets/
│  ├──common
│  │  ├──constant                  
│  │  │  └──CommonConstants.ets               // 公共常量
│  │  ├──types  
│  │  │  └──CommonTypes.ets                   // 公共类型
│  │  └──utils 
│  │     └──Common.ets                        // 工具类
│  ├──entryability
│  │  └──EntryAbility.ets                     // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets               // 备份恢复派生类
│  └──pages                 
│     └──Index.ets                            // H5页面入口
└──entry/src/main/resources                   // 应用资源目录
```

## 使用说明

1. 搭建nodejs环境：H5 Web网站是基于nodejs实现的，需要安装nodejs，如果您本地已有nodejs环境可以跳过此步骤。
    1. 检查本地是否安装nodejs：打开命令行工具（如Windows系统的cmd和Mac电脑的Terminal，这里以Windows为例），输入node -v，如果可以看到版本信息，说明已经安装nodejs。

       ![](screenshots/device/node.PNG)

    2. 如果本地没有nodejs环境，您可以去nodejs官网上下载所需版本进行安装配置。
    3. 配置完环境变量后，重新打开命令行工具，输入node -v，如果可以看到版本信息，说明已安装成功。
2. 启动H5网站：在本项目的h5web目录下打开命令行工具，输入npm install 安装服务端依赖包，安装成功后输入npm run server点击回车。看到“服务器启动成功！”则表示服务端已经在正常运行。
3. 构建局域网环境：测试本Sample时要确保运行H5网站的电脑和测试机连接的是同一局域网下的网络，您可以用您的手机开一个个人热点，然后将测试机和运行H5网站的电脑都连接您的手机热点进行测试。

   ![](screenshots/device/npm.jpg)

4. 连接H5网站地址：打开命令行工具，输入ipconfig命令查看本地ip，将本地ip地址复制到src/main/ets/common/constant/CommonConstants.ets文件下的16行，注意只替换ip地址部分，不要修改端口号，保存好i


---
## HMMediaDiagnosticsTool
源码: https://gitcode.com/HarmonyOS_Samples/HMMediaDiagnosticsTool

# 实现音频类应用能力检测功能

## 简介
本场景主要提供检测音频类应用能力的功能，用于检测音频类应用在不同音频场景下的功能完备度和准确性，支持如音频后台播放、来电接听、闹钟、播控中心音频控制、VoIP 通话、导航、语音助手播报、静音播放等多种场景。

#### 效果图预览

| 主页面                                                      | 确认页                                                         | 打分页                                                       | 得分页                                                       |
|----------------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| <img src="./screenshots/device/zh/main.png" width="320"> | <img src="./screenshots/device/zh/confirm.png" width="320"> | <img src="./screenshots/device/zh/check.png" width="320"> | <img src="./screenshots/device/zh/score.png" width="320"> |

## 工程主要模块结构

```
├──entry/src/main/ets/
│  ├──common
│  │  ├──constants                     // 常量
│  │  │  └──ResourceConstant.ets       // 资源常量
│  │  ├──store                         // 全局变量
│  │  │  ├──AppStore.ets               // 步骤计数，操作结果等变量
│  │  │  ├──DataInterface.ets          // 配置数据对应的接口
│  │  │  └──Score.ets                  // 步骤计数及操作结果需要的接口和类
│  │  └──utils                         // 工具
│  │     ├──ConfirmService.ets         // 特殊确认弹框使用的函数
│  │     ├──GenerateFileTips.ets       // 文件生成提示框
│  │     └──ListBorder.ets             // 设置列表边框
│  ├──components                       // 各模块组件
│  │  ├──CheckList.ets    


---
## HMOS_LiveAudioCall
> 本示例在媒体直播案例基础上实现了媒体直播连麦功能

源码: https://gitcode.com/HarmonyOS_Samples/HMOS_LiveAudioCall

# 基于媒体子系统实现媒体直播连麦功能

## 项目简介

本示例基于媒体子系统，实现媒体直播的开直播端、看播端和直播连麦模块。实现了直播场景常用的音视频采集、音视频播放、音频焦点管理、ROI、
背景音乐添加、前后摄像头翻转等功能。基于本示例可帮助应用开发开启直播和观看直播的场景。

- 看播端是通过播放视频文件来模拟的，主要流程是将直播端录制的视频文件通过AvPlayer播放。
- 直播端视频录制的主要流程是相机采集->Opengl旋转->编码->封装成mp4文件。
- 直播过程通过分布式文件进行模拟。两台手机分别模拟直播端和看播端，须登录同一个华为账号并开启WIFI和蓝牙，完成分布式组网。具体流程为：直播端
  将录制的视频文件保存到沙箱并拷贝到分布式目录中，看播端将分布式文件下的视频文件拷贝到沙箱后，通过AvPlayer进行播放。
- 录制场景在相机和编码之间加了OpenGL渲染管线，开发者可参考该流程加上对应的Shader，如直播场景加上美颜、滤镜等算子。
- 直播连麦是在录制视频的同时，对上一次直播录制的mp4文件进行编解码。上半屏使用相机录制视频，实现逻辑参考本节第二条直播端视频录制。下半屏点击加入连麦后，会对上次直播产生的视频文件进行编解码播放。

### 播放支持的原子能力规格

| 媒体格式 | 封装格式    | 码流格式                                |
|------|:--------|:------------------------------------|
| 视频   | mp4     | 视频码流：H.264/H.265， 音频码流：AAC          |
          

### 录制支持的原子能力规格

| 封装格式 | 视频编解码类型     | 音频编解码类型 | 
|------|-------------|---------|
| mp4  | H.264/H.265 | AAC |

## 效果预览

| 应用主界面                                                      | 直播页                                                                                     | 看播页                                                                                 | 加入连麦页                                                                              | 直播连麦页                                                                                |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------


---
## HMOS_LiveStream
> 基于HarmonyOS媒体子系统实现媒体直播开播端和看播端方案。

源码: https://gitcode.com/HarmonyOS_Samples/HMOS_LiveStream

# 基于HarmonyOS媒体子系统实现媒体直播功能

## 项目简介

本示例基于HarmonyOS媒体子系统，实现媒体直播的开直播端和看播端。本示例实现了直播场景常用的音视频采集、音视频播放、音频焦点管理、ROI、
背景音乐添加、前后摄像头翻转等功能。基于本示例可帮助应用开发开启直播和观看直播的场景。

- 看播端是通过播放视频文件来模拟的，主要流程是将直播端录制的视频文件通过AvPlayer播放。
- 直播端视频录制的主要流程是相机采集->Opengl旋转->编码->封装成mp4文件。
- 直播过程通过分布式文件进行模拟。两台手机分别模拟直播端和看播端，须登录同一个华为账号并开启WIFI和蓝牙，完成分布式组网。具体流程为：直播端
  将录制的视频文件保存到沙箱并拷贝到分布式目录中，看播端将分布式文件下的视频文件拷贝到沙箱后，通过AvPlayer进行播放。
- 录制场景在相机和编码之间加了OpenGL渲染管线，开发者可参考该流程加上对应的Shader，如直播场景加上美颜、滤镜等算子。

### 播放支持的原子能力规格

| 媒体格式 | 封装格式    | 码流格式                                |
|------|:--------|:------------------------------------|
| 视频   | mp4     | 视频码流：H.264/H.265， 音频码流：AAC          |
          

### 录制支持的原子能力规格

| 封装格式 | 视频编解码类型     | 音频编解码类型 | 
|------|-------------|---------|
| mp4  | H.264/H.265 | AAC |

## 效果预览

| 应用主界面                                                                            | 直播页                                                                                      | 看播页                                                                                  |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <img src="screenshots/device/Index_zh.png" width="320"  alt="App Home Screen" /> | <img src="screenshots/device/StartLive_zh.png" width="320"  alt="Live Streaming Demo" /> | <img src="screenshots/d


---
## HMRouter
源码: https://gitcode.com/HarmonyOS_Samples/HMRouter

# 基于HMRouter的页面跳转
## 项目简介
本示例展示了使用HMRouter路由框架在各种页面跳转场景中的使用，覆盖场景

- 一次开发多端部署
- 路由跳转及拦截跳转场景
- 生命周期配置使用场景
- 转场动画配置使用场景

## 效果预览

 <img src="./screenshots/image.png" width="320">

## 工程目录
```
├─entry/src/main/ets                         // 代码区
├── animation                                // 自定义动画
|  └── CustomPageAnimator.ets
├── component                                // HMRouter页面代码
|  ├── common
|  |  ├── ConfirmDialog.ets
|  |  ├── ReturnHeader.ets
|  |  ├── constants
|  |  |  ├── BreakpointConstants.ets
|  |  |  ├── CommonConstants.ets
|  |  |  ├── DetailConstants.ets
|  |  |  ├── HomeConstants.ets
|  |  |  ├── LiveConstants.ets
|  |  |  ├── LoginConstants.ets
|  |  |  ├── MineConstants.ets
|  |  |  ├── PayConstants.ets
|  |  |  └── ShoppingBagConstants.ets
|  |  └── utils
|  |     ├── BreakpointType.ets
|  |     ├── ResourceUtil.ets
|  |     └── SelectAnimatorItem.ets
|  ├── home
|  |  ├── Categories.ets
|  |  ├── CommonView.ets
|  |  ├── HomeContent.ets
|  |  ├── HomeHeader.ets
|  |  ├── RecommendedProductView.ets
|  |  └── WelfareView.ets
|  ├── live
|  |  ├── Comment.ets
|  |  ├── CommentInput.ets
|  |  ├── Live.ets
|  |  ├── LiveCommentFooter.ets
|  |  ├── LiveComments.ets
|  |  ├── LiveCommentsHeader.ets
|  |  ├── LiveHome.ets
|  |  ├── LiveMaskLayer.ets
|  |  ├── LiveShopList.ets
|  |  ├── LiveVideo.ets
|  |  └── LiverHeader.ets
|  ├── login
|  |  └── LoginPage.ets
|  ├── mine
|  |  ├── AnimatorTransition.ets
|  |  ├── ExitLogin.ets
|  |  ├── MineContent.ets
|  |  └


---
## HarmonyOSComponentUXExamples
> 开发者可直接复用代码或参考UI实现组件，打造符合HarmonyOS Design规范的“原生感”视觉体验。项目涵盖操作、容器、输入、导航、展示、选择六大类核心组件的样式与交互实现。

源码: https://gitcode.com/HarmonyOS_Samples/HarmonyOSComponentUXExamples

# ArkUI组件示例集合

## 项目简介

本项目是一个基于ArkUI的UI组件示例集合，旨在为开发者提供一套符合**HarmonyOS Design**设计规范的组件实现参考。

项目通过组合基础组件与样式特性，展示了如何在鸿蒙应用中打造具有“原生感”的视觉体验。开发者可以直接复用代码，或参考其实现逻辑定制自己的业务组件。本项目涵盖了六大类核心组件的样式与交互实现，具体包含：

- 操作类组件：[按钮](https://developer.huawei.com/consumer/cn/doc/design-guides/button-0000001929683228)、[核心操作栏](https://developer.huawei.com/consumer/cn/doc/design-guides/component_actionbar-0000002306891560)、[菜单](https://developer.huawei.com/consumer/cn/doc/design-guides/menu-0000001957001877)；
- 容器类组件：[半模态面板](https://developer.huawei.com/consumer/cn/doc/design-guides/bindsheet-0000001956852753)、[弹出框](https://developer.huawei.com/consumer/cn/doc/design-guides/dialog-0000001957012569)、[列表](https://developer.huawei.com/consumer/cn/doc/design-guides/list-0000001929853910)；
- 输入类组件：[数字加减](https://developer.huawei.com/consumer/cn/doc/design-guides/counter-0000001929853284)、[搜索框](https://developer.huawei.com/consumer/cn/doc/design-guides/search-0000001956852741)、[文本框](https://developer.huawei.com/consumer/cn/doc/design-guides/textinput-0000001957012557)；
- 导航类组件：[底部页签](https://developer.huawei.com/consumer/cn/doc/design-guides/bottomtab-0000001956787789)、[子页签](https://developer.huawei.com/consumer/cn/doc/design-guides/chipsgroup-0000001929788350)、[标题栏](https://developer.huawei.com/consumer/cn/doc/design-guides/titlebar-0000001929628982)；
- 展示类组件：[新事件标记](https://developer.huawei.com/consumer/cn/doc/design-guides/badge-0000001929816016)、[进度条](https://developer.huawei.com/consumer/cn/doc/design-guide


---
## HiTraceMeterPrefTag
源码: https://gitcode.com/HarmonyOS_Samples/HiTraceMeterPrefTag

# 基于HiTraceMeter实现性能打点功能

### 简介

本示例主要介绍使用HiTraceMeter实现性能打点，包括在ArkTS侧、Native侧、组件回调中、自定义组件生命周期中进行打点。 开发者可以使用HiTraceMeter进行打点分析，判断应用具体耗时点并进行合理的优化，提高应用性能。

### 效果预览
![](screenshots/device/HiTraceMeterPerfTag.gif) 

### 使用说明

点击对应按钮会分别跳转到不同场景的页面。 在ArkTS侧HiTraceMeter打点与Native侧HiTraceMeter打点页面中，包含了一个按钮，点击按钮会执行耗时任务并进行打点计时，调用完成后会弹窗显示结果。在组件回调耗时打点页面中，包含了一个Grid组件和一个按钮，点击按钮会跳转到Grid指定位置并进行打点记录。在生命周期耗时打点页面中，包含了一个List列表，在组件刷新时会进行组件复用，在组件复用的生命周期回调中进行打点记录判断其生命周期耗时。

#### 打点信息查询
1. 通过DevEco Studio的Profiler工具查看
   1. 运行项目，然后通过Profiler工具选择应用线程，创建CPU分析任务抓取数据，录制期间需要在设备中执行自己的业务调用逻辑。

      ![img.png](screenshots/device/img1.png)
   2. 等待数据加载完成，查看泳道，当存在Trace任务时，可在对应的线程泳道中查看当前线程已触发的Trace任务层叠图。例如图中的ArkTSPerfTag，该泳道名称对应代码中HiTraceMeter打印的name（如hiTraceMeter.startTrace("ArkTSPerfTag", 1)中的ArkTSPerfTag）。案例中四个场景分别对应的打点name是ArkTSPerfTag，NativePerfTag，ComponentCBPerfTag，LifeCyclePerfTag。

      ![img.png](screenshots/device/img2.png)
2. 通过命令行查看
   1. 运行项目，然后通过hitrace命令获取跟踪任务的相关日志
      在DevEco Studio Terminal中执行如下命令抓取trace(xxx\xxx代表项目路径)：
      
      PS D:\xxx\xxx> hdc shell
      
      $ hitrace --trace_begin app
   2. 执行完抓取trace后，先在设备中执行自己的业务调用逻辑，然后继续执行如下命令（xxx代表代码中HiTraceMeter打印的name，例如hiTraceMeter.startTrace("ArkTSPerfTag", 1)中的ArkTSPerfTag）:
   
      $ hitrace --trace_dump |grep xxx
   
      $ hitrace --trace_finish
   3. 抓取结果：
   
      ![img.png](screenshots/device/img3.png)
### 工程结构
```
├──entry/src/main/cpp                   // C++代码区
│  ├──types
│  │  └──libentry                       // C++接口


---
## ImageGetAndSave
源码: https://gitcode.com/HarmonyOS_Samples/ImageGetAndSave

# 实现图片获取与保存功能
## 简介
本项目基于Media Library Kit和Image Kit等HarmonyOS API实现了在HarmonyOS系统上获取图片、读取图片信息和保存图片的方式，开发者可以选择适合自己业务场景的方式参考开发。
## 效果预览
![](./screenshots/device/image.png)

## 技术原理
1. 图片获取提供了四种实现方式：分别是Photo Picker组件、PhotoViewPicker接口、CameraPicker接口和DocumentViewPicker。
2. 读取图片信息使用了getImageInfo和getImageProperties方法。
3. 创建PixelMap对象使用imageSource.createPixelMap()方法。
4. 保存图片使用了安全控件和photoAccessHelper模块。

## 使用说明
1. 点击“获取图片”按钮，在弹出界面中选择一种获取图片方式，然后获取对应的图片。
2. 点击“读取图片信息”按钮，可以读取图片信息。
3. 点击“创建PixelMap对象”按钮，可以将图片转换成PixelMap对象。
4. 点击“保存图片”按钮，在弹出界面中选择“保存至应用沙箱”或者“保存至图库”，可以将图片保存到相应位置。

## 工程目录
```
├──ets
│  ├──common
│  │  └──utils                     
│  │     └──Utils.ets                  // 通用方法类
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  └──pages
│     └──Index.ets                     // 首页
└──resources                           // 资源类
```

## 相关权限
无

## 约束与限制
1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## ImageToVideo
源码: https://gitcode.com/HarmonyOS_Samples/ImageToVideo

# 实现图片合成视频功能

## 项目简介
本示例基于AVCodec能力，实现了Buffer模式下的图片合成视频功能。通过ImageSource将图片解码为PixelMap对象，传递PixelMap到Native侧，然后调用Native侧的编码器和封装器，完成从图片解码、视频编码、封装的过程。

## 效果预览
<img src='./screenshots/device/effect.png' width='320'>

## 使用说明
1. 进入首页，点击"选择图片并合成视频"按钮，拉起相册模态界面。
2. 选择至少2张图片并点击 “确定”，系统开始合成视频，并显示加载弹窗。
3. 视频合成完成后，加载弹窗消失，视频自动播放。

## 工程目录

```       
├──entry/src/main/cpp                 // Native层
│  ├──capbilities                     // 能力接口和实现
│  │  ├──include                      // 能力接口
│  │  ├──Muxer.cpp                    // 封装实现
│  │  └──VideoEncoder.cpp             // 视频编码实现
│  ├──common                          // 公共模块
│  │  ├──dfx                          // 日志
│  │  ├──SampleCallback.cpp           // 编解码回调实现   
│  │  ├──SampleCallback.h             // 编解码回调定义
│  │  └──SampleInfo.h                 // 功能实现公共类  
│  ├──transcoding                     // Native层合成视频的接口和实现
│  │  ├──include                      // 能力接口
│  │  ├──Transcoding.cpp              // Native层合成视频的功能调用逻辑的实现
│  │  └──TranscodingNative.cpp        // Native层合成视频的入口    
│  ├──types                           // Native层暴露上来的接口
│  │  ├──index.d.ts                   // 接口定义
│  │  └──oh-package.json5             // 配置文件
│  └──CMakeLists.txt                  // 编译入口       
├──ets                                // UI层
│  ├──common                          // 公共模块
│  │  ├──utils                        // 共用的工具类
│  │  │  └──TimeUtils.ets             // 获取当前时间
│  │  └──CommonConstants.ets          // 参数常量
│  ├──entryabilit


---
## Immersive
> 本示例介绍设置窗口全屏和扩展组件安全区域两种实现沉浸式效果的方式，并对状态栏、导航栏、挖空区域根据不同场景进行适配，为用户提供更优的视觉体验。

源码: https://gitcode.com/HarmonyOS_Samples/Immersive

## 实现沉浸式页面效果

### 介绍

本示例介绍了背景沉浸及全屏沉浸两种沉浸式体验，提供多种实现方案。并根据不同的场景对状态栏、导航栏、挖孔区域进行适配，为用户提供更优的视觉体验。

### 效果预览

| 首页                                  | 背景沉浸                                         | 全屏沉浸                                    |
|-------------------------------------|----------------------------------------------|-----------------------------------------|
| ![](./screenshots/devices/home.png) | ![](./screenshots/devices/shopping_home.png) | ![](./screenshots/devices/game_top.png) |

| 避让挖孔（竖屏-挖孔在顶部）                          | 避让挖孔（横屏-挖孔在左侧）                           | 避让挖孔（反向竖屏-挖孔在底部）                           | 避让挖孔（反向横屏-挖孔在右侧）                          |
|-----------------------------------------|------------------------------------------|--------------------------------------------|-------------------------------------------|
| ![](./screenshots/devices/game_top.png) | ![](./screenshots/devices/game_left.png) | ![](./screenshots/devices/game_bottom.png) | ![](./screenshots/devices/game_right.png) |

| 自由窗口标题栏沉浸                                    |
|----------------------------------------------|
| ![](./screenshots/devices/shopping_free.png) |

使用说明：

1. 首页列出了沉浸式页面的实现方式和常见场景，点击对应的菜单项进入即可。
2. 避让挖孔的小游戏页面可通过切换不同挖孔位置的机型或旋转屏幕观察避让挖孔功能。
3. 平板/电脑/Mate XTs设备的自由窗口模式下，可查看自由窗口标题栏沉浸效果。

### 工程目录

```
 
├──AppScope 
│  ├──resources 
│  └──app.json5
├──commons 
│  └──commons 
│     ├──src 
│     │  └──main 
│     │     ├──ets 
│     │     │  ├──constants                              


---
## IntentsKitGameRevisit
源码: https://gitcode.com/HarmonyOS_Samples/IntentsKitGameRevisit

# 基于意图框架及习惯推荐能力实现常用复访

## 介绍

本示例基于意图框架，使用`@kit.IntentsKit`实现意图共享，使用`@kit.AbilityKit`的`InsightIntentExecutor`
  实现意图调用。根据意图调用的参数实现游戏复访。

## 效果预览

| 主页                               | 游戏页                                      | 小艺卡片展示共享意图                               | 点击意图卡片实现复访                                 |
|----------------------------------|------------------------------------------|------------------------------------------|--------------------------------------------|
| ![界面展示](screenshots/device/1.png "界面展示") | ![模拟游戏](screenshots/device/2.png "模拟游戏") |![小艺建议展示界面0](screenshots/device/3.png "小艺建议展示界面0") | ![意图调用0](screenshots/device/2.png "意图调用0") |

使用说明：
1. 点击`小游戏1或2`的卡片进入游戏卡片页面。进入游戏页面会调用shareIntent()接口。游戏卡片页面底部会显示接口执行状态。
2. 待系统将共享的意图完成处理后，将会在小艺建议的卡片内展示共享的意图。
3. 点击展示的对应小艺卡片，会重新拉起示例应用，完成游戏卡片的复访。

## 工程目录

```
├──entry/src/main/ets
│  ├──common
│  │  ├──constants
│  │  │  └──CommonConstants.ets         // 公共常量类
│  │  └──utils
│  │     ├──FileReader.ets              // 文件读取类
│  │     └──Logger.ets                  // 日志类
│  ├──entryability
│  │  └──EntryAbility.ets               // 入口Ability
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets         // 备份Ability
│  ├──insightintents
│  │  └──IntentExecutorImpl.ets         // 意图调用类
│  ├──model
│  │  └──DataModel.ets                  // 游戏模型类
│  └──pages
│     ├──Index.ets                      // Ability实现的应用的入口页面
│     └──PlayPage.ets                   // 详情页
└──entry/src/main/resources            
   ├──base
   


---
## IntentsKitVideoContinue
源码: https://gitcode.com/HarmonyOS_Samples/IntentsKitVideoContinue

# 基于意图框架推荐常用接续

## 介绍

- 本示例基于意图框架，使用`@kit.IntentsKit`实现意图共享，使用`@kit.AbilityKit`的`InsightIntentExecutor`
  实现意图调用。根据意图调用的参数实现视频接续。

## 效果预览

| 主页                               | 播放页                                 | 小艺卡片展示共享意图                               | 点击意图卡片实现接续                                 |
|----------------------------------|-------------------------------------|------------------------------------------|----------------------------------------------------|
| ![界面展示](screenshots/device/1.png "界面展示") | ![视频播放](screenshots/device/2.png "视频播放") |![小艺建议展示界面0](screenshots/device/3.png "小艺建议展示界面0") | ![意图调用0](screenshots/device/2.png "意图调用0") |

使用说明：
1. 点击`演示视频1或2`的卡片进入视频播放页面。视频播放时会自动触发shareIntent()接口的调用。视频页面底部会显示接口执行状态。
2. 待系统将共享的意图完成处理后，将会在小艺建议的卡片内展示共享的意图。
3. 点击展示的对应小艺卡片，会重新拉起示例应用，并进行视频接续播放。

## 工程目录

```
entry/src/main/
├──ets
│  ├──common/constants
│  │  └──CommonConstants.ets                               // 公共常量类
│  ├──common/utils
│  │  ├──FileReader.ets                                    // 文件读取类
│  │  └──Logger.ets                                        // 日志类
│  ├──entryability
│  │  └──EntryAbility.ets                                  // 入口Ability
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                            // 备份Ability
│  ├──insightintents
│  │  └──IntentExecutorImpl.ets                            // 意图调用类
│  ├──model
│  │  └──DataModel.ets                                     // 视频模型类
│  └──pages
│     ├──Index.ets                   


---
## JumpBetweenApps
源码: https://gitcode.com/HarmonyOS_Samples/JumpBetweenApps

# 基于AppLinking实现应用间跳转

## 介绍

本示例基于AppLinking拉端能力，实现了应用间跳转相关功能，包括拉起设置应用，指定应用拉起，指定意图拉起，拉起应用完成后带参返回等，为应用间跳转场景提供了统一可信的拉端体验。

## 效果预览
手机运行效果图如下：

![image](screenshots/device/phone.png)

## 使用说明
安装应用后，可体验以下功能：
- 点击华为阅读的应用分享消息，可跳转至应用市场的华为阅读详情页；
- 点击地图位置消息，可跳转至地图应用；
- 点击商品消息，可跳转至商品详情页（需安装dependence目录下的应用并配置 AppLinking）。

## 工程目录结构

```  
├──entry/src/main/ets                         // 代码区  
│  ├──pages  
│  │  └──Index.ets                            // 首页  
│  ├──entryability  
│  │  └──EntryAbility.ets                     
│  ├──entrybackupability  
│  │  └──EntryBackupAbility.ets               
│  ├──view  
│  │  ├──CommunicationArea.ets                // 对话区域  
│  │  ├──FooterBar.ets                        // 底部功能区  
│  │  ├──HeaderBar.ets                        // 头部信息区  
│  │  ├──MessageItem.ets                      // 单条消息  
│  │  └──WarningBox.ets                       // 警告  
│  └──viewmodel  
│     └──MessageViewModel.ets                 // 信息数据  
└──entry/src/main/resources                   // 应用资源目录  
```  

## 具体实现

指定应用拉起使用openLink()接口，配置拉起的应用App Linking链接进行应用的拉起。

拉起指定类型应用使用startAbilityByType接口，配置要拉起的应用的参数，系统将会弹窗提示用户选择要在哪个应用中继续操作，用户选择后，在具体应用中继续操作。

注：
1. 开发者需自行在`src/main/ets/viewmodel/MessageViewModel.ets`第67行代码修改自行配置的App Linking链接。
2. 拉起自开发的应用需要开发者自行在dependence/AppLinkingTestDemo应用内进行App Linking相关配置，包括申请App Linking链接、申请证书与Profile签名等。

## 相关权限

不涉及

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5


---
## KVStore
源码: https://gitcode.com/HarmonyOS_Samples/KVStore

# 实现键值型数据库读写功能

### 介绍

本示例主要使用@ohos.data.distributedKVStore接口，实现了键值型数据库的访问及增删改查功能。帮助开发者在键值型数据库使用场景开发中，实现数据库的增删改查功能。

### 效果预览

| 首页                                  | 详情页                                     | 新增页                              |
|-------------------------------------|-----------------------------------------|----------------------------------|
| ![](screenshots/devices/create.png) | ![](screenshots/devices/read_write.png) | ![](screenshots/devices/new.png) |


使用说明：

1. 选择数据等级及是否加密数据后，点击“创建”按钮，进入详情页；
2. 点击“新增”，弹出新增半模态，可以自定义新增类型、键、值；
3. 点击“提交”，数据库增加一条数据（相同键名只能存在一条），点击右上X键或者蒙层区域，退出半模态，数据不更新；
4. 数据库每条数据可编辑，可删除，点击“删除”，数据库删除该条数据；
5. 点击“编辑”，弹出编辑半模态，可修改数据的类型和值，不允许修改键名；
6. 点击“提交”，数据库该条数据信息更新。

### 工程目录

```
├──entry/src/main/ets                              // 代码区
│  ├──constants                                  
│  │  └──utils
│  │     └──KVStore.ets                            // 键值数据库相关操作
│  ├──entryability  
│  │  └──EntryAbility.ets 
│  ├──entrybackupability  
│  │  └──EntryBackupAbility.ets 
│  ├──pages
│  │  ├──Index.ets                                 // 首页                                
│  │  └──ReadWritePage.ets                         // 读写页
│  └──viewmodel
│     └──KVStoreType.ets                           // 数据库信息类     
└──entry/src/main/resources                        // 应用资源目录
```

### 具体实现

1. 使用createKVManager()接口，创建一个KVManager对象实例，用于管理数据库对象。
2. 使用getKVStore()接口，指定options和storeId，创建并得到SingleKVStore类型的KVStore数据库。
3. 使用put()接口，添加指定类型的键值对到数据库。
4. 使用getE


---
## KnockFileShare
源码: https://gitcode.com/HarmonyOS_Samples/KnockFileShare

# 基于Share Kit实现碰一碰文件分享

### 介绍

本示例基于Share Kit实现了跨设备文件的快速分享功能：通过调用`harmonyShare.on('knockShare')`方法注册碰一碰监听事件，在回调中触发`sharableTarget.share()`方法传输文件数据，即可完成碰一碰文件分享流程，供接收端设备获取。其中，接收端接收的文件默认存储于图库或文件管理系统，若接收端为PC端，应用可通过`harmonyShare.on('dataReceive')`方法注册文件接收监听，碰一碰后文件会自动保存至应用的沙箱目录。

### 效果图预览

| 首页                                                 |
|----------------------------------------------------|
| <img src="screenshots/device/phone.png" width=320> |

**使用说明**

1. 设设备安装应用后，即可使用碰一碰文件分享功能，具体使用约束可参考[手机与手机碰一碰分享](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-between-phones)、[手机与PC/2in1碰一碰分享](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones)。
2. 在首页勾选文件后，通过碰一碰即可分享已选文件。
3. 若接收端为PC设备，需确保手机与PC登录同一华为账号，方可实现碰一碰分享。
4. 接收端文件默认存储于图库或文件管理器中，其中PC端应用可通过调用`harmonyShare.on('dataReceive')`方法注册文件接收监听，碰一碰传输的文件将存储至该应用的沙箱路径下。
5. PC端应用接收时最大支持接收5个文件。

### 工程结构

```
├───entry/src/main/ets
│   ├───constants                      
│   │   └───BreakpointConstants.ets    // 常量
│   ├───controller                     
│   │   └───KnockController.ets        // 碰一碰分享控制类
│   ├───entryability                   
│   │   └───EntryAbility.ets           // 程序入口类
│   ├───entrybackupability             
│   │   └───EntryBackupAbility.ets     // 数据备份恢复类
│   ├───model                          
│   │   └───FileData.ets               // 文件数据
│   ├───pages                          
│   │   └───Index.ets                  // 首页
│   └───utils                          


---
## LandscapePortraitToggle
> 本示例实现了视频播放的横竖屏切换功能。

源码: https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle

# 实现视频横竖屏切换功能

## 介绍

本示例基于媒体播放[AVPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer)、窗口方向设置[setPreferredOrientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setpreferredorientation9-1)、Navigation的自定义导航转场动画([customNavContentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#customnavcontenttransition11))等能力、实现了一个视频播放应用，分别实现了页面内和页面级两种视频播放的横竖屏切换效果。其中页面内横竖屏切换是在当前页面，动态改变窗口方向来实现横竖屏切换；页面级横竖屏切换是在当前页面，跳转到新的页面实现横竖屏切换，该页面为横屏显示。



## 效果预览

| 页面内横竖屏切换                                              | 页面间横竖屏切换                                               | 
|-------------------------------------------------------|--------------------------------------------------------|
| <img src="screenshots/devices/case1.gif" width='320'> | <img src="screenshots/devices/case2.gif" width='320' > |

## 使用说明
1. 点击应用首页底部的“页面横屏播放”和“页面级横竖屏”播放按钮，分别跳转到对应场景的视频播放详情页面。
2. 页面内视频播放横竖屏切换：在视频竖屏播放的情况下（视频播放详情页），点击右下角的全屏图标，窗口会旋转到横屏状态，视频会跟着旋转并且铺满屏幕。
3. 页面级视频播放横竖屏切换：在视频竖屏播放的情况下（视频播放详情页），点击右下角的全屏图标，会跳转到新的页面（视频播放页面），该页面为横屏显示，同时视频会跟着旋转并且铺满屏幕。此外页面在跳转过程中会有“一镜到底”的显示动画效果，详情页的播放视图会旋转放大过渡到播放页面。
4. 在状态栏工具栏中的“旋转锁定”开关未打开的情况下，在视频详情页旋转屏幕到横屏，视频会自动旋转为横屏播放。

## 目录结构

```
├──entry/src/main/ets
│  ├──common 
│  │  ├──AnimationProperties.ets          // 属性动画辅助类  
│  │  ├──CustomTransition.ets             // 自定义转场动画管理类
│  │  ├──Logger.ets                       // 日志打印类
│  │  └──VideoNodeC


---
## ListScrollComponent
源码: https://gitcode.com/HarmonyOS_Samples/ListScrollComponent

# 基于ScrollComponents实现长列表

## 项目简介

本示例展示了使用ScrollComponents构建长列表页面，覆盖场景包括

- 长列表Item组件复用
- 长列表分组布局场景
- 长列表跨页面复用场景
- 加速首屏渲染场景
- 长列表数据处理场景：下拉刷新、上拉加载；
- 长列表无限滑动场景
- 长列表侧滑删除场景
- 长列表多类型列表项场景
- 长列表Tabs吸顶场景
- 分组吸顶场景
- 长列表二级联动场景
- 长列表动态切换列数场景
- 设置边缘渐隐场景

## 效果预览

<img src="./screenshots/img.gif" width = "40%" alt="图片名称"/>

## 使用说明

1. 打开应用首页，显示场景列表。点击SameItemListPage，实现了列表项结构相同的组件复用场景、长列表加速首屏渲染场景、长列表侧滑删除场景、设置边缘渐隐场景、长列表动态切换列数场景。
2. 返回首页，点击CombineItemListPage，实现了列表项内子组件可拆分组合的复用场景、长列表加速首屏渲染场景、长列表无限滑动场景。
3. 返回首页，点击DifferentItemListPage，实现了列表项结构类型不同的组件复用场景、长列表下拉刷新和上拉加载场景。
4. 返回首页，点击GroupLayoutListPage，实现了长列表分组布局场景、长列表多类型列表项（ListHeaderView）场景、长列表分组吸顶场景、长列表二级联动场景。
5. 返回首页，点击TabsCeilingListPage，实现了Tabs吸顶场景、跨页面复用场景。

## 工程目录

```
├─entry/src/main/ets
├── common  
│  ├── contants  
│  │  └── CommonConstants.ets         // 常量
│  └── utils   
│     ├── Logger.ets                  // 日志类
│     ├── ToastUtil.ets               // 弹窗工具类
│     └── Utils.ets                   // 工具类
├── component  
│  └── PublicView.ets                 // 公共组件类
├── entryability  
│  └── EntryAbility.ets               // 程序入口类
├── entrybackupability  
│  └── EntryBackupAbility.ets         // 数据备份恢复类
├── model                              
│  ├── mock.ets                       // 模拟加载数据类
│  ├── types.ets                      // 数据模型
│  └── CategoryModel.ets              // 分类模型
├── viewmodel   
│  ├── SameItemViewModel.ets          // 列表项结构类型相同页面ViewModel
│  ├── CombineItemViewModel.ets       // 列表项内子组件可拆分组合页面ViewModel


---
## LiveViewLockScreen
源码: https://gitcode.com/HarmonyOS_Samples/LiveViewLockScreen

# 实现锁屏沉浸实况窗

## 项目简介

“Live View Kit”基于HarmonyOS实现了即时配送等多个场景下实况窗的创建、更新和结束功能。基于不同的场景，皆提供了定制的状态节点，帮助用户聚焦关键信息，提升用户体验。
锁屏沉浸实况窗则是应用进一步展示实时活动状态的通道，系统通过实况窗服务（Live View Kit），将重要信息展示在锁屏界面，让用户一览无余，无需进入应用就能获取活动最新状态，适用于实时性要求高、需要用户及时了解状态的场景。

## 相关概念

- 实况窗：实况窗是一种帮助用户聚焦正在进行的任务，方便快速查看和即时处理的通知形态。实况窗具有时效性、时段性、变化性的特点。

## 效果预览

锁屏界面：

![image](screenshots/phone_lock_screen.png)

## 使用说明

1. 打开应用后自动开启实况窗与沉浸实况窗，主页面无具体功能，仅做展示使用。

2. 上划退出到桌面后，点击位于页面导航栏左侧的胶囊态实况窗或下拉查看消息通知，可查看实况窗卡片页面。

3. 点击锁屏键锁屏后再次点击锁屏键激活屏幕，可查看锁屏沉浸实况窗。

4. 本Sample仅提供在本地创建、更新与结束实况窗的能力(不能后台更新，若要后台更新，请使用Push Kit)。若要使用Push Kit更新，可参考[推送实况窗消息服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-update-liveview)，用已有服务器调用对应的REST API。

## 工程目录

```
├─entry/src/main/ets                
│   ├───constant                           
│   │   └───Constant.ets                   // 常量
│   ├───entryability                       
│   │   └───EntryAbility.ets               // EntryAbility
│   ├───liveview                           
│   │   ├───LiveViewExtAbility.ets         // 实况窗
│   │   └───LockScreenPage.ets             // 锁屏页面
│   ├───model                              
│   │   └───RouteDataModel.ets             // 导航数据Model
│   ├───pages                              
│   │   └───Index.ets                      // 主页面
│   ├───utils                              
│   │   ├───BreakpointUtil.ets             // 断点工具类
│   │   ├───LiveView.ets                   // 实况窗类
│   │   └───LiveViewUtil.ets               // 实况窗工具类
│   ├───view      


---
## LongSnapshotPractice
源码: https://gitcode.com/HarmonyOS_Samples/LongSnapshotPractice

# 实现长截图功能

### 介绍

本示例介绍了如何实现滚动组件（如List组件）以及Web组件长截图功能。分别通过滚动控制器Scroller和WebView的控制器WebviewController，结合组件截图@ohos.arkui.componentSnapshot模块，实现长截图功能。

### 效果预览

| 滚动组件长截图                                    | Web组件长截图                                |
|--------------------------------------------|-----------------------------------------|
| ![](screenshots/device/pic1.png) | ![](screenshots/device/pic2.png) |

### 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  ├──CommonUtils.ets                  // 通用工具类
│  │  ├──ImageUtils.ets                   // 图片处理工具类
│  │  ├──LazyDataSource.ets               // 懒加载数据源管类
│  │  └──Logger.ets                       // 日志打印工具类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets           // 数据备份恢复类
│  ├──pages
│  │  └──Index.ets                        // 应用入口页
│  └──view
│     ├──NewsItem.ets                     // List列表项视图
│     ├──ScrollSnapshot.ets               // 滚动组件长截图视图
│     ├──SnapshotPreview.ets              // 长截图预览弹窗
│     ├──WebSnapshot.ets                  // Web组件长截图视图
│     └──WebSnapshotWebTag.ets            // 使用webPageSnapshot()方法进行网页全量截图
└──entry/src/main/resources               // 应用静态资源目录
```

### 使用说明

1. 分别点击应用首页“滚动组件长截图”和“Web组件长截图”按钮，分别跳转到对应的界面。
2. 在滚动组件长截图页面，点击“一键截图”按钮，稍等后自动生成整个滚动组件页面长截图缩略图，点击“保存图片”按钮，图片会保存到图库。
3. 在滚动组件长截图页面，点击“滚动截图”按钮，列表视图会自动滚动，此时点击列表或者直到列表滑动到底部，会自动生成从滑动开始到滑动结束这段期间的的长截图，缩略图操作与步骤2相同。
4. 在Web组件长截图页面，点击“一键截图”按钮，稍等后自动生成整个网页的


---
## MSLiteHumanSegmentation
源码: https://gitcode.com/HarmonyOS_Samples/MSLiteHumanSegmentation

# 基于 MindSpore Lite 实现端侧人物图像分割
## 介绍
本示例基于`@ohos.ai.mindSporeLite`提供的ArkTS API，实现“端侧人物图像分割”示例程序。

## 效果预览
| 主页                                                | 相册页                                                     | 原图预览页                                                          | 人物图像分割合成结果页                                                         |
|---------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------------|---------------------------------------------------------------------|
| ![主页](screenshots/device/screenshot_001.png "主页") | ![相册页](screenshots/device/screenshot_002.png "相册页") | ![原图预览页](screenshots/device/screenshot_003.png "原图预览页") | ![人物图像分割合成结果页](screenshots/device/screenshot_004.png "人物图像分割合成结果页") |


使用说明
1. 在图像分割页面，可以点击图像合成按钮，进入相册选择图片界面。
2. 在相册界面，选择`一张人物图像`（建议开发者使用1:1尺寸的人物图像以保证最佳合成效果），点击确定按钮。
3. 图像选择好后，会跳转到图像合成页面，默认选中原图tab并展示选择后的原图。
4. 点击合成tab会默认对第一张背景图和原图进行人物图像分割推理（推理过程会涉及模型加载到内存，执行推理，由于模型较大，这个过程会比较耗时，开发者可以参考[@ohos.ai.mindSporeLite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mindsporelite)配置NPU推理以提高推理效率），推理的结果会显示在主界面。
5. 在合成tab下，可以选择列表中的任意背景，进行人物图像分割推理，并在主界面展示推理结果。

## 工程目录
```
├──entry/src/main/ets/
│  ├──common
│  │  └──constants 
│  │     └──ImageDataListConstant.ets  // 图像推理静态配置
│  ├──entryability
│  │  └──EntryAbility.ets              // Ability的生命周期回调内容
│  ├──model
│  │  └──NavigationParam.ets           // Navig


---
## MSLiteSceneRecognition
源码: https://gitcode.com/HarmonyOS_Samples/MSLiteSceneRecognition

# 基于 MindSpore Lite 实现端侧场景检测
## 介绍
本示例基于`@ohos.ai.mindSporeLite`提供的 Native C++ API，实现“端侧场景检测”示例程序。

## 效果预览
| 主页                                                | 相册选取页                                                     | 场景分析结果页                                                     |
|---------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------|
| ![主页](screenshots/device/screenshot_001.png "主页") | ![相册选取页](screenshots/device/screenshot_002.png "相册选取页")   | ![场景分析结果页](screenshots/device/screenshot_003.png "场景分析结果页") |


使用说明
1. 在场景检测页面，可以点击“选择图片”按钮，进入相册选择图片界面。
2. 在相册界面，选择一张图片，点击确定按钮。
3. 图像选择好后，会跳转到场景分析结果页，会自动调用模型进行推理，场景检测结果会显示到界面上。

## 工程目录
```
├──entry/src/main/cpp
│  ├──types
│  │  └──libentry
│  │     ├──index.d.ts                  // 导入NAPI接口供JS调用
│  │     └──oh-package.json5            // 接口注册配置文件
│  ├──CMakeLists.txt                    // Cmake打包配置文件，编译工程动态库脚本，依赖头文件、cpp以及相关依赖
│  └──napi_init.cpp                     // NAPI实现JS与C++通信的接口
├──entry/src/main/ets
│  ├──entryability
│  │  └──EntryAbility.ets               // Ability的生命周期回调内容
│  ├──constants
│  │  └──Constants.ets                  // 静态配置类
│  ├──model
│  │  └──NavigationParam.ets            // 导航参数传输类 
│  ├──pages
│  │  ├──Index.ets                      // Ability实现的应用的入口页面
│  │  └──ResultPage.ets                 // 场景检测结果页
│  └──utils
│     └──Logger.ets                     // 日志工具类
└──entry/src/main


---
## MSLiteStyleTransform
源码: https://gitcode.com/HarmonyOS_Samples/MSLiteStyleTransform

# 基于MindSpore Lite实现端侧图像风格迁移

## 介绍
本示例基于`@ohos.ai.mindSporeLite`提供的ArkTS API，MindSpore Lite风格迁移模型完成端侧推理，实现“端侧图像风格迁移”示例程序。

## 效果预览
| 主页                                                | 相册页                                                     | 原图预览页                                                          | 图像合成页                                                              |
|---------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------|
| ![主页](screenshots/device/screenshot_001.png "主页") | ![相册页](screenshots/device/screenshot_002.png "相册页") | ![原图预览页](screenshots/device/screenshot_003.png "原图预览页") | ![图像合成页](screenshots/device/screenshot_004.png "图像合成页") |


使用说明
1. 在主页面，点击图像合成按钮，进入相册选择图片界面。
2. 在相册界面，选择图片，点击确定按钮。
3. 图像选择好后，会跳转到图像合成页面，默认选中原图tab并展示选择后的原图。
4. 点击合成tab会默认对原图按照第一张风格图进行图像风格类型转换，转换的结果会显示在主界面。
5. 在合成tab下，可以选择列表中的任意风格图片，进行图像风格转换，并实时在主界面展示推理结果。

**合成效果说明**：  
由于当前使用的是开源模型，开发者可以自行在网上寻找其它图像风格迁移开源模型，并[使用MindSpore Lite进行模型转换](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-converter-guidelines)，将第三方模型转换成 MindSpore Lite 支持的格式，自行替换该Sample的模型和模型参数（参考 [模型参数配置指导文档](./MODEL_CONFIG.md)）并查看对应的图像合成效果。

## 工程目录
```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets          // Ability的生命周期回调内容
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets    // 备份A


---
## MindSporeLiteArkTS
> 本示例基于MindSporeLite提供的ArkTS API，实现“端侧图像分类”示例程序，来演示端侧部署的流程。

源码: https://gitcode.com/HarmonyOS_Samples/MindSporeLiteArkTS

# 基于MindSporeLite接口实现图像分类

### 介绍

本文基于MindSporeLite推理能力，实现了从相册选择一张图片，对图片识别处理，根据推理模型进行分类，产生图片解析的结果。帮助开发者掌握如何加载算法模型，并通过算法模型分析图像。

1. 选择图像分类模型。
2. 将模型转换成MindSporeLite模型格式。
3. 在端侧使用MindSporeLite推理模型，显示出可能的分类结果。

### 效果预览

| 主页                                                         |
|------------------------------------------------------------|
| <img src="screenshots/device/MindSporeLiteArkTSDemo.jpg"/> |

#### 使用说明

1. 在主界面，可以点击photo按钮，进入相册选择图片界面；
2. 在相册界面，选择图片，点击确定按钮；
3. 自动进行选择图片的图像分类模型推理，部分推理结果显示在主界面。

### 工程目录

```
 ├──entry/src/main/ets/                     // 应用首页
 │  ├──common
 │  │  ├──constants                         
 │  │  │  └─CommonConstants.ets             // 常量类
 │  │  └──utils          
 │  │     └─Logger.ets                      // 日志打印类
 │  ├──entryability
 │  │  └─EntryAbility.ets                   // 程序入口类
 │  ├──model
 │  │  └─Model.ets                          // 模型推理
 │  └──pages                 
 │     └──Index.ets                         // 主页入口
 ├──entry/src/main/resource                 // 应用静态资源
 │  └──rawfile
 │     └──mobilenetv2.ms                    // 模型文件
 └──entry/src/main/module.json5             // 模块配置相关
 
```

### 具体实现

* 本示例程序中使用的终端图像分类模型文件为mobilenetv2.ms，放置在entry\src\main\resources\rawfile工程目录下。

  注：开发者可按需手工下载[MindSpore Model Zoo中图像分类模型](https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/1.5/mobilenetv2.ms)。

* 调用@ohos.file.picker（图片文件选择）、@ohos.multimedia.image（图片处理效果）、@ohos.file.fs（基础文件操作） 等API实现相册图片获取及图


---
## MindSporeLiteCpp
源码: https://gitcode.com/HarmonyOS_Samples/MindSporeLiteCpp

# **基于C++MindSporeLite接口实现图像分类**

### 介绍

本文基于MindSporeLite提供的C++ API，实现“端侧图像分类”示例程序，来演示端侧部署的流程，以便用户掌握图像分类C++接口的能力。

1. 选择图像分类模型。
2. 将模型转换成MindSporeLite模型格式。
3. 在端侧使用MindSporeLite推理模型，显示出可能的分类结果。

### 效果预览

| 主页                                                  |
|-----------------------------------------------------|
| <img src="screenshots/MindSporeLiteArkTSDemo.png"  width="240px"> |

### 使用说明

1. 在主界面，可以点击photo按钮，进入相册选择图片界面；
2. 在相册界面，选择图片，点击确定按钮；
3. 自动进行选择图片的图像分类模型推理，部分推理结果显示在主界面。

### 工程目录

```
 ├──entry/src/main/cpp/                     // 模型推理
 │  ├──types/libentry/                       
 │  │  ├──Index.d.ts                        // 声明C++方法
 │  │  └──oh-package.json5                  // 声明依赖
 │  ├──CMakeLists.txt                       // 链接MindSporeLite动态库
 │  └──napi_init.cpp                        // 图像识别                             
 ├──entry/src/main/ets/                     // 应用首页
 │  ├──common
 │  │  ├──constants                         
 │  │  │  └──CommonConstants.ets             // 常量类
 │  │  └──utils          
 │  │     └──Logger.ets                      // 日志打印类
 │  ├──entryability
 │  │  └──EntryAbility.ets                   // 程序入口类
 │  ├──entrybackupability
 │  │  └──EntryBackupAbility.ets             // 数据备份恢复类
 │  └──pages                 
 │     └──Index.ets                         // 主页入口
 ├──entry/src/main/resource                 // 应用静态资源
 │  └──rawfile
 │     └──mobilenetv2.ms                    // 模型文件
 └──entry/src/main/module.json5           


---
## MultiBusinessOffice
> 本示例主要使用断点监听和SidebarContainer组件、Navigation组件相结合的方式，实现了商务办公类差异化的多场景响应式变化效果。

源码: https://gitcode.com/HarmonyOS_Samples/MultiBusinessOffice

# 多设备商务办公界面

### 介绍

本示例主要使用断点监听和sidebarContainer组件、navigation组件相结合的方式，实现了商务办公类差异化的多场景响应式变化效果。

### 效果预览

本示例分为三个页面：

**入口页**:

| 直板机                                       | 折叠屏（展开态）                                        | 平板                                        |
|------------------------------------------|-------------------------------------------------|-------------------------------------------|
| ![](screenshots/devices/entry-phone.png) | ![](screenshots/devices/entry-foldablescre.png) | ![](screenshots/devices/entry-tablet.png) |

**备忘录页**:

| 直板机                                       | 折叠屏（展开态）                                          | 平板                                        |
|------------------------------------------|---------------------------------------------------|-------------------------------------------|
| ![](screenshots/devices/notes-phone.png) | ![](screenshots/devices/notes-foldablescreen.png) | ![](screenshots/devices/notes-tablet.png) |

**日历页**:

| 直板机                                         | 折叠屏（展开态）                                             | 平板                                           |
|---------------------------------------------|------------------------------------------------------|----------------------------------------------|
| ![](screenshots/devices/calendar-phone.png) | ![](screenshots/devices/calendar-foldablescreen.png) | ![](screenshots/devices/calendar-tablet.png) |

使用说明：

* 入口页

  1. 点击备忘录或日历按钮，打开备忘录或日历实例页面;

  2. 页面旋转跟随


---
## MultiCommunityApplication
> 基于自适应和响应式布局，实现一次开发，多端部署-社区评论类应用，视觉、控件等符合设计规范，并包含键鼠适配、横屏适配等。

源码: https://gitcode.com/HarmonyOS_Samples/MultiCommunityApplication

# 多设备社区评论界面

## 简介

基于自适应布局和响应式布局，实现一次开发，多端部署的社区评论页。

直板机运行效果图如下：

![](screenshots/device/phone.png)

双折叠运行效果图如下：

![](screenshots/device/foldable.png)

平板运行效果图如下：

![](screenshots/device/tablet.png)

## 相关概念

- 一次开发，多端部署：一套代码工程，一次开发上架，多端按需部署。支撑开发者快速高效的开发支持多种终端设备形态的应用，实现对不同设备兼容的同时，提供跨设备的流转、迁移和协同的分布式体验。
- 自适应布局：当外部容器大小发生变化时，元素可以根据相对关系自动变化以适应外部容器变化的布局能力。相对关系如占比、固定宽高比、显示优先级等。
- 响应式布局：当外部容器大小发生变化时，元素可以根据断点、栅格或特定的特征（如屏幕方向、窗口宽高等）自动变化以适应外部容器变化的布局能力。
- GridRow：栅格容器组件，仅可以和栅格子组件（GridCol）在栅格布局场景中使用。
- GridCol：栅格子组件，必须作为栅格容器组件（GridRow）的子组件使用。

## 使用说明

1. 分别在直板机、双折叠、平板安装并打开应用，不同设备的应用页面通过响应式布局和自适应布局呈现不同的效果。
2. 点击底部首页、热点、消息、我的图片文字按钮，切换显示对应的标签页，默认显示热点标签页。
3. 点击热搜标题，切换热搜列表。
4. 点击查看完整榜单按钮，跳转至热搜榜单页。热搜榜单页支持上下及左右滑动，点击返回按钮退回至热点页。
5. 热点页点击图片进入图片详情页。手机设备只展示图片，折叠屏及平板展示正文及评论。点击图片或返回按钮退回至热点页。
6. 热点页点击卡片正文进入详情页。详情页正文文字区域支持双指缩放。折叠屏右上角按钮支持切换左右及上下布局。点击返回按钮退回至热点页。

## 相关权限

不涉及。

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：直板机、双折叠（Mate X系列）、平板。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.2 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.2 Release SDK及以上。



---
## MultiDeviceCamera
> 本示例展示了如何使用HarmonyOS提供的相机开放能力和一多能力，在多设备（手机、大折叠、阔折叠、三折叠、平板）上实现正常状态和折叠状态切换时的预览旋转、拍照旋转、切换镜头等功能。

源码: https://gitcode.com/HarmonyOS_Samples/MultiDeviceCamera

# 基于相机开放能力和一多能力实现多设备相机

## 介绍

本示例展示了如何使用HarmonyOS提供的相机开放能力和一多能力，主要包括使用Camera Kit预览拍照、photoAccessHelper进行保存图片和一多断点实现多设备页面及功能差异。本示例主要用于如何在多设备（手机、大折叠、阔折叠、三折叠、平板）上实现正常状态和折叠状态切换时的预览旋转、拍照旋转、切换镜头等功能。

## 效果展示

手机运行效果图：

![](screenshots/device/mate60.png)

阔折叠运行效果图：

![](screenshots/device/purax.png)

大折叠运行效果图：

![](screenshots/device/matex5.png)

三折叠运行效果图：

![](screenshots/device/matext.png)

平板运行效果图：

![](screenshots/device/matepadpro.png)

## 使用说明

应用可以点击底部按钮拍摄照片，同时可以实现旋转相机角度、切换前后摄像头、切换折叠状态完成拍摄的操作，拍摄完成后可以预览照片。

## 工程目录

```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages
│  │  └──Index.ets                       // 主页
│  ├──utils
│  │  ├──BreakpointType.ets              // 一多断点工具类
│  │  ├──CameraUtil.ets                  // 相机工具类
│  │  └──WindowUtil.ets                  // 窗口工具类
│  └──views
│     └──CommonView.ets                  // 公共视图类
└──entry/src/main/resource               // 应用静态资源目录
```

## 实现思路

1.  使用Camera Kit预览拍照。
2.  使用photoAccessHelper保存图片。
3.  使用一多断点能力实现多设备页面和功能差异。

## 相关权限

1. 相机权限：ohos.permission.CAMERA，用于相机开发场景。
2. 受限开放权限-媒体库权限：ohos.permission.READ_IMAGEVIDEO，用于读取图库文件。可申请此权限的特殊场景与功能： 应用需要克隆、备份或同步图片/视频类文件。 
3. 受限开放权限-媒体库权限：ohos.permission.WRITE_IMAGEVIDEO，用于保存文件至图库。可申请此权限的特殊场景与功能： 应用需要克隆、备份或同步图片/视频类文件。

## 依赖

不涉及。

## 约束与限制

1.本示例仅支持标准系统上运行，支持设备：直板机、双折叠（Mate X系列）、平板、阔折叠、三折叠。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.Harm


---
## MultiDeviceCommunication
> 基于自适应和响应式布局，实现一次开发，多端部署-即时通讯类应用，视觉、控件等符合设计规范，并包含键鼠适配、横屏适配等。

源码: https://gitcode.com/HarmonyOS_Samples/MultiDeviceCommunication

# 多设备即时通讯界面

### 简介

基于自适应和响应式布局，实现一次开发，多端部署-即时通讯。

#### 介绍

本篇Codelab基于自适应布局和响应式布局，实现一次开发，多端部署的即时通讯页面。通过“三层工程架构”实现代码复用，并根据手机、折叠屏以及平板不同的设备尺寸设计对应页面。
手机效果如图所示：

![](screenshots/device/phone.png)

折叠屏展开态效果如图所示：

![](screenshots/device/foldable.png)

平板效果如图所示：

![](screenshots/device/pad.png)

#### 相关概念

- 一次开发，多端部署：一套代码工程，一次开发上架，多端按需部署。支撑开发者快速高效的开发支持多种终端设备形态的应用，实现对不同设备兼容的同时，提供跨设备的流转、迁移和协同的分布式体验。
- 自适应布局：当外部容器大小发生变化时，元素可以根据相对关系自动变化以适应外部容器变化的布局能力。相对关系如占比、固定宽高比、显示优先级等。常见的自适应布局有：线性布局、层叠布局、弹性布局、相对布局等。自适应布局能力可以实现界面显示随外部容器大小连续变化。
- 响应式布局：当外部容器大小发生变化时，元素可以根据断点、栅格或特定的特征（如屏幕方向、窗口宽高等）自动变化以适应外部容器变化的布局能力。
- Navigation：页面根容器，一般用于分栏布局场景使用。

#### 相关权限

不涉及。

#### 使用说明

- 分别在手机、折叠屏、平板安装并打开应用，不同设备的应用页面通过响应式布局和自适应布局呈现不同的效果。
- 点击底部消息、通讯录、社交圈，将切换显示对应的标签页，默认显示消息标签页。

#### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：直板机、双折叠（Mate X系列）、平板。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.2 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.2 Release SDK及以上。



---
## MultiFinancialManagement
> 基于自适应和响应式布局，实现一次开发，多端部署-银行理财类应用，视觉、控件等符合设计规范。

源码: https://gitcode.com/HarmonyOS_Samples/MultiFinancialManagement

# 多设备银行理财界面

## 简介

基于自适应和响应式布局，实现一次开发、多端部署银行理财。

直板机效果图如下：

<img src='./screenshots/device/phone.png' width='320'>

双折叠效果图如下：

<img src='./screenshots/device/foldable.png' width='480'>

平板效果图如下：

<img src='./screenshots/device/pad.png' width='800'>

## 相关权限

不涉及

## 使用说明

1. 分别在直板机、双折叠、平板安装并打开应用，不同设备的应用页面通过响应式布局和自适应布局呈现不同的效果。
2. 点击界面内财富精选下的图片跳转到产品详情页。
3. 点击界面内稳健增长内容跳转到基金详情页。
4. 点击基金详情页下方对比跳转至基金比较页。
5. 基金详情页勾选基金后点击开始对比跳转至基金比较页。

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：直板机、双折叠（Mate X系列）、平板。
2. HarmonyOS系统：HarmonyOS 5.1.0 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.2 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.2 Release SDK及以上。


---
## MultiPictureBeautification
> 基于自适应和响应式布局，实现一次开发，多端部署的图片美化应用。

源码: https://gitcode.com/HarmonyOS_Samples/MultiPictureBeautification

# 多设备图片美化界面

## 简介

基于自适应和响应式布局，实现一次开发，多端部署-图片美化。

## 介绍

本篇Codelab基于自适应布局和响应式布局，实现一次开发，多端部署的即时通讯页面。通过“三层工程架构”实现代码复用，并根据直板机、装折叠、平板不同的设备尺寸设计对应页面。
直板机效果如图所示：

![](screenshots/device/phone.png)

双折叠展开态效果如图所示：

![](screenshots/device/foldable.png)

平板效果如图所示：

![](screenshots/device/pad.png)

## 相关概念

- 一次开发，多端部署：一套代码工程，一次开发上架，多端按需部署。支撑开发者快速高效的开发支持多种终端设备形态的应用，实现对不同设备兼容的同时，提供跨设备的流转、迁移和协同的分布式体验。
- 组件区域变化事件：组件区域变化事件指组件显示的尺寸、位置等发生变化时触发的事件。
- 双指缩放：用于触发捏合手势，触发捏合手势的最少手指为2指，最大为5指，最小识别距离为5vp。

## 相关权限

不涉及。

## 使用说明

- 分别在直板机、双折叠、平板安装并打开应用，不同设备的应用页面通过响应式布局和自适应布局呈现不同的效果。
- 点击编辑、相册图标将分别进入图片编辑页面，相册页面。

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：直板机、双折叠（Mate X系列）、平板。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.2 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.2 Release SDK及以上。


---
## MultiShoppingPriceComparison
> 基于自适应和响应式布局，实现一次开发，多端部署的购物比价应用。

源码: https://gitcode.com/HarmonyOS_Samples/MultiShoppingPriceComparison

# 多设备购物比价界面

### 简介

本篇Codelab基于自适应布局和响应式布局，实现一次开发，多端部署的购物比价页面。通过“三层工程架构”实现代码复用，并根据手机、折叠屏以及平板不同的设备尺寸实现对应页面。

直板机运行效果图如下：

![](screenshots/device/phone.png)

双折叠（Mate X系列）运行效果图如下：

![](screenshots/device/foldable.png)

平板运行效果图如下：

![](screenshots/device/tablet.png)

### 相关概念

- 一次开发，多端部署：一套代码工程，一次开发上架，多端按需部署。支撑开发者快速高效的开发支持多种终端设备形态的应用，实现对不同设备兼容的同时，提供跨设备的流转、迁移和协同的分布式体验。
- 自适应布局：当外部容器大小发生变化时，元素可以根据相对关系自动变化以适应外部容器变化的布局能力。相对关系如占比、固定宽高比、显示优先级等。
- 响应式布局：当外部容器大小发生变化时，元素可以根据断点、栅格或特定的特征（如屏幕方向、窗口宽高等）自动变化以适应外部容器变化的布局能力。
- GridRow：栅格容器组件，仅可以和栅格子组件（GridCol）在栅格布局场景中使用。
- GridCol：栅格子组件，必须作为栅格容器组件（GridRow）的子组件使用。
- 画中画：应用在视频播放、视频会议、视频通话等场景下，可以使用画中画能力将视频内容以小窗（画中画）模式呈现。

### 相关权限

不涉及。

### 使用说明

1. 分别在直板机、双折叠（Mate X系列）、平板安装并打开应用，不同设备的应用页面通过响应式布局和自适应布局呈现不同的效果。
2. 打开应用，查看首页内容。
3. 点击底部分类按钮，查看分类页内容。
4. 点击底部购物袋，查看购物袋页内容。
5. 点击分类页的商品图，查看商品详情页内容。
6. 点击右上角的分屏按钮，分屏比较商品信息。
7. 点击商品详情页底部的聊天按钮，查看商品详情咨询客服页内容。
8. 点击商品详情页底部的购物袋按钮，查看商品详情-购物袋页内容。
9. 点击商品详情页底部的购买按钮，查看商品详情-支付页内容。
10. 点击商品详情页的直播中按钮，查看直播间页内容，点击右上角关闭按钮以画中画模式观看直播。
11. 点击直播间页推荐商品，查看直播间-商品详情页内容。
12. 点击直播间页底部购物袋按钮，查看直播间-购物袋页内容。
13. 点击直播间-购物袋页的立即购买按钮，查看直播间-支付页内容。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：直板机、双折叠（Mate X系列）、平板。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.2 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.2 Release SDK及以上。



---
## MultiTarget
源码: https://gitcode.com/HarmonyOS_Samples/MultiTarget

# 构建多目标产物工程

### 介绍

本示例展示了如何通过一个工程构建出多个不同的应用包，该示例可以构建出official和test两个版本的应用包。通过该示例，开发者能够了解不同类型包支持的多目标定制项以及如何进行资源的差异化定制。便于开发者更好的掌握构建多目标产物的能力。
* official版本工程：工程会在首页中显示Official版本的资源，包含一段描述、 一张图片以及一个按钮。点击按钮会实现页面跳转，第二个页面包含一个运算器逻辑，official版本支持进行加法运算和减法运算。输入两个不超过五位的数字，点击对应按钮，弹窗显示计算结果。
* test版本工程：工程会在首页中显示Test版本的资源，包含一段描述、 一张图片以及一个按钮。点击按钮会实现页面跳转，第二个页面包含一个运算器逻辑，test版本仅支持进行减法运算。输入两个不超过五位的数字，点击减法按钮，弹窗显示计算结果；点击加法按钮，弹窗显示不支持该功能。

### 效果图预览

| official版本                             | test版本                           |
|----------------------------------------|----------------------------------|
| ![](screenshots/device/official.gif)   | ![](screenshots/device/test.gif) |

### 使用说明

需要先对每个product进行签名配置，然后构建对应的版本，查看页面效果。点击按钮，跳转下一个页面。在第二个页面输入参数，点击对应方法按钮，查看调用结果。

**注意事项**

该示例仅展示official版本与test版本内容对比，default版本未实现其逻辑，开发者请勿使用default版本运行。

**多目标产物签名配置方案：**

1. 在工程级的build-profile.json5文件中，给每个需要构建的多目标product下配置如图所示参数：

![](screenshots/device/signingConfigs.png)

2. 然后进入到签名配置页面，点击加号，添加签名信息：

![](screenshots/device/signingConfigs1.png)

3. 然后选择对应的bundle name，并填写上面配置的"signingConfigs"信息：

![](screenshots/device/signingConfigs2.png)

4. 签名之后点击ok即可：

![](screenshots/device/signingConfigs3.png)

**工程构建方法：**

首先点击DevEco Studio工具右上角的Product按钮，即图中的1号标识处，然后在2号标识处选择对应的Product工程，选择完工程之后会自动映射出我们文件中已经依赖的target，最后点击Apply应用。上述操作完成之后就可以点击运行按钮查看多目标产物的效果了。

![](screenshots/device/product_build.png)

### 实现思路

1. 在每个HAP，HAR模块的模块级build-profile.json文件中定制出official版本和test版本对应的target，然后为每个target进行资源的差异化定制。
2. 在工程级build-profi


---
## MultiThreadIO
源码: https://gitcode.com/HarmonyOS_Samples/MultiThreadIO

# 基于Taskpool和@Sendable的关系型数据库和文件读写

### 介绍

本示例基于TaskPool和@Sendable实现了密集型文件和关系型数据库的读写操作,使用Taskpool创建线程，使用@Sendable实现线程间的数据传递，帮助开发者实现多线程的密集型读写。

### 效果预览

| 首页                                   |
|--------------------------------------|
| ![image](screenshots/device/index.gif) |

### 使用说明：

本示例提供8个按钮触发使用TaskPool和@Sendable对于文件和关系型数据库的读写：
1. TaskPool 文件-写入：点击该按钮完成使用TaskPool对于文件的写入。
2. TaskPool 文件-读取：点击该按钮完成使用TaskPool对于文件的读取。
3. @Sendable 文件-写入：点击该按钮完成使用TaskPool和@Sendable对于文件的写入。
4. @Sendable 文件-读取：点击该按钮完成使用TaskPool和@Sendable对于文件的读取。
5. TaskPool 数据库-写入：点击该按钮完成使用TaskPool对于数据库的写入。
6. TaskPool 数据库-读取：点击该按钮完成使用TaskPool对于数据库的读取。
7. @Sendable 数据库-写入：点击该按钮完成使用TaskPool和@Sendable对于数据库的写入。
8. @Sendable 数据库-读取：点击该按钮完成使用TaskPool和@Sendable对于数据库的读取。
9. 读写成功后会以“成功”Toast弹窗作为提示；当在进行其他I/O任务时会以“在执行任务，请稍后”，作为提示；若无写入内容，执行读取，会提示读取内容为空。

### 工程目录

```
├──entry/src/main/ets/
│  ├──commons                                  
│  │  ├──constants               
│  │  │  └─CommonConstants.ets          // 常量类 
│  │  └──utils          
│  │     ├─DatabaseSendable.ets         // 关系型数据库Sendable操作类
│  │     ├─DatabaseTaskPool.ets         // 关系型数据库TakPool操作类
│  │     ├─FileSendable.ets             // 文件Sendable操作类
│  │     └─FileTaskPool.ets             // 文件TakPool操作类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets         // 备份恢复类
│  └──pages                 
│     └──Index.ets                      // 首页
└──entry/src/main/resources       


---
## MultiVideoApplication
源码: https://gitcode.com/HarmonyOS_Samples/MultiVideoApplication

# 多设备长视频界面

## 项目简介

本示例基于一多能力，实现了一次开发、多端部署的长视频应用界面，覆盖直板机、折叠屏、平板、电脑及智慧屏等多种设备形态。同时，采用三层架构组织代码工程，结合自适应布局与响应式布局，构建了从首页、搜索到视频详情的完整长视频体验。

## 效果预览

直板机运行效果图如下：

![](screenshots/device/phone.png)

折叠屏运行效果图如下：

![](screenshots/device/foldable.png)

平板运行效果图如下：

![](screenshots/device/tablet.png)

电脑运行效果图如下：

![](screenshots/device/2in1.png)

智慧屏运行效果图如下：

![](screenshots/device/tv.png)


## 使用说明

1. 在手机、平板、电脑上安装名称为**default**的hap包，在智慧屏上安装名称为**tv**的hap包。安装完成后打开应用，即可在不同设备上看到通过自适应和响应式布局呈现的差异化长视频界面。

2. 在首页推荐视频区域，支持长按第一张图片预览视频。在电脑上，鼠标右键点击推荐视频区域可弹出菜单，鼠标悬停时图片放大。在md、lg和xl横向断点下，支持双指捏合缩放推荐视频区域。

3. 在首页往期回顾区域，在手机、平板、电脑设备上点击播放/继续播放可跳转到视频详情页，在智慧屏上点击视频封面图片可跳转到视频详情页。

4. 顶部Tab区域可切换不同内容区块。在手机、平板、电脑设备上，切换到社区Tab可查看首页的沉浸式设计；在lg和xl断点下切换到视频Tab，可查看Banner图的创新排版。在智慧屏设备上的首页Tab，可查看为大屏优化的Banner图样式。

5. 在手机、平板、电脑设备上，点击顶部搜索框进入搜索页：输入关键字“华”后可看到智能提示列表；点击智能提示中的“华为发布会”进入搜索结果页，点击结果中的播放按钮跳转到视频详情页。在智慧屏设备上，输入关键字“H”后可看到搜索结果视频列表，点击列表中的视频封面图片跳转到视频详情页。

6. 在手机、平板、电脑设备上，视频详情页默认播放当前视频，支持播放/暂停、拖动进度条跳转、进入/退出全屏播放，全屏状态下可打开/关闭选集工具栏，评论区根据断点进行上下布局或左右分区。在智慧屏设备上，视频详情页默认展示选集信息，点击任意一集后进入视频播放页面，视频默认全屏播放，支持播放/暂停、拖动进度条跳转、打开/关闭选集工具栏。

7. 在手机、平板、电脑设备上，当评论区上下布局时，上滑视频会先隐藏相关列表区域，视频再等比缩小让出空间给评论区；当评论区左右分区时，上滑视频会等比缩小并优先展示简介区内容。

## 工程目录

```
├──commons                                                     // 公共能力层
│  └──base
│     └──src
│        └──main
│           └──ets
│              ├──constants
│              │  ├──BreakpointConstants.ets                   // 断点相关常量
│              │  └──CommonConstants.ets                       // 公共静态常量
│     


---
## MultiWeb
源码: https://gitcode.com/HarmonyOS_Samples/MultiWeb

# 基于Web响应式能力实现一多布局


### 简介
本示例基于Web侧提供的一多能力，如相对单位、媒体查询、添加窗口事件等，实现了常见的Web的一多效果，包括：字体大小调整、图片大小调整、宫格布局、轮播布局、自定义弹窗。通过集成Web一多的相关能力，可以让应用在多设备上都有良好的用户体验。

### 效果预览

| 断点   | sm                                   | md                                      | lg                                    |
| ------ | ------------------------------------ | --------------------------------------- | ------------------------------------- |
| 效果图 | ![](./screenshots/devices/phone.png) | ![](./screenshots/devices/foldable.png) | ![](./screenshots/devices/tablet.png) |


### 工程目录

```
├──WebProject                           // Web程序位置
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──entrybackupability  
│  │  └──EntryBackupAbility.ets  
│  └──pages              
│     └──Index.ets                      // 程序页面入口
└──entry/src/main/resources             // 应用静态资源目录
```

### 使用说明
本项目为Web一多示例，实现了在不同设备尺寸上字体与图片大小都能自动调整到合适的尺寸，同时本项目对轮播、宫格、弹窗这些常见场景进行了一多布局适配，开发者可在不同设备上运行该程序查看布局效果。

### 具体实现
1. 字体大小与图片大小都依靠媒体查询，通过媒体查询来动态设置元素的相关属性，实现一多效果。
2. 轮播图一多主要依靠动态调整每个轮播项的尺寸以及单次轮播距离实现不同尺寸下不同的轮播效果。
3. 宫格部分主要依靠媒体查询在不同屏幕断点尺寸下，设置不同的列数与间距，从而实现一多效果。
4. 自定义弹窗主要依靠媒体查询，在不同断点下设置不同的弹窗尺寸。

### 相关权限

不涉及

### 约束与限制
1. 本示例仅支持标准系统上运行，支持设备：直板机、双折叠（Mate X 系列）、平板。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## MultiWindowPractice
源码: https://gitcode.com/HarmonyOS_Samples/MultiWindowPractice

# 基于ArkUI实现智慧多窗界面适配

### 介绍

本示例展示了在智慧多窗（分屏和悬浮窗）开发中解决界面适配问题的方案。通过优化布局和调整元素显示逻辑，确保应用在不同窗口模式下均能提供一致且优质的用户体验。

### 效果预览

部分效果图如下

| 页面被截断问题优化                                           | Video组件分屏状态下被截断问题优化                                 | 悬浮窗顶部操作栏无法响应操作问题优化                                  |
|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| ![Question1.png](screenshots/devices/Question1.png) | ![Question3.png](screenshots/devices/Question3.png) | ![Question7.png](screenshots/devices/Question7.png) |

使用说明
1. 安装应用后，点击应首页上的某些按钮，例如点击“页面被截断，无法上下滑动”按钮，跳转到二级页面。
2. 点击二级页面上的“优化前”按钮，跳转到问题优化前的页面，从屏幕底部向上滑至左上方热区，进入待分屏状态，点击桌面另一个支持分屏的应用图标或卡片，查看优化前界面分屏效果。
3. 返回二级页面，点击二级页面上的“优化后”按钮，跳转到问题优化后的页面，查看优化后的分屏效果。

### 目录结构

```
├──entry/src/main/ets/
│  ├──common
│  │  ├──AVPlayerUtil.ets                 // 视频播放工具类
│  │  ├──Constants.ets                    // 常量封装类
│  │  └──Logger.ets                       // 日志打印工具类
│  ├──entryability
│  │  └──EntryAbility.ets                 // Ability的生命周期回调内容
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets           // 程序入口类
│  └──pages
│     ├──Index.ets                        // 应用入口页
│     ├──Question.ets                     // 通用问题场景入口菜单
│     ├──Question1Correct.ets             // 问题场景一优化后
│     ├──Question1Incorrect.ets           // 问题场景一优化前
│     ├──...                              // 此处省略其它问题场景描述
│     └──Question8Incorrect8.ets     


---
## MultipleImage
> 本示例是基于Swiper组件和自定义指示器实现多图片合集功能。

源码: https://gitcode.com/HarmonyOS_Samples/MultipleImage

# 使用Swiper组件实现轮播布局
## 介绍
本示例介绍了两个案例，第一个是如何使用Swiper组件实现图片轮播效果，以及如何自定义Swiper组件的指示器，来实现图片的切换效果；
第二个是如何使用Stack组件实现轮播图层叠效果。

在短视频平台上，经常可以见到图文合集。它的特点是：由多张图片组成一个合集，图片可以自动进行轮播，也可以手动去进行图片切换。图片下方的进度条
会跟随图片的切换而切换；在各类应用和网站中，轮播图的使用非常广泛，而轮播图的叠加效果，也能创造独特的视觉层次和交互体验。

## 预览效果

| 直板机                             | 折叠屏                           |
|--------------------------------|--------------------------------|
| <img src="./screenshots/device/image.gif" width="320"> | <img src="./screenshots/device/fold.png" width="600"> |

## 工程目录
``` 
├──entry/src/main/ets                                   // 代码区
│  ├──common
│  │  └──CommonConstants.ets                            // 常量
│  ├──entryability
│  │  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages 
│  │  ├──ImageSwitch                                    // 多图片合集页
│  │  ├──Index.ets                                      // 首页
│  │  └──StackSwitch.ets                                // 层叠布局页
│  └──utils.ets
│     └──DataSource.ets                                 // 图片数据资源类
└──entry/src/main/resources                             // 应用资源目录
``` 
## 使用说明
* 运行应用后，点击首页的ImageSwitch按钮跳转至多图片合集页面，不滑动屏幕时，图片自动轮播，且下方进度条缓慢增长至已完成状态，播放完成时，会继续循环播放。
滑动屏幕时，图片跟随滑动方向而进行切换，此时会关闭自动轮播和循环播放的效果，且下方进度条瞬间增长至已完成状态。

* 运行应用后，点击首页的StackSwitch按钮跳转至轮播图层叠布局页面，左右滑动可进行轮播图切换。
## 实现说明
* 多图片合集页

  上面图片的轮播部分使用Swiper组件实现。

  下面的指示器，需要关闭原生指示器，自定义指示器（进度条）来实现。

  进度条可以使用Row容器来实现对应的效果，通过层叠布局方式将Row容器叠放在一起。进度条缓慢增长，可以通


---
## MusicCard
源码: https://gitcode.com/HarmonyOS_Samples/MusicCard

# 基于Form Kit实现音乐服务卡片

### 介绍

音乐服务卡片是服务卡片在音乐领域的一种应用形式。它集成了音乐APP
的核心功能，如歌曲播放、歌单推荐、心动歌词、动态歌词等，并以卡片的形式呈现给用户。音乐服务卡片通常设计有简洁明了的交互界面，用户可以快速访问音乐播放、暂停、切换等功能，无需打开完整的应用即可实现操作，大大提高了使用的便捷性。

### 效果预览

| 播放界面                             | 播控卡片                                | 歌词卡片                               | 推荐卡片                                    | 动态歌词卡片 |
|----------------------------------|-------------------------------------|------------------------------------|-----------------------------------------|--------|
| ![](screenshots/device/play.png) | ![](screenshots/device/control.png) | ![](screenshots/device/lyrics.png) | ![](screenshots/device/recommended.png) |  ![](screenshots/device/DynamicLyrics.png)       |

### 工程目录

```
├──entry/src/main/ets                     // 代码区
│  ├──components                          // 自定义组件
│  │  ├──CustomTabBar.ets                 // 首页自定义导航Tabbar
│  │  ├──PlayController.ets               // 首页底部音乐播控组件
│  │  ├──PlayerView.ets                   // 音乐播放界面
│  │  ├──PlayList.ets                     // 歌曲播放列表
│  │  ...                                 
│  │  └──SongListItem.ets                 // 音乐列表列表项目
│  ├──database                            // 数据库工具类
│  │  ├──FormRdbHelper.ets                // 卡片数据库工具类
│  │  ├──PreferencesUtil.ets              // 首选项工具类
│  │  ├──RdbUtils.ets                     // 关系型数据工具类
│  │  └──SongRdbHelper.ets                // 歌曲数据库工具类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybac


---
## MusicHome
> 基于自适应和响应式布局，实现一次开发、多端部署音乐专辑。

源码: https://gitcode.com/HarmonyOS_Samples/MusicHome

# 多设备音乐界面

## 项目简介

基于自适应和响应式布局，实现一次开发、多端部署音乐专辑。

## 效果预览
直板机效果图如下：

![](screenshots/device/phone.png)

双折叠效果图如下：

![](screenshots/device/foldable.png)

平板效果图如下：

![](screenshots/device/tablet.png)

智能穿戴效果图如下：

<img src="./screenshots/device/wearable.png" width="320">

## 工程目录
```
├──common                                     // 公共能力层
│  ├──constantsCommon/src/main/ets            // 公共常量
│  │  └──constants
│  └──mediaCommon/src/main/ets                // 公共媒体方法
│     ├──utils
│     └──viewmodel
├──features                                   // 基础特性层
│  ├──live/src/main/ets                       // 直播页
│  │  ├──constants
│  │  ├──view
│  │  └──viewmodel
│  ├──live/src/main/resources                 // 资源文件目录
│  ├──musicComment/src/main/ets               // 音乐评论页
│  │  ├──constants
│  │  ├──view
│  │  └──viewmodel
│  ├──musicComment/src/main/resources         // 资源文件目录
│  ├──musicList/src/main/ets                  // 歌曲列表页
│  │  ├──components
│  │  ├──constants
│  │  ├──lyric
│  │  ├──view
│  │  └──viewmodel
│  └──musicList/src/main/resources            // 资源文件目录
└──products                                   // 产品定制层
   ├──phone/src/main/ets                      // 支持直板机、双折叠、平板
   │  ├──common
   │  ├──entryability
   │  ├──pages
   │  ├──phonebackupextability
   │  └──viewmodel
   ├──phone/src/main/resources                // 资源文件目录
   ├──watch/src/main/ets                      // 支持智能穿戴
   │  ├──constants                      
   │  ├──pages
   │  ├──view
   │  ├──watchability


---
## NFCTag
源码: https://gitcode.com/HarmonyOS_Samples/NFCTag

# 基于NFC的应用跳转

## 介绍

近场通信（Near Field Communication，NFC）是一种短距高频的无线电技术。电子设备可以通过NFC通信技术和NFC标签通信，从标签中读取数据。

其分为两种场景：

* NFC标签前台读取：打开特定应用程序，设备触碰NFC标签后，会把读取到的卡数据分发给前台应用。
* NFC标签后台读取：不打开特定应用程序，设备触碰NFC标签后，根据NFC标签的技术类型，分发给能够处理的应用。如果匹配到多个，则弹出应用选择器给用户手动选择。如果只匹配到一个，则直接打开匹配到的应用程序。

（注：无论是前台读取还是后台读取，电子设备能够发现NFC标签的前提条件是设备必须是亮屏和解锁状态）。

## 预览效果

| 前台读取                                  | 后台读取                                   |
|---------------------------------------|----------------------------------------|
| ![](screenshots/divice/forground.gif) | ![](screenshots/divice/background.gif) |

## 工程目录

```
├──entry/src/main/ets                                   // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages                              
│  │  └──Index.ets                                      // 首页
│  └──view  
│     └──ReadNFCTag.ets                                 // 展示NFC信息页面
└──entry/src/main/resources                             // 应用资源目录
```

## 使用说明

示例代码包含两个场景：

* 前台读卡：打开应用，NFC标签触碰设备NFC可识别区域，读取NFC标签数据，跳转子页面并在页面中展示NFC标签支持的技术类型和标签信息。


* 后台读卡：不打开应用，NFC标签触碰设备NFC可识别区域，根据NFC标签的技术类型匹配应用，若匹配多个则弹出选择框给用户手动选择打开应用；若匹配一个应用，则直接打开匹配到的应用程序，展示NFC标签支持的技术类型和标签信息。

## 相关权限

* 允许应用读取Tag卡片：ohos.permission.NFC_TAG。

## 约束与限制

* 本示例仅支持标准系统上运行，支持设备：华为手机。
* HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
* DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
* HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## NativeDataConversion
> 本示例介绍如何使用DevEco Studio创建一个Native C++应用，将ArkTS侧的数据（基础的数据类型）传递到Native侧进行处理并返回结果到ArkTS侧。

源码: https://gitcode.com/HarmonyOS_Samples/NativeDataConversion

# 实现ArkTS侧基础类型转化为Native侧数据类型功能

## 简介

本示例介绍如何使用DevEco Studio创建一个Native C++应用，将ArkTS侧的数据（基础的数据类型）传递到Native侧进行处理并返回结果到ArkTS侧。
界面如下所示：

![synchronized_operation](screenshots/device/data_conversion.gif)

## 工程目录

```
├──conversion/src/main/cpp                    // C++ 代码区
│  ├──types
│  │  └──libconversion                        // C++接口导出
│  │     ├──index.d.ts                        
│  │     └──oh-package.josn5                 
│  ├──ArraybufferType.cpp                     // Arraybuffer类型转换
│  ├──ArraybufferType.h                       
│  ├──ArrayType.cpp                           // 数组类型转换
│  ├──ArrayType.h
│  ├──CMakeLists.txt                          // CMake配置文件
│  ├──DateType.cpp                            // Date类型转换
│  ├──DateType.h
│  ├──hello.cpp                               // Native模块注册                             
│  ├──NumberType.cpp                          // number类型转换
│  ├──NumberType.h                          
│  ├──ObjectType.cpp                          // Object类型转换
│  ├──ObjectType.h                            
│  ├──StringBoolType.cpp                      // string,bool类型转换
│  └──StringBoolType.h                        
├──conversion/src/main/ets                    // ets 代码区
│  ├──common
│  │  ├──constants  
│  │  │  └──CommonConstants.ets               // 常量定义文件
│  │  └──utils
│  │     └──Logger.ets                        // 日志类
│  ├──conversionability
│  │  └──ConversionAbility.ets       
│  └──pages
│     ├──ArraybufferType.ets                 


---
## NativeFileAccess
源码: https://gitcode.com/HarmonyOS_Samples/NativeFileAccess

# 实现Native侧文件访问

### 介绍

应用在Native侧进行文件访问主要有三种场景，第一种是访问应用沙箱文件，第二种是访问应用资源文件，最后一种是访问公共目录文件，本sample将针对这三种场景给出实现方案。

### 效果预览

| 应用主界面                                                                      |
|----------------------------------------------------------------------------|
| ![NativeFileAccess_show.png](screenshots/device/NativeFileAccess_show.png) | 

### 使用说明

点击进入页面后，页面有六个按钮，分别对应不同的文件访问方案。
- 点击前三个按钮会出现弹窗显示访问的文件内容；
- 点击第四个按钮拉起picker，创建文件；
- 点击第五个按钮会拉起picker选择文件，返回对文件操作的结果；
- 点击第六个按钮会拉起picker选择文件，返回文件的内容。

### 工程目录

```       
├──entry/src/main/cpp                 // Native层
│  ├──types                           // Native层暴露上来的接口
│  │  └──libfile_access               // 暴露给UI层的接口
│  ├──CMakeLists.txt                  // 编译入口
│  └──FileAccessMethods.cpp           // Native文件操作方法       
├──ets                                // UI层
│  ├──common                          // 公共模块
│  │  └──utils                        // 共用的工具类
│  │     ├──FileOperate.ets           // 调用picker文件操作方法
│  │     ├──Logger.ets                // 日志类
│  │     └──ReadFile.ets              // ArkTS侧读取文件方法
│  ├──entryability                    // 应用的入口
│  │  └──EntryAbility.ets            
│  ├──entrybackupability            
│  │  └──EntryBackupAbility.ets          
│  ├──model            
│  │  └──FileNameModel.ets            
│  └──pages                           // EntryAbility 包含的页面
│     └──Index.ets                    // 应用主页面
├──resources                          // 用于存放应用所用到的资源文件
│  ├──base  


---
## NativeFileIO
源码: https://gitcode.com/HarmonyOS_Samples/NativeFileIO

# 实现Native侧的文件读写

### 介绍

本示例展示了如何在Native侧对文件进行读写，ArkTS侧的数据可以传到Native侧进行文件写入，Native侧读取的文件数据可以返回给ArkTS侧。该示例可以帮助开发者学习在Native侧如何精准获取ArkTS侧传入的字符串长度，并掌握如何在Native侧对文件进行读写。

### 效果预览

![](screenshots/device/native_fileio.png) 


使用说明

1、点击写入数据的输入框，输入对应的内容，点击【写入】按钮将输入的内容写到本地文件中。

2、点击读取数据的【读取】按钮，读取文件中已写入的数据，并进行展示。




### 工程目录
```
├──entry/src/main/cpp                   // C++代码区
│  ├──types
│  │  └──libentry                       // C++接口导出
│  │     ├──Index.d.ts                
│  │     └──oh-package.josn5              
│  ├──CMakeLists.txt                    // CMake配置文件     
│  └──napi_init.cpp                     // Native业务代码实现
├──entry/src/main/ets                   // ArkTS代码区
│  ├──entryability                      
│  ├──entrybackupability                
│  └──pages    
│     └──Index.ets                      // 主页界面
└──entry/src/main/resources             // 应用资源文件
```
### 具体实现
* 在写入文件时，需要在ArkTS侧获取文件的路径和写入的内容，并传递到Native侧。
* 先调用napi_get_value_string_utf8函数来获取字符串的长度，然后根据长度分配char数组的内存空间。
* 再次调用napi_get_value_string_utf8函数来获取字符串的内容，并写入到文件中。
* 在读取文件时，使用napi_create_string_utf8获取文件内容，再返回到ArkTS侧。

注意：在为写入的内容分配内存时，可以将长度+1，以便为字符串添加终止符'\0'。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## NativeSoIntegration
源码: https://gitcode.com/HarmonyOS_Samples/NativeSoIntegration

# 实现动态链接库（.so）的引用

### 介绍

针对团队实际开发过程中需要引用三方so库的场景，本示例提供三种解决方案，帮助开发者将项目的不同功能模块化，提升代码的复用性和工程的可维护性：

1. Native侧通过编译动态链接库的方式引用三方so库
2. Native侧通过调用dlopen的方式引用三方so库
3. ArkTS侧通过配置模块动态依赖引用已经适配Native的三方so库

### 效果预览

| 应用主界面                                                        |
|--------------------------------------------------------------| 
| ![NativeSoIntegration_main.png](screenshots/device/main.png) |

### 使用说明

进入应用主页面后，输入参数X和参数Y，点击下方的三个按钮可以通过不同方案调用三方so库进行计算：

1. 点击第一个按钮，在Native侧通过编译动态链接库的方式引用三方so库进行加法计算
2. 点击第二个按钮，在Native侧通过调用dlopen的方式引用三方so库进行减法运算
3. 点击第三个按钮，在ArkTS侧通过配置模块动态依赖引用已经适配Native的三方so库进行乘法运算

### 工程目录

```
├──entry/libs                         // 三方so库文件
│  └──arm64-v8a                             
│     ├──libmultiply.so               // 乘法三方so库文件
│     ├──libnativeAdd.so              // 加法三方so库文件
│     └──libnativeSub.so              // 减法三方so库文件
├──entry/src/main/cpp                 // Native层
│  ├──add                             
│  │  └──add.h                        // 加法头文件
│  ├──types                           // Native层提供的接口
│  │  ├──libentry     
│  │  │   ├──index.d.ts               // Native侧接口文件  
│  │  │   └──oh-package.json5         // Native侧配置文件               
│  │  └──libmultiply      
│  │     ├──index.d.ts                // Native侧接口文件
│  │     └──oh-package.json5          // Native侧配置文件                        
│  ├──CMakeLists.txt                  // 编译入口
│  └──napi_init.cpp                   // NAPI接口实现
├──ets                                //


---
## NativeSubMainThreadCommunication
源码: https://gitcode.com/HarmonyOS_Samples/NativeSubMainThreadCommunication

# 实现Native侧子线程与UI主线程通信

### 介绍

本示例主要介绍如何实现在Native侧子线程中回调UI主线程的函数，实现UI主线程页面刷新。该示例可以帮助开发者学习线程安全函数和libuv异步库的使用，并掌握Native侧跨线程调用的相关能力。

### 效果图预览
![](screenshots/device/NativeSub_MainThreadComm.gif) 

### 使用说明

点击对应按钮会分别调用两种不同方式的代码执行逻辑进行数据处理（即对数据进行加30操作），处理后的结果会显在页面中。

**注意事项**

推荐开发者主要使用线程安全函数来实现在Native侧子线程中回调UI主线程的函数，尽量避免使用libuv的方式。如果非要使用libuv异步库，应使用uv_async_send的方式进行线程间通信，而非使用uv_queue_work函数，该函数主要用于抛异步任务，异步任务的execute回调被提交到线程池后会经过调度执行，因此并不保证多次提交的任务之间的时序关系。 uv_queue_work仅限于在loop线程中调用，这样不会产生多线程安全问题。尽量不要将uv_queue_work作为线程间通信的手段，即A线程获取到B线程的loop，并通过uv_queue_work抛异步任务的方式，把execute回调置为空任务，而把complete回调放在B线程中执行。 这种方式不仅低效，而且还增加了发生故障时定位问题的难度。

### 工程结构&模块类型
```
├──entry/src/main/cpp                   // C++代码区
│  ├──types
│  │  └──libentry                       // C++接口导出
│  │     ├──Index.d.ts                
│  │     └──oh-package.josn5              
│  ├──CMakeLists.txt                    // CMake配置文件     
│  └──napi_init.cpp                     // Native业务代码实现
├──entry/src/main/ets                   // ArkTS代码区
│  ├──entryability                      
│  ├──entrybackupability                
│  └──pages    
│     └──index.ets                      // 主页界面
└──entry/src/main/resources             // 应用资源文件
```

### 具体实现

1. 线程安全函数方式：
   1. 首先在ArkTS侧传递函数到Native侧。
   2. 在Native侧主线程中创建线程安全函数并绑定回调，并拆分子线程。
   3. 在子线程中请求并调用线程安全函数触发回调。
   4. 在回调函数中使用napi_call_function接口调用ArkTS传递的函数。
2. libuv异步库方式：
   1. 首先在ArkTS侧传递函数到Native侧。
   2. 在Native侧主线程中保存上下文环境和函数引用。
   3. 在主线程中声明loop、初始化async句柄绑定回调函数，并拆分


---
## NavigationSettings
> 本示例展示了设置应用的典型页面，其在小窗口和大窗口有不同的显示效果，体现一次开发、多端部署的能力。

源码: https://gitcode.com/HarmonyOS_Samples/NavigationSettings

# 开发设置应用页面功能

### 介绍

本示例展示了设置应用的典型页面，其在小窗口和大窗口有不同的显示效果，体现一次开发、多端部署的能力。  

1. 本示例使用一次开发多端部署中介绍的自适应布局能力和响应式布局能力进行多设备（或多窗口尺寸）适配，保证应用在不同设备或不同窗口尺寸下可以正常显示。
2. 本示例使用Navigation组件，实现小窗口单栏显示、大窗口双栏显示的效果。

### 效果预览

本示例在不同窗口尺寸下的显示效果。

![](screenshots/devices/img4.png)

![settings.gif](products/default/src/main/resources/base/media/settings.gif)

使用说明：

1. 启动应用，查看应用在全屏状态下的显示效果。
2. 依次点击`WLAN` -> `更多WLAN设置`，查看应用的显示效果。
3. 依次点击`更多连接`->`NFC`，查看应用的显示效果。

### 工程目录
```
├──features/settingitems/src/main/ets              // 代码区
│  ├──components
│  │  ├──ItemDescription.ets                       // 每个单元组模块前的标题描述模块
│  │  ├──ItemGroup.ets                             // 单元组模块
│  │  ├──MainItem.ets                              // 主体框架模块
│  │  ├──SearchBox.ets                             // 搜索框模块
│  │  ├──SubItemArrow.ets                          // 下一步模块(箭头跳转组件)
│  │  ├──SubItemToggle.ets                         // 状态按钮组件
│  │  └──SubItemWifi.ets                           // 子网络列表模块   
│  ├──moreconnections  
│  │  ├──MoreConnectionsItem.ets                   // 更多连接模块
│  │  └──Nfc.ets                                   // nfc对象操作类
│  ├──settinglist
│  │  └──SettingList.ets                           // 设置页面
│  └──wlan                                    
│     ├──WlanMoreSetting.ets                       // 更多网络设置模块
│     └──WlanSettingItem.ets                       // 网络设置模块
└──entry/src/main/resources                        // 应用资源目录
                                  
```

### 具体实现
本示例介绍如何实现不同断点下存在单栏和双


---
## NetAdaptiveVideoStream
源码: https://gitcode.com/HarmonyOS_Samples/NetAdaptiveVideoStream

# 网络视频流自适应码率调节

## 简介

本示例基于HarmonyOS提供的媒体(AVPlayer)、网络质量评估(Network Boost Kit)等能力，实现视频流码率的自定义调节功能，可以在弱网环境下以画面质量换取播放流畅度，减少视频卡顿次数。

## 效果预览

| 码率下调                               | 码率上调                             |
|------------------------------------|----------------------------------|
| ![](./screenshots/bitrateDown.png) | ![](./screenshots/bitrateUp.png) |

## 工程目录

```
├──entry/src/main/ets
│  ├──common  
│  │  ├──utils                          // 工具类
│  │  │  ├──CommonUtils.ets             // 通用工具类
│  │  │  └──Logger.ets                  // 日志类
│  │  ├──CommonConstants.ets            // 常量类
│  │  └──CustomConfigs.ets              // 自定义配置类                         
│  ├──entryability  
│  │  └──EntryAbility.ets               // 程序入口
│  ├──model                                     
│  │  ├──NetInfoModel.ets               // 网络信息类
│  │  └──ViewInfoModel.ets              // 视频信息类
│  ├──pages                                     
│  │  └──Index.ets                      // 首页
│  ├──viewmodel                                     
│  │  ├──AVPlayerController.ets         // 视频核心控制类
│  │  └──NetInfoViewModel.ets           // 视频信息交互类
│  └──view
│     ├──VideoPlayControl.ets           // 视频播放暂停控制组件
│     ├──VideoPlayInfo.ets              // 视频播放信息展示组件
│     ├──VideoProgressBar.ets           // 视频进度条组件
│     └──VideoResolutionSelector.ets    // 视频分辨率切换组件
└──entry/src/main/resources             // 应用资源目录
```

## 使用说明

1. 准备可用的多码率hls视频流。本示例使用FFmpeg+Nginx搭建测试用视频播放服务器，可参考[测试环境搭建](./server/R


---
## NetBoost
源码: https://gitcode.com/HarmonyOS_Samples/NetBoost

# 基于多网并发能力实现网络加速

## 项目简介
本示例基于多网并发能力，通过系统返回的多个网络通路，帮助开发者在上传、下载大吞吐场景下实现网络加速的功能。

## 效果预览
| 下载                                                      | 上传                                     | 
|---------------------------------------------------------|----------------------------------------|
|<img src="screenshots/device/download.webp" width="320"/> |<img src="screenshots/device/upload.webp" width="320"/> | 

## 注意事项
1. 本示例无法直接运行，如需正常使用下载功能，请开发者在[CommonConst.ets](./entry/src/main/ets/common/CommonConst.ets)中配置下载地址**DOWN_URL1**和**DOWN_URL2**，并且这两个地址均需要服务端支持**HEAD**方法及**Range**字段。如需正常使用上传功能，则需要开发者在[CommonConst.ets](./entry/src/main/ets/common/CommonConst.ets)配置上传地址**UP_HOST**，并且确认[FilePartsUploadManager.ets](./entry/src/main/ets/viewmodel/upload/FilePartsUploadManager.ets)中的三个文件上传相关接口是否需要修改。因为文件分段上传通常为私有协议，此处给出示例代码的详解，供开发者理解和修改使用。<br>
   1. 第一步，首先会通过初始化方法**initMultiPartUpload**告知服务端初始化，此时传递文件路径和文件名称，如果成功，则会返回指定的**InitiateMultipartUpload**数据格式；<br>
   2. 第二步，分段上传文件方法**uploadSegment**，示例代码使用指定的网络，同时搭配第一步返回的初始化结果上传了文件分段的内容，并记录了所有返回的分段结果**UploadPartResult**；<br>
   3. 第三步，通知服务端合并文件，此处会上传第二步骤的所有**UploadPartResult**。如果开发者在以上三个步骤中有不同的要求，例如返回的数据格式不同、网络请求的Header不同等问题，请自行修改使用。<br>
2. 打开应用的 "多网络并发传输" 开关，可能会因为各种原因导致打开失败，例如额度用尽、多网并发能力不支持等，开发者可参考[多网并发错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/networkboost-nethandover#section8508131819279)排查。

## 使用说明
1. 下载本示例代码导入到IDE，打开AppScope->app.json文件，修改bundleName为您自己的应用名称。
2. 参考[签名配置指导](https://developer.huawei.com/consumer/c


---
## NetworkReconnection
源码: https://gitcode.com/HarmonyOS_Samples/NetworkReconnection

# 实现应用网络重连功能

## 介绍

本示例通过HTTP下载、RCP下载和Socket下载三个案例，介绍了应用网络超时重连、应用网络恢复后重连、应用网络前后台切换后重连。其中，HTTP下载、RCP下载使用的网络视频资源，Socket下载使用的本地服务端资源，通过网络监听和状态变量监听获取应用的网络状态和应用的前后台状态，进而对网络进行重连。

## 效果预览

![](screenshots/device/net_connection.gif)

## 使用说明

1. 打开服务端应用，点击“初始化”按钮，对服务端进行初始化。
2. 打开客户端应用，点击“Socket下载”按钮，进入客户端Socket下载页面。
3. 在Socket下载页面，点击【保存至图库】下载视频文件。
4. 在HTTP下载页面，点击【保存至图库】下载视频文件。
5. 在RCP下载页面，点击【保存至图库】下载视频文件。

## 工程目录

```
├──NetworkReconnection                         // 网络重连客户端工程
└──ServerSocket                                          // 网络重连服务端工程
```

## 具体实现

1. import需要的socket模块。
2. 创建一个TCPSocketServer连接，返回一个TCPSocketServer对象。 
3. 绑定本地IP地址和端口，监听并接受与此套接字建立的客户端TCPSocket连接。 
4. 订阅TCPSocketServer的connect事件，用于监听客户端的连接状态。 
5. 客户端与服务端建立连接后，返回一个TCPSocketConnection对象，用于与客户端通信。 
6. 订阅TCPSocketConnection相关的事件，通过TCPSocketConnection向客户端发送数据，客户端保存文件数据到相册。 
7. HTTP下载通过requestInStream完成下载，并通过SaveButton保存到相册。
8. RCP下载通过GET方式完成下载，并通过SaveButton保存到相册。

## 相关权限

- 允许应用使用Internet网络权限:ohos.permission.INTERNET。
- 允许应用获取数据网络信息:ohos.permission.GET_NETWORK_INFO。

## 依赖

不涉及

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。 
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。 
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## ObtainingDeviceID
源码: https://gitcode.com/HarmonyOS_Samples/ObtainingDeviceID

# 实现获取设备标识功能

## 介绍
设备标识是一种用于标识设备的代码或符号，应用可以通过设备标识来区分不同设备，HarmonyOS提供了三种设备标识：
* [ODID（开发者匿名设备标识符）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-device-info#常量)：一般用于设别同一设备上运行的同一个开发者的应用，标识应用身份。
* [OAID（开放匿名设备标识符）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/oaid-service)：一般用于广告跟踪，可在保护用户个人数据隐私安全的前提下，向用户提供个性化广告。
* [AAID（应用匿名标识符）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-get-aaid)：一般用于应用的推送，标识应用身份。

## 预览效果
![](./screenshots/device/Effect.gif)

## 工程目录
``` 
├──entry/src/main/ets                                   // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages                              
│  │  └──Index.ets                                      // 入口文件
│  └──view
│     └──CreateIDComponent.ets                          // 创建设备标识页面
└──entry/src/main/resources                             // 应用资源目录
``` 
## 使用说明
依次点击应用首页的3个按钮，进入创建设备标识页面后，可以实现以下3个场景：
* 创建ODID，创建成功后显示在上方输入框内，点击保存按钮将设备标识保存至关键资产中，最后点击查询按钮，查询成功后即可显示在下方输入框内。
* 创建AAID，创建成功后显示在上方输入框内，点击保存按钮将设备标识保存至关键资产中，最后点击查询按钮，查询成功后即可显示在下方输入框内。
* 创建OAID，创建成功后显示在上方输入框内，点击保存按钮将设备标识保存至关键资产中，最后点击查询按钮，查询成功后即可显示在下方输入框内。

## 实现说明
* 通过[deviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-device-info#属性)获取ODID
* 通过[identifier.getOAID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-oaid#identifiergetoaid)获取OAID



---
## OnlineEditorCollaboration
> 本示例基于ArkWeb和自由流转实现办公编辑协同，包括：在线文档编辑（如字体加粗、上传图片），以及跨设备协作（如跨设备剪贴板、块设备拖拽以及在平板或PC/2in1设备上可调用手机的相机、扫描、图库等跨设备互通功能）。应用接入了华为分享能力，可通过分享面板、碰一碰或隔空传送将文档链接分享至其他设备；在PC/2in1上还支持碰一碰接收文件。本示例同时支持应用接续能力，便于在多个设备间快速切换。

源码: https://gitcode.com/HarmonyOS_Samples/OnlineEditorCollaboration

# 基于ArkWeb和自由流转实现办公编辑协同

## 项目简介

本示例基于ArkWeb和自由流转实现办公编辑协同，包括：在线文档编辑（如字体加粗、上传图片），以及跨设备协作（如跨设备剪贴板、跨设备拖拽以及在平板或PC/2in1设备上可调用手机的相机、扫描、图库等跨设备互通功能）。应用接入了华为分享能力，可通过分享面板、碰一碰或隔空传送将文档链接分享至其他设备；在PC/2in1上还支持碰一碰接收文件。本示例同时支持应用接续能力，便于在多个设备间快速切换。

## 效果预览

|                      **主页**                       |                     **编辑页**                      |                      **拖拽**                       |                      **剪贴**                       |
|:-------------------------------------------------:|:------------------------------------------------:|:-------------------------------------------------:|:-------------------------------------------------:|
| <img src='screenshots/phone/index.png' width=320> | <img src='screenshots/phone/edit.png' width=320> | <img src='screenshots/tablet/drag.png' width=800> | <img src='screenshots/tablet/copy.png' width=800> |

## 使用说明

### 一、运行服务端

应用通过Web组件加载在线编辑器页面，所有文档数据、上传文件及实时协作均由本机或局域网内的Node服务端提供。**使用前必须先启动WebEditor服务端**，且确保运行应用的设备能访问该服务地址。

1. **环境要求**：本机已安装Node.js（建议v16及以上）。
2. **进入目录**：打开Terminal，在项目根目录下执行：
   ```bash
   cd WebEditor
   ```
3. **安装依赖**（首次运行或依赖变更时执行）：
   ```bash
   npm install
   ```
4. **启动服务**：
   ```bash
   npm start
   ```
5. **确认端口**：服务默认监听 **8082** 端口，启动成功后会输出类似 `Server running at http://0.0.0.0:8082`。
6. **配置应用中的服务地址**：HarmonyOS应用通过[Constants.ets](entry/src/main/ets/common/Constants.ets)中的`SERVER_IP`和`SERVER_PORT`访问服务端。请将`SERVER_IP`改为**运行上述服务的电脑在本机/局域网内的IP地址（运行服务端的设备和运行应用的设备都需要在同一局域网）**，`SERVER_PORT`与启动服务时的端口一致（默认8

**EntryAbility.ets**
```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

import { Constant } from '../common/Constants';
import { IndexViewModel } from '../viewmodel/IndexViewModel';
import { EditViewModel } from '../viewmodel/EditViewModel';
import { LanguageChangeListener } from '../utils/LanguageChangeListener';

const LOG_TAG: string = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  // [Start continue3]
  // [Start share6]
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // [StartExclude continue3]
    // [StartExclude share6]
    try {
      // Set up language change event listener.
      LanguageChangeListener.setupLanguageChangeListener();
    } catch (err) {
      const error = err as BusinessError;
      hilog.error(Constant.HILOG_DOMAIN, LOG_TAG,
        'Failed to setup language change listener. Cause: %{public}s.', error.message);
    }
    
    hilog.info(Constant.HILOG_DOMAIN, LOG_TAG, '%{public}s', 'Ability onCreate.');
    // [EndExclude continue3]
    // Check if it's launched from continuation - use launchParam.launchReason.
    if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
      // When restoring from continuation, get the saved Web browsing progress data.
      this.restoreWebProgress(want);
    }
    // [StartExclude continue3]
    // [EndExclude share6]
    this.getShareData(want);
    // [EndExclude continue3]
  }
  // [End continue3]
  // [End share6]

  /**
   * This method is called when continuing from another device to the current device.
   */
  // [Start continue4]
  // [Start share6]
  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    //
```


---
## PageFlip
源码: https://gitcode.com/HarmonyOS_Samples/PageFlip

# 实现阅读器翻页效果

## 介绍

本示例基于显式动画、List组件、drawing接口实现了阅读器上下翻页、左右覆盖翻页、仿真翻页等效果。

## 效果预览

<img src="./screenshots/device/page_flip.webp" width="320">

### 使用说明

- 进入应用默认为仿真翻页，在屏幕上滑动手指执行翻页。支持点击左右两侧自动翻页。点击屏幕中部区域，弹出翻页选项。
- 选择上下翻页，显示上下翻页页面。支持上下滑动。
- 选择覆盖翻页，显示覆盖翻页页面。支持左右滑动翻页，以及点击屏幕左右侧后滑动翻页。

## 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  └──Constants.ets               // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets            // 程序入口类
│  ├──pages
│  │  └──Index.ets                   // 首页
│  ├──view
│  │  ├──BottomView.ets              // 按钮弹窗
│  │  ├──CoverFlipPage.ets           // 覆盖翻页
│  │  ├──EmulationFlipPage.ets       // 仿真翻页
│  │  ├──ReaderPage.ets              // 文字页面
│  │  └──UpDownFlipPage.ets          // 上下翻页
│  └──viewmodel
│     ├──BasicDataSource.ets         // 列表数据类
│     └──PageNodeController.ets      // 节点控制类
└──entry/src/main/resource           // 应用静态资源目录
```

## 具体实现

1. 使用List组件实现上下滑动效果；使用组件位移及显式动效animateTo实现左右覆盖翻页效果。

2. 使用ArkGraphics 2D（方舟2D图形服务） @ohos.graphics.drawing接口及NodeContainer组件，实现仿真翻页效果的绘制。根据手指滑动触摸位置，计算仿真页的边缘节点，填充区域后实现。

## 相关权限

不涉及

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机、平板。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## PageSlip
> 本项目是一个基于ArkTS的应用程序，基于伙伴高频使用场景，构建复杂的流畅滑动页面，滑动时不丢帧。

源码: https://gitcode.com/HarmonyOS_Samples/PageSlip

# 优化瀑布流加载慢丢帧问题
## 简介
本示例展示了如何在构建复杂的瀑布流滑动页面时，优化加载慢和丢帧问题。本示例是一个ArkTs的应用程序，基于应用高频使用场景，构建复杂的流畅滑动页面，使用
懒加载、缓存列表项、组件复用等性能优化方式，达到滑动不丢帧的效果。                                                                                                                                                                                                                                            
## 效果预览
![](./screenshots/device/page_slip.gif)
## 工程目录
```
├──ets
│  ├──constants
│  │  ├──BreakpointConstants.ets       // 断点相关常量
│  │  ├──CommonConstants.ets           // 一般常量
│  │  └──HomeConstants.ets             // 主页的常量
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──model
│  │  ├──FooterTabData.ets             // 底部导航栏
│  │  ├──FunctionEntryData.ets         // 功能区
│  │  ├──FunctionEntryListData.ets     // 功能区数据列表
│  │  ├──WaterFlowData.ets             // 瀑布流数据
│  │  ├──WaterFlowDescriptionData.ets  // 瀑布流item底部描述信息
│  │  ├──WaterFlowHeadData.ets         // 瀑布流item媒体信息
│  │  └──WaterFlowListData.ets         // 瀑布流数据列表
│  ├──pages
│  │  └──Index.ets                     // 滑动页面入口
│  ├──utils
│  │  ├──BreakpointSystem.ets          // 一多断点监听
│  │  ├──BreakpointType.ets            // 一多断点类型
│  │  ├──CollectionsCountModifier.ts   // 按需更新数据
│  │  ├──Logger.ts                     // 日志
│  │  └──NetworkUtil.ets               // 网络请求
│  └──view
│     ├──FunctionView.ets              // 功能区页面
│     ├──HomeContent.ets               // 主页
│     ├──IndexNavDestin


---
## PermissionApplication
源码: https://gitcode.com/HarmonyOS_Samples/PermissionApplication

# 实现权限申请功能

### 介绍

本示例以位置权限为例，演示权限申请全流程的实现过程。帮助开发者在权限申请的场景开发中，了解申请全流程。

### 效果预览

| 位置权限申请弹窗                           | 提示文字                                    | 当前位置信息                               |
|------------------------------------|-----------------------------------------|--------------------------------------|
| ![](screenshots/device/pop_up.png) | ![](screenshots/device/text_prompt.png) | ![](screenshots/device/location.png) |

使用说明

1. 点击“获取当前位置”，弹出位置权限申请弹窗；
2. 权限申请禁止后，按钮上方显示提示文字；
3. 点击提示文字中蓝色字体或“获取当前位置”按钮，二次弹出权限弹窗；
4. 二次权限申请允许后，若不允许精确位置，关闭弹窗后提示获取精确位置信息，并在当前位置显示模糊定位信息；
5. 允许精确位置后，点击“获取当前位置”按钮，若系统位置服务功能关闭，则拉起全局开关弹窗；
6. 若不允许访问我的位置，关闭弹窗后提示开启位置服务信息；
7. 若允许访问我的位置，点击“获取当前位置”按钮，显示当前位置信息。


### 工程目录
```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  └──pages
│     └──Index.ets                 // 首页
└──entry/src/main/resources        // 应用静态资源目录
```

### 实现思路

1. 调用requestPermissionsFromUser()方法向用户申请授权，通过返回结果authResults判断用户是否授权，通过返回结果dialogShownResults判断是否有系统弹框；
2. 当authResults为-1，dialogShownResults为false时，表示当前应用没有被授权且没有向用户展示请求授权的弹框，则应用可调用requestPermissionOnSetting()方法，拉起权限设置弹框；
3. 通过isLocationEnabled()方法判断位置服务是否开启，若关闭可使用requestGlobalSwitch()方法拉起全局开关设置弹框。

### 依赖
无

### 相关权限

获取定位权限：ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SD


---
## Phone_Connection
源码: https://gitcode.com/HarmonyOS_Samples/Phone_Connection

# 实现手机手表互联通信与手表心率监听

### 简介

本示例主要通过展示手机手表的互联通信，以及手表传感器的使用等场景，帮助开发者了解与掌握智能手表相关的特有场景开发。
由于手机手表互联通信涉及到WearEngine的使用，因此需要去AGC上[申请接入WearEngine服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wearengine_apply)，请开发者参考链接进行WearEngine权限的申请与签名的手动配置。

### 效果预览
手机运行效果图：

![](./screenshots/phone.png)

手表地图页：

![](./screenshots/watch.png)


### 工程代码结构
```                                      
├───commons                                                   // commons层
│   └───utils/src/main/ets/utils                              // 工具
│       └───ConnectUtil.ets                                   // 互联工具类
└───products                                                  // 产品定制层
    ├───phone/src/main/ets                                    // 手机模块
    │   ├───entryability                            
    │   │   └───EntryAbility.ets                              // 程序入口类
    │   ├───entrybackupability                      
    │   │   └───EntryBackupAbility.ets                        // 数据备份恢复
    │   ├───pages
    │   │   ├───Index.ets                                     // 首页         
    │   │   └───NotifyPage.ets                                // 互联通信页       
    │   └───view                                   
    │       └───ConnectView.ets                                // 互联通信页视图
    ├───phone/src/main/resources 
    ├───wearable/src/main/ets                                  // 手表模块
    │   ├───applicationbackupability                            
    │   │   └───ApplicationBa


---
## PicturePreview
> 本示例是基于ArkUI接口和swiper组件实现的图片预览应用，其功能包括图片的切换、图片的缩放，同时支持通过双击图片实现放大或缩小的效果，并且在图片被放大后，可以对图片进行滑动查看，当图片滑动到边界时，可切换图片。

源码: https://gitcode.com/HarmonyOS_Samples/PicturePreview

# 基于ArkUI实现图片预览功能

### 简介
本示例是基于ArkUI接口和swiper组件实现的图片预览应用，其功能包括图片的切换、图片的缩放，同时支持通过双击图片实现放大或缩小的效果，并且在图片被放大后，可以对图片进行滑动查看，当图片滑动到边界时，可切换图片。

### 效果预览
![image](screenshots/device/PicturePreview_CN.gif)

### 工程目录
```
├──entry/src/main/ets                            // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets                        // 本地启动ability      
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                     
│  ├──model
│  │  └──CommonModel.ets                         // 公共实体类        
│  ├──pages
│  │  └──HomePage.ets                            // 主页面    
│  ├──utils
│  │  └──CommonUtils.ets                         // 公共工具类
│  └──view
│     ├──ImageItemView.ets                       // 主图模块
│     └──ThumbnailView.ets                       // 缩略图模块
└──entry/src/main/resources                      // 资源文件目录
```

### 使用说明
1. 左右滑动/点击页面下方缩略图，主图图片会随之变化。
2. 轻触页面，开启图片预览模式。
3. 双击图片可切换其大小，在预览模式下再次双击，图片恢复至默认尺寸。
4. 双指轻捏图片，即可轻松实现缩放操作。
5. 在图片预览模式下，左右滑动页面中的图片，即可切换至下一张或上一张图片。

### 具体实现
1. 使用matrix实现图片的缩放。

   ```
   @State matrix: matrix4.Matrix4Transit = matrix4.identity().copy();
   
   Image(this.imageData)
     .transform(this.matrix)
   ```

2. 使用translate属性对图片进行偏移。

   ```
   @State curOffsetX: number = 0;
   @State curOffsetY: number = 0;
   
   Image(this.imageData)
     .translate({
       x: this.imageModel.curOffsetX,
       y: this.imageModel.curOffsetY
     })
   ```

3. Image的objectFit属性设置为Cover，锁定图片宽高比，并使其能够超出父组件边界显示。

   ```
   Image(this.imageData)
     


---
## PixelMapImageEdit
源码: https://gitcode.com/HarmonyOS_Samples/PixelMapImageEdit

# 基于PixelMap编解码图片编辑功能

## 项目简介
通过图片解码将图片转换为PixelMap格式，获取并展示解码后的原图信息。基于PixelMap实现图片编辑功能，包括几何变换(裁剪、旋转、平移、缩放、镜像)和颜色调整(亮度、透明度、饱和度）等功能。完成编辑后，可将图片重新编码并保存至图库。

## 效果预览
| 裁剪                                                       | 图片信息                                                     | 调节                                                       |
|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| <img src="./screenshots/zh1_converted.png" width="320"/> | <img src="./screenshots/zh2_converted.png" width="320"/> | <img src="./screenshots/zh3_converted.png" width="320"/> |

| 滤镜                                                       | 平移                                                       | 缩放                                                       |
|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| <img src="./screenshots/zh4_converted.png" width="320"/> | <img src="./screenshots/zh5_converted.png" width="320"/> | <img src="./screenshots/zh6_converted.png" width="320"/> |

## 使用说明

1. 点击顶部信息按钮，查看原图信息。
2. 使用底部标签页切换不同的编辑功能：
   - **裁剪**：支持多种比例裁剪
   - **调节**：调整图片亮度、透明度、饱和度
   - **滤镜**：应用各种滤镜效果
   - **平移**：水平和垂直移动图片
   - **缩放**：放大或缩小图片
3. 实时预览编辑效果。
4. 点击保存按钮保存编辑后的图片。

## 工程目录

```
├──ets
│  ├──common
│  │  └──constant
│  │     └──consta


---
## PlayShortVideosBasedOnVideoComponent
> 本示例基于Video组件实现短视频播放，实现了包括基础播控、自定义进度条、全屏播放、跳转播放、播放倍速调节、自动连播、音量控制以及前后台状态感知等功能。

源码: https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent

# 基于Video组件播放短视频

## 项目简介

本示例基于Video组件实现短视频播放，实现了包括基础播控、自定义进度条、全屏播放、跳转播放、播放倍速调节、自动连播、音量设置以及前后台状态感知等功能。

## 效果预览

| 基础播控                                | 播放倍速调节                              | 音量设置                                |           
|-------------------------------------|-------------------------------------|-------------------------------------|
| ![image](screenshots/effect_01.png) | ![image](screenshots/effect_02.png) | ![image](screenshots/effect_03.png) |

| 全屏播放                                | 
|-------------------------------------|
| ![image](screenshots/effect_04.png) |

## 使用说明

1. 启动应用后视频自动播放；点击视频画面可暂停，再次点击则继续播放。
2. 点击或拖动进度条，即可跳转至指定时间点。
3. 长按视频画面左侧或右侧，可将播放速度切换为2倍速。
4. 在视频画面上长按并垂直滑动，可调出音量控制条：上滑增大音量，下滑减小音量。
5. 点击进度条右侧的全屏按钮，或横置设备，均可进入全屏模式；进入全屏后，点击返回按钮即可退出。
6. 应用退至后台时，视频自动暂停；重新回到前台后，视频将从暂停处继续播放。
7. 当前视频播放结束后，将自动连播下一个视频。

## 工程目录

```
├───entry/src/main/ets
│   ├───common                        
│   │   ├───TimeUtils.ets                   // 时间工具
│   │   ├───VideoData.ets                   // 视频资源
│   │   ├───VideoDataModel.ets              // 视频定义类
│   │   └───WindowUtil.ets      	        // 窗口工具
│   ├───constants                               
│   │   └───CommonConstants.ets             // 常量
│   ├───entryability                        
│   │   └───EntryAbility.ets                // Ability的生命周期回调内容
│   ├───entrybackupability                  
│   │   └───EntryBackupAbility.ets          // 程序备份和恢复
│   ├───pages                               
│   │   └───Index

**EntryAbility.ets**
```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { WindowUtil } from '../common/WindowUtil';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    WindowUtil.getInstance().setWindowStage(windowStage);
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      try {
        let windowClass: window.Window = windowStage.getMainWindowSync();
        windowClass?.setWindowLayoutFullScreen(true).catch(() => {
          hilog.error(DOMAIN, 'testTag', 'setWindowLayoutFullScreen is failed.');
        });
      } catch (err) {
        hilog.error(DOMAIN, 'testTag', 'Failed to getMainWindowSync. Cause: %{public}s', JSON.stringify(err));
      }
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  // [Start get_isForeGround]
  
```


---
## PureTabs
源码: https://gitcode.com/HarmonyOS_Samples/PureTabs

# Tabs组件应用场景
### 简介    
 本示例主要展示了HarmonyOS中ArkUI框架下的Tabs组件在日常开发中常用的场景实践，将各子场景结合设计出的一个综合场景，并使用MVVM模式组织代码，示例包含如下场景
- 实现双层嵌套Tabs
- 实现tabs滑动吸顶
- 实现底部自定义变化页签
- 实现顶部可滑动标签
- 实现增删现实页签项
- 实现Tabs切换动效
### 效果预览
| 双层Tabs嵌套，自定义页签样式                      | 页签上滑吸顶                                | 增删显示页签                          | 可滑动页签                             |                         
|---------------------------------------|---------------------------------------|--------------------------------------|---------------------------------------|
| ![image](screenshots/device/tab1.png) | ![image](screenshots/device/tab2.png) | ![image](screenshots/device/tab3.png) | ![image](screenshots/device/tab4.png) |
### 使用说明
1. 下载sample，编译运行
2. 下方Tabs为外层Tabs，可展示自定义页签功能
3. 上方依次往下为搜索栏、广告位、内层Tabs，上下滑动内层Tabs可展示滑动吸顶功能，左右滑动内层Tabs可展示Tabs切换动效功能
4. 点击内层Tabs选项卡最右方的更多按钮，展示自定义Tabs选项面板，可选择需要展示的Tab选项，关闭面板后生效，以展示动态增删页签功能

### 工程目录
```
├──entry/src/main/ets                       // 代码区
│  ├──common                                // 
│  │  ├──constant
│  │  │  └──Constants.ets                   // 常量类
│  │  └──utils
│  │     └──StringUtil.ets                  // 字符串工具类
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──model
│  │  ├──ContentItemModel.ets               // 展示内容项数据类
│  │  ├──InTabsModel.ets                    // 展示内容列表数据类
│  │  ├──SelectTabsModel.ets                // 选择显示页签数据类
│  │  └──TabItemModel.ets                   // 页签项数据类
│  ├──pages
│  │  


---
## Push-kit-service-notification-sample-code-java
> 本示例基于Java语言实现了向元服务推送基于账号的订阅消息。

源码: https://gitcode.com/HarmonyOS_Samples/Push-kit-service-notification-sample-code-java

# Push Kit 服务通知 服务端 demo

- 本 demo 为面向 Java 的元服务通知示例代码。
- 本 demo 与 Push Kit 服务通知 端侧的[服务通知-推送服务-客户端](https://gitcode.com/harmonyos_samples/push-kit-sample-code-client-atomic-arkts)demo 提供的服务对应，您可先调试端侧 demo,发起基于账号的订阅请求并通过用户授权,后再使用本 demo 发送消息。
- 若您已有自己的端侧代码，也可直接使用本 demo 发送通知消息；

## 支持发送的通知

- [服务通知](src/main/java/com/huawei/push/notification/NotificationSendExamples.java)
  - [消息参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-api-service-noti#section18768181215219)
    - thing:可汉字,字母,数字或符号组合(128位以内)。值不可为空。
    - time:代表日期或时间范围，值不可为空。  
      样例：  
      2023年1月1日 22:22  
      2023年1月1日 22:22:00  
      2023年1月1日 00:00~2023年1月2日 23:59  
      2023年1月1日 00:00:00~2023年1月2日 23:59:59  
      2023年1月1日 00:00~12:30  
      2023年1月1日 00:00:00~12:30:00  
      2023年1月1日  
      2023年1月1日~2023年1月2日。
    - phone_number:代表电话号码。数字，符号，电话号码，如：+86-025-85697456。值不可为空。
    - car_number:代表车牌号。8位以内，第一位与最后一位可为汉字，其余为字母或数字，例如车牌号码：粤A8Z888挂。值不可为空。

  - 点击消息动作
    - [点击消息进入应用首页并传递数据](https://developer.huawei.com/consumer/cn/doc/atomic-guides/push-as-send-sub-noti#section561410563213)
    - [点击消息进入应用内页并传递数据](https://developer.huawei.com/consumer/cn/doc/atomic-guides/push-as-send-sub-noti#section9101628153218)
  

## 支持的 Java 版本

Java 8+

## 快速开始

### 下载

下载此 demo 并在 IDE 中打开。

### 开发准备

1. 参考[开通服务通知并选用订阅模板](https://developer.huawei.com/consumer/cn/doc/atomic-guides/push-as-service-noti)，开通服务通知并选用订阅模板。
2. 获取 Service Account 凭据文件，具体步骤如下：

- 登录华为开发者联盟，进入[API Console](https://develo


---
## QueryAppPackageInfo
源码: https://gitcode.com/HarmonyOS_Samples/QueryAppPackageInfo

# 实现查询应用包信息功能

### 简介

本示例主要介绍如何获取应用包相关信息并展示，主要包括在ArkTS侧分别获取应用图标、名称等resource资源信息和应用包签名信息以及在Native侧获取应用包名和签名信息。基于本示例，开发者可以掌握应用包管理相关的使用能力。

### 效果预览
![](screenshots/device/QueryAppPackageInfo.gif) 

### 使用说明

在主页面中点击对应按钮会分别跳转到不同场景的页面。在每个场景页面中都包含了一个信息展示区域和一个按钮，点击按钮会调用接口将相关信息显示到信息展示区域上。

#### 提醒

模拟器中不包含应用包签名相关信息，所以如果在模拟器中运行代码，获取签名相关信息时可能会显示为空。

### 工程结构
```
├──entry/src/main/cpp                   // C++代码区
│  ├──types
│  │  └──libentry                       // C++接口导出
│  │     ├──Index.d.ts                
│  │     └──oh-package.json5           
│  ├──CMakeLists.txt                    // Cmake配置文件 
│  └──napi_init.cpp                     // Native侧代码区
├──entry/src/main/ets                   // ArkTS代码区                  
│  ├──common        
│  │  └──CommonConstants.ets            // 常量定义文件
│  ├──entryability        
│  │  └──EntryAbility.ets                                
│  ├──entrybackupability 
│  │  └──EntryBackupAbility.ets                           
│  ├──model                
│  │  ├──AppInfoData.ets                // 应用包信息初始数据 
│  │  ├──AppInfoItem.ets                // 应用包信息通用类 
│  │  ├──AppSignatureInfoData.ets       // 应用包签名信息初始数据
│  │  └──NativeAppInfoData.ets          // Native侧应用包信息初始数据
│  ├──pages     
│  │  ├──GetAppInfo.ets                 // ArkTS侧获取应用包信息页面 
│  │  ├──GetSignatureInfo.ets           // ArkTS侧获取应用包签名信息页面 
│  │  ├──MainPages.ets                  // 主页面 
│  │  └──NativeGetAppInfo.ets           // Native侧获取应用包信息页面           
│  └──view    
│     └──


---
## RAG_QA
源码: https://gitcode.com/HarmonyOS_Samples/RAG_QA

# 基于RAG实现智能问答系统

### 介绍
本示例利用ArkData向量数据库，和RAG的开发框架，针对邮件的信息格式，开发一个邮件信息提取总结问答助手。
通过接入LLM进行多次流式问询并对私域数据在端侧进行知识加工，在通过LLM进行知识问答的过程中附带准确相关的私域信息，帮助大模型生成更加精准的回答内容

## 效果预览
| 对话                                            | 
|-----------------------------------------------|
| <img src='./screenshots/index.png' width=320> | 

## 使用说明
### ChatLLM apikey生成与配置
1. 进入并登录网址ModelArts - Console (https://console.huaweicloud.com/modelarts/?locale=zh-cn&region=cn-southwest-2#/model-studio/homepage)，
   在顶部导航栏选择对应区域，在左侧菜单中选择API Key管理，点击右上角创建API key，生成Key。 生成的key值只在弹窗中出现一次，请立刻保存后再关闭弹窗。
2. 在  LLMHttpUtils.ets 中进行key的配置，粘贴到Authorization属性中，"Authorization": "Bearer 生成的key值“
3. 在左侧菜单中选择在线推理，在商用服务列表中开通商用服务Qwen3-235B-A22B-32K。
4. 在右上角费用中心-总览 管理页面进行服务充值。

### 编译安装
使用DevEco Studio打开工程，并进行编译安装。

### 触发知识加工
> 日志过滤knowledge，如果有相关日志且未报错，说明知识加工已启动，不再新增knowledge日志，则说明加工结束，问答需要在加工结束后进行，加工流程约十分钟左右。如果未触发或者加工报错，则重启Demo（不用点击清理重建按钮），查看日志。

### 应用使用
1. 系统已经内置部分邮件，包括手机优惠政策、搬迁等信息，具体见resource->rawfile->sourceData.json，提问相关内容系统给出回答。
2. 点击右下角添加信息按钮，输入邮件信息并确认，进行提问后可以得到与知识库相关的回答。

## 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │   └──utils                           // 工具
│  │     └──LLMHttpUtils.ets              // 大模型工具
│  ├──entryability
│  │   └──EntryAbility.ets                // Ability的生命周期回调内容
│  ├──entrybackupability
│  │   └──EntryBackupAbility.ets          // EntryBackupAbility的生命周期回调内容
│  ├──pages                
│  │   └──Index.ets                       //  主页，邮件插入弹窗
│  ├──view                
│  │   └──Custo


---
## RcpFileTransfer
源码: https://gitcode.com/HarmonyOS_Samples/RcpFileTransfer

## 基于RCP实现文件上传下载功能

### 介绍

本示例基于Remote Communication Kit远场通信服务，使用post、fetch、downloadToFile等方法实现相册的文件上传下载、文件分片下载、断点续传、后台文件上传下载功能。为开发者提供基于RCP上传下载各种场景的开发指导。

### 效果预览

![](./screenshots/devices/home.png)

使用说明：
1. 环境配置：根据[文件服务器配置](./service/README.md)配置本地文件服务器。
2. 相册图片上传与下载：页面展示文件服务器中的图片列表，选中某个文件，点击下载，下载成功后在相册查看。点击上传拉起相册，选择图片后上传，上传成功更新列表。
3. 文件断点续传：选中某个文件，点击下载，按钮变为暂停，再点击下载开始继续下载。
4. 其他页面交互逻辑与1相同。

### 工程目录

```
├──entry/src/main/ets/                              
│  ├──components             
│  │  ├──CustomList.ets                             // 自定义列表组件
│  │  ├──ProgressButton.ets                         // 带进度显示的按钮组件
│  │  └──SelectionList.ets                          // 选择列表组件
│  ├──entryability
│  │  └──EntryAbility.ets                           // 程序入口类
│  ├──constants
│  │  └──Constants.ets                              // 常量文件
│  ├──pages             
│  │  ├──AlbumImageTrasfer.ets                      // 相册图片上传下载页面
│  │  ├──BackgroundFileTransfer.ets                 // 后台文件上传下载页面
│  │  ├──ChunkedFileTransfer.ets                    // 文件分片下载页面
│  │  ├──Index.ets                                  // 应用首页
│  │  └──ResumableFileTransfer.ets                  // 断点续传页面
│  ├──service             
│  │  ├──Env.ets                                    // 服务端环境配置文件
│  │  ├──FileRequest.ets                            // 文件上传下载请求接口模块
│  │  ├──Formatter.ets                              // 服务端与客户端数据格式化模块
│  │  ├──Interceptor.ets                            // 请求拦截相关类
│  │  └──Model.ets   


---
## RemoteCommunicationPlatform
> 本实例介绍remote communication platform（简称RCP）的一些网络请求能力，包括基础网络请求、多表单提交、双向证书校验、DNS的相关设置、请求与响应拦截和捕获有关HTTP请求/响应流的详细信息等。

源码: https://gitcode.com/HarmonyOS_Samples/RemoteCommunicationPlatform

# 基于RCP的网络请求能力
## 介绍
RCP指的是远程通信平台（remote communication platform），RCP提供网络数据请求功能，相较于Network Kit中HTTP请求能力，RCP更具易用性，且拥有更多的功能。例如：
* 支持发送PATCH请求

* 支持设置BaseURL

* 支持取消请求，取消指定或正在进行的会话请求

* 支持自定义证书校验，可以根据自身业务需要，对证书进行校验

* 支持自定义DNS解析

* 支持自定义拦截器实现响应缓存

* 支持在会话中的HTTP请求期间捕获详细的跟踪信息
## 预览效果
![](screenshots/device/rcp.gif)
## 工程目录
``` 
├──entry/src/main/ets                                   // 代码区
│  ├──common
│  |  ├──CommonConstants.ets                            // 日志工具类
│  |  └──Logger.ets                                     // 常量
│  ├──entryability
│  |  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  |  └──EntryBackupAbility.ets
│  ├──pages
│  |  ├──BaseRequest.ets                                // 基础网络请求
│  |  ├──DNSSetting.ets                                 // DNS相关设置
│  |  ├──Index.ets                                      // 首页
│  |  ├──MultipartForm.ets                              // 多表单提交
│  |  ├──RequestAndResponse.ets                         // 请求与响应拦截示例
│  |  └──TracingPoint.ets                               // 捕获有关HTTP请求/响应流的详细信息
|  └──utils.ets                            
│     └──Interceptors.ets                               // 请求与响应拦截
└──entry/src/main/resources                             // 应用资源目录
``` 
## 相关权限
应用需要访问互联网，需要使用网络权限。

`ohos.permission.INTERNET`
## 使用说明
1. 点击“基础请求”按钮跳转至二级页面，点击“发起PATCH请求”按钮，可发起PATCH请求；点击“设置会话中URL的基地址”按钮，可设置请求的BaseUrl。
2. 点击“多表单提交”按钮跳转至二级页面，在表单一中输入姓名；切换至表单二中选择兴趣爱好。点击“提交”按钮，可进行表单提交并展示相关参数。
3. 点击“请求与响应拦截


---
## ResponsiveLayout
> 本示例展示了如何使用HarmonyOS提供一多响应式能力，在多设备（直板机、双折叠、三折叠、平板、PC/2in1）上实现常见的响应式布局。

源码: https://gitcode.com/HarmonyOS_Samples/ResponsiveLayout

# 基于一多能力实现响应式布局

## 介绍

本示例展示了如何使用HarmonyOS提供一多响应式能力，在多设备（直板机、双折叠、三折叠、平板、PC/2in1）上实现常见的响应式布局。

## 效果展示

手机运行效果图：

![](screenshots/device/mate60pro.png)

双折叠运行效果图：

![](screenshots/device/matex5.png)

三折叠运行效果图：

![](screenshots/device/matext.png)

平板运行效果图：

![](screenshots/device/matepadpro.png)

PC/2in1运行效果图：

![](screenshots/device/matebookx.png)

## 使用说明

应用可以点击首页不同的列表项，展示在多设备上的响应式布局页面效果，包括：列表布局、瀑布流布局、轮播布局、宫格布局、侧边栏、二分栏、三分栏、挪移布局、底部/侧边导航和缩进布局。
在二分栏和三分栏布局中，分别展示了聊天、日历和邮箱应用场景，帮助开发者使用分栏布局。

## 工程目录

```
├──entry/src/main/ets/
│  ├──constants                          
│  │  ├──CommonConstants.ets             // 通用常量类
│  │  ├──ConversationConstants.ets       // 会话相关常量类
│  │  └──ProductDetailConstants.ets      // 商品详情常量类
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages
│  │  ├──DoubleColumnConversation.ets    // 单双栏聊天页 
│  │  ├──DoubleColumnLayout.ets          // 单双栏页
│  │  ├──GridLayout.ets                  // 网格页
│  │  ├──IndentedLayout.ets              // 缩进布局页
│  │  ├──Index.ets                       // 主页
│  │  ├──ListLayout.ets                  // 列表布局页
│  │  ├──MoveLayout.ets                  // 挪移布局页
│  │  ├──SidebarLayout.ets               // 侧边栏页
│  │  ├──SwiperLayout.ets                // 轮播布局页
│  │  ├──TabsLayout.ets                  // 底部/侧边导航页
│  │  ├──TripleColumnCalendar.ets        // 三分栏日历页
│  │  ├──TripleColumnLayout.ets          // 三分栏页
│  │  ├──TripleColumnMail.ets            // 三分栏邮箱页
│  │  └──Wate


---
## SmallWindowScene
源码: https://gitcode.com/HarmonyOS_Samples/SmallWindowScene

# 基于上下分屏实现滑动沉浸式浏览能力

### 介绍

本示例介绍应用在手机（直板机）上下分屏或Pura X外屏使用时的典型场景适配，包含使用List组件或Scroll组件滑动能力相关事件实现滑动沉浸式浏览，使用Scroll组件实现页面支持滑动，使用Stack组件实现短视频播放页，和使用constraintSize限制约束尺寸实现弹窗适配小窗口。

### 效果图预览

|          | 首页                                                    | 首页/分屏（动沉浸式浏览）                                                  | 短视频                                                   | 图文详情                                                  | 瀑布流场景                                                 |
|----------|-------------------------------------------------------|----------------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| Pura X外屏 | <img src='screenshots/devices/home_tools_widefolding_cn.png' width=320> | <img src='screenshots/devices/home_no_tools_widefolding_cn.png' width=320> | <img src='screenshots/devices/short_video_widefolding_cn.png' width=320> | <img src='screenshots/devices/image_text_widefolding_cn.png' width=320> | <img src='screenshots/devices/waterfall_flow_widefolding_cn.png' width=320> |
| 直板机      | <img src='screenshots/devices/home_tools_phone_cn.png' width=320> | <img src='screenshots/devices/home_no_tools_phone_cn.png' width=320> | <img src='screenshots/devices/short_video_phone_cn.png' width=320> | <img src='screenshots/devices/image_text_phone_cn.png' width=320> | <img src='screenshots/device


---
## SmartPhotoPicker
源码: https://gitcode.com/HarmonyOS_Samples/SmartPhotoPicker

# 基于PhotoPicker实现图片推荐功能

### 介绍

本示例旨在解决特殊场景需要相册picker提供图片推荐功能的问题，主要使用接口与组件两种方式，拉起系统photoPicker，并分别实现了基于recommendationType配置完成特定服务类型的图片推荐，以及基于textContextInfo配置完成文案的图片推荐 ，帮助开发者通过PhotoPicker实现图片推荐功能。

### 效果预览
![](screenshots/Devices/smartPhotoPicker.png)

#### 使用说明：

1. 点击首页的两个按钮，分别进入通过组件实现与通过接口实现的页面。
2. 点击不使用图片推荐能力，仅拉起一个普通的picker界面。
3. 下拉框选择身份证或二维码，点击基于特定服务推荐图片按钮，若相册中存在该类型的图片，会拉起对应类型图片的picker界面。
4. 输入文案（例如：人像、银行卡等），会识别并拉起特殊文案推荐picker进行推荐。
5. 当前TextContextInfo仅支持250字以内的简体中文，输入英文字符无法进行图片推荐。

### 工程目录
```
├──entry/src/main/ets                                  // 代码区
│  ├──commons                                  
│  │  └──utils          
│  │     └──SmartPhotoPickerUtils.ets                   // picker接口工具类
│  ├──entryability  
│  │  └──EntryAbility.ets 
│  ├──entrybackupability  
│  │  └──EntryBackupAbility.ets
│  ├──pages                                
│  │  └──Index.ets                                      // 首页
│  └──view  
│     ├──ComponentImplPage.ets                          // 组件实现页
│     └──InterfaceImplPage.ets                          // 接口实现页    
└──entry/src/main/resources                             // 应用资源目录

```

### 具体实现
* 基于接口实现特定服务类型的图片推荐，需要将recommendationType配置到recommendationOptions，随后配置到PhotoSelectOptions中。
```typescript
// SmartPhotoPickerUtils.ets
let recommendationOptions: photoAccessHelper.RecommendationOptions = {
  recommendationType: recommendType
};
let option: photoAccessHelper.PhotoSelectOptions = {
  recommendationOptions: recommendationOptions,


---
## SmartWatchCarControl
源码: https://gitcode.com/HarmonyOS_Samples/SmartWatchCarControl

# 实现智能手表上的车控应用

### 介绍

本实例旨在通过完成智能手表上远程车控应用的实现，通过Swiper组件、TextPicker组件等的使用，帮助开发者学习智能手表设备的布局特点以及布局方式。

### 效果预览
| 车辆信息页                                                 | 车辆控制页                                                   |
|-------------------------------------------------------|---------------------------------------------------------|
| <img src="./screenshots/devices/car_Information.png" width="320"> | <img src="./screenshots/devices/car_control.png" width="320"> |

#### 使用说明：

1. 首页包含车辆信息页和车辆控制页，可以通过上下滑动切换视图。
2. 车辆控制页包含五个按钮，车锁、车窗、空调、后备箱、寻车。
3. 车锁按钮点击后跳转安全码页面，输入123456即可成功，并返回车辆控制页，表示密码正确，车锁打开；输入不为123456，弹窗告知用户密码错误，密码清空，不进行跳转。
4. 车窗按钮点击后，按钮会在蓝和灰背景间切换，表示车窗的开与关。
5. 空调按钮点击后，跳转至空调控制页，滑动选取温度，点击开启空调，会跳转安全码页，输入成功后返回空调控制页，表示开启成功。
6. 后备箱按钮点击后，会跳转后备箱控制页，上划滑动条至顶部，跳转安全码页，输入密码跳转回车辆控制页，表示后备箱打开。
7. 寻车按钮点击后，会跳转寻车页，点击两个寻车按钮，会在一个加载动效后，弹窗提示寻车已开启。


### 工程目录
```
├──entry/src/main/ets                                  // 代码区
│  ├──commons                                  
│  │  └──constants          
│  │     └──CommonConstants.ets                        // 常量类
│  ├──entryability  
│  │  └──EntryAbility.ets 
│  ├──entrybackupability  
│  │  └──EntryBackupAbility.ets
│  ├──model  
│  │  └──Dot.ets                                       // 密码输入点实体类
│  ├──pages  
│  │  └──Index.ets                                     // 首页
│  └──view  
│     ├──CarControlView.ets                            // 车辆控制视图类
│     ├──CarInformationView.ets                        // 车辆信息视图类
│     ├──ConditionerPageView.


---
## SmartWatchMap
源码: https://gitcode.com/HarmonyOS_Samples/SmartWatchMap

# 实现智能手表上的地图应用

## 简介

本示例使用Map Kit的基本能力，实现了智能手表上查看地图并实现定位的功能，指导开发者在穿戴设备上适配地图。

## 效果预览

<img src="./screenshots/device/home.png" width="320">

## 使用说明

1. 进入主页，授予应用获取位置权限。
2. 点击定位按钮，地图视图移动至当前位置。

## 工程目录
```
├──entry/src/main/ets                     // 代码区
│  ├──common  
│  │  └──util                 
│  │     └──PermissionUtil.ets            // 权限工具类  
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  └──pages
│     └──Index.ets                        // 首页
└──entry/src/main/resources               // 应用静态资源目录
```

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为智能穿戴。
2. HarmonyOS系统：HarmonyOS 5.1.0 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.1.0 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.1.0 Release SDK及以上。


---
## SmartWatchMapNavigation
源码: https://gitcode.com/HarmonyOS_Samples/SmartWatchMapNavigation

# 基于WearEngine实现协同导航应用

## 介绍

本示例基于WearEngine、Map Kit、Location Kit及Sensor Kit，通过deviceClient.getConnectedDevices()、p2pClient.sendMessage()等核心接口，实现了一个手机与智能手表协同操作的地图导航应用。该示例为开发者提供了跨设备通信与地图导航功能的完整实现方案，可作为开发同类应用的参考范例。

## 效果展示

手机运行效果图：

![](screenshots/device/phone.png)

手表地图页：

![](screenshots/device/wearable_map.png)

手表导航页：

![](screenshots/device/wearable_navigation.png)


## 使用说明

1. 手机手表运行应用授权后，展示地图。
2. 手机手表均可通过点击地图，点击后地图生成标记，表示目的地。对目的地的选择，手机操作后会同步至手表，手表操作也会同步至手机。
3. 确定目的地后，手机点击绘制路线按钮，手机会展示路线。
4. 手机点击开始导航按钮后，手表将进行路由跳转，进入导航页，根据导航路线进行步行导航。（导航为真实导航，但与自身位置无关，手机会通过SetTimeOut定时发送导航信息）。
5. 导航结束后，手表进行震动提醒，弹窗显示到达目的地，手表返回地图页。

## 工程目录

```
└───SmartWatchMapNavigation                                        
    ├───commons                                                   // commons层
    │   ├───Communication/src/main/ets/common                     // 互联通信模块
    │   │   ├───model                                             // model
    │   │   │   ├───CommunicationInformation.ets                  // 互联通信消息实体类
    │   │   │   └───RouteInfomation.ets                           // 路线信息实体类
    │   │   └───utils                                             // 工具类
    │   │       └───CommunicationUtils.ets                        // 互联通信工具类
    │   ├───map/src/main/ets                                      // 地图模块
    │   │   ├───common                                            // 
    │   │   │   └───utils                                         // 工具
    │   │   │       └───DrawRouteUtils.


---
## SmartWatchRideNavigation
源码: https://gitcode.com/HarmonyOS_Samples/SmartWatchRideNavigation

# 实现智能手表上的骑行导航应用

## 介绍

本实例旨在通过智能表骑行导航类应用页面的实现，通过Navigation组件完成智能手表设备的页面跳转，帮助开发者学习智能表设备的布局特点以及布局方式。

## 效果预览

| 二维码                                                  | 语音搜索页                                                | 搜索结果页                                                | 路线选择页                                                | 路线导航页                                                |
|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| <img src="./screenshots/device/img_2.png" width=320> | <img src="./screenshots/device/img_1.png" width=320> | <img src="./screenshots/device/img_5.png" width=320> | <img src="./screenshots/device/img_4.png" width=320> | <img src="./screenshots/device/img_3.png" width=320> |



## 使用说明：

1. 首页包含一个二维码，通过点击二维码模拟手机扫码登录的场景，点击后跳转至语音搜索页。
2. 通过点击麦克风按钮模拟语音输入的场景，点击后直接跳转至搜索结果页。
3. 搜索结果可以滑动展示，列表项点击后跳转至路线选择页。
4. 路线选择页主要内容为长列表，列表项点击后跳转至路线导航页。
5. 路线导航页内容固定，点击停止导航后跳转回语音搜索页。


## 工程目录
```
├──entry/src/main/ets                                  // 代码区
│  ├──commons                                  
│  │  └──constants          
│  │     └──CommonConstants.ets                        // 常量类
│  ├──entryability  
│  │  └──EntryAbility.ets 
│  ├──entrybackupability  
│  │  └──EntryBackupAbility.ets
│  ├──model  
│  │  ├──LocationInfo.ets         


---
## SmartWatchShortVideo
源码: https://gitcode.com/HarmonyOS_Samples/SmartWatchShortVideo

# 实现智能手表上的短视频应用

## 简介

本示例实现了一款智能手表上的短视频应用，可在应用页面内查看视频推荐列表、播放视频，并展示二维码页面，支持使用手机扫码。

## 效果预览

| 热搜推荐页                                                 | 更新提醒页                                                   | 视频播放页                                                  |
|-------------------------------------------------------|---------------------------------------------------------|--------------------------------------------------------|
| <img src="./screenshots/device/home.png" width="320"> | <img src="./screenshots/device/update.png" width="320"> | <img src="./screenshots/device/video.png" width="320"> |

## 使用说明

1. 进入主页，上下滑动页面查看推荐列表；左右滑动切换“热搜推荐”、“更新提醒”视图。
2. 点击“热搜推荐”中任意图片，进入视频播放页面。
3. 点击暂停/播放按钮控制视频播放状态；点击放大/缩小按钮改变视频大小；拖动进度条更改视频进度。

## 工程目录
```
├──entry/src/main/ets                     // 代码区
│  ├──common
│  │  ├──constants     
│  │  │  └──CommonConstants.ets           // 常量类         
│  │  └──util                 
│  │     └──ScreenUtil.ets                // 屏幕工具类  
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages
│  │  └──Index.ets                        // 首页
│  └──view
│     ├──HotSearchView.ets                // 热搜推荐页
│     ├──UpdateReminderView.ets           // 更新提醒页
│     └──VideoView.ets                    // 视频播放页
└──entry/src/main/resources               // 应用静态资源目录
```

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为智能穿戴。
2. HarmonyOS系统：HarmonyOS 5.1.0 Release及以上。
3. DevEco Studio版本：Dev


---
## SmartWatchTakeTaxi
源码: https://gitcode.com/HarmonyOS_Samples/SmartWatchTakeTaxi

# 实现智能手表上的打车应用

## 项目简介

本示例实现了一款智能手表上的打车应用，可在应用页面上显示打车进度和提示信息，并基于组件导航(Navigation)和定时器能力(Timer)，实现页面之间的定时跳转。

## 效果预览
| 首页                                                        |
|-----------------------------------------------------------|
| <img src="./screenshots/devices/TakeTaxi.png" width=320> |

## 使用说明

1. 进入主页，点击"回家"或"公司"按钮进去打车流程，每个页面停留3s后自动跳转至下一页面，直到跳转至行程结束页。

2. 在找车页点击"取消打车"按钮、在司机赶来页和司机到达页点击"取消行程"按钮、在行程结束页点击"我知道了"按钮，跳转回首页。

3. 在前往目的地页点击"结束行程"按钮，跳转至行程结束页。

## 功能特性
### 技术原理

+ 在司机赶来页、司机到达页和前往目的地页的页面显示接口onShown()中，通过setTimeout()接口设置一个3s的定时器，并在定时器到期后自动刷新页面内容或跳转至下一页面；在页面隐藏接口onHidden()中，通过clearTimeout()接口删除定时器。

+ 在找车页通过TextTimer组件实现文本显示计时信息和定时跳转功能。在页面的显示接口onShown()中开启计时，并通过TextTimer的onTimer()接口触发3s后跳转至下一页面；在页面隐藏接口onHidden()中暂停定时。

## 工程目录

```
├──entry/src/main/ets                     // 代码区
│  ├──common
│  │  └──utils                            
│  │     └──WindowManager.ets             // 窗口管理类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets           
│  ├──pages
│  │  └──Index.ets                        // 主页面
│  └──view
│     ├──FindCar.ets                      // 找车页
│     ├──OnTheWay.ets                     // 前往目的地页
│     ├──PayTheBill.ets                   // 行程结束页
│     └──WaitingAndSuccess.ets            // 司机赶来页和司机到达页
└──entry/src/main/resources               // 应用静态资源目录
```

## 相关权限

不涉及。

## 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为智能穿戴。

2.HarmonyOS系统：HarmonyOS 5.1.0 Release及以上。

3.DevEco


---
## SmoothSwitchShortVideos
> 本示例基于在线短视频场景，通过LazyForEach进行数据懒加载，同时搭配组件复用能力以达到高性能效果，帮助开发者解决在应用中在线短视频快速切换时容易出现起播时间延长的问题，提供对应场景的解决方案。

源码: https://gitcode.com/HarmonyOS_Samples/SmoothSwitchShortVideos

# 实现流畅切换短视频

### 简介

本示例基于在线短视频场景，通过LazyForEach进行数据懒加载，同时搭配组件复用能力以达到高性能效果，帮助开发者解决在应用中在线短视频快速切换时容易出现起播时间延长的问题，提供对应场景的解决方案。

### 效果预览：

![image](screenshots/Main.png)

### 使用说明：

1. 本示例需要访问网络视频直链来获取视频资源，您可以修改entry/src/main/ets/common/CommonConstants.ets中的VIDEO_SOURCE为想要播放的视频直链，本示例也提供了本地视频和本地搭建服务器的方案，来模拟访问网络视频的情况，请参考《搭建服务器》章节。

2. 安装应用后打开，应用会播放资源链接的视频，可上下滑动切换短视频。

### 搭建服务器

1. 本示例提供了Python脚本快速搭建服务器，需要本地有Python环境，另外，您需要安装Flask框架，可以通过Python的包管理器pip来安装Flask，在终端输入以下命令：

    ```
    pip install flask
    ```

2. 修改video_server.py中的VIDEO_PATH，将其替换为想要播放的视频的实际路径。

3. 修改entry/src/main/ets/common/CommonConstants.ets中的VIDEO_SOURCE中的链接，按照提示替换为PC的IP地址。

4. 保证播放设备和搭建服务器的PC在同一局域网内，在server文件夹内使用终端运行脚本：

    ```
    python video_server.py
    ```

5. 脚本将启动一个Flask服务器，默认监听5000端口。

### 工程目录

```
├──entry/src/main/ets
│  ├──common
│  │  ├──utils         
│  │  │  └──CommonUtils.ets             // 公共方法类
│  │  └──CommonConstants.ets            // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets        
│  ├──model
│  │  ├──AVDataSource.ets               // 视频数据类
│  │  └──AVPlayereState.ets             // 视频状态类
│  ├──pages                  
│  │  └──Index.ets                      // 首页
│  └──view
│     └──VideoPlayView.ets              // 视频播放组件
└──entry/src/main/resources             // 应用静态资源目录
```

### 具体实现

1. 视频播放框架AVPlayer和滑块视图容器Swiper进行短视频滑动轮播切换。

2. 绘制组件XComponent的Surface类型动态渲染视频流。

3. 使用LazyForEach进行数据懒加载，设置cach


---
## SocialShareJump
> 本示例基于App Linking实现一个社交类型的应用，可以通过Share Kit分享文章详情的App Linking链接给好友（畅连好友），好友可以点击链接实现应用跳转，直达文章详情，提升用户体验。

源码: https://gitcode.com/HarmonyOS_Samples/SocialShareJump

# 基于App Linking实现社交分享跳转

### 介绍
本示例基于App Linking实现一个社交类型的应用，可以通过Share Kit分享文章详情的App Linking链接给好友（畅连好友），好友可以点击链接实现应用跳转，直达文章详情，提升用户体验。当应用未安装应用时，一键直达文章详情页或者应用市场（未安装该社交应用的情况下，方便好友直接安装）。

### 效果预览
![image](screenshots/devices/image.gif)

使用说明
1. 在运行项目前，需要完成App Linking的配置，以及对应用进行手动签名，具体可以参考[使用App Linking实现应用间跳转](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startup)。
2. 在完成App Linking的配置后，请前往[Detail.ets](entry/src/main/ets/pages/Detail.ets)文件，将share()方法中的content参数替换为真实可用的链接地址，同时将[module.json5](./entry/src/main/module.json5)文件中uris的host修改为可用的域名。
3. 启动应用，点击首页文章列表项，跳转到详情页。
4. 点击详情页右上角的分享按钮拉起分享面板，分享至畅连好友。
5. 在畅连消息列表中点击分享的消息，进行页面跳转。

### 工程目录

```
├──entry/src/main/ets                           // 代码区
│  ├──common
│  │  ├──LazyDataSource.ets                     // 懒加载数据源管理类
│  │  └──Logger.ets                             // 日志打印类   
│  ├──entryability
│  │  └──EntryAbility.ets                       // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                 // 数据备份恢复类
│  ├──model
│  │  └──Article.ets                            // 文章实体类
│  ├──pages
│  │  ├──Detail.ets                             // 文章详情页
│  │  └──Index.ets                              // 应用入口页
│  └──view
│     └──IArticleItem.ets                       // 文章列表项组件
└──service
   │──detail                                    // 文章Web详情页，用于部署到服务器
   └──index                                     // App Linking对应的Web页面
```

### 具体实现

* 通过Share Kit的systemShare模块实现分享功能。
* 应用首次启动时，通过


---
## SpatialStatistics
> 本示例介绍应用空间统计和文件系统空间统计接口的使用。

源码: https://gitcode.com/HarmonyOS_Samples/SpatialStatistics

# 实现系统和文件空间的统计与展示

### 介绍

本示例介绍应用空间统计和文件系统空间统计接口的使用，包括对内外卡的空间查询，对应用分类数据统计的查询，对应用数据的查询等。提供文件系统相关存储信息的功能，向应用程序提供获取文件系统总字节数、空闲字节数接口。

### 效果图预览

| 应用首页                                                 | 应用空间统计页                                             | 文件系统空间统计页                                            |
|------------------------------------------------------|-----------------------------------------------------|------------------------------------------------------|
| <img src='screenshots/device/home_cn.png' width=320> | <img src='screenshots/device/app_cn.png' width=320> | <img src='screenshots/device/file_cn.png' width=320> |

##### 使用说明

1. 主页面，点击“应用空间统计”按钮，进入应用空间统计页面。
2. 点击“应用空间统计”，展示应用空间数据。
3. 点击左上角“返回”按钮，返回主页面。
4. 主页面，点击“文件系统空间统计”按钮，进入文件系统空间统计页面。
5. 点击“文件系统空间统计”，展示文件系统相关存储数据。

## 工程目录

```
├──entry/src/main/ets                         // 代码区
│  ├──constants
│  │  └──Constants.ets                        // 公共常量
│  ├──entryability
│  │  └──EntryAbility.ets                     // 程序入口
│  ├──pages
│  │  ├──AppSpatialPage.ets                   // 应用空间统计页面
│  │  ├──FileSpacePage.ets                    // 文件系统空间统计页面
│  │  └──Home.ets                             // 主页面
│  ├──utils
│  │  └──Logger.ets                           // 日志文件
│  ├──view
│  │  └──SpaceInfo.ets                        // 卡片子组件
│  └──viewmodel
│     └──CommonViewModel.ets                  // 公共方法
└──entry/src/main/resources                   // 应用资源目录
```

### 相关权限

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持


---
## StageModelContext
源码: https://gitcode.com/HarmonyOS_Samples/StageModelContext

# 实现获取应用上下文功能

### 介绍

本示例详细展示了如何在不同类型的HarmonyOS应用包（HAP、HAR、HSP）环境中获取关键的应用上下文实例，具体包括UIAbilityContext、ApplicationContext和WindowStage实例。通过这些实例，开发者可以在各种应用模块中实现对用户界面、全局应用状态以及窗口管理的精细控制。

### 效果预览

| 获取UIAbilityContext                        | 获取ApplicationContext                      | 获取WindowStage                            |
|-------------------------------------------|-------------------------------------------|------------------------------------------|
| ![pic1.png](screenshots/devices/pic1.png) | ![pic2.png](screenshots/devices/pic2.png) | ![pic3png](screenshots/devices/pic3.png) |

### 目录结构

```
├──entry
│  ├──src/main/ets/
│  │  ├──common
│  │  │  └──Logger.ets                       // 日志打印工具类
│  │  ├──entryability
│  │  │  └──EntryAbility.ets                 // 程序入口类
│  │  ├──entrybackupability
│  │  │  └──EntryBackupAbility.ets           // 数据备份恢复类
│  │  ├──pages
│  │  │  ├──GetApplicationContextDemo.ets    // 获取ApplicationContext代码示例
│  │  │  ├──GetUIAbilityContextDemo.ets      // 获取UIAbilityContext代码示例
│  │  │  ├──GetWindowStageDemo.ets           // 获取WindowStage代码示例
│  │  │  └──Index.ets                        // 应用入口页
│  │  └──workers
│  │     └──MyWorker.ets                     // Worker子线程类
│  └──src/main/resources                     // 应用静态资源目录
├──har                                       // har模块
│  ├──Index.ets                              // 入口文件，对外暴露模块方法
│  ├──src/main/ets/components/mainpage                                
│  │  └──MainPgge.ets             


---
## StateStore
源码: https://gitcode.com/HarmonyOS_Samples/StateStore

# 基于StateStore实现全局状态管理最佳实践

## 简介

本示例展示了使用StateStore状态管理库实现全局状态管理，覆盖场景：

- UI与状态数据解耦
- 子线程进行状态对象更新
- 状态更新日志埋点

解决开发者在使用ArkUI状态管理时UI组件和数据操作逻辑高度耦合的问题

## 效果预览

![img.png](./screenshots/effect.png)

## 工程目录

```text
├──entry/src/main/ets                       // 代码区
├──components                               // UI组件
│   ├──AddSheetBuilder.ets                  // 添加todo弹窗
│   ├──AsyncProgress.ets                    // 同步进度条
│   ├──IconContainer.ets                    // Icon容器
│   └──TodoItem.ets                         // todoItem组件
├──entryability
│   └──EntryAbility.ets
├──middleware                               // 中间件
│   └──LoggerMiddleware.ets                 // 日志监控中间件
├──model                                    // 数据模型
│   └──TodoListModel.ets                    // todo列表数据
├──pages                                    // 页面
│   └──Index.ets                            // 主页
├──store                                    // store仓库
│   ├──TodoListActions.ets                  // action事件管理对象
│   ├──TodoListReducer.ets                  // reducer逻辑处理函数
│   └──TodoListStore.ets                    // todoListStore定义
└──utils                                    // 工具函数
    ├──RdbUtil.ets                          // rdb工具
    ├──Sleep.ets                            // sleep函数
    └──TaskpoolUtil.ets                     // 子线程工具                                  
```

# StateStore简介

StateStore作为ArkUI状态与UI解耦的解决方案，支持全局维护状态，优雅地解决状态共享的问题。

StateStore库提供共享模块StateStore单例，支持根据唯一标识创建store存储


---
## SuperFastTrans
源码: https://gitcode.com/HarmonyOS_Samples/SuperFastTrans

# 基于SFFT的大文件高速并发传输

## 项目简介

本项目是使用[super_fast_file_trans](https://gitcode.com/openharmony-sig/super_fast_file_trans)的三方库源码与Sample示例代码，Sample实现的是一个包含文件下载和文件上传的页面。
页面中展示的功能包括文件的下载/上传、暂停、继续、删除等。

## 下载功能预览

![](./screenshots/sfft_download.png)

## 上传功能预览

![](./screenshots/sfft_upload.png)

## 使用说明
1. 本Sample无法直接运行，需要在src/main/ets/common/ConstantsConfig.ets下配置下载地址、上传地址、上传文件本地地址。
2. 由于安全限制证书没有直接在Sample提供，当需要在双向校验下发送HTTPS请求时，请根据需要src/main/resources/rawfile/下进行补充和调整，会话安全相关接口详情见[SFFT库说明文档](https://gitcode.com/openharmony-sig/super_fast_file_trans/blob/master/library/README.md)。

## 工程目录

```
├── entry               # Sample工程项目模块
│      └── src
│           └── main
│                 ├── ets
│                 │  ├── common
│                 │  │  └── ConstantsConfig.ets     # 公共常量类（需在此配置Sample所需的URL）
│                 │  ├── components
│                 │  │  ├── CustomMenuItem.ets      # Navigation菜单项组件
│                 │  │  ├── DownloadItem.ets        # 下载项组件
│                 │  │  └── UploadItem.ets          # 上传项组件
│                 │  ├── entryability
│                 │  │  └── EntryAbility.ets
│                 │  ├── entrybackupability
│                 │  │  └── EntryBackupAbility.ets
│                 │  ├── model
│                 │  │  └── FileItem.ets            # 文件项
│                 │  ├── pages
│                 │  │  └── Index.ets               # 首页面
│                 │  ├── util
│                 │  │  └── MemoryTool.ets          # 内存工具类
│                 │  └─


---
## SwipePlayer
源码: https://gitcode.com/HarmonyOS_Samples/SwipePlayer

# 实现短视频流畅点播
## 简介
本场景主要聚焦短视频流畅点播切换场景，提供了短视频上下滑动、快速起播、动态添加数据源、自定义跟随视频滑动的组件、自定义滑动组件切换、全屏和弹框等能力，同时通过自定义能力的开放，满足应用不同短视频滑动场景的业务诉求，开发者可以基于SwipePlayer
库快速实现短视频流畅滑动的场景开发体验，可以更加聚焦实际场景业务的开发。

## 预览图效果

| 竖屏页                                               | 评论页                                               | 横屏页                                            |
|---------------------------------------------------|---------------------------------------------------|------------------------------------------------|
| <img src="./screenshots/display.png" width="320"> | <img src="./screenshots/comment.png" width="320"> | <img src="./screenshots/full.png" width="320"> | 

## 使用说明
SwipePlayer是一个基于HarmonyOS ArkUI实现的短视频滑动播放示例工程，主要演示以下能力：

- 支持网络视频（http/https）上下滑动及快速起播
- 支持动态添加/刷新播放源数据
- 支持自定义跟随视频滑动的组件
- 支持自定义滑动切换组件
- 支持自定义弹框（可自定义动画和弹出方向，提供默认的动画实现）
- 支持全屏/退出全屏播放，支持定义全屏播放界面组件
- 支持进度条（通过组件形式提供）

该示例适用于以下业务场景：

- 短视频信息流
- 上下滑切换的视频详情页
- 沉浸式视频浏览
- 类“刷视频”交互实现

## 工程主要模块结构
```typescript
├──entry/src/main/ets/
│  │──constants                        // 常量
│  │  ├──AdvertConstants.ets           // 广告页资源常量
│  │  ├──CommonConstant.ets            // 资源常量
│  │  └──TabConstants.ets              // 标签栏资源常量
│  ├──entryability
│  │  └──EntryAbility.ets              // Ability的生命周期回调内容
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets        // EntryBackupAbility的生命周期回调内容
│  ├──model
│  │  ├──CommonModel.ets               // 页面公共方法
│  │  └──CommonUtils.ets               // 组件公共方法
│  ├──pages
│  │  └──Index.ets   


---
## SwiperPerformance
源码: https://gitcode.com/HarmonyOS_Samples/SwiperPerformance

# 实现Swiper组件加载慢丢帧优化

### 介绍

本示例通过采用懒加载和预加载技术，优化了Swiper组件在多图片场景下的加载性能，实现了流畅的滑动体验。这种方式不仅减少了初始加载时间，还确保了用户在浏览时的顺畅与高效。

### 效果预览

| 答题页                                           | 图片页                                          |
|-----------------------------------------------|----------------------------------------------|
| ![Question.png](screenshots/devices/pic1.png) | ![Picture.png](screenshots/devices/pic2.png) |

### 目录结构

```
├──entry/src/main/ets/
│  ├──common
│  │  ├──ImageUtils.ets                   // 图片处理工具类
│  │  ├──MyDataSource.ets                 // 懒加载数据源工具类
│  │  └──Logger.ets                       // 日志打印工具类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets           // 数据备份恢复类
│  ├──model
│  │  ├──Question.ets                     // 问题实体类
│  │  └──SwiperData.ets                   // 图片实体类
│  └──pages
│     ├──Index.ets                        // 应用入口页
│     ├──LazyForEachSwiper.ets            // Swiper懒加载（答题）页面
│     └──PreloadDataSwiper.ets            // Swiper数据预加载（图片）页面
└──entry/src/main/resources               // 应用静态资源目录

```

### 使用说明

1. 点击首页按钮“使用LazyForEach加载Swiper”，进入问答页面，页面左右滑动流畅。
2. 点击首页按钮“提前加载数据加载Swiper”，进入图片页面，页面左右滑动流畅。

### 实现说明

1. Swiper懒加载使用LazyForEach实现。
2. Swiper数据预加载在onAnimationStart方法中提前加载数据。

### 相关权限

* ohos.permission.INTERNET：允许使用Internet网络。

### 依赖

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco 


---
## SystemEnvVarSubscriber
源码: https://gitcode.com/HarmonyOS_Samples/SystemEnvVarSubscriber

# 实现订阅系统环境变量变化能力

### 介绍

本示例详细介绍了如何获取和订阅系统环境变量的变化，包括系统语言、深浅色模式以及屏幕像素密度等关键设置。通过监听这些系统属性的变动，应用可以即时响应并调整自身的显示和行为，以提升用户体验。

### 效果预览

![preview.gif](screenshots/devices/preview.png)

使用说明
1. 进入系统设置->系统->语言和地区，切换系统语言，切回到应用，应用列表项“系统语言”的值发生改变。
2. 进入系统设置->显示和亮度->字体大小和界面缩放，分别拖动字体大小字体粗细进度条，然后切回到应用，应用列表项“字体大小缩放比例”和“字体粗细缩放比例”发生改变。
3. 旋转设备屏幕，应用随设备旋转，应用列表项“屏幕方向”的值发生改变。
4. 下拉系统菜单栏，开启深色模式，应用列表项“深浅色模式”的值发生改变。

### 目录结构

```
├──entry/src/main/ets/
│  ├──common
│  │  └──Logger.ets                       // 日志打印工具类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets           // 数据备份恢复类
│  └──pages
│     └──Index.ets                        // 应用入口页
└──entry/src/main/resources               // 应用静态资源目录
```

### 具体实现

* 在module.json5中声明添加orientation属性，取值为auto_rotation，使应用可以随屏幕方向旋转。
* 在app.json5中添加configuration标签，使应用字体大小可以跟随系统变更，具体实现可以参考：[configuration标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file#configuration%E6%A0%87%E7%AD%BE)。
* 在EntryAbility.ets添加[onConfigurationUpdate()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability#abilityonconfigurationupdate)回调方法，用于订阅深浅色模式、系统语言、文本大小缩放等系统环境变量的变化。
* 在Index.ets使用[display.on('change')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displayonaddremovechange)方法，订阅横竖屏切换变化。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 


---
## TextExpand
源码: https://gitcode.com/HarmonyOS_Samples/TextExpand

## 实现富文本收起展开功能

### 介绍

本示例展示列表中的博文、评论等应用场景在展示文本内容，超过多行时，往往需要提供“展开”“折叠”的功能。

### 效果预览

| 首页                                  | 富文本显示展开按钮                                    | 富文本显示收起按钮                                  | 纯文本显示收起按钮                                  | 纯文本显示展开按钮                                    |
|-------------------------------------|----------------------------------------------|--------------------------------------------|--------------------------------------------|----------------------------------------------|
| ![](./screenshots/devices/home.png) | ![](./screenshots/devices/rich_collapse.png) | ![](./screenshots/devices/rich_expand.png) | ![](./screenshots/devices/text_expand.png) | ![](./screenshots/devices/text_collapse.png) |

使用说明：
1. 打开应用，首页点击富文本折叠，跳转到富文本展示页面，点击展开按钮列表展开，点击收起按钮，列表收起。
2. 打开应用，首页点击纯文本折叠，跳转到纯文本展示页面，点击展开按钮列表展开，点击收起按钮，列表收起。

### 工程目录

```
├──ets
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages
│  │  ├──index .ets              // 主页
│  │  ├──RichTextExpand .ets     // 富文本场景
│  │  ├──TextExpand.ets          // 纯文本场景
│  ├──utils
│  │  ├──Models .ets             // 数据模型
│  │  ├──TextUtils .ets          // 文本处理工具
│  └──view
│     ├──ItemPart.ets            // 纯文本场景List数据展示组件
│     ├──RichItemPart.ets        // 富文本场景List数据展示组件
│     ├──RichTextExpandView.ets  // 封装的富文本展开折叠组件
│     ├──TextExpandView.ets      // 封装的纯文本展开折叠组件
└──resources
```

### 具体实现

1. 使用[MeasureText](https://devel


---
## TurboTransJSON
> 通过turbo_trans库，实现高效JSON等数据序列化

源码: https://gitcode.com/HarmonyOS_Samples/TurboTransJSON

# 基于TurboTransJSON实现高性能JSON解析

## 简介
本示例展示了使用TurboTrans实现高性能JSON解析操作，覆盖场景包括：
- 结合Sendable跨线程数据传递场景
- 网络数据交互场景
- 结合跨线程和网络数据交互场景
- JSON大文件解析
- JsonNode懒加载
## 效果预览
<img src='./screenshots/device/image_zh.png' width='320'>

## 使用说明
> **注意：项目包含LFS大文件，请勿直接下载ZIP！**

正确获取完整项目的方式：
1. 安装Git LFS：`git lfs install`
2. 克隆仓库（自动拉取LFS文件）：`git clone https://gitcode.com/harmonyos_samples/TurboTransJSON.git`

## 工程目录

```
entry/src/main/ets                            // 代码区
├── common                                  
│   ├── components                            // 公共组件
│   │   ├── CardContainer.ets                 // 功能模块卡片-案例描述，示例代码，执行结果
│   │   ├── CellComponent.ets                 // 单个功能模块菜单
│   │   ├── CellGroupComponent.ets            // 功能模块卡片
│   │   ├── LayoutContainer.ets               // 页面根布局组件
│   │   ├── NavBar.ets                        // 页面标题
│   │   └── interface
│   │       └── MainPageListItem.ets          // 单个菜单的数据结构定义
│   ├── constants
│   │   ├── CodeExample.ets                   // 示例代码
│   │   ├── MenuConstants.ets                 // 首页菜单目录
│   │   ├── NavigationConstants.ets           // 页面NavgationId常量
│   │   ├── PageConstant.ets                  // 页面公共样式常量定义
│   │   └── PageRouteConstants.ets            // router name常量定义
│   ├── styles
│   │   ├── BaseContentStyles.ets             // 页面基础样式
│   │   └── ButtonStyles.ets                  // 按钮公共样式
│   └── index.ets                             // common入口文件
├── entryability
│   └── EntryAbility.ets                 


---
## UniversalKeystoreCollection
> 本示例主要通过使用@ohos.security.huks (通用密钥库系统)模块，完成加解密、签名验签、密钥协商等基础的通用密钥库操作。

源码: https://gitcode.com/HarmonyOS_Samples/UniversalKeystoreCollection

# 基于@ohos.security.huks模块的密钥库功能实现

### 介绍

本示例主要通过使用@ohos.security.huks (通用密钥库系统)模块，完成加解密、签名验签、密钥协商等基础的通用密钥库操作。

### 效果展示
![](screenshots/Devices/UniversalKeystoreCollection.gif)

### 使用说明

1. 在主界面点击加解密、签名验签、密钥协商可以跳转至对应功能页面。
2. 点击加解密按钮后，可以选择加密算法，点击跳转后，可以根据不同的加解密算法进行加解密，可以在待加密文本处输入内容，并点击加密按钮进行加密并弹窗提
醒，并将加密内容显示在已加密文本处，点击解密会进行解密，弹窗提醒并将结果显示在已解密文本处。
3. 点击签名验签按钮后，可以根据不同算法进行签名验签，点击签名按钮会进行签名并弹窗提醒签名结果，点击验签会弹窗提醒用户，验签通过，在未完成签名，
进行验签，会提示签名为空，无法通过验签。
4. 点击密钥协商按钮，会根据不同算法进行密钥协商，分别点击生成非对称密钥A、B按钮生成密钥，在A、B密钥均存在时，点击密钥协商按钮，会提示协商通过，
否则会弹窗提示，密钥缺失，协商失败。

### 工程目录
```
├──entry/src/main/ets                             // 代码区
│  ├──common
│  │  ├──constants                                
│  │  │  ├──CommonConstants.ets                   // 常量类
│  │  │  └──HuksPropertiesConstants.ets           // 加解密常量类
│  │  └──utils
│  │     ├──EncodingUtils.ets                     // 编码工具类
│  │     ├──EncryptAndDecryptUtils.ets            // 加解密工具类
│  │     ├──KeyNegotiationUtils.ets               // 密钥协商工具类
│  │     ├──Logger.ets                            // 日志打印工具类
│  │     └──SignatureVerificationUtils.ets        // 签名验签工具类
│  ├──entryability
│  │  └──EntryAbility.ets                         // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages
│  │  ├──EncryptionDetailPage.ets                 // 加解密详情页
│  │  ├──EncryptionPage.ets                       // 加解密方案选择页
│  │  ├──Index.ets                                // 首页
│  │  ├──KeyNegotiationDetailPage.ets             // 密钥协商详情页
│  │  ├─


---
## UseAVTranscoderVideo
源码: https://gitcode.com/HarmonyOS_Samples/UseAVTranscoderVideo

## 使用AVTranscoder实现视频转码

### 介绍

本示例将以“开始转码-暂停转码-恢复转码-转码完成”的一次流程向开发者讲解AVTranscoder视频转码相关功能。

### 效果预览

| 首页                                                      | 视频转码页                                                            | 转码完成页                                                           |
|---------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------|
| <img src="./screenshots/devices/home.png" width="300"/> | <img src="./screenshots/devices/transcodering.png" width="300"/> | <img src="./screenshots/devices/transcodered.png" width="300"/> |

使用说明：
1. 打开应用，首页支持选择视频转码所需的参数配置，选择完成后，点击开始转码按钮，跳转到视频转码页面。
2. 视频转码页面可以看到视频转码的进度，点击暂停按钮，暂停转码，点击恢复按钮，恢复转码；点击取消按钮，弹窗提醒是否取消转码；转码完成后，点击完成按钮，跳转到转码完成页面。
3. 转码完成页面可以观看转码完成后的视频，点击首页按钮，返回到首页。

### 工程目录


```
├──ets
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──pages
│  │  ├──index .ets                    // 主页
│  │  ├──TranscoderFinishPage.ets      // 视频转码完成页面
│  │  └──VideoTranscoderPage.ets       // 视频转码进度页面
│  └──utils
│     └──AVTranscoderManager.ets       // 视频转码管理类
└──resources
   └──rawfile
      └──video_sample.mp4              // 转码视频
```

### 具体实现

1. 使用[AVTranscoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avtranscoder)
视频转码管理类，先通过createAVTranscoder()
构建一个AVTranscoder实例，然后注册转码监听事件，最后调用相关接口实现“开始转码-暂停转码-恢复转码-转码完成”的流程。
2. 通过[AVTranscoder](https://developer.huawe


---
## UseSendable
> 本示例介绍几种Sendable的使用案例：生产者消费者模式多线程协同工作（日志、打点信息处理）、Sendable共享对象实现跨线程通信&UI状态刷新。

源码: https://gitcode.com/HarmonyOS_Samples/UseSendable

# 基于Sendable实现多线程功能

### 介绍

本示例介绍Sendable的多种使用案例。Sendable的线程间共享：以文件下载为例，点击“启动”即转为“暂停”，进度条递增至100%则变为“完成”。生产者消费者模式多线程协同工作：支持单/双消费者线程消费，十子线程生产日志，长时生产及停止，以及消费者线程停止。

### 效果图预览

![](screenshots/device/UseSendable.gif)

##### 使用说明

1. 点击“Sendable的线程间共享”按钮，进入“文件下载列表”页面；
2. 点击“启动”按钮，“启动”按钮变成“暂停”按钮，页面进度条每次增加20%；
3. 当进度条到达“100%”，“启动”按钮变成“完成”按钮；
4. 点击“暂停”按钮，“暂停”按钮变成“继续”按钮，页面进度条停止增加；
5. “继续”按钮变成“暂停”按钮，页面进度条每次增加20%；
6. 返回上一页面，点击“生产者消费者模式”按钮，进入“生产者消费者模式”页面；
7. 点击“一个消费者线程消费”按钮，点击“主线程生产一条日志”按钮，打印出一条带有“consumerOne”日志；
8. 点击“二个消费者线程消费”按钮，多次点击“主线程生产一条日志”按钮，打印多条带有“consumerOne”和“consumerTwo”日志；
9. 点击“十个子线程生产十条日志”按钮，打印出10条日志；
10. 点击“长时生产日志”按钮，会一直打印日志；
11. 点击“停止长时生产日志”按钮，日志停止打印；
12. 点击“停止消费者线程”按钮；
13. 退出应用。

## 工程目录

```
├──entry/src/main/ets                         // 代码区
│  ├──constants
│  │  └──Constants.ets                        // 公共常量
│  ├──downLoadFilePage
│  │  ├──model                                // 实体类   
│  │  ├──DownLoadComponent.ets                // 下载子组件
│  │  ├──DownLoadFilePage.ets                 // 文件下载页面
│  │  └──DownLoadVideo.ets                    // 进度条
│  ├──entryability
│  │  └──EntryAbility.ets                     // 程序入口              
│  ├──pages
│  │  └──Index.ets                            // 首页     
│  ├──producerConsumer
│  │  ├──model                                // 实体类   
│  │  ├──tasks                                // Task
│  │  └──ProducerConsumerPage.ets             // 生产者消费者模式（日志打印）页面
│  └──utils
│     └──Logger.ets                           // 日志类
└──en


---
## UseTaskPool
源码: https://gitcode.com/HarmonyOS_Samples/UseTaskPool

# 基于TaskPool实现多线程任务

### 介绍

本示例基于TaskPool的能力与特性，实现不同场景的多线程任务的功能，例如优先级任务，周期任务，延时任务以及任务组等场景。基于本示例，可以快速学习TaskPool的使用方法和能力，帮助应用开发计算任务大，并行任务多的功能场景。

### 效果预览

| 应用主界面                                                            |
|------------------------------------------------------------------|
| ![UseTaskPool_show.png](screenshots/device/UseTaskPool_show.png) | 

### 使用说明

点击进入页面后，页面有八个按钮，分别对应不同的TaskPool能力的使用示例，点击跳转到不同类型任务的使用示例页面，各页面内有相应的功能按钮；线程执行的关键信息会在各示例页面的第一个文本框内打印出来；TaskPool内部的线程以及任务信息会打印在第二个文本框内。
- 优先级任务示例：首先点击‘创建任务’按钮，会创建高、中、低三种优先级任务各100个；然后点击‘执行任务’按钮，TaskPool会执行这些任务，并打印任务执行的线程、时间等信息，可以观察TaskPool对优先级任务的调度。运行过程中点击‘取消任务’按钮可以取消这些任务。
- 周期任务示例：首先点击‘创建任务’按钮，会创建1个周期任务；然后点击‘执行任务’按钮，TaskPool会执行该任务，并打印任务执行的线程、时间等信息，可以观察周期任务周期执行的情况。运行过程中点击‘取消任务’按钮可以取消该任务。
- 延时任务示例：首先点击‘创建任务’按钮，会创建1个延时任务；然后点击‘执行任务’按钮，TaskPool会在延时一定时间后执行该任务，并打印任务提交和执行的线程、时间等信息，可以观察延时任务的执行情况。运行过程中点击‘取消任务’按钮可以取消该任务。
- 长任务示例：首先点击‘创建任务’按钮，会创建1个长任务；然后点击‘执行任务’按钮，TaskPool会执行该任务，并打印任务执行和结束的线程、时间等信息，可以观察长任务的执行情况。运行过程中点击‘取消任务’按钮可以取消该任务。
- 依赖任务示例：首先点击‘创建任务’按钮，会创建2个有依赖关系的任务；然后点击‘执行任务’按钮，TaskPool会执行这两个任务，并打印任务提交和执行的线程、时间等信息，可以观察依赖任务的执行情况。运行过程中点击‘取消任务’按钮可以取消任务。
- TaskGroup示例：首先点击‘创建任务’按钮，会创建1个包含10个任务的任务组；然后点击‘执行任务’按钮，TaskPool会执行该任务组，并打印任务执行的线程、时间等信息，可以观察任务组的执行情况。运行过程中点击‘取消任务’按钮可以取消该任务组。
- SequenceRunner示例：首先点击‘创建任务’按钮，会创建10个串行执行的任务；然后点击‘执行任务’按钮，TaskPool会执行这些任务，并打印任务执行的线程、时间等信息，可以观察串行任务的执行情况。运行过程中点击‘取消任务’按钮可以取消这些任务。
- 线程交互示例：该页面的三个按钮分别展示了TaskPool与宿主线程，Worker与宿主线程，TaskPool与Worker之间的通信，点击后会打印发送消息和接收消息的线程、时间等信息，可以观察线程间通信的情况。

### 工程目录


---
## UserAuth
> 本示例主要使用人脸和指纹认证用户身份、使用密码保险箱实现密码自动填充以及涉及口令输入的应用界面防截屏或录屏等功能的实现方式。

源码: https://gitcode.com/HarmonyOS_Samples/UserAuth

# 实现用户认证登录功能

## 介绍

本示例主要使用人脸和指纹认证用户身份、使用密码保险箱实现密码自动填充以及涉及口令输入的应用界面防截屏或录屏等功能的实现方式。


## 效果预览
| **主页**                                                  |
|---------------------------------------------------------|
| <img src="screenshots/UserAuthDemo.png"  width="300px"> |

## 工程目录
```
├──entry/src/main/ets 
│  ├──common/constant    
│  │  └──CommonConstants.ets                   // 公共常量类 
│  ├──common/utils                             
│  │  ├──Logger.ets                            // 日志工具类 
│  │  └──PromptUtil.ets                        // 消息工具类 
│  ├──entryability
│  │  └──EntryAbility.ets                      // 程序入口类 
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                // 程序出口类
│  ├──pages
│  │  ├──LoginPage.ets                         // 登录页面  
│  │  └──MainPage.ets                          // 首页页面
│  ├──model
│  │  ├──HuksModel.ets                         // 加解密模型文件  
│  │  ├──ItemDataModel.ets                     // 数据模型文件
│  │  ├──PreferenceModel.ets                   // 数据储存模型文件  
│  │  └──userAuthModel.ets                     // 用户认证模型文件
│  ├──view
│  │  ├──Home.ets                              // 首页页面
│  │  ├──RegisterPage.ets                      // 注册页面  
│  │  └──Setting.ets                           // 设置页面
│  └──viewmodel
│     └──MainViewModel.ets                     // 图片模型
└──entry/src/main/resources                    // 应用资源目录
```

## 使用说明

1. 初次登录界面没有人脸识别和指纹识别登录；

2. 注册时选择人脸识别和指纹识别按钮，再次返回登录界面就会提供人脸识别和指纹识别登录(模拟器不支持)；

3. 登录界面防截屏功能(模拟器


---
## UtilizeHWCEfficiently
源码: https://gitcode.com/HarmonyOS_Samples/UtilizeHWCEfficiently

# 高效利用HWC的低功耗设计

### 介绍
Hardware Composer（下文简称HWC）专用硬件辅助系统相对于通用计算单元，在图层叠加场景具有更高的处理效率和更低的能耗，但是需要满足一定条件才能充分发挥其硬件能力。本示例列举了视频或Web页与UI图层叠加的三种典型场景，展示通过去除模糊效果或调整自渲染图层透明度等方式调整视效设计，扩大HWC的生效范围，降低应用场景功耗。

### 效果预览
| Video组件叠加模糊控件                                 | Video组件上方控件无模糊                             | Web组件叠加模糊控件                                 | Web组件上方控件无模糊                             | 视频图层设置透明度                                       | 视频图层不透明                                    |
|-----------------------------------------------|--------------------------------------------|---------------------------------------------|------------------------------------------|-------------------------------------------------|--------------------------------------------|
| ![](./screenshots/device/video_with_blur.gif) | ![](./screenshots/device/normal_video.gif) | ![](./screenshots/device/web_with_blur.png) | ![](./screenshots/device/normal_web.png) | ![](./screenshots/device/transparent_video.gif) | ![](./screenshots/device/opaque_video.gif) |

### 使用说明
1. 点击Video组件叠加模糊控件按钮进入场景页面，视频自动播放。
2. 点击Video组件上方控件无模糊按钮进入场景页面，视频自动播放。
3. 点击Web组件叠加模糊控件按钮进入场景页面，上下滑动Web页面。
4. 点击Web组件上方控件无模糊按钮进入场景页面，上下滑动Web页面。
5. 点击视频图层设置透明度按钮进入场景页面，视频自动播放。
6. 点击视频图层不透明按钮进入场景页面，视频自动播放。

### 工程目录
```
entry/src/main/ets
├── entryability
│   ├── EntryAbility.ets                // Ability的生命周期回调内容
│   └── EntryBackupAbility.ets          // 应用数据备份恢复类
├── pages
│   ├── Index.ets                       // 视图层-主页面
│   ├── VideoWithBlur.


---
## VideoCast
源码: https://gitcode.com/HarmonyOS_Samples/VideoCast

# 实现视频投播功能

### 介绍

本实例基于播控中心和系统投播实现完整的视频投播功能，包含投播和播控基础控制：设备切换、集数切换、音量增减、进度切换。

### 效果图预览
| 视频选择                                          | 本端播放                                          | 遥控器控制                                         |
|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| <img src='./screenshots/page1.png' width=320> | <img src='./screenshots/page2.png' width=320> | <img src='./screenshots/page3.png' width=320> |
**使用说明**

1. 本端设备播放视频，进度/音量/集数控制。
2. 播控中心控制本端设备，进度/音量/集数。
3. 建立投播，本端控制远端设备进度/音量/集数。

### 工程结构&模块类型

```
├───entry/src/main/ets
│   ├───common                              
│   │   ├───contants                        
│   │   │   └───CommonConstants.ets         // 常量
│   │   └───utils                           
│   │       ├───BackgroundTaskManager.ets   // 后台任务工具类
│   │       ├───ImageUtil.ets               // 图片处理工具类
│   │       └───TimeConvert.ets             // 时间转换工具类
│   ├───controller                          
│   │   ├───VideoCastController.ets         // 投播控制器
│   │   ├───VideoPlayerController.ets       // 本地播放控制器
│   │   └───VideoSessionController.ets      // 播控中心控制器
│   ├───entryability                        
│   │   └───EntryAbility.ets                // Ability的生命周期回调内容
│   ├───entrybackupability                  
│   │   └───EntryBackupAbility.ets          // Ability的生命周期回调内容
│   ├───model                               
│   │   └───VideoData.et


---
## VideoProcessBaseWeb
源码: https://gitcode.com/HarmonyOS_Samples/VideoProcessBaseWeb

# 基于Web组件实现视频处理功能

### 介绍

本示例基于Web长按处理onContextMenuShow()方法与Web组件下载能力等，为用户在视频观看场景中提供了全屏播放、复制视频链接地址、快捷打开浏览器观看以及视频下载的综合功能，丰富了用户交互体验，增强了内容的可获取性和分享便捷性

### 效果预览

手机运行效果图如下：

![image](screenshots/device/phone.png)

**注意**：本示例中的视频地址仅供演示，且该视频地址有下载次数限制，开发者请按需使用自有视频地址替代。

### 工程目录结构

```
├──entry/src/main/ets                                   // 代码区
│  ├──common
│  |  └──Constants.ets                                  // 常量
│  ├──entryability
│  |  └──EntryAbility.ets
│  ├──entrybackupability
│  |  └──EntryBackupAbility.ets
│  ├──pages
│  |  └──Index.ets                                      // 入口界面
│  ├──utils
│  |  ├──CustomFunction.ets                             // 功能函数封装
│  |  └──WebDownloadManager.ets                         // Web下载功能封装
│  └──view
│     ├──CustomPopupMenu.ets                            // 自定义弹出菜单
│     └──DownloadControlView.ets                        // 下载过程UI视图
└──entry/src/main/resources                             // 应用资源目录
```

### 使用说明
安装打开应用后，点击全屏按钮可以横屏观看视频，长按视频播放区域可出现操作菜单，可按需体验以下功能：
1. 复制视频地址：选中该项后可将视频的地址复制到剪贴板，方便用户到其他应用分享查看；
2. 在浏览器打开视频：选中该项后可在浏览器中查看视频；
3. 下载视频：点击该项后，会弹出安全控件要求用户选择保存位置，选择后可自动开始下载并展示下载进度，下载完成后可以到选中的目录查看。

### 具体实现
* 全屏播放视频需要监听Web页面进入全屏的onFullScreenEnter()事件，在进入全屏后，将屏幕方向通过setPreferredOrientation()设置为横屏显示，在退出全屏的onFullScreenExit()回调中，将屏幕方向调转回竖屏显示，需要兼容返回手势退出全屏。
* 长按复制视频链接依靠Web组件的onContextMenuShow()方法，在该方法中可通过事件回调event参数，取得长按项目的相关属性，对于视频而言，其中的event.param.getSourceUrl()方法可获取到视频的链接地址，获取成功后通过pasteboard.getSystemPasteboard().setData()设置到剪贴板中。
* 浏览


---
## VideoProcessing
源码: https://gitcode.com/HarmonyOS_Samples/VideoProcessing

# 使用VideoProcessing对视频处理

### 介绍

本场景解决方案主要面向视频编辑相关开发人员，指导开发者使用VideoProcessing对视频进行缩放增强，动态元数据生成，色彩空间转换的操作。

### 效果预览

<img src='screenshots/device/videoprocessing.png' width='320' />

### 使用说明

1. 点击选择视频，选择需要处理的视频。
2. 点击视频缩放，弹出视频缩放增强等级弹窗，选择对应增强等级对视频进行增强。
3. 点击元数据生成，弹出元数据生成弹窗，选择元数据格式，生成相应元数据信息的视频。
4. 点击色彩空间转换，弹出色彩空间转换弹窗，根据色彩空间格式，生成相应色彩空间的视频。
5. 点击播放视频按钮，播放视频，不处理。
6. 如果视频不支持此处理，则点击处理时，提示“该视频不支持当前操作”。

### 工程目录
````
├──entry/src/main/ets/
│  ├──common
│  │  ├──entryability
│  │  │  └──CommonConstants.ets        // 公共常量类
│  │  └──utils
│  │     ├──DateTimeUtil.ets           // 日期工具类
│  │     ├──Logger.ets                 // 日志工具类
│  │     └──WindowUtil.ets             // 窗口设置工具类
│  ├──entryability
│  │  └──EntryAbility.ets              // 程序入口类
│  ├──page                  
│  │  └──VideoPage.ets                 // 视频处理页
│  └──view 
│     └──MultiStatusButton.ets         // 自定义状态按钮
├──entry/src/main/cpp/
│  ├──CMakeLists.txt                   // 构建脚本
│  ├──capbilities
│  │  ├──AudioDecoder.cpp              // 音频解码实现类  
│  │  ├──Demuxer.cpp                   // 解封装实现类
│  │  ├──VideoDecoder.cpp              // 视频解码实现类
│  │  └──include
│  │     ├──AudioDecoder.h             // 音频解码头文件
│  │     ├──Demuxer.h                  // 解封装头文件
│  │     └──VideoDecoder.h             // 视频解码头文件
│  ├──common                  
│  │  ├──SampleCallback.cpp            // 回调实现类  
│  │  ├──SampleCallback.h              // 回调头文件
│  │  ├──SampleInfo.h                  // 数据实体类
│  │  └──dfx
│  │     ├──err


---
## VideoThumbnail
源码: https://gitcode.com/HarmonyOS_Samples/VideoThumbnail

# 基于系统能力获取视频缩略图

### 项目简介

本示例展示了通过系统能力获取视频缩略图的两种方法；第一种是获取视频的默认缩略图封面，主要通过getThumbnail()接口实现；第二种是获取指定视频时间的缩略图，主要通过AVImageGenerator类实现；参考本项目可快速开发需要获取视频缩略图的场景，例如生成视频的封面，在视频浏览、分享等场景帮助用户快速浏览和选择想要的内容。

### 效果预览：

![image](screenshots/Main.png)

### 使用说明：

1. 点击第一个按钮，会拉起图库picker，选择一个视频后会返回应用页面展示该视频的默认缩略图封面。

2. 点击第二个按钮，会拉起图库picker，选择一个视频后会返回应用页面展示该视频的首帧作为缩略图，此时拉动图片下方的进度条可选择指定时间的缩略图。


### 工程目录

```
├──entry/src/main/ets
│  ├──common
│  │  └──utils 
│  │     ├──PhotoUtils.ets              // 视频图片操作类         
│  │     └──TimeUtils.ets               // 视频时间工具类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets        
│  ├──model
│  │  └──VideoSizeData.ets              // 视频数据类
│  └──pages                  
│     └──Index.ets                      // 首页
└──entry/src/main/resource              // 应用静态资源目录
```

### 相关权限

- 不涉及

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## WaterFlowScrollComponent
源码: https://gitcode.com/HarmonyOS_Samples/WaterFlowScrollComponent

# 基于ScrollComponents实现瀑布流

## 简介
本示例展示了使用ScrollComponents构建瀑布流页面，覆盖场景包括

- 瀑布流Item组件复用，以及跨页面的组件复用场景；
- 瀑布流加速首屏渲染的场景；
- 瀑布流无限滑动的场景；
- 瀑布流数据处理场景：下拉刷新、上拉加载、长按删除；
- 瀑布流分组混合布局场景；
- 瀑布流滑动吸顶场景；
- 旋转屏幕瀑布流动态切换列数场景；
- 瀑布流动效场景：边缘渐隐效果、删除滑动错位效果；

## 效果预览
<img src="./screenshots/index.png" width = 320 alt="图片名称"/>

## 工程目录
```        
├─entry/src/main/ets                    // 代码区
├─common 
│  ├─constants
│  │  └─CommonConstants.ets             // 公共常量
│  │
│  └─util
│     ├─Logger.ets                      // 日志类
│     └─Utils.ets                       // 工具类
│
├─entryability
│  └─EntryAbility.ets                   // 程序入口类
│
├─entrybackupability
│  └─EntryBackupAbility.ets
│
├─model
│  ├─mock.ets
│  └─types.ets
│
├─pages
│  ├─CombineWaterFlowPage.ets           // 瀑布流列表项内子组件可拆分组合复用
│  ├─Index.ets
│  ├─MultiFlowItemPage.ets
│  ├─SharedPoolPage.ets
│  ├─SharedPoolSecondPage.ets
│  ├─StandardWaterFlowPage.ets          // 瀑布流列表项结构相同复用
│  ├─StickyWaterFlowPage.ets            // 瀑布流滑动吸顶
│  └─TabBarPage.ets                     // 瀑布流跨页面复用
│
└─workers
   ├─FetchAgent.ets
   └─GetNetworkData.ets
```

## 使用说明
1. StandardWaterFlowPage.ets：实现了列表项结构相同的组件复用、瀑布流加速首屏渲染场景，瀑布流自适应屏幕旋转动态修改列数场景、瀑布流长按删除和删除滑动错位效果场景、瀑布流边缘渐隐效果场景；
2. CombineWaterFlowPage.ets：实现了列表项内子组件可拆分组合的复用、瀑布流加速首屏渲染场景、瀑布流无限滑动场景；
3. TabBarPage.ets：实现了SharedPoolPage.ets和SharedPoolSecondPage.ets之间的跨页面复用功能, 瀑布流下拉刷新和上拉加载场景；
4. StickyWaterFlowPage.ets：实现了瀑布流滑动吸顶场景、瀑布流分组混合布局场景；


## 实现说明
> 下文介绍高效无限瀑布流页面渲染。

### 1. 定义瀑布流视图管理类，注册item节点模板
WaterFlowManage


---
## WearableBus
源码: https://gitcode.com/HarmonyOS_Samples/WearableBus

# 实现智能手表上的公交出行应用

## 介绍

本实例实现了智能手表上公交出行应用的页面布局，通过Navigation组件完成智能手表设备的页面跳转，帮助开发者学习智能手表设备的布局特点以及布局方式。

## 预览效果

| 首页                                 | 附近公交                               | 实时公交                               | 去哪儿                                | 线路方案                               |
|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|
| ![image](screenshots/device/1.png) | ![image](screenshots/device/2.png) | ![image](screenshots/device/3.png) | ![image](screenshots/device/4.png) | ![image](screenshots/device/5.png) |


## 使用说明

1. 首页包含获取定位，2个二级页面入口
2. 从首页点击“附近公交”，进入附近公交列表，选中列表中的某一趟公交，跳转实时公交页面。
3. 从首页点击“去哪儿”，进入“去哪儿”列表，选中列表中的“回家”或“公司”，跳转线路方案页面。

## 工程目录

``` 
├──entry/src/main/ets                          
│  ├──common
│  │  ├──Constants.ets                  // 公共常量
│  │  └──GlobalBuilderContext.ets       // 缓存全局@Builder
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets         // 自定义应用数据转换和迁移模板类
│  ├──model                              
│  │  ├──BusStationModel.ets            // 公交数据结构
│  │  └──RoadModel.ets                  // 线路数据结构
│  ├──pages
│  │   └──Index.ets                     // 首页
│  ├──util
│  │  ├──LocationUtil.ets               // 获取定位工具类                              
│  │  ├──PermissionUtil.ets             // 权限工具类
│  │  └──ScaleUtil.ets    


---
## WearableMusic
源码: https://gitcode.com/HarmonyOS_Samples/WearableMusic

# 实现智能手表播放音乐功能

## 介绍

本示例通过实现一个智能手表上的播放音乐应用，帮助开发者掌握在穿戴设备上开发一款应用的布局方式以及布局特点。

## 预览效果

|                               音乐                               |
|:--------------------------------------------------------------:|
| <img src="./screenshots/device/img.png" width="320"/> |

## 使用说明

1. 安装应用，启动应用。
2. 点击播放按钮，开始播放音乐
3. 点击暂停按钮，暂停音乐。
4. 点击上一首按钮，音乐切到上一首开始播放。
5. 点击下一首按钮，音乐切到下一首开始播放。
6. 点击收藏按钮，收藏按钮点亮。
7. 点击播放模式，可以切换不同的播放模式（注：播放模式未实现实际功能）。

## 工程目录

``` 
├──entry/src/main/ets/
│  ├──common
│  │  └──Constants.ets                          // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets                       // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                 // 数据迁移类
│  ├──model
│  │  └──mediaData.ets                          // 媒体数据类型  
│  ├──pages
│  │  └──Index.ets                              // 界面 page
│  ├──utils
│  │  ├──GlobalContextUtils.ets                 // 缓存context
│  │  ├──Logger.ets                             // 日志工具类
│  │  └──MediaPlayerUtils.ets                   // 音乐播放控制类
│  ├──view
│  │  └──MusicHomeView.ets                      // 界面 UI
│  └──viewmodel
│     └──ProviderManager.ets                    // 媒体提供方状态管理
└───entry/src/main/resources                    // 应用资源目录
``` 

## 具体实现

1. 在[module.json](entry/src/main/module.json5)中设置deviceTypes为wearable
2. 将页面适配为圆形[borderRadius：“50%”](entry/src/main/ets/pages/Index.ets)
3. 采用[AVPlayer](entry/src/main/ets/utils/MediaPlayerUtils.ets)播控音乐
4. 采用[AVSession](entry/src/main/ets/viewm


---
## WebCrossDomain
源码: https://gitcode.com/HarmonyOS_Samples/WebCrossDomain

# 基于ArkWeb拦截器和Cookies管理能力实现Web页面跨域

## 介绍

本示例基于ArkWeb拦截器和Cookies管理能力实现Web页面跨域，聚焦Web页面跨域问题，通过典型场景案例，直观演示跨域解决方案。涵盖本地资源跨域、远程请求跨域、跨域Cookies设置场景及自定义协议跨域，提供可参考的实现思路与代码示例，助力开发者理解跨域原理，快速解决实际项目中的跨域难题。

## 效果预览

<table>
  <tr>
    <td align="center">首页</td>
    <td align="center">本地资源跨域场景详情页</td>
    <td align="center">远程请求跨域场景详情页</td>
  </tr>
  <tr>
    <td align="center"><img src="./screenshots/Screenshot_WebCrossDomain.png" alt="首页" width=320></td>
    <td align="center"><img src="./screenshots/Screenshot_LocalResource.png" alt="本地资源跨域场景详情页" width=320></td>
    <td align="center"><img src="./screenshots/Screenshot_RemoteRequest.png" alt="远程请求跨域场景详情页" width=320></td>
  </tr>
  <tr>
    <td align="center">跨域Cookies设置场景详情页</td>
    <td align="center">自定义协议跨域场景详情页</td>
    <td></td>
  </tr>
  <tr>
    <td align="center"><img src="./screenshots/Screenshot_CookiesSettings.png" alt="跨域Cookies设置场景详情页" width=320></td>
    <td align="center"><img src="./screenshots/Screenshot_CustomProtocol.png" alt="自定义协议跨域场景详情页" width=320></td>
    <td></td>
  </tr>
</table>


## 运行步骤

1. 使用DevEco打开本工程，在根目录打开DevEco的Terminal，执行`hvigorw startServer`命令，启动本地服务器。

   ![Screenshot_terminal](./screenshots/Screenshot_terminal.png)

2. 点击运行，等待编译完成。

3. 重启本地服务器，执行`hvigorw restartServer`命令。

4. 关闭本地服务器，执行`hvigorw stopServer`命令。

## 使用说明

1. 在本地资源跨域页面，点击按钮发出请求，日志区显示请求结果。
2. 在远程请求跨域页面，点击按钮发出请求，日志区显示请求结果。
3. 在跨域Cookies设置页面，进入页面会自动向A域名发出请求，设置cookies，日志区显示请求结果。
4. 在跨域Cookie


---
## WindowOrientation
> 本示例以窗口旋转策略实现的高频场景为载体，通过窗口级配置实现多设备的窗口方向变化。示例中实现了开发中的五个典型场景：应用首页、横竖屏游戏、图库、个股详情页&股票K线图页以及视频详情页&全屏播放页。

源码: https://gitcode.com/HarmonyOS_Samples/WindowOrientation

# 窗口方向

## 项目简介

本示例以窗口旋转策略实现的高频场景为载体，通过窗口级配置实现多设备的窗口方向变化。示例中实现了开发中的五个典型场景：应用首页、横竖屏游戏、图库、个股详情页&股票K线图页以及视频详情页&全屏播放页。

## 效果预览
以首页案例为例的效果图。

| 直板机、双折叠折叠态、三折叠F态                                        | 双折叠展开态、三折叠M态、三折叠G态、平板                                    |
|---------------------------------------------------------|----------------------------------------------------------|
| <img src='screenshots/device/home_phone.gif' width=480> | <img src='screenshots/device/home_tablet.gif' width=480> |

## 使用说明

1. 通过Navigation组件，配置应用的路由信息。
2. 通过点击主页List的ListItem跳转进入对应的高频场景案例中。
3. 在高频场景案例的主页aboutToAppear()生命周期中设置窗口级的窗口旋转策略，并在退出当前页面时恢复上一页面的窗口策略。
4. 对于不同场景及不同设备形态切换做监听，更新符合用户体验的窗口旋转策略。

## 工程目录

```

├──commons                                  // 公共常量及工具
├──features                                 // 程序har包
│  ├──home/src/main/ets                     // 首页案例代码区
│  │  ├──model 
│  │  │  └──TabBarModel.ets                 // 底部导航条数据模型
│  │  ├──viewmodel 
│  │  │  ├──TabBarViewModel.ets             // 底部导航条视图模型
│  │  │  └──WaterFlowDataSource.ets         // 瀑布流视图模型
│  │  └──views 
│  │     └──Home.ets                        // 首页案例主页
│  ├──landscapeModeGame/src/main/ets        // 横屏游戏代码区
│  │  └──views 
│  │     └──LandscapeModeGame.ets           // 横屏游戏主页
│  ├──photos/src/main/ets                   // 图库代码区
│  │  ├──model 
│  │  │  └──PhotsTabBarModel.ets            // 图库底部导航条数据模型
│  │  ├──viewmodel 
│  │  │  ├──ListDataSource.ets              // 图库列表视图模型
│  │  │  └──PhotoTabBarViewModel.ets 


---
## ability-start-mode
> 本示例展示了在一个Stage模型中，实现multiton、singleton、specified多种模式场景。

源码: https://gitcode.com/HarmonyOS_Samples/ability-start-mode

# 基于Stage模型中的UIAbility组件启动模式

### 介绍

本示例展示了在一个stage模型中，针对不同的业务场景，实现UIAbility实例在启动时的不同呈现状态，提供了三种启动模式： singleton启动模式为单实例模式， multiton启动模式为多实例模式， specified启动模式为指定实例模式。

### 效果预览

![](./screenshots/devices/effect.gif)

使用说明

1、multiton模式：

1）进入首页，点击番茄，会新建一个番茄的Ability，展示番茄的详情；

2）在番茄的详情界面，点击黄瓜，会新建一个黄瓜的Ability，展示黄瓜的详情；

3）使用aa工具查看Ability信息，此时存在以下Ability：1个番茄的Ability、1个黄瓜的Ability、1个首页的Ability；

2、singleton模式：

1）进入首页，点击冰淇凌，会新建一个冰淇凌的Ability，展示冰淇凌的详情；

2）在冰淇凌的详情界面，点击螃蟹，会复用冰淇凌的Ability，页面数据会刷新并展示螃蟹的详情；

3）使用aa工具查看Ability信息，此时存在以下Ability：1个冰淇凌的Ability、1个首页Ability；

3、specified模式：

1）进入首页，点击核桃，会新建一个核桃的Ability，展示核桃的详情；

2）在核桃的详情界面，点击蓝莓，会新建一个蓝莓的Ability，展示蓝莓的详情；

3）在蓝莓的详情界面，点击核桃，会复用已存在的核桃的Ability，实现specified模式下的单实例特性，页面数据会刷新并展示核桃的详情；

4）使用[aa工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/aa-tool)查看Ability信息，此时存在以下Ability：1个核桃的Ability、1个蓝莓的Ability、1个首页Ability；

### 工程目录
```
├──entry/src/main/ets/
│  ├──application
│  │  └──MyAbilityStage.ets 
│  ├──common
│  │  ├──Constants.ets                    // 常量类
│  │  ├──Logger.ts                        // 日志工具
│  │  └──Util.ets                         // 封装常用函数
│  ├──entryability
│  │  └──MainAbility.ets 
│  ├──model
│  │  ├──DataModels.ets                   // 封装数据类型
│  │  ├──DataUtil.ets                     // 封装数据处理函数
│  │  └──MokeData.ets                     // 模拟数据
│  ├──multitonability                  
│  │  └──MultitonAbility.ets              // multiton模式的Ability
│  ├──pages
│  │  ├──component
│  │  │  └──FoodListItem.ets 


---
## account-kit-samplecode-clientdemo-for-atomicservice-arkts
> 本示例基于HarmonyOS实现了Account Kit（华为账号服务）提供的华为账号静默登录、获取头像昵称、快速验证手机号、获取收货地址、获取发票抬头、未成年人模式等功能。

源码: https://gitcode.com/HarmonyOS_Samples/account-kit-samplecode-clientdemo-for-atomicservice-arkts

# 基于华为账号服务实现登录、授权等功能（元服务）

## 项目简介

本示例展示了使用 authentication.AuthenticationController 接口实现静默登录的能力，使用 FunctionalButton 组件提供的获取头像、手机号、收货地址、发票抬头的能力以及使用 Account Kit 开启或关闭未成年人模式的能力。

本示例模拟了在元服务里调用登录接口实现静默登录；使用 FunctionalButton 组件获取头像功能获取头像；使用 FunctionalButton 组件获取手机号功能获取手机号；使用 FunctionalButton 组件获取收货地址功能获取收货地址；使用 FunctionalButton 组件获取发票抬头功能获取发票抬头；调用未成年人模式接口开启或关闭未成年人模式，订阅未成年人模式公共事件，调用未成年人模式验密接口验证未成年人模式密码。

需要使用 Account Kit 接口 **@kit.AccountKit** 以及 **FunctionalButton** 组件。

## 效果预览

注意：本示例中的效果预览图均为HarmonyOS最新版本效果图，如有差异请以实际效果为准。

|                                                    |                                                    |                                                    |
|:--------------------------------------------------:|:--------------------------------------------------:|:--------------------------------------------------:|
|                      **购物页面**                      |                      **我的页面**                      |                      **获取头像**                      |
| <img src="screenshots/device/img_1.png" width=320> | <img src="screenshots/device/img_2.png" width=320> | <img src="screenshots/device/img_3.png" width=320> |
|                     **获取手机号**                      |                     **获取收货地址**                     |                     **获取发票抬头**                     |
| <img src="screenshots/device/img_4.png" width=320> | <img src="screenshots/device/img_5.png" width=320> | <img src="screenshots/device/img_6.png" width=320> |
|     


---
## accountkit-samplecode-clientdemo-arkts
> 本示例基于HarmonyOS实现了Account Kit（华为账号服务）提供的华为账号一键登录、静默登录、获取头像昵称、获取手机号、获取收货地址、未成年人模式和获取发票抬头等功能。

源码: https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-arkts

# 基于华为账号服务实现华为账号一键登录等功能

## 项目简介

本示例展示了使用 Account Kit 提供的登录、授权头像昵称、快速验证手机号、收货地址、发票抬头、未成年人模式的能力。

本示例模拟了在应用里，调用一键登录 Button 组件拉起符合华为规范的登录页面；调用登录接口实现静默登录；调用获取头像昵称接口获取头像昵称；调用快速验证手机号接口拉起手机号快速验证页面；调用收货地址接口获取收货地址；调用发票抬头接口获取发票抬头；调用未成年人模式接口开启未成年人模式；订阅未成年人模式公共事件；调用未成年人模式验密接口验证未成年人模式密码。

需要使用 Account Kit 接口 **@kit.AccountKit**。

## 效果预览

注意：本示例中的效果预览图均为HarmonyOS最新版本效果图，如有差异请以实际效果为准。

|                                                       |                                                       |                                                      |
|:-----------------------------------------------------:|:-----------------------------------------------------:|:----------------------------------------------------:|
|                      **登录/注册页面**                      |                    **一键登录组件登录页面**                     |                    **一键登录组件弹窗页面**                    |
| <img src="screenshots/device/img_1.png" width="320">  | <img src="screenshots/device/img_2.png" width="320">  | <img src="screenshots/device/img_3.png" width="320"> |
|                      **应用其他登录页**                      |                      **用户登录后首页**                      |                     **用户个人信息页面**                     |
| <img src="screenshots/device/img_4.png" width="320">  | <img src="screenshots/device/img_5.png" width="320">  | <img src="screenshots/device/img_6.png" width="320"> |
|                      **头像昵称授权页**                      |                    **获取快速验证手机号页面**                 


---
## accountkit-samplecode-clientdemo-flutter
> 本示例演示了基于 Flutter 使用 Account Kit 提供的华为账号一键登录 Button 组件登录流程。

源码: https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-flutter

# Account Kit

## 介绍

本示例演示了基于 Flutter 使用 Account Kit 提供的华为账号一键登录 Button 组件登录流程。

本示例模拟了应用调用一键登录 Button 组件，拉起符合华为规范的登录页面。

需要使用 Account Kit 接口 **@kit.AccountKit**。

## 效果预览

|               **登录/注册页面**               |             **一键登录组件登录页面**              |
|:---------------------------------------:|:---------------------------------------:|
| ![avatar](screenshots/device/img_1.png) | ![avatar](screenshots/device/img_2.png) |

|             **一键登录组件弹窗页面**              |              **用户个人信息页面**               |
|:---------------------------------------:|:---------------------------------------:|
| ![avatar](screenshots/device/img_3.png) | ![avatar](screenshots/device/img_4.png) |


## 本示例的配置与使用

### Flutter 开发环境配置如下
1. 使用 git 下载 OpenHarmony 版 flutter: ``` git clone https://gitee.com/openharmony-sig/flutter_flutter.git ```。
2. 添加环境变量 ``` FLUTTER_ROOT= ${clone下来的项目代码} ```，在path中添加``` %FLUTTER_ROOT%\bin ```。
3. 安装 jdk17 并配置环境变量 ``` JAVA_HOME=${jdk的安装位置} ```，在path中添加 ``` %JAVA_HOME%\bin ```。
4. 添加环境变量 ``` FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn ``` 和 ``` PUB_HOSTED_URL=https://pub.flutter-io.cn ```。
5. 添加环境变量 ``` PUB_CACHE=D:/PUB(自定义路径，新建一个空文件夹即可) ```。
6. 在命令行执行 ``` flutter doctor -v ```，检查当前环境，按提示进行操作。
7. 详细的环境搭建请查看[OpenHarmony版Flutter环境搭建指导](https://gitee.com/openharmony-sig/flutter_samples/blob/master/ohos/docs/03_environment/%E9%B8%BF%E8%92%99%E7%89%88Flutter%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA%E6%8C%87%E5%AF%BC.md)和[环境依赖](https://gitee.com/openharmony-sig/fl


---
## accountkit-samplecode-clientdemo-h5
> 本示例演示了基于H5使用 Account Kit 提供的华为账号一键登录 Button 组件登录流程。

源码: https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-h5

# Account Kit

## 介绍

本示例演示了基于H5使用 Account Kit 提供的华为账号一键登录 Button 组件登录流程。

本示例模拟了应用调用一键登录 Button 组件，拉起符合华为规范的登录页面。

需要使用 Account Kit 接口 **@kit.AccountKit**。

## 效果预览

|               **登录/注册页面**               |             **一键登录组件登录页面**              |
|:---------------------------------------:|:---------------------------------------:|
| ![avatar](screenshots/device/img_1.png) | ![avatar](screenshots/device/img_2.png) |

|             **一键登录组件弹窗页面**              |              **用户个人信息页面**               |    
|:---------------------------------------:|:---------------------------------------:|
| ![avatar](screenshots/device/img_3.png) | ![avatar](screenshots/device/img_4.png) |

## 本示例的配置与使用

### 在DevEco中配置本示例的步骤如下
1. 在华为开发者联盟官网下载安装[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)(5.0.5 Release 及以上)。
2. 参考Account Kit开发指南的[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-preparations)章节，创建项目和应用、申请账号权限（华为账号一键登录）、配置签名和指纹、配置Client ID。
3. 使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)配置的包名替换app.json5文件中的bundleName属性值。

### 本示例使用说明
1. 运行本示例前，请先查看[约束与限制](#约束与限制)，确保满足示例运行条件。
2. 登录符合条件的账号，运行本示例。应用在申请完“华为账号一键登录”权限后，点击首页的“登录/注册”按钮，会拉起嵌有“华为账号一键登录”按钮的登录页面。登录成功后跳转到个人信息页，展示用户信息（匿名手机号），点击退出按钮返回首页。
3. 点击首页的“登录/注册”按钮时，会先获取匿名手机号。如果未获取成功，则不会拉起嵌有“华为账号一键登录”按钮的登录页面，并且本示例中只声明对应错误码，未做相应处理，请开发者自行实现跳转其他登录页面的逻辑。
4. 点击“华为账号一键登录”按钮时，如果未勾选下方的同意协议多选框，则会拉起协议弹窗提示用户同意协议或取消登录。如点击“同意并登录”按钮则完成华为账号一键登录，点击“取消”按钮则关闭弹窗。
5


---
## accountkit-samplecode-clientdemo-rn
> 本示例展示了基于React-Native（RN）使用 Account Kit 提供的华为账号一键登录 Button 组件登录流程。

源码: https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-rn

# Account Kit

## 介绍

本示例展示了基于React-Native（RN）使用 Account Kit 提供的华为账号一键登录 Button 组件登录流程。

本示例模拟了在应用里，调用一键登录 Button 组件拉起符合华为规范的登录页面。

需要使用 Account Kit 接口 **@kit.AccountKit**。

## 效果预览

|               **登录/注册页面**               |             **一键登录组件登录页面**              |
|:---------------------------------------:|:---------------------------------------:|
| ![avatar](screenshots/device/img_1.png) | ![avatar](screenshots/device/img_2.png) |

|             **一键登录组件弹窗页面**              |              **用户个人信息页面**               |
|:---------------------------------------:|:---------------------------------------:|
| ![avatar](screenshots/device/img_3.png) | ![avatar](screenshots/device/img_4.png) |

## 本示例的配置与使用

### 在WebStorm/DevEco中配置本示例的步骤如下

1. 在[WebStorm官方网站](https://www.jetbrains.com/webstorm/)下载WebStorm，用于打开和查看RN工程。
2. 在华为开发者联盟官网下载安装[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)(5.0.5 Release 及以上)。
3. 在AppGallery Connect[创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
4. 在DevEco Studio中打开示例MyReact/harmony，将[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)配置的应用包名配置到示例根目录下的MyReact/harmony/AppScope/app.json5中，替换bundleName属性值。
5. 在示例中使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)配置的应用Client ID替换MyReact/harmony/entry/src/main/modul


---
## accountkit-samplecode-clientdemo-uniapp
> 本示例展示了基于uni-app使用 Account Kit 提供的华为账号一键登录 Button 组件登录的相关流程。

源码: https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-uniapp

# Account Kit

## 介绍

本示例展示了基于uni-app使用 Account Kit 提供的华为账号一键登录 Button 组件登录的相关流程。

本示例模拟了在应用里，调用华为账号一键登录 Button 组件拉起符合华为规范的登录页面。

需要使用 Account Kit 接口 **@kit.AccountKit**。

## 效果预览

|               **登录/注册页面**               |             **一键登录组件登录页面**              |
|:---------------------------------------:|:---------------------------------------:|
| ![avatar](screenshots/device/img_1.png) | ![avatar](screenshots/device/img_2.png) |

|             **一键登录组件弹窗页面**              |              **用户个人信息页面**               |
|:---------------------------------------:|:---------------------------------------:|
| ![avatar](screenshots/device/img_3.png) | ![avatar](screenshots/device/img_4.png) |

## 本示例的配置与使用

### 在HBuilderX/DevEco中配置本示例的步骤如下
1. 在华为开发者联盟官网下载安装[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)(5.0.5 Release 及以上)。
2. 在uni-app官网下载安装4.62及以上版本的[HBuilderX](https://dcloud.io/hbuilderx.html)。
3. 在AppGallery Connect[创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
4. 打开 HBuilderX [设置 DevEco Studio 的安装位置](https://zh.uniapp.dcloud.io/tutorial/harmony/runbuild.html#hbxsettings)。
5. 在 HBuilderX 中打开示例工程，将[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)配置的应用包名配置到示例工程根目录下的manifest.json中，参考[App配置的图示位置](https://zh.uniapp.dcloud.io/tutorial/harmony/runbuild.html#config-app-harmony)。



---
## adaptive-buffer-resolution-samplecode-clientdemo-cpp
> 本示例主要展示基于图形加速服务（Graphics Accelerate Kit）的ABR API实现游戏自适应稳态渲染功能

源码: https://gitcode.com/HarmonyOS_Samples/adaptive-buffer-resolution-samplecode-clientdemo-cpp

# 自适应稳态渲染（ABR）

## 介绍

本示例展示了基于Graphics Accelerate Kit提供的ABR API在图形绘制场景实现自适应稳态渲染功能。

需要编译依赖AdaptiveBufferResolution的动态库libabr.so。

## 效果预览

|            **桌面**             |                 **主界面**                 |
|:-----------------------------:|:---------------------------------------:|
| ![desk](screenshots/desk.png) | ![interface](screenshots/interface.png) |

使用说明：

1. 在手机的主屏幕，点击”ABR Demo“，启动应用，进入图形绘制场景。
2. 点击左上角，可手动开启或关闭ABR功能。显示“ABR开启”表示动态分辨率功能已开启，显示“ABR关闭”表示自适应稳态渲染功能已关闭。
3. 退出应用时，自动关闭ABR。

## 工程目录

```
└── entry/src/main                          // 代码区
    ├── cpp
    │    ├── types/libentry
    │    │     └── index.d.ts               // native层接口注册文件
    │    ├── napi_init.cpp                  // native api层接口的具体实现函数
    │    ├── CMakeLists.txt                 // native层编译配置
    │    ├── include                        // 头文件
    │    ├── source                         // C++代码区
    │    │    ├── core.cpp                  // 核心入口，管理生命周期
    │    │    ├── renderer.cpp              // 渲染管理类的实现
    │    │    ├── scene_base.cpp            // ABR基类的实现
    │    │    ├── scene_abr.cpp             // ABR类的实现
    │    │    ├── opaque_layer_base.cpp     // 场景绘制基类的实现
    │    │    ├── opaque_layer.cpp          // 场景绘制派生类的实现
    │    │    ├── gui.cpp                   // UI绘制
    │    │    └── ...
    ├── ets
    │    ├── ability 
    │    │     └── EntryAbility.ts          // 程序入口类
    │    ├── pages 
    │    │     └── Index.ets                // 主界面
    └── resources
    │   


---
## adaptive-service-widget
> 本示例展示Js工程中服务卡片的布局和使用，其中卡片内容显示使用了一次开发，多端部署的能力实现多设备自适应。

源码: https://gitcode.com/HarmonyOS_Samples/adaptive-service-widget

#  基于服务卡片实现多设备自适应能力

### 介绍

本示例采用一次开发、多端部署的技术，简化了JS卡片的布局设计，确保其在多种设备上实现智能自适应。开发者无需为每个设备单独调整布局，从而提高了开发效率和用户体验的一致性。

### 效果预览

| 主页                                | 卡片                                |
|-----------------------------------|-----------------------------------|
| ![](screenshots/device/main.png) | ![](screenshots/device/card.png) |

使用说明

1.部分设备的桌面不支持卡片，可以通过自己的开发卡片使用方，进行卡片的创建、更新和删除等操作。

2.安装应用，并在桌面上长按本应用的桌面图标，长按后弹出选项列表。

3.点击弹出列表中的**服务卡片**选项进入卡片添加界面。

4.点击正下方的**添加到桌面**按钮，卡片就会出现在桌面上。

### 工程目录
```
├──entry/src/main/ets                         // ets代码区
│  ├──entryability  
│  │  └──EntryAbility.ets         
│  ├──entryformability                                   
│  │  └──EntryFormAbility.ets                 // 定义卡片对象首次被创建时需要做的操作
│  ├──pages  
│  │  └──index.ets                            // 首页
│  └──utils  
│     └──Logger.ets                           // 日志工具类
├──entry/src/main/js                          // js代码区
│     ├──common                               // 卡片资源文件目录               
│     ├──complex/pages/index                  // 证券卡片（4x4）   
│     ├──grid/pages/index                     // 网格布局卡片                       
│     ├──i18n                                 // 卡片国际化语言目录              
│     ├──imgText/pages/index                  // 图文卡片                
│     ├──immersive/pages/index                // 沉浸式卡片
│     └──test/pages/index                     // 证券卡片（2x2）  
├──entry/src/main/resources                   // 应用资源目录 
└──module.json5              


---
## ads-kit-sample-code-client-demo-arkts
> 本示例向您介绍如何在应用中使用鲸鸿动能API实现广告加载和展示能力。


源码: https://gitcode.com/HarmonyOS_Samples/ads-kit-sample-code-client-demo-arkts

# 实现广告服务

## 目录

- [简介](#简介)
- [使用说明](#使用说明)
- [效果预览](#效果预览)
- [工程目录](#工程目录)
- [示例代码](#示例代码)
- [相关权限](#相关权限)
- [约束与限制](#约束与限制)

## 简介

鲸鸿动能广告服务HarmonyOS ArkTs示例代码向您介绍如何在应用中使用将鲸鸿动能API并实现广告展示。

## 使用说明

运行本示例前需要参考指导[配置应用签名信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview#section42841246144813)。

## 效果预览

| 广告样式主页面                                       | 横幅广告页面                                     | 原生视频广告页面                                         |
|-----------------------------------------------|--------------------------------------------|--------------------------------------------------|
| ![avatar](./screenshots/device/home_page.png) | ![avatar](./screenshots/device/banner.png) | ![avatar](./screenshots/device/native_video.png) | 

| 原生大图广告页面                                               | 原生小图广告页面                                               | 原生三图广告页面                                               |
|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|
| ![avatar](./screenshots/device/native_large_image.png) | ![avatar](./screenshots/device/native_small_image.png) | ![avatar](./screenshots/device/native_three_image.png) |

| 激励广告页面                                     | 插屏视频广告页面                                               | 插屏图片广告页面                                                  |
|------------------------------


---
## aicharacter-recognition
> 本示例通过使用@ohos.multimedia.camera (相机管理)和textRecognition（文字识别）接口来实现识别提取照片内文字的功能。

源码: https://gitcode.com/HarmonyOS_Samples/aicharacter-recognition

# 基于基础视觉服务及相机实现拍照识别文字功能

## 介绍

本示例通过使用@ohos.multimedia.camera (相机管理)和textRecognition（文字识别）接口实现拍照后识别提取照片内文字的功能。帮助开发者了解开发文字识别工具类应用时，如何将照片输入流与文字识别接口关联，从而实现文字识别的功能。

## 效果预览

| 主页                                | 文字识别弹窗                             |
|-----------------------------------|------------------------------------|
| ![](screenshots/device/index.png) | ![](screenshots/device/dialog.png) |

使用说明

1.点击界面下方圆形文字识别图标，弹出文字识别结果信息界面，显示当前照片的文字识别结果；

2.点击除了弹窗外的空白区域，弹窗关闭，返回主页。

## 工程目录

```
├──entry/src/main/ets/
│  ├──common/constant
│  │  └──CommonConstants.ets            // 公共常量类
│  ├──common/utils
│  │  ├──DeviceScreen.ets               // 屏幕尺寸计算工具
│  │  ├──Logger.ets                     // 日志工具
│  │  ├──PermissionUtils.ets            // 权限获取工具
│  │  └──Camera.ets                     // 相机管理工具
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──page                  
│  │  └──Index.ets                      // 首页
│  └──view                  
│     └──CustomDialogView.ets           // 识别弹窗页面
└──entry/src/main/resources             // 应用静态资源目录
```
## 具体实现

* 本实例完成AI文字识别的功能模块主要封装在CameraModel，源码参考:[Camera.ets](entry/src/main/ets/common/utils/Camera.ets) 。
    * 相机模块：在Camera中封装了相机初始化、相机释放。
    * 在Index页面通过点击事件触发相机拍摄，在获取到照片输出流后通过@hms.ai.ocr.textRecognition文字识别接口进行识别。

## 相关权限

获取相机权限：ohos.permission.CAMERA。

## 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：Harmony


---
## animation-collection
> 本示例基于基础组件、通用属性、显式动效，实现多种常见动效案例。

源码: https://gitcode.com/HarmonyOS_Samples/animation-collection

# 实现动效功能合集

### 介绍

本示例基于基础组件、通用属性、显式动效，实现多种常见动效案例，便于用户进行常见的动效场景开发。

### 效果预览


| 翻转动效                                           | 标题下拉缩放                                   | 状态栏显隐切换                                 | 水波纹动效                                                |
|------------------------------------------------|------------------------------------------|-----------------------------------------|------------------------------------------------------|
| ![image](screenshots/device/Flag.gif)          | ![image](screenshots/device/Drag.gif)    | ![image](screenshots/device/Hide.gif)   | ![image](screenshots/device/Water.gif)               |
| 滑动到指定列表                                        | 跑马灯                                      | swiper高度变化效果                            | 自定义进度动画                                              |
| ![image](screenshots/device/Move.gif)          | ![image](screenshots/device/Marquee.gif) | ![image](screenshots/device/Swiper.gif) | ![image](screenshots/device/Progress.gif)            |
| 数字滚动动效                                         | 卡片预览效果                                   | 投票动效                                    | 语音录制动效                                               |
| ![image](screenshots/device/Scroll.gif)        | ![image](screenshots/device/Preview.gif) | ![image](screenshots/device/Vote.gif)   | <img src="screenshots/device/Voice.gif" width="231"> |
| 弹簧曲线实现抖动效果                                     | 侧边栏淡入淡出动效                       


---
## app-account-manager
> 本示例选择应用进行注册/登录，并设置帐号相关信息，简要说明应用帐号管理。

源码: https://gitcode.com/HarmonyOS_Samples/app-account-manager

# 基于AppAccountManager能力实现应用账号管理

### 介绍
本示例通过使用AppAccountManager能力，实现了一个支持注册/登录，并设置账号相关信息的功能，帮助开发者掌握应用账号管理AppAccountManager的基本能力。 效果图如下：

### 效果预览

|主页| 注册页面                                 | 登录页面                              | 账户信息页面|
|--------------------------------|--------------------------------------|-----------------------------------|------|
|![](screenshots/device/index.png)| ![](screenshots/device/register.png) | ![](screenshots/device/login.png) |![](screenshots/device/account.png)|

使用说明

1.首页面选择想要进入的应用，首次进入该应用需要进行注册，如已注册账号则直接登录。

2.注册页面可设置账号名、邮箱、个性签名、密码（带*号为必填信息），注册完成后返回登录页面使用注册的账号进行登录。

3.登录后进入账号详情界面，点击**修改信息**按钮可跳转至账号信息修改页面重新设置账号信息。

4.点击**切换应用**按钮则退出该账号并返回首页面。重新选择想要进入的应用。

5.点击**删除账号**按钮则会删除该账号所有相关信息。

### 工程目录
```
├──entry/src/main/ets                         // 代码区
│  ├──common
│  │  ├──AccountInfo.ets                      // 切换应用组件
│  │  ├──BundleInfo.ets                       // 首页列表组件
│  │  ├──LoginInfo.ets                        // 登录组件
│  │  ├──ModifyInfo.ets                       // 修改信息组件
│  │  ├──NavigationBar.ets                    // 路由跳转组件
│  │  └──RegisterInfo.ets                     // 注册组件
│  ├──entryAbility  
│  │  └──EntryAbility.ts               
│  ├──model  
│  │  ├──AccountData.ts                       // 数据存储
│  │  ├──AccountModel.ts                      // 数据管理
│  │  └──Logger.ts                            // 日志工具
│  └──pages  
│     ├──Index.ets                            // 首页
│     ├──Account.ets                          // 切换应用页面
│


---
## appgallerykit-samplecode-clientdemo-arkts
> 本示例实现了应用详情展示、元服务加桌以及按需加载HAP包等功能。

源码: https://gitcode.com/HarmonyOS_Samples/appgallerykit-samplecode-clientdemo-arkts

# 基于对外开放功能实现提高应用曝光度

## 介绍

基于Stage模型，实现了展示应用详情页下载安装目标应用、展示元服务详情页添加至桌面、查询广告验签标签版本、获取模块安装信息和添加按需加载模块、应用市场更新和应用归因服务、查询隐私链接、查询隐私签署结果以及停止隐私协议等功能。

## 效果预览
![](screenshots/device/sample.jpg)
![](screenshots/device/loadproduct.jpg)
![](screenshots/device/loadservice.jpg)
![](screenshots/device/getadsverificationversion.jpg)
![](screenshots/device/getselfscenecode.jpg)
![](screenshots/device/loadinstall_cn.jpg)
![](screenshots/device/checkupdate_cn.jpg)
![](screenshots/device/attributionmanager.jpg)
![](screenshots/device/getappprivacymgmtinfo.jpg)
![](screenshots/device/getappprivacyresult.jpg)
![](screenshots/device/disableservice.jpg)
![](screenshots/device/requestappprivacyconsent.jpg)
![](screenshots/device/addshortcuttodesktop_cn.jpg)
![](screenshots/device/dynamiciconmanager_cn.jpg)

## 工程目录

```
├─Attribution/src/main/ets
│                       │  
│                       ├─attributionability/AttributionAbility.ets  // 本地启动应用归因ability 
│                       ├─common/utils/SignUtil.ets     // 生成签名方法    
│                       └─pages
│                           └─Attribution.ets  // 应用归因服务及应用归因接入调试功能接口页面
├─entry/src/main/ets
                   ├─common/bean/EntryItemInfo.ets   // 页面入口工具类
                   ├─entryability/EntryAbility.ets   // 本地启动ability   
                   │              
                   └─pages
                       ├─ CheckUpdatePage.ets           // 应用检查更新
                       ├─ DisableService.ets            // 停止隐私协议
                       ├


---
## application-track
源码: https://gitcode.com/HarmonyOS_Samples/application-track

# 基于UIObserver能力的应用埋点

## 介绍

本示例基于UIObserver能力实现了常见的埋点行为：点击埋点、曝光埋点、页面埋点。开发者可以结合业务场景进行应用埋点，针对用户行为收集、处理和发送一些信息，以跟踪应用的使用情况，包括访问数、访客数、停留时长、页面浏览数和跳出率等。

## 效果预览

![](screenshots/device/ApplicationTrack_CN.gif)

## 工程目录

```
├──entry/src/main/ets                        // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets                    // Ability的生命周期回调内容
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets              // EntryBackupAbility的生命周期回调内容
│  ├──pages                                  
│  │  ├──ClickPage.ets                       // 点击埋点
│  │  ├──HomePage.ets                        // 主页面
│  │  ├──NavigationPage.ets                  // 使用Navigation路由时的页面切换埋点页面  
│  │  ├──PageOne.ets                         // 第一个Navigation路由埋点页面 
│  │  ├──PageTwo.ets                         // 第二个Navigation路由埋点页面  
│  │  ├──RouterPageA.ets                     // 第一个Router路由埋点页面 
│  │  ├──RouterPageB.ets                     // 第二个Router路由埋点页面            
│  │  ├──WaterFlowCard.ets                   // 瀑布流卡片       
│  │  └──WaterFlowPage.ets                   // 组件的曝光展示埋点页面        
│  └──viewModel                              // 埋点逻辑
│     ├──CallBackManager.ets                  
│     ├──DataResource.ets                    
│     ├──TrackNode.ets              
│     └──WaterFlowDataSource.ets              
└──entry/src/main/resources                  // 应用资源目录
```

## 使用说明

1. 请参考[应用埋点](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-track-practice)


#


---
## applinkingkit_samplecode_deferredlink_arkts
> 本示例将引导您先作为目标方应用集成App Linking Kit（应用链接服务）延迟链接能力，然后作为拉起方应用，打开目标方应用，并跳转到目标方应用的详情页面。

源码: https://gitcode.com/HarmonyOS_Samples/applinkingkit_samplecode_deferredlink_arkts

# 基于延迟链接能力跳转应用详情页

## 简介

本示例展示了作为目标方应用（AppLinkingSampleDestination）如何获取拉起方应用（AppLinkingSampleOriginal）的延迟链接地址，并跳转详情页面，提升链接转化率；作为拉起方如何拉起集成了App Linking Kit的目标方应用，缩短应用链接打开步骤，提升用户体验。

1. 在目标方应用的module.json5里配置需要拉起的延迟链接的skills信息。
2. 在目标方应用中使用deferredLink.popDeferredLink()接口获取延迟链接的url。
3. 在拉起方应用中使用context.openLink()接口拉起延迟链接的url。

## 效果预览

|             **主页面**             |
| :--------------------------------: |
| ![](./SampleImg/device/sample.gif) |


## 配置与使用

### 目标方应用配置步骤

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。

2. 打开应用，使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)配置的应用包名替换app.json5文件中的bundleName属性值。

3. 使用[手动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)创建一个签名，替换工程中build-profile.json5文件中的signingConfigs的内容。

4. 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台开通App Linking服务，并且配置网址域名，具体操作步骤请参见[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/applinking-preparations)。

5. 在应用的module.json5里面配置skills的相关信息，可以参考以下图片。

   ![](./SampleImg/setting/module.png)

### 拉起方应用配置步骤

打开应用，配置[自动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section18815157237)并运行。

### 使用说明

1. 提前将拉起方应用（AppLinkingSampleOriginal）安装到手机上，点击页面上的按钮会触发打开链接的功能。
2. 首次安装并点击目标方应用


---
## arkts-clock
> 本示例通过使用@ohos.display接口以及Canvas组件来实现一个简单的时钟应用。

源码: https://gitcode.com/HarmonyOS_Samples/arkts-clock

# 基于Canvas组件开发时钟应用

### 介绍

本示例通过使用@ohos.display接口以及Canvas组件来实现一个简单的时钟应用，帮助开发者掌握通过Canvas组件绘制周期性实时刷新页面的方法。

### 效果预览

| 主页                                   |
|--------------------------------------|
| ![main](screenshots/device/main.png) |

使用说明

1.界面通过setInterval实现周期性实时刷新时间，使用Canvas绘制时钟，指针旋转角度通过计算得出。

例如："2 * Math.PI / 60 * second"是秒针旋转的角度。

### 工程目录
```
├──entry/src/main/ets                         // 代码区
│  ├──common
│  │  └──CommonConstants.ets                  // 公共常量
│  ├──entryability
│  │  └──EntryAbility.ets 
│  ├──pages
│  │  └──Index.ets                            // 首页
│  └──utils
│     ├──DrawClock.ets                        // 时钟绘制工具
│     └──Logger.ets                           // 日志工具
└──entry/src/main/resources                   // 应用资源目录

```
### 具体实现

* 本示例展示简单时钟的方法主要封装在Index中，源码参考:[Index.ets](entry/src/main/ets/pages/Index.ets) 。
    * 设置表盘大小：通过Index中的display.getDefaultDisplay()方法来获取设备宽高计算表盘大小；
    * 获取当前时间：调用updateTime函数，执行new Date().getHours()、new Date().getMinutes()、new Date().getSeconds()获取当前时间。
    * 绘制表盘内容：通过CanvasRenderingContext2D来画表盘背景、时针、分针、秒针、圆心以及表盘下方文本；
    * 启动时钟：添加setInterval定时器，每隔1s执行一次updateTime函数。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK 及以上。


---
## arkweb-same-level-rendering
> 该方案展示了ArkWeb同层渲染：将系统原生组件直接渲染到前端H5页面上，原生组件不仅可以提供H5组件无法实现的一些功能，还能提升用户体验的流畅度。

源码: https://gitcode.com/HarmonyOS_Samples/arkweb-same-level-rendering

# 基于ArkWeb实现系统原生组件渲染至H5页面上

### 介绍

该方案展示了采用ArkWeb进行同层渲染的示例，可以将系统原生组件的内容直接渲染到前端H5页面上，原生组件不仅提供了H5组件无法实现的一些功能，还能提升流畅度，并增强用户的体验感。

### 效果图预览

![](./screenshot/device/pic.png)

**使用说明**

进入页面即可看到同层渲染效果，Text，Image都是原生组件。

### 高性能知识点

ArkWeb同层渲染原生组件，原生组件不仅可以提供H5组件无法实现的一些功能，还能提升用户体验的流畅度；同层渲染节点上下树，实现节点复用，节省节点重复开销。

### 工程结构&模块类型
```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets                    // 配置类
│  ├──model
│  │  └──GoodsModel.ets                      // 类型声明
│  ├──pages
│  │  └──Index.ets                           // 程序入口类
│  └──viewmodel
│     └──GoodsViewModel.ets                  // 模拟数据类
└──entry/src/main/resource                   // 应用静态资源目录
```
### 相关权限

- 允许应用使用Internet网络权限：ohos.permission.INTERNET。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## aspect
> Aspect 是面向 OpenHarmony（鸿蒙）应用工程的轻量级 AOP（面向切面编程）插件库，核心基于鸿蒙libabcKit字节码操作能力（abckit 框架）， 实现字节码层面的无侵入式代码增强。通过该插件，开发者无需修改业务源码，即可在指定方法的执行前、执行后等切面点插入自定义逻辑，轻松实现日志埋点、 参数拦截、方法替换等通用功能，大幅提升代码复用性和业务逻辑的解耦程度。

源码: https://gitcode.com/HarmonyOS_Samples/aspect

# 基于Aspect插件库实现切面编程
## 项目简介
本示例代码展示了如何通过Aspect插件库实现切面编程。覆盖场景包括：
- 方法定义点前置、后置插桩
- API调用点前置、后置、替换插桩
- UI组件事件回调函数前置、后置插桩
- API异步回调函数前置、后置、替换插桩

## 效果预览

|                                    首页                                    |                                 方法回调插桩                                  |                                    原始效果                                     |
|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
|      <img src="./screenshots/device/aspect_home.png" width="320"/>       | <img src="./screenshots/device/aspect_callback_main.png" width="320"/>  | <img src="./screenshots/device/aspect_callback_primitive.png" width="320"/> |
|                                   前置插桩                                   |                                  后置插桩                                   |                                    替换插桩                                     |
| <img src="./screenshots/device/aspect_callback_before.png" width="320"/> | <img src="./screenshots/device/aspect_callback_after.png" width="320"/> |  <img src="./screenshots/device/aspect_callback_replace.png" width="320"/>  |

## 使用说明
下载代码请复制以下命令到终端运行
```bash
git clone https://gitcode.com/HarmonyOS_Samples/aspect.git
```
或者使用[**Gitcode**](https://gitcode.com/HarmonyOS_Samples/aspect)下载ZIP

Aspect插件的使用说明请参考[**Aspect插件快速开始**](htt


---
## asset-store-arkts
> 本示例主要展示了Asset Store Kit开发指导(ArkTS)中新增关键资产、删除关键资产、更新关键资产、查询关键资产等场景。

源码: https://gitcode.com/HarmonyOS_Samples/asset-store-arkts

# Asset Store Kit开发指导(ArkTS)

### 介绍

Asset Store Kit（关键资产存储开发套件）包含了关键资产存储服务（ASSET）开放的接口能力集合，提供了用户短敏感数据的安全存储及管理能力。其中，短敏感数据可以是密码类（账号/密码）、Token类（应用凭据）、关键明文（如银行卡号）等长度较短的用户敏感数据。

本示例主要展示了Asset Store Kit开发指导(ArkTS)中新增关键资产、删除关键资产、更新关键资产、查询关键资产等场景。该工程中展示的代码详细描述可查如下链接中业务扩展场景介绍部分。

- [新增关键资产(ArkTS)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-js-add.md)
- [删除关键资产(ArkTS)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-js-remove.md)
- [更新关键资产(ArkTS)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-js-update.md)
- [查询关键资产(ArkTS)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-js-query.md)
- [查询需要用户的关键资产(ArkTS)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-js-query-auth.md)
- [管理群组关键资产(ArkTS)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-js-group-access-control.md)
- [同步（备份恢复）关键资产(ArkTS)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-js-sync.md)

### 效果预览

| 首页效果图                                                   | 执行结果图                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="./screenshots/AssetStoreArkTS1.png" style="zoom: 50%;" /> | <img src="./screen


---
## asset-store-ndk
> 本示例主要展示了Asset Store Kit开发指导(C/C++)中新增关键资产、删除关键资产、更新关键资产、查询关键资产等场景。

源码: https://gitcode.com/HarmonyOS_Samples/asset-store-ndk

# Asset Store Kit开发指导(C/C++)

### 介绍

Asset Store Kit（关键资产存储开发套件）包含了关键资产存储服务（ASSET）开放的接口能力集合，提供了用户短敏感数据的安全存储及管理能力。其中，短敏感数据可以是密码类（账号/密码）、Token类（应用凭据）、关键明文（如银行卡号）等长度较短的用户敏感数据。

本示例主要展示了Asset Store Kit开发指导(C/C++)中新增关键资产、删除关键资产、更新关键资产、查询关键资产等场景。该工程中展示的代码详细描述可查如下链接中业务扩展场景介绍部分。

- [新增关键资产(C/C++)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-native-add.md)
- [删除关键资产(C/C++)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-native-remove.md)
- [更新关键资产(C/C++)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-native-update.md)
- [查询关键资产(C/C++)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-native-query.md)
- [管理群组关键资产(C/C++)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-native-group-access-control.md)
- [同步（备份恢复）关键资产(C/C++)](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/security/AssetStoreKit/asset-native-sync.md)

### 效果预览

| 首页效果图                                                   | 执行结果图                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="./screenshots/AssetStoreNdk1.png" style="zoom: 50%;" /> | <img src="./screenshots/AssetStoreNdk2.png" style="zoom: 50%;" /> |

### 使用说明

1. 运行Index主界面。
2. 页面呈现为上述首页效果图，点击对应文本的按钮可以管理关键资产


---
## audio-capturer-record-pcm
> 该示例用来展示使用AudioCapturer录制PCM音频

源码: https://gitcode.com/HarmonyOS_Samples/audio-capturer-record-pcm

# 基于AudioCapturer录制音频(ArkTS)

## 项目简介

本示例基于AudioCapturer(ArkTS)实现了音频PCM录制。AudioCapturer用于录制PCM（Pulse Code Modulation）音频数据，开发者可以基于本示例实现录制音频PCM，适用于实现更灵活的录制功能。

## 效果预览

| 首页                                                        | 录制页                                                        |
|-----------------------------------------------------------|------------------------------------------------------------|
| <img src="screenshots/devices/MainPage.png" width=320>    | <img src="screenshots/devices/RecorderPage.gif" width=320> |

## 使用说明

1. 打开应用，点击录制按钮进行音频录制。
2. 完成录制后返回，点击音频进行播放。

## 工程目录

```
├──ets                                   // UI层
│  ├──common                             // 公共模块
│  │  └──Constants.ets                   // 参数常量
│  ├──components                  
│  │  └──RecordDialog.ets                // 录制弹窗页面
│  ├──controller                         // 控制模块
│  │  ├──AudioCapturerController.ets     // AudioCapturer音频采集类
│  │  └──AudioRendererController.ets     // AudioRenderer播放类
│  ├──entryability                       // 应用入口函数
│  │  └──EntryAbility.ets
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──model
│  │  └──RecordFileInfo.ets              // 录制文件实体
│  ├──pages
│  │  └──Index.ets                       // 首页
│  └──utils                              // 组件模块
│     ├──BackgroundTaskUtil.ets          // 后台任务工具类
│     ├──Logger.ets                      // 日志工具类
│     ├──PermissionUtil.ets              // 权限工具类
│     └──StringUtil.ets           


---
## audio-codec
> 基于系统能力的音频编解码示例

源码: https://gitcode.com/HarmonyOS_Samples/audio-codec

# 基于OH_AVCodec编解码能力实现音频编解码

## 项目简介
本示例基于OH_AVCodec编解码能力和OH_Audio能力，实现音频的播放、压缩、转换和录制等功能。通过调用Native侧的音频采集器实现音频的录制，通过编码器，解码器，以及封装和解封装，实现音频的播放和转码。基于本示例可帮助应用开发需要编解码进行音频播放和录制的场景。

- 音频播放的主要流程：选择本地音频->解封装->解码->播放
- 音频转码的主要流程：选择本地音频->解封装->解码->编码->封装->保存文件到本地
- 音频录制的主要流程：麦克风采集->编码->封装->保存文件到本地

## 效果预览
| 应用主界面                              | 应用使用展示                             |
|------------------------------------|------------------------------------|
| <img src='screenshots/device/1.png' width=320> | <img src='screenshots/device/2.gif' width=320> | 


## 使用说明

### 录制

1. 点击“录制”按钮，弹出是否允许“AudioCodec”访问你的麦克风，点击“允许”。
2. 点击“允许”后，弹出选择录制格式，选好需要录制的格式后，弹出目标保存格式，选好保存格式后，弹出选择保存文件路径和文件名。
3. 点击“暂停”图标暂停录制，点击“继续”图标继续录制，再次点击红色图标终止录制。
4. 终止录制后，弹出是否保存到本地，点击“确定”，等待3秒后再退出录制界面。

### 播放
1. 点击“本地音频选择”按钮，选择要播放的音频文件，点击“播放”图标开始播放音频，点击“暂停”图标暂停播放音频。
2. 点击“转码”按钮，弹出转码格式，选好需要转码的格式后后，弹出选择保存文件路径和文件名，点击“确定”，弹出是否保存到本地，点击“确定”。

## 工程目录

```
├──entry/src/main/cpp                    // Native层
│  ├──capbilities
│  │  ├──include
│  │  │  ├──AudioCapturer.h              // 音频采集接口定义
│  │  │  ├──AudioDecoder.h               // 音频解码接口定义
│  │  │  ├──AudioEncoder.h               // 音频编码接口定义
│  │  │  ├──AVCodecSampleError.h         // 日志参数接口定义
│  │  │  ├──Demuxer.h                    // 解封装接口定义
│  │  │  ├──Muxer.h                      // 封装接口定义
│  │  │  ├──SampleCallback.h             // 编解码回调接口定义
│  │  │  └──SampleInfo.h                 // 功能实现公共类 
│  │  └──src 
│  │     ├──AudioCapturer.cpp            // 音频采集实现
│  │     ├──Au


---
## audio-focus
> 本示例基于AudioRender、AudioCapturer、AVPlayer以及CallServiceKit等能力，实现了视频播放、音乐播放以及VoIP语言通话场景。这些场景实现中重点突出了音频流类型选择、音频焦点中断事件处理、AudioSession自定义焦点策略以及AVSession后台播控。开发者可以使用设备上其它三方音频应用体验与本示例之间的音频冲突处理。

源码: https://gitcode.com/HarmonyOS_Samples/audio-focus

# 实现音频焦点管理功能

## 介绍

本示例基于AudioRender、AudioCapturer、AVPlayer以及CallServiceKit等能力，实现了视频播放、短视频播放，嵌入式短视频播放，音乐播放、短音播放、VoIP语言通话、静音播放和同应用多音频流播放场景。这些场景实现中重点突出了音频流类型选择、音频焦点中断事件处理、AudioSession自定义焦点策略以及AVSession后台播控。开发者可以使用设备上其它三方音频应用体验与本示例之间的音频冲突处理。

## 效果图预览

| 首页                                          | 视频播放页                                              | 音乐播放页                                              | 短视频播放页                                             |
|----------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| <img src='./screenshots/home.png' width=320> | <img src='./screenshots/videoScene.png' width=320> | <img src='./screenshots/audioScene.png' width=320> | <img src='./screenshots/shortVideo.png' width=320> |
| 点击按钮后，选择进入不同场景                               | 视频自动播放，被打断后暂停                                      | 音频自动播放，被打断后暂停                                      | 上下滑动切换不同短视频页面                                      |


| 嵌入式短视频播放页                                                  | VoIP语音通话页                                  | VoIP语音拨打页面                                       | 短音播放页面                                            |
|------------------------------------------------------------|--------------------------------------------|--------------------------------------------------|-----------------------------------------------


---
## audio-format-switch
> 本示例主要介绍了AudioRender和AVPlayer、AVPlayer和AVPlayer实例之间如何进行不同音频格式文件的播放切换，且切换后保持播放进度一致，并续播。

源码: https://gitcode.com/HarmonyOS_Samples/audio-format-switch

# 实现音质切换

## 项目简介

本案例实现了音质切换的功能，指导开发者了解在AVPlayer和AudioRenderer之间如何进行切换播放。其中，AVPlayer用于播放MP3、FLAC的音频格式，AudioRenderer用于播放PCM的音频格式。同时，还包含了AudioRenderer播放字节进度与AVPlayer播放时间进度之间的转化。


## 效果预览

| 主页面                                  | 
|--------------------------------------|
| ![](screenshots/MainPage.png) |

## 使用说明
1. 安装进入应用。
2. 点击切换音频格式，音频格式包含MP3、FLAC、PCM三种格式。

## 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  └──Constants.ets                 // 常量
│  ├──components                       // 各模块组件
│  │  └──ControlAreaComponent.ets      // 音频操控区组件
│  ├──entryability
│  │  └──EntryAbility.ets              // Ability的生命周期回调内容
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets        // EntryBackupAbility的生命周期回调内容
│  ├──model                        
│  │  └──SongData.ets                  // 歌曲实体
│  ├──pages                             
│  │  └──Index.ets                     // 首页
│  ├──player                             
│  │  ├──AudioRendererController.ets   // AudioRenderer播放控制
│  │  ├──AVPlayerController.ets        // AVPlayer播放控制
│  │  └──PlayerController.ets          // 整体播放控制
│  └──utils
│     ├──ColorTools.ets                // 背景颜色工具类
│     ├──Logger.ets                    // 日志工具类
│     └──MediaTools.ets                // 媒体工具类
└──entry/src/main/resources            // 应用静态资源目录
```

## 具体实现
1. 通过AVPlayer实现播放MP3、FLAC的功能，包括AVPlayer初始化、播放、暂停等功能。
2. 通过AudioRenderer实现播放PCM的功能，包括AudioRenderer初始化、播放、暂停等功能。
3. 记录AVPlayer与AudioRenderer的当前播放的进度。其中，AVPlayer记录的为时间进度，AudioRend


---
## audio-haptic-sound-vibration-collaboration
> 该示例展示了AudioHaptic音振协同播放

源码: https://gitcode.com/HarmonyOS_Samples/audio-haptic-sound-vibration-collaboration

# AudioHapticPlay

#### 介绍
该示例展示了AudioHaptic音振协同播放

#### 软件架构
软件架构说明


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)



---
## audio-in-ear-monitor
> 该示例包含了软件音频耳返和硬件音频耳返实现方案，帮助开发者实现音频耳返功能。

源码: https://gitcode.com/HarmonyOS_Samples/audio-in-ear-monitor

# 实现音频耳返

## 项目简介
本示例实现了音频耳返功能，指导开发者了解如何在ArkTS侧通过AudioLoopback能力、在Native侧通过native_audiocapturer结合native_audiorenderer能力开启耳返，以及耳返音量的调节。同时，使用AVRecorder和AVPlayer实现耳返音频的录制和播放。

## 效果预览

| ArkTS侧实现返听                           | Native侧实现返听                                     |
|--------------------------------------|-------------------------------------------------|
| <img src="./screenshots/ArkTS.gif"  width=320> | <img src="./screenshots/Native.gif"  width=320> |


## 使用说明
1. 安装进入应用。
2. 点击进入对应场景页面，点击录制按钮，打开耳返并进行音频录制；点击暂停/继续按钮，暂停/继续耳返音频录制；点击完成按钮，跳转页面进行音频播放。 
    
    a. AudioLoopback实现耳返，仅支持有线耳机。

    b. native_audiocapturer+native_audiorenderer实现耳返，支持有线耳机和蓝牙耳机。

## 工程目录
```
├──entry/src/main/cpp                    // Native层
│  ├──common
│  │  └──SampleInfo.h                    // 功能实现公共类
│  ├──types
│  │  └──libentry
│  │     ├──index.d.ts                   // 接口定义
│  │     └──oh-package.json5             // 配置文件
│  ├──AudioRecording.cpp                 // Native层音频采集及渲染逻辑的实现
│  └──CMakeLists.txt                     // 编译入口 
├──ets                                   // UI层
│  ├──constants
│  │  └──CommonConstants.ets             // 常量
│  ├──controller
│  │  ├──AudioLoopbackController.ets     // AudioLoopback耳返控制
│  │  ├──AVPlayerController.ets          // AVPlayer播放控制
│  │  └──RecorderController.ets          // AVRecorder录制控制
│  ├──entryability                       
│  │  └──EntryAbility.ets                // 程序入口类
│  ├──entrybackupability            
│  │  └──EntryBackupAbilit


---
## audio-interaction
> 本场景解决方案主要面向前台音频开发人员。指导开发者基于AudioRenderer开发音频播控功能。功能包括后台播放、和播控中心的交互、适配不同类型的焦点打断策略、切换路由发声设备、切换输出设备等基础音频常见功能。

源码: https://gitcode.com/HarmonyOS_Samples/audio-interaction

# 音频播放交互场景

## 简介

本场景解决方案主要面向前台音频开发人员。指导开发者基于AudioRenderer开发音频播控功能，AudioRenderer用于播放PCM（Pulse Code Modulation）音频数据，播放其他格式的音频文件会产生杂音。功能包括后台播放、和播控中心的交互、适配不同类型的焦点打断策略、切换路由发声设备、切换输出设备等基础音频常见功能。

## 使用说明

1. 播放功能：运行工程，进入首页后，点击底部播放按钮，可播放音乐。
2. 切歌功能：播放按钮两侧有切歌按钮，点击切换上一首下一首。
3. 进度跳转功能：推动播放按钮上面的播放条，可以调整歌曲进度。
4. 循环模式：点击进度条上部，左侧第一个图标，可以切换不同播放模式，支持的模式有“顺序播放”、“单曲循环”、“随机播放”。
5. 歌单列表：点击进度条上部，左侧第二个图标，可以打开歌曲列表，点击歌曲名称，可以切换播放歌曲。
6. 静音播放：点击进度条上部，左侧第三个图标，可以打开静音播放功能。
7. 收藏：点击点击进度条上部，左侧第三个“爱心”图标，将歌曲变成已收藏状态，可以同步至播控中心。
8. 点击右上角图标，可以切换音频的输出设备。

## 效果图预览

| 主页面 | 歌词页                                                    |
|--|--------------------------------------------------------|
| <img src="./screenshots/device/main.png" width="320"> | <img src="./screenshots/device/lyric.png" width="320"> |

## 工程主要模块结构

```
├──entry/src/main/ets/
│  ├──common
│  │   ├──constants                     // 常量
│  │   └──utils                         // 工具
│  ├──components                        // 各模块组件
│  │   ├──ControlAreaComponent.ets      // 音频操控区组件
│  │   ├──LyricsComponent.ets           // 歌词组件
│  │   ├──MusicInfoComponent.ets        // 音乐内容组件
│  │   ├──PlayerInfoComponent.ets       // 播控内容区组件
│  │   └──TopAreaComponent.ets          // 顶部区域组件
│  ├──dataSource                        // 歌单数据
│  │   ├──SongDataSource.ets            // 歌曲数据
│  │   └──SongListData.ets              // 歌曲列表数据
│  ├──entryability
│  │   └──EntryAbility.ets              // Ability的生命周期回调内容
│  ├──entrybackupability
│  │   └──EntryBackupAbility


---
## audio-native
> 本示例主要展示音频低时延录制和播放的相关功能。

源码: https://gitcode.com/HarmonyOS_Samples/audio-native

# 基于AudioCapturer录制音频(C++)

## 项目简介

本示例基于OH_Audio的能力，在C/C++侧实现了音频低时延录制功能，录制使用了音频采集器AudioCapturer，参考本示例可学习OH_Audio的使用，帮助应用开发音频录制场景。

## 效果预览

| 主页                                                    | 录制页面                                                      |
|-------------------------------------------------------|-----------------------------------------------------------|
| <img src="screenshots/device/MainPage.png" width=320> | <img src="screenshots/device/RecorderPage.gif" width=320> |

## 使用说明

1. 弹出麦克风权限访问提示框，点击“允许”，如果点击"禁止"则不可进行录制，需要用户去设置页面给应用授权后方可正常录制。
2. 点击录制按钮，开始录制，录音时间开始计时。
3. 点击暂停按钮，暂停录制，录音时间也停止计时。
4. 点击继续按钮，继续录制，录音时间继续计时。
5. 停止录制后，会生成录制结果，点击播放按钮即可播放。

## 工程目录

```
├──entry/src/main/cpp/  
│  ├──types
│  │  └──libentry
│  │     ├──index.d.ts                   // 接口导出
│  │     └──oh-package.json5             // 配置管理文件
│  ├──AudioRecording.cpp                 // 调用native接口
│  └──CMakeLists.txt                     // 编译脚本
├──entry/src/main/ets                    // UI层
│  ├──common                             // 公共模块
│  │  └──Constants.ets                   // 参数常量
│  ├──components                  
│  │  └──RecordDialog.ets                // 录制弹窗页面
│  ├──entryability                       // 应用入口函数
│  │  └──EntryAbility.ets
│  ├──model
│  │  └──RecordFileInfo.ets              // 录制文件实体
│  ├──pages
│  │  └──Index.ets                       // 首页
│  └──utils                              // 组件模块
│     ├──BackgroundTaskUtil.ets          // 后台任务工具类
│     ├──Logger.ets   


---
## audio-playing-sample
> 该示例用于展示媒体子系统各类音频播放解决方案，包括AudioRenderer播放PCM音频、OHAudio播放PCM音频、AVPlayer播放格式化音频、低功耗播放器播放音频以及SoundPool播放短音等。

源码: https://gitcode.com/HarmonyOS_Samples/audio-playing-sample

# AudioPlayingSample

#### 介绍
该示例用于展示媒体子系统各类音频播放解决方案，包括AudioRenderer播放PCM音频、OHAudio播放PCM音频、AVPlayer播放格式化音频、低功耗播放器播放音频以及SoundPool播放短音等。

#### 软件架构
软件架构说明


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)



---
## audio-renderer-play-pcm
> 该示例用于AudioRenderer播放PCM音频。

源码: https://gitcode.com/HarmonyOS_Samples/audio-renderer-play-pcm

# 基于AudioRenderer播放PCM音频

## 项目简介

本场景解决方案主要面向前台音频开发人员。指导开发者基于AudioRenderer开发音频播放功能，AudioRenderer用于播放PCM（Pulse Code
Modulation）音频数据，播放其他格式的音频文件会产生杂音。功能包括后台播放、和播控中心的交互、适配不同类型的焦点打断策略、切换输出设备、倍数播放、音量调节等基础音频常见功能。

## 使用说明

1. 播放功能：运行工程，进入首页后，点击底部播放按钮，可播放音乐。
2. 切歌功能：播放按钮两侧有切歌按钮，点击切换上一首下一首。
3. 进度跳转功能：推动播放按钮上面的播放条，可以调整歌曲进度。
4. 循环模式：点击进度条上部，左侧第一个图标，可以切换不同播放模式，支持的模式有“顺序播放”、“单曲循环”、“随机播放”。
5. 歌单列表：点击进度条上部，左侧第二个图标，可以打开歌曲列表，点击歌曲名称，可以切换播放歌曲。
6. 静音播放：点击进度条上部，左侧第三个图标，可以打开静音播放功能。
7. 倍数设置：点击进度条上部，左侧第四个图标，可以调整歌曲播放速度。
8. 音量设置：点击进度条上部，左侧第五个图标，可以调整歌曲播放音量。
9. 收藏：点击页面“爱心”图标，将歌曲变成已收藏状态，可以同步至播控中心。

## 效果预览

| 主页面                                                | 歌单列表                                                  | 倍速设置                                               | 音量设置                                                |
|----------------------------------------------------|-------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------|
| <img src="screenshots/device/index.png" width=320> | <img src="screenshots/device/songList.png" width=320> | <img src="screenshots/device/speed.png" width=320> | <img src="screenshots/device/volume.png" width=320> |

## 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  ├──constants                                        // 常量
│  │  │  ├──BreakpointConstants.ets                       // 断点常量
│  │  │  ├──ContentConstants.ets                          // 内容常量
│  │  │  ├──


---
## audio-ripple-animation
> 实现音频播放、音频录制的波纹

源码: https://gitcode.com/HarmonyOS_Samples/audio-ripple-animation

# 实现音频动效

## 项目简介

本示例基于AudioRenderer的播放能力和AudioCapturer的录制能力，分别实现了音频录制的动效和音频播放的动效。通过实时获取音频的位深，再计算当前音频的分贝，最后绘制对应的动画。基于本示例可帮助开发者掌握实现音频动效。

## 效果预览
| 应用首页                                           | 音频录制                                         | 音频播放                                       | 
|------------------------------------------------|----------------------------------------------|--------------------------------------------|
| <img src="screenshots/MainPage.png" width=320> | <img src="screenshots/record.gif" width=320> | <img src="screenshots/play.gif" width=320> |


## 使用说明

1.  在弹出麦克风的权限后，点击授权麦克风权限。
2.  点击录制的按钮，即可在音频录制的同时显示音频频谱动效。
3.  在音频列表中，点击对应的音频，播放音频的同时显示音频频谱动效。

## 工程目录
```
├──entry/src/main/ets/
│  ├──common
│  │  ├──Constants.ets                                     // 公共常量类
│  │  └──RecordFileInfo.ets                                // 录制文件实体
│  ├──components                  
│  │  ├──PlayDialog.ets                                    // 播放弹窗页面
│  │  └──RecordDialog.ets                                  // 录制弹窗页面
│  ├──entryability                                         // 应用的入口
│  │  └──EntryAbility.ets                                  // 入口函数类
│  ├──entrybackupability                                   // 应用的后台
│  │  └──EntryBackupAbility.ets                            // 后台管理类
│  ├──manager                                   
│  │  ├──AudioCapturerManager.ets                          // 音频采集管理
│  │  └──AudioRendererManager.ets                          // 音频播放管理
│


---
## audio-volume-management
> 该示例展示了如何进行音频音量管理

源码: https://gitcode.com/HarmonyOS_Samples/audio-volume-management

# 音频流音量管理

## 项目简介

本案例展示如何获取音量、设置音量、使用手势调节音量、自定义音量面板和如何屏蔽音量键。


## 效果预览
<img src="./screenshots/device/screenshot.png" width="320">

## 使用说明
1. 安装进入应用。
2. 进入播放页后，点击播放按钮播放音乐。点击右上角图标进入音量设置，点击禁用音量键的开关组件可禁用系统音量键，滑动音频流音量和应用音量的滑动条可增大或减小音乐的音量。

## 工程目录

```
├──entry/src/main/ets/
│  ├──common                           // 各模块组件
│  │  └──CommonConstants.ets           // 常量类
│  ├──components                       // 各模块组件
│  │  ├──AVVolumePanelView.ets         // 系统音量条组件
│  │  ├──ControlAreaComponent.ets      // 播控区域组件
│  │  ├──SystemVolumePanelView.ets     // 自定义系统音量条组件
│  │  └──VolumePanelView.ets           // 自定义音量条组件
│  ├──entryability
│  │  └──EntryAbility.ets              // Ability的生命周期回调内容
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets        // EntryBackupAbility的生命周期回调内容
│  ├──model                        
│  │  └──SongData.ets                  // 歌曲实体
│  ├──pages
│  │  ├──Index.ets                     // 首页                             
│  │  └──Player.ets                    // 播放页
│  ├──player                             
│  │  ├──AudioRendererController.ets   // AudioRenderer播放控制
│  │  └──AudioVolumeController.ets     // AudioVolumeManager音量管理
│  ├──utils
│  │  ├──ColorTools.ets                // 背景颜色工具类
│  │  ├──Logger.ets                    // 日志工具类
│  │  └──MediaTools.ets                // 媒体工具类
│  └──viewModel
│     └──PlayerViewModel.ets           // 播放页数据
└──entry/src/main/resources            // 应用静态资源目录
```

## 具体实现
1. 通过audioVolumeManager管理系统音量，滑动自定义音量条，


---
## avcastpicker-for-call
源码: https://gitcode.com/HarmonyOS_Samples/avcastpicker-for-call

# 实现自定义通话设备图标样式

### 介绍

本示例基于AVCastPicker组件，实现通话过程中音频输出设备切换功能，并使用customPicker参数实现自定义音频输出设备图标。

### 效果预览

| 应用主界面                                  | 默认图标界面                                   | 自定义图标界面                                 |           
|----------------------------------------|------------------------------------------|-----------------------------------------|
| ![image](screenshots/device/index.png) | ![image](screenshots/device/default.png) | ![image](screenshots/device/custom.png) |

##### 使用说明

1.进入应用为场景选择界面，有默认样式和自定义样式两个按钮，点击可分别进入相应界面。

2.默认样式组件界面初始有两个按钮，点击第一个可播放模拟通话的音频，同时出现最右侧的设备切换按钮可进行设备切换，播放时点击第二个按钮可结束播放。

3.自定义样式组件界面功能与默认样式组件界面一致，但可以看到音频输出设备图标的样式和颜色不同。

### 工程目录

```             
├──entry/src/main/ets                      // 代码区
│  ├──common                         
│  │  ├──constants                       
│  │  │  └──Contants.ets                   // 公共常量类
│  │  └──utils                       
│  │     └──Logger.ets                     // 日志类
│  ├──entryability                   
│  │  └──EntryAbility.ets                  // 程序入口类
│  ├──entrybackupability                   
│  │  └──EntryBackupAbility.ets
│  ├──pages                   
│  │  └──Index.ets                         // 首页-场景选择
│  ├──view
│  │  ├──CustomPickerComponent.ets         // 自定义样式页面组件         
│  │  └──DefaultPickerComponent.ets        // 系统默认样式页面组件        
│  └──viewmodel                         
│     └── AudioCapabilityManager.ets       // 音频能力管理类
└──resources                       


---
## avcodec-buffer-mode
> 基于buffer模式进行视频转码

源码: https://gitcode.com/HarmonyOS_Samples/avcodec-buffer-mode

# 基于Buffer模式进行视频转码

### 介绍
本实例基于AVCodec能力，实现了Buffer模式下的视频转码功能。通过调用Native侧的编码器，解码器，以及封装和解封装功能，完成从视频解封装、解码、编码、封装的过程。基于本实例可以帮助开发者理解Buffer模式，并通过Buffer模式进行转码。

### 效果预览
| 应用主界面                                                      |
|------------------------------------------------------------|
| ![AVCodec_Index.png](screenshots/device/AVCodec_Index.png) |

### 使用说明
1. 进入首页后，配置视频转码的参数。
2. 点击开始转码后即可开始转码，等待转码完成。
3. 在转码完成后，跳转到下一个页面，可以查看转码完成的视频。

### 工程目录

```       
├──entry/src/main/cpp                 // Native层
│  ├──capbilities                     // 能力接口和实现
│  │  ├──include                      // 能力接口
│  │  ├──Demuxer.cpp                  // 解封装实现
│  │  ├──Muxer.cpp                    // 封装实现
│  │  ├──VideoDecoder.cpp             // 视频解码实现
│  │  └──VideoEncoder.cpp             // 视频编码实现
│  ├──common                          // 公共模块
│  │  ├──dfx                          // 日志
│  │  ├──SampleCallback.cpp           // 编解码回调实现   
│  │  ├──SampleCallback.h             // 编解码回调定义
│  │  └──SampleInfo.h                 // 功能实现公共类  
│  ├──sample                          // Native层
│  │  └──transcoding                  // Native层转码接口和实现
│  │     ├──Transcoding.cpp           // Native层转码功能调用逻辑的实现
│  │     ├──Transcoding.h             // Native层转码功能调用逻辑的接口
│  │     ├──TranscodingNative.cpp     // Native层转码的入口
│  │     └──TranscodingNative.h         
│  ├──types                           // Native层暴露上来的接口
│  │  └──libtranscoding               // 转码模块暴露给UI层的接口
│  └──CMakeLists.txt            


---
## avplayer-basic-control
> AVPlayer自有基础播控能力，主要包括播放、暂停、跳转播放、静音播放、循环播放、窗口缩放模式设置、倍速设置、音量设置等场景。

源码: https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control

# 基于AVPlayer实现视频基础播控功能

## 项目简介

本示例主要展示了如何基于AVPlayer系统播放器实现播放本地视频相关功能，指导开发者实现视频加载、播放、暂停、退出；跳转播放；静音播放；循环播放；窗口缩放模式设置；倍速设置；音量设置；字幕挂载等开发场景。

## 效果预览

| 播放                                                              | 暂停                                       | 倍速弹窗                                               |
|-----------------------------------------------------------------|------------------------------------------|----------------------------------------------------|
| <img src='screenshots/devices/playing.png' width=320/> | <img src='screenshots/devices/pause.png' width=320/> |<img src='screenshots/devices/speed_dialog.png' width=320/> |

| 静音设置                                                 | 音量设置                                            | 窗口缩放模式设置                                           |
|------------------------------------------------------|-------------------------------------------------|----------------------------------------------------|
| <img src='screenshots/devices/set_media_muted.png' width=320/> | <img src='screenshots/devices/set_volume.png' width=320/> | <img src='screenshots/devices/scale_fit.png' width=320/> |

## 使用说明

1. 下载sample，编译运行；
2. 运行成功后，视频自动开始播放；
3. 点击视频界面，唤起视频操作面板，再次点击操作面板消失，如果不做任何操作操作界面会5s自动消失;
4. 点击暂停/播放按钮，控制视频暂停播放;
5. 滑动视频进度条，视频跳转到指定位置,在视频中间会出现时间进度方便用户查看视频进度;
6. 点击倍速，可以选择1.0、1.25、1.75、2.0进行倍速调节;
7. 点击静音按钮，可以设置静音模式播放;
8. 点击窗口缩放模式按钮，可以选择拉伸至与窗口等大、缩放至最短边填满窗口;
9. 长按屏幕，控制视频2.0倍速播放;
10. 上下滑动屏幕，可以设置视频播放音量；
11. 视频下方显示字幕，并可以点击语言切换按钮切换字幕;
12. 视


---
## avplayer-embeded-short-video
> 基于AVPlayer播放嵌入式短视频，主要包括视频列表切换（进度保持）、列表中第一个视频自动播放、基本播控、焦点管理、视频首帧显示（用来显示列表中每个视频）等场景。

源码: https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video

# 基于AVPlayer实现嵌入式短视频播放

## 项目简介

本示例适用于嵌入式短视频播放类应用的开发，通过[AVPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer)和[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)组件，使用[LazyForEach()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach)方法进行数据懒加载，根据列表滑动自动切换播放，并在点击进入视频详情页面时继续播放。

## 效果预览

<img src="screenshots/device/result.png" style="width:320px">

## 使用说明

1. 向下滑动列表，自动播放首个可见视频。

2. 点击视频跳转到视频详情页，继续播放当前视频。

## 工程目录

```
├──entry/src/main/ets
│  ├──common
│  │  ├──constants
│  │  │  └──Constants.ets               // 公共常量
│  │  └──utils
│  │     ├──AppRouter.ets               // 页面跳转方法定义
│  │     ├──GlobalContext.ets           // 公共方法
│  │     ├──TimeUtils.ets               // 时间工具
│  │     └──WindowUtil.ets              // 系统处理工具
│  ├──component
│  │  ├──AVVolumePanelView.ets          // 音量控制组件
│  │  ├──BulletCommentView.ets          // 弹幕展示组件
│  │  ├──CaptionFontView.ets            // 字幕字体设置组件
│  │  ├──LanguageDialog.ets             // 字幕语言切换组件
│  │  ├──ScaleDialog.ets                // 视频缩放组件
│  │  ├──ScreenBrightnessView.ets       // 亮度控制组件
│  │  ├──SpeedDialog.ets                // 倍速播放组件
│  │  ├──VideoDetail.ets                // 无缝转场组件
│  │  └──VideoList.ets                  // 视频列表组件
│  ├──controller
│  │  ├──AvPlayerController.ets         // avplayer公共控制类
│  │  └──PiPWindowController.ets        // 画中画公共控制类
│  ├──entrya


---
## avplayer-long-video
> 基于AVPlayer播放长视频，主要有基本播控、精准跳转、倍速播放、音量控制、亮度控制、焦点管理、前后台感知、弹幕发送与显示、字幕挂载、视频截图、画中画播放等场景。

源码: https://gitcode.com/HarmonyOS_Samples/avplayer-long-video

# 基于AVPlayer实现长视频播放

## 项目简介

本文介绍了如何基于AVPlayer系统播放器实现长视频播放应用。

本文指导开发者实现基本播控、亮度控制、焦点管理、前后台感知、弹幕发送与显示、字幕挂载、视频截图、画中画、视频首帧显示等开发场景。

## 效果预览

|                           应用首页                           |                         画中画                         |                            播控中心                             |                           闹铃打断                           |
|:--------------------------------------------------------:|:---------------------------------------------------:|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| <img src="screenshots/device/mainpage.png" height='320'> | <img src="screenshots/device/pip.png" height='320'> | <img src="screenshots/device/backcontrol.png" height='320'> | <img src="screenshots/device/interrupt.png" height='320'> |

|                           横屏页-亮度调节                           |                         横屏页-弹幕输入                          |
|:--------------------------------------------------------:|:---------------------------------------------------:|
| <img src="screenshots/device/screenbright.png" width='320'> | <img src="screenshots/device/bulletcomment.png" width='320'> |

|                        横屏页-字幕设置                         |                         横屏页-视频截图                         |
|:-------------------------------------------------------:|:--------------------------------------------------------:|
| <img src="screenshots/device/subtitle.png" 


---
## avplayer-online-video
> 基于AVPlayer播放网络视频，主要包括基本播控、播放网络视频、网络视频缓冲条、网络视频边缓冲边播放等场景。

源码: https://gitcode.com/HarmonyOS_Samples/avplayer-online-video

# 基于AVPlayer播放网络视频实践
## 项目简介    
 本示例主要展示了HarmonyOS中如何基于AVPlayer系统播放器实现网络视频播放，指导开发者实现以下开发场景
- 网络视频URL设置
- 基本播控
- 网络视频缓冲条
- 网络视频边缓冲边播放
## 效果预览
| 预设URL视频列表                            | 手动输入URL                              | URL视频播放                              | 带缓冲条网络视频播放                           |                         
|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
| ![image](screenshots/device/pv1.png) | ![image](screenshots/device/pv2.png) | ![image](screenshots/device/pv3.png) | ![image](screenshots/device/pv4.png) |
## 使用说明
1. 下载sample，编译运行
2. 主页是个视频列表，视频列表的各项代表各场景，点击列表项，播放视频
3. 点击主页右上角按钮，可设置自定义视频URL，确认进行播放
4. 本示例中M3U8测试资源非公网测试资源，用户可自行修改为自备测试资源: 
   - entry/src/main/ets/model/VideoDataModel.ets:44
   - entry/src/main/resources/rawfile/test.m3u8

## 工程目录
```
├──entry/src/main/ets                           // entry模块
│  ├──common
│  │  ├──constants
│  │  │  └──CommonConstants.ets                 // 常量类
│  │  └──utils
│  │     ├──BackgroundTaskManager.ets           // 后台任务相关工具
│  │     ├──ImageUtil.ets                       // 图片工具
│  │     ├──Logger.ets                          // 日志工具
│  │     └──TimeUtils.ets                       // 时间工具
│  ├──components
│  │  ├──BulletCommentView.ets                  // 弹幕组件
│  │  ├──ExitVideo.ets                          // 退出应用组件
│  │  ├──LanguageDialog.ets                     // 字母语言切换
│  │  ├──ScaleDialog.ets           


---
## avplayer-play-formatted-audio-arkts
> 该示例展示了使用AVPlayer播放格式化音频（ArkTS）

源码: https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-arkts

# 基于AVPlayer播放格式化音频（ArkTS）

## 项目简介
本场景解决方案主要面向前台音频开发人员。指导开发者基于AVPlayer开发音频播放功能，AVPlayer用于播放格式化音频（MP3、WAV、FLAC等）。功能包括后台播放、和播控中心的交互、适配不同类型的焦点打断策略、切换输出设备、倍数播放、音量调节等基础音频常见功能。

## 使用说明
1. 播放功能：运行工程，进入首页后，点击底部播放按钮，可播放音乐。
2. 切歌功能：播放按钮两侧有切歌按钮，点击切换上一首下一首。
3. 进度跳转功能：推动播放按钮上面的播放条，可以调整歌曲进度。
4. 循环模式：点击进度条上部，左侧第一个图标，可以切换不同播放模式，支持的模式有“顺序播放”、“单曲循环”、“随机播放”。
5. 歌单列表：点击进度条上部，左侧第二个图标，可以打开歌曲列表，点击歌曲名称，可以切换播放歌曲。
6. 静音播放：点击进度条上部，左侧第三个图标，可以打开静音播放功能。
7. 倍数设置：点击进度条上部，左侧第四个图标，可以调整歌曲播放速度。
8. 音量设置：点击进度条上部，左侧第五个图标，可以调整歌曲播放音量。
9. 收藏：点击页面“爱心”图标，将歌曲变成已收藏状态，可以同步至播控中心。

## 效果预览

| 主页面                                                | 歌词页                                                | 歌单列表                                                  | 倍数设置                                               |
|----------------------------------------------------|----------------------------------------------------|-------------------------------------------------------|----------------------------------------------------|
| <img src="screenshots/device/index.png" width=320> | <img src="screenshots/device/lyric.png" width=320> | <img src="screenshots/device/songList.png" width=320> | <img src="screenshots/device/speed.png" width=320> |

## 工程目录
```
├──entry/src/main/ets/
│  ├──common
│  │  ├──constants                                        // 常量
│  │  │  ├──BreakpointConstants.ets                       // 断点常量
│  │  │  ├──ContentConstants.ets                          // 内容常量
│  │  │  ├──LyricConst.ets                           


---
## avplayer-play-formatted-audio-cpp
> 该示例展示了使用AVPlayer播放格式化音频（C++）

源码: https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp

# 基于AVPlayer播放格式化音频（C++）

## 项目简介
本场景解决方案主要面向前台音频开发人员。指导开发者基于AVPlayer的cpp方法开发音频播放功能，AVPlayer用于播放格式化音频（MP3、WAV、FLAC等）。功能包括后台播放、和播控中心的交互、适配不同类型的焦点打断策略、切换输出设备、倍数播放、音量调节等基础音频常见功能。

## 使用说明
1. 播放功能：运行工程，进入首页后，点击底部播放按钮，可播放音乐。
2. 切歌功能：播放按钮两侧有切歌按钮，点击切换上一首下一首。
3. 进度跳转功能：推动播放按钮上面的播放条，可以调整歌曲进度。
4. 循环模式：点击进度条上部，左侧第一个图标，可以切换不同播放模式，支持的模式有“顺序播放”、“单曲循环”、“随机播放”。
5. 歌单列表：点击进度条上部，左侧第二个图标，可以打开歌曲列表，点击歌曲名称，可以切换播放歌曲。
6. 静音播放：点击进度条上部，左侧第三个图标，可以打开静音播放功能。
7. 倍数设置：点击进度条上部，左侧第四个图标，可以调整歌曲播放速度。
8. 音量设置：点击进度条上部，左侧第五个图标，可以调整歌曲播放音量。
9. 收藏：点击页面“爱心”图标，将歌曲变成已收藏状态，可以同步至播控中心。

## 效果预览

| 主页面                                                | 歌单列表                                                  | 倍数设置                                               | 音量设置                                                |
|----------------------------------------------------|-------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------|
| <img src="screenshots/device/index.png" width=320> | <img src="screenshots/device/songList.png" width=320> | <img src="screenshots/device/speed.png" width=320> | <img src="screenshots/device/volume.png" width=320> |

## 工程目录
```
├──entry/src/main/ets/
│  ├──common
│  │  ├──constants                                        // 常量
│  │  │  ├──BreakpointConstants.ets                       // 断点常量
│  │  │  ├──ContentConstants.ets                          // 内容常量
│  │  │  ├──LyricConst.ets                    


---
## avplayer-short-video
> 基于AVPlayer播放短视频，主要展示视频列表切换、横竖屏切换等场景。

源码: https://gitcode.com/HarmonyOS_Samples/avplayer-short-video

# 基于AVPlayer实现短视频播放

## 项目简介

本示例基于AVPlayer系统播放器实现，适用于短视频播放类应用的开发，指导开发者实现短视频流畅切换，提炼一套可复制的方案，帮助开发者交付极速、流畅的短视频播放体验。

## 效果预览
<img src="./screenshots/devices/Index.webp" width="320">

## 功能特性
1. 本示例包含基本播控、静音播放、循环播放、倍数播放和字幕挂载功能，具体效果可参考[基于AVPlayer基本播放](https://gitee.com/harmonyos_samples/avplayer-basic-control/blob/master/README.md)
2. 本示例包含焦点管理、横竖屏切换与旋转感知和前后台感知，具体效果可参考[基于AVPlayer长视频播放](https://gitee.com/harmonyos_samples/avplayer-long-video/blob/master/README.md)

## 使用说明
1. 打开应用，可以上下滑动**流畅切换视频**，且支持断点持播功能，切回原视频会从之前的位置继续播放。

## 工程目录
```
├──entry/src/main/
├──ets
│  ├──common
│  │  ├──contanstants
│  │  │  └──CommonConstants.ets        // 公共常量
│  │  └──utils
│  │     ├──Logger.ets                 // 日志工具
│  │     ├──WindowUtil.ets             // 窗口工具
│  │     └──TimeUtils.ets              // 时间工具
│  ├──component
│  │  ├──LanguageDialog.ets            // 语言切换弹窗组件
│  │  ├──VideoPlayer.ets               // 视频播放组件
│  │  ├──SpeedDialog.ets               // 播放倍数弹窗组件
│  │  └──VideoToolBar.ets              // 视频工具栏
│  ├──controller
│  │  └──AvPlayerController.ets        // AVPlayer控制类
│  ├──entryability
│  │  └──EntryAbility.ets              // 入口函数
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──model
│  │  ├──AVDataSource.ets              // 数据操作类
│  │  ├──DataModel.ets                 // 数据源
│  │  └──VideoData.ets                 // 数据类型
│  └──pages
│     ├──AVPlayerView.ets              // 视频播放页
│     └──Index.ets                     // 首页 
└──resources                 


---
## avrecorder-record-formatted-audio-arkts
> 该示例展示了使用AVRecorder录制格式化音频（ArkTS）

源码: https://gitcode.com/HarmonyOS_Samples/avrecorder-record-formatted-audio-arkts

# 基于AVRecorder录制音频（ArkTS）

## 项目简介

本示例基于AVRecorder(ArkTS)实现了音频录制。AVRecorder集成了音频采集、音频编码、音视频封装功能，开发者可以基于本示例实现音频录制，适用于实现简单音频录制并直接得到本地媒体文件的场景。

## 效果预览

| 首页                                                        | 录制页                                                        |
|-----------------------------------------------------------|------------------------------------------------------------|
| <img src="screenshots/devices/MainPage.png" width=320>    | <img src="screenshots/devices/RecorderPage.gif" width=320> |

## 使用说明

1. 打开应用，点击录制按钮进行音频录制。
2. 完成录制后返回，点击音频进行播放。

## 工程目录

```
├──ets                                   // UI层
│  ├──common                             // 公共模块
│  │  └──Constants.ets                   // 参数常量
│  ├──components                  
│  │  └──RecordDialog.ets                // 录制弹窗页面
│  ├──controller                         // 控制模块
│  │  ├──AVPlayerController.ets          // AVplayer播放类
│  │  └──RecorderController.ets          // Recorder录制类
│  ├──entryability                       // 应用入口函数
│  │  └──EntryAbility.ets
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──model
│  │  └──RecordFileInfo.ets              // 录制文件实体
│  ├──pages
│  │  └──Index.ets                       // 首页
│  └──utils                              // 组件模块
│     ├──BackgroundTaskUtil.ets          // 后台任务工具类
│     ├──Logger.ets                      // 日志工具类
│     ├──PermissionUtil.ets              // 权限工具类
│     └──StringUtil.ets                  // 字符串工具类
├──resources


---
## avrecorder-record-formatted-audio-cpp
> 该示例展示了使用AVRecorder录制格式化音频（C++）

源码: https://gitcode.com/HarmonyOS_Samples/avrecorder-record-formatted-audio-cpp

# 基于AVRecorder录制音频（C++）

## 项目简介

本示例基于AVRecorder(C++)实现了音频文件录制。AVRecorder集成了音频采集、音频编码、音视频封装功能，开发者可以基于本示例实现音频文件录制，适用于实现简单音频录制并直接得到本地媒体文件的场景。

## 效果预览

| 首页                                                        | 录制页                                                        |
|-----------------------------------------------------------|------------------------------------------------------------|
| <img src="screenshots/devices/MainPage.png" width=320>    | <img src="screenshots/devices/RecorderPage.gif" width=320> |

## 使用说明

1. 打开应用，点击录制按钮进行音频录制。
2. 完成录制后返回，点击音频进行播放。

## 工程目录

```
├──entry/src/main/cpp                    // Native层
│  ├──capbilities                        // 接口能力实现
│  │  ├──AVRecorder.cpp                  // 音频录制实现
│  │  └──AVRecorder.h                    // 音频录制实现
│  ├──types                              // Native层暴露上来的接口
│  │  └──libentry                        // 录制模块暴露给UI层的接口
│  │     ├──index.d.ts                   // 描述C++ API接口行为
│  │     └──oh-package.json5             // 配置.so三方包声明文件的入口及包名
│  ├──CMakeLists.txt                     // 编译入口
│  └──napi_init.cpp                      // Native侧入口
├──ets                                   // UI层
│  ├──common                             // 公共模块
│  │  └──Constants.ets                   // 参数常量
│  ├──components                  
│  │  └──RecordDialog.ets                // 录制弹窗页面
│  ├──controller                         // 控制模块
│  │  └──AvPlayerController.ets          // AVplayer播放类
│  ├──entryability            


---
## avscreen-capture-record-system-audio-arkts
> 该示例展示通过AVScreenCapture内录系统声音（ArkTS）

源码: https://gitcode.com/HarmonyOS_Samples/avscreen-capture-record-system-audio-arkts

# 基于AVScreenCapture录制音频（C++）

## 项目简介

本示例基于AVScreenCapture(C++)实现了音频文件录制。AVScreenCapture可以实现屏幕录制和音频录制，开发者可以基于本示例实现音频文件录制，适用于实现简单音频录制并直接得到本地媒体文件的场景。

## 效果预览

| 首页                                                        | 录制页                                                        |
|-----------------------------------------------------------|------------------------------------------------------------|
| <img src="screenshots/devices/MainPage.png" width=320>    | <img src="screenshots/devices/RecorderPage.gif" width=320> |

## 使用说明

1. 打开应用，点击录制按钮进行音频录制。
2. 完成录制后返回，点击音频进行播放。

## 工程目录

```
├──entry/src/main/cpp                    // Native层
│  ├──capbilities                        // 接口能力实现
│  │  ├──AVScreenCapture.cpp             // 音频录制实现
│  │  └──AVScreenCapture.h               // 音频录制实现
│  ├──types                              // Native层暴露上来的接口
│  │  └──libentry                        // 录制模块暴露给UI层的接口
│  ├──CMakeLists.txt                     // 编译入口
│  └──napi_init.cpp                      // Native侧入口
├──ets                                   // UI层
│  ├──common                             // 公共模块
│  │  └──Constants.ets                   // 参数常量
│  ├──components                  
│  │  └──RecordDialog.ets                // 录制弹窗页面
│  ├──controller                         // 控制模块
│  │  └──AvPlayerController.ets          // AVplayer播放类
│  ├──entryability                       // 应用入口函数
│  │  └──EntryAbility.ets
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──mod


---
## avscreen-capture-screen-record
> 关于录屏的示例代码

源码: https://gitcode.com/HarmonyOS_Samples/avscreen-capture-screen-record

# 基于AVScreenCapture实现录屏功能

### 简介

本示例主要介绍如何基于AVScreenCapture实现屏幕录制，主要包括基于ArkTS方法录屏到文件、基于C/C++方法录屏到文件以及基于C/C++方法录屏转码流三种实现方案。基于该案例，开发者可以掌握AVScreenCapture录屏相关能力。

### 效果预览

<img src="screenshots/device/PreviewImage_ZH.png" width="320">

### 使用说明

在主页面中点击对应按钮会分别跳转到不同场景的页面。在每个场景页面中都包含了一个视频播放区域和一个录制按钮。点击右上角录制按钮，会向用户发起权限申请。用户同意后将会开启屏幕录制，期间可以退出到后台进行录制。然后再次点击录制按钮或者点击屏幕左上角胶囊的停止按钮会停止视频录制。录制完成后页面会进行刷新，并显示录制完成的文件信息。点击播放按钮，会在播放区域播放录制好的视频文件。

### 工程结构

```
├──entry/src/main/cpp                   // C++代码区
│  ├──CAVScreenCaptureToFile            // 基于C/C++方法录屏到文件模块
│  │  ├──CAVScreenCaptureToFile.cpp
│  │  └──CAVScreenCaptureToFile.h      
│  ├──CAVScreenCaptureToStream          // 基于C/C++方法录屏转码流模块
│  │  ├──AudioCapturer.cpp              // 音频录制文件
│  │  ├──AudioCapturer.h
│  │  ├──AudioEncoder.cpp               // 音频编码器文件
│  │  ├──AudioEncoder.h
│  │  ├──CAVScreenCaptureToStream.cpp   // 录屏转码流
│  │  ├──CAVScreenCaptureToStream.h
│  │  ├──Muxer.cpp                      // 复用器文件
│  │  ├──Muxer.h
│  │  ├──SampleInfo.h                   // 自定义数据类型
│  │  ├──VideoEncoder.cpp               // 视频编码器文件
│  │  └──VideoEncoder.h    
│  ├──types
│  │  └──libentry                       // C++接口导出
│  │     ├──Index.d.ts                
│  │     └──oh-package.json5           
│  ├──CMakeLists.txt                    // Cmake配置文件
│  └──napi_init.cpp                     // Native侧代码入口
├──entry/src/main/ets                   // ArkTS代码区                  
│  ├──entryability        
│  │  └──EntryAbility.ets    


---
## bicycle-sharing
> 本示例实现了扫码、地图找车、实况通知等功能，主要用到ScanKit、MapKit、LiveViewKit等能力。

源码: https://gitcode.com/HarmonyOS_Samples/bicycle-sharing

# 基于实况窗和扫码功能实现快捷触达的骑行场景

## 简介

本示例展示了使用实况窗、地图导航、统一扫码服务等技术实现共享单车的使用场景，用户在骑行过程中可以通过实况窗获取骑行状态，为整个骑行流程带来更好的体验。

## 效果展示
![预览图](screenshots/riding.gif)

## 使用说明
1.应用包含找车、扫码解锁、实况窗功能。<br>
2.通过解锁按钮开启实况窗<br>
3.通过还车按钮更新实况窗状态<br>
4.通过立即支付按钮结束流程

## 工程目录
```
├──ets
│  ├──constants
│  │  └──CyclingConstants.ets        //公共常量类
│  ├──entryability  
│  │  ├──EntryAbility.ets
│  │  └──LiveViewLockScreenExtAbility.ets  //沉浸态实况窗扩展ability         
│  ├──liveview  
│  │  ├──LiveNotification.ets       //实况窗通知类
│  │  ├──LiveViewContext.ets        //实况窗内容类
│  │  ├──LiveViewController.ets     //实况窗控制类
│  │  ├──LiveViewDataBuilder.ets    //实况窗数据构建类
│  │  ├──LiveViewEnvironment.ets    //实况窗环境类
│  │  ├──TextCapsuleBuilder.ets     //文本胶囊类
│  │  └──TextLayoutBuilder.ets      //文本扩展区类
│  ├──pages  
│  │  ├──ConfirmUnlock.ets          //解锁页面
│  │  ├──CyclingPage.ets            //首页
│  │  ├──FindBike.ets               //找车页面
│  │  ├──LiveViewLockScreenPage.ets //沉浸态实况窗页面
│  │  ├──Pay.ets                    //支付页面
│  │  ├──PayCompleted.ets           //支付完成页面
│  │  └──Riding.ets                 //骑行中页面
│  └──utils
│     ├──Logger.ets                 //日志工具类
│     ├──MapUtil.etx                //地图工具类
│     └──ScanUtil.ets               //扫码工具类
└──resources                        //应用静态资源目录
```
## 具体实现
1. 地图、定位与路线规划相关使用Map Kit能力实现。
2. 扫码使用Scan Kit能力实现
3. 实况窗使用Live View Kit能力实现

## 相关权限
[实况窗AGC参考配置流程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-preparations)。<br>
[地图定位AGC参考配置流程](https


---
## bottom-drawer-slide-case
> 本示例介绍了利用List实现底部抽屉滑动效果场景，并将界面沉浸式（全屏）显示，及背景地图可拖动。

源码: https://gitcode.com/HarmonyOS_Samples/bottom-drawer-slide-case

# 实现底部抽屉滑动效果

### 介绍

本示例介绍了利用List实现底部抽屉滑动效果场景，使用RelativeContainer和Stack布局，将界面沉浸式（全屏）显示，实现地图拖动功能，开发者可以使用底部抽屉滑动效果。

### 效果图预览

![](screenshots/device/BottomDrawerSlideCase.gif)

##### 使用说明

1. 向上滑动底部列表，支持根据滑动距离进行分阶抽屉式段滑动。

### 具体实现

1. 本示例使用RelativeContainer和Stack布局，实现可滑动列表在页面在底部，且在列表滑动到页面顶部时，显示页面顶部标题栏。
2. 通过对List设置onTouch属性，记录手指按下和离开屏幕纵坐标，判断手势是上/下滑。
3. 根据手指滑动的长度对列表高度进行改变。
4. 在手指滑动结束离开屏幕后，通过判断此时列表高度处于哪个区间，为列表赋予相应的高度。

## 工程目录

```
├──entry/src/main/ets                         // 代码区
│  ├──constants
│  │  └──CommonConstants.ets                  // 公共常量
│  ├──entryability
│  │  └──EntryAbility.ets       
│  ├──model
│  │  └──CommonModel.ets                      // 公共实体类       
│  ├──pages
│  │  └──BottomDrawerSlideCase.ets            // 首页     
│  ├──utils
│  │  ├──ArrayUtil.ets                        // 数组工具类
│  │  ├──GlobalContext.ets                    // 变量工具类
│  │  ├──Logger.ets                           // 日志文件
│  │  ├──SettingItem.ets                      // 图片实体类
│  │  └──WindowModel.ets                      // 窗口管理
│  └──view
│     └──ComComponent.ets                     // 公用子组件
└──entry/src/main/resources                   // 应用资源目录
```


### 相关权限

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## calculator
> 本示例展示了使用ArkTS卡片开发的计算器模型。

源码: https://gitcode.com/HarmonyOS_Samples/calculator

# 基于ArkTS实现卡片计算器功能

### 介绍

本示例基于ArkTS卡片实现了一个卡片计算器，利用ArkTS的优势，卡片的设计注重简洁直观的用户界面，确保操作简便流畅，并且能够快速响应用户的输入。

### 效果预览

| 添加卡片                                             | 卡片预览                                                    | 操作卡片                                             |
|--------------------------------------------------|---------------------------------------------------------|--------------------------------------------------|
| ![CalculatorAdd](screenshots/CalculatorAdd.png) | ![CalculatorPreview](screenshots/CalculatorPreview.png) | ![CalculatorUse](screenshots/CalculatorUse.png) |

### 使用说明

1.长按应用图标，将卡片添加到桌面。

2.对桌面上的卡片进行计算操作。

### 工程目录

```
├──entry/src/main/ets                         // 代码区
│  ├──calc/pages
│  │  └──CardCalc.ets                         // 计算器卡片页面
│  ├──entryability
│  │  └──EntryAbility.ets                     // 程序入口类
│  ├──entryformability
│  │  └──EntryFormAbility.ets                 // 卡片声明周期处理文件
│  ├──model
│  │  └──Logger.ts                            // 日志工具
│  └──pages
│     └──index.ets                            // 首页
├──entry/src/main/resources                   // 应用资源目录
└──module.json5                               // 应用配置文件
```

### 相关权限

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## callkit-samplecode-voipdemo-arkts
> 本示例主要展示了通话服务联合Push Kit、Image Kit，实现了订阅VoipCallUiEvent事件、上报音视频来电、上报通话状态变化等功能。


源码: https://gitcode.com/HarmonyOS_Samples/callkit-samplecode-voipdemo-arkts

# 社交通信-通话服务

### 介绍
本示例主要展示了Call Service Kit（通话服务）相关的功能
使用Call Service Kit、Push Kit、Image Kit等接口，实现了订阅'voipCallUiEvent'事件、上报音视频来电、上报通话状态变化等功能。

### 相关概念
Call Service Kit是华为提供给VoIP类应用的通话相关接口，管理VoIP类应用通话，做到VoIP类应用来电体验一致。

### 相关权限
1. ohos.permission.MICROPHONE，用于在语音通话中，使用麦克风。
2. ohos.permission.CAMERA，用于在视频通话中，使用相机。

### 使用说明
本示例展示了应用接收到服务端推送音视频来电信息后的操作行为。
为模拟服务端的发送音视频通话请求行为，需要您有自己的云服务器，并且结合Push Kit的Token相关内容，进行实际的音视频通话发送及接收操作。

### 效果预览
![锁屏预期效果图](screenshots/device/lock.jpeg) ![未锁屏预期效果图](screenshots/device/unlock.jpeg)

### 工程目录
```bash
├─entry/src/main/ets              // 代码区
│ ├─entryability
│ │ ├─EntryAbility.ets            // 程序入口类
│ │ └─VoipCallAbility.ets         // 事件响应
│ └─model                         // 业务逻辑和工具类
│ | └─CallDataManager.ets         // 通话业务逻辑
│ | └─TypeUtils.ets               // 工具类
│ └─pages                         // 存放页面文件的目录
│   └─Index.ets                   // 主页界面
│   └─VoipCallPage.ets            // 通话界面
└─entry/src/main/resources        // 应用资源目录
```

### 具体实现
本示例主要展示了应用调用通话服务相关接口等具体操作，包括：
1. 应用在接收到音视频来电后，订阅'voipCallUiEvent'事件，当用户在来电界面进行接听、挂断等操作时，会收到对应事件上报进而打出log：“Voip call event”。
2. 应用调用reportIncomingCall上报来电信息。
3. 应用内部处理完接听、挂断等操作后，调用reportCallStateChange接口向系统通知通话状态变化。

### 约束与限制
1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS NEXT Developer Beta1及以上。
3. DevEco Studio版本：DevEco Studio NEXT Developer Beta1及以上。
4. HarmonyOS SDK版本：HarmonyOS NEXT Developer Beta1 SDK及以上。
   
   



---
## camera
> 本示例主要展示了相机的相关功能 接口实现相机的预览拍照功能。

源码: https://gitcode.com/HarmonyOS_Samples/camera

﻿# 实现相机数据采集保存功能

### 介绍

本示例主要展示了相机的相关功能接口，实现相机的预览拍照功能。帮助开发者在相机相关场景开发中，实现相机的预览、拍照、录像、变焦、对焦等功能。

### 效果预览

| 效果展示                                        |
|---------------------------------------------|
| ![auth](screenshot/device/cameraSample.png) |

使用说明
1. 弹出是否允许“Camera”使用相机？点击“允许”
2. 弹出是否允许“Camera”使用麦克风？点击“允许”
3. 进入预览界面，预览正常，点击拍照按钮，跳转到图片预览页面，跳转正常，图片预览页面显示当前所拍照的图片，显示正常
4. 进入预览界面，预览正常，点击拍照按钮，跳转到图片预览页面，跳转正常，图片预览页面显示当前所拍照的图片，显示正常，退出应用并进入图库应用，第一张图片显示为刚刚拍照的图片，拍照正常
5. 点击图片预览页面的左上角返回按钮，重新进入预览页面，预览正常
6. 进入预览界面，预览正常，滑动变焦条，变焦条上方显示变焦值，显示正常，并且预览界面随着变焦条的滑动放大或缩小，预览正常
7. 进入预览界面，预览正常，点击预览显示区域进行对焦，对焦正常
8. 进入预览界面，预览正常，点击“拍照”旁边的“录像”切换到录像模式，预览正常，点击录像按钮，开始录像，录像正常，点击停止录像按钮，跳转到录像预览界面，跳转正常，点击视频播放按钮，播放正常

### 工程目录

```
├──entry/src/main/ets
│  ├──common
│  │  ├──utils
│  │  │  ├──Logger.ets                  // 日志工具
│  │  │  └──DateTimeUtil.ets            // 日期工具
│  │  │  └──GlobalContext.ets           // 全局上下文工具
│  │  └──Constants.ets                  // 基本参数枚举：分辨率、icon大小、按钮边距...
│  ├──entryability
│  │  └──EntryAbility.ets               // Ability的生命周期回调内容
│  ├──pages
│  │  ├──Index.ets                      // Ability实现的应用的入口页面，相机APP首页
│  │  └──EditPage.ets                   // 提供拍照后图片预览和编辑页面
│  ├──mode
│  │  └──CameraService.ets              // 相机初始化、选择分辨率、打开摄像头、调整焦距等功能
│  └──views
│     ├──ModeComponent.ets              // 拍照录制组件
│     ├──FlashingLightComponent.ets     // 闪光灯组件
│     ├──FocusAreaComponent.ets         // 对焦区域逻辑计算组件
│     ├──FocusComponent.ets             // 对焦框组件
│     └──SlideCo


---
## camera-data-collection
> 本示例主要展示了相机的相关功能，使用libohcamera.so 接口实现相机的预览、拍照、录像、前后置摄像头切换进行拍照、录像，以及对焦、曝光等控制类功能。

源码: https://gitcode.com/HarmonyOS_Samples/camera-data-collection

# 实现相机数据采集保存功能（C++）

### 介绍

本示例主要展示了相机的相关功能，使用libohcamera.so
接口实现相机的预览、拍照、录像、前后置摄像头切换进行拍照、录像，以及对焦、曝光等控制类功能。

### 效果预览

| 效果展示                                      |
|-------------------------------------------|
| ![auth](screenshot/device/ndk_camera.png) |

使用说明
1. 弹出是否允许“相机数据采集保存”使用相机？点击“允许”
2. 弹出是否允许“相机数据采集保存”使用麦克风？点击“允许”
3. 弹出是否允许“相机数据采集保存”修改你的图片和视频？点击“允许”
4. 进入预览界面，预览正常，点击画面模糊处，画面会变得清晰，对焦效果明显
5. 进入预览界面，预览正常，上下滑动屏幕，屏幕场景亮度发生变化，曝光效果明显
6. 进入预览界面，预览正常，进入拍照模式，点击拍照按钮，拍照正常，左下角会生成照片缩略图，点击左下角缩略图，能够跳转到图库，图片保存正常，打开图片显示正常
7. 进入预览界面，预览正常，切换到前置摄像头，点击拍照按钮，拍照正常，左下角生成照片缩略图，点击左下角缩略图，能够跳转到图库，图片保存正常，打开图片显示正常
8. 进入预览界面，预览正常，切换到录像模式，点击录像，开始录像，再点击停止录像按钮，录像成功，左下角会生成视频缩略图，点击左下角缩略图，能够跳转到图库，录像文件保存正常，播放录像文件正常
9. 进入预览界面，预览正常，切换到后置摄像头，点击录像，开始录像，再点击停止录像按钮，录像成功，左下角会生成视频缩略图，点击左下角缩略图，能够跳转到图库，录像文件保存正常，播放录像文件正常

### 工程目录

```
├──entry/src/main/cpp
│  ├──types
│  │  └──libentry
│  │     ├──index.d.ts                  // 导入NAPI接口供JS调用
│  │     └──oh-package.json5            // 接口注册配置文件
│  ├──camera_manager.cpp                // 相机基本功能接口定义cpp实现侧
│  ├──camera_manager.h                  // 相机基本功能接口定义
│  ├──CMakeLists.txt                    // Cmake打包配置文件，编译工程动态库脚本，依赖头文件、cpp以及相关依赖
│  └──main.cpp                          // NAPI实现JS与C++通信的接口
├──entry/src/main/ets
│  ├──common
│  │  ├──utils
│  │  │  ├──Logger.ets                  // 日志工具
│  │  │  └──MediaUtils.ets              // 媒体工具
│  │  ├──Constants.ets                  // 基本参数枚举：纵横比、设备类型、视频帧数...
│  │  └──DisplayCalculator.ets          // 计算界面宽高显示数值
│  ├──entr


---
## camera-kit-avrecorder
源码: https://gitcode.com/HarmonyOS_Samples/camera-kit-avrecorder

# 基于CameraKit通过AVRecorder录像

### 介绍

本示例通过CameraKit自定义相机，并通过AVRecorder进行录像。帮助开发者在自定义相机的场景开发中，实现使用AVRecorder录像的功能。

### 效果图预览

|               获取权限              |             录制页                  |
|-----------------------------------|------------------------------------|
|![](screenshots/device/request.png)| ![](screenshots/device/record.png) |

|                录制中                      |              主页                  |
|-------------------------------------------|-----------------------------------|
| ![](screenshots/device/stopRecording.png) | ![](screenshots/device/index.png) |

### 使用说明

1. 通过[requestPermissionsFromUser](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9)获取权限。
2. 点击“录制视频”按钮，判断授权权限，若权限均已授权，则跳转录制页面，否则需按提示开启所有权限后重新点击“录制视频”按钮。
3. 点击开始录制按钮，开始录制视频。
4. 点击停止录制按钮，停止录制视频，并返回首页，在“录制视频”按钮上方显示录制的视频，视频可手动播放。

### 工程目录
```
├───entry/src/main/ets
│   ├───common
│   │   └───CommonConstants.ets            // 常量
│   ├───entryability                        
│   │   └───EntryAbility.ets               // Ability的生命周期回调内容
│   ├───pages    
│   │   ├───Index.ets                      // 主页
│   │   └───Record.ets                     // 录制页
│   └───utils                               
│       ├───FileUtil.ets                   // 文件工具类
│       ├───Logger.ets                     // 日志工具类
│       └───RouterParams.ets               // 路由参数类
└───entry/src/main/resources                        
```

### 实现思路

1. 通过c


---
## camera-picker
> 本示例展示了如何拉起系统相机拍一张照片并返回应用。

源码: https://gitcode.com/HarmonyOS_Samples/camera-picker

# 基于系统相机实现拍照功能

### 介绍

本示例展示了系统相机的调用，通过cameraPicker拉起系统相机并进行拍照，获得图片。参考本示例可以学习系统相机的使用，帮助应用开发基本的照相功能。

### 效果预览
![image](screenshots/device/mainpage.png)

### 使用说明

1、点击拍照按钮，拉起系统相机，进行拍照。

2、拍照后点击确定返回应用，应用展示拍摄的照片。

### 工程目录
```
├──entry/src/main/ets
│  ├──common
│  │  └──constants
│  │     └──CommonConstants.ets             // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets                   // 程序入口类
│  └──pages
│     └──MainPage.ets                       // 主页面
└──entry/src/main/resources                 // 应用静态资源目录
```
### 具体实现

* 使用cameraPicker拉起系统相机。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## cannkit-samplecode-clientdemo-cpp
> 本示例展示CANN Kit的AI能力，运行AI模型进行图片分类的功能。

源码: https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp

# 基于SqueezeNet模型实现图像分类

## 介绍

本示例展示了使用CANN API提供的模型推理能力。

本示例展示了对图片中的物体进行分类识别的能力展示。

需要编译依赖CANN的动态库libhiai_foundation.so和AI 领域公共动态库libneural_network_core.so。

## 效果预览

|         **主界面**          |          **分类**          |          **下一张图片**          |
|:------------------------:|:------------------------:|--------------------------|
| ![](screenshots/launch.jpg) | ![](screenshots/guitar.jpg) | ![](screenshots/next.jpg) |

使用说明：

1. 在手机的主屏幕，点击“cannDemo”，启动应用，自动加载模型。
2. 点击“Click for classification”，进行模型推理对当前图片进行分类识别，推理完成后会把概率最大的三个分类结果展示在图片下方。
3. 点击“Click for next image”，展示下一张图片。 
4. 退出应用时，自动卸载模型。

## 工程目录
```
└── entry/src/main                      // 代码区
    ├── cpp
    │    ├── types/libentry
    │    │     └── index.d.ts           // native层接口注册文件
    │    ├── Classification.cpp         // native api层接口的具体实现函数
    │    ├── CMakeLists.txt             // native层编译配置
    │    ├── HIAIModelManager.cpp       // 模型管理类的实现
    │    ├── HIAIModelManager.h         // 模型管理类的定义
    ├── ets
    │    ├── entryability 
    │    │     └── EntryAbility.ets      // 程序入口类
    │    ├── pages 
    │    │     └── Index.ets            // 主界面展示类
    └── resources
    │    ├── base/media                 // 图片资源
    │    │   ├── cup.jpg
    │    │   └── guitar.jpg
    │    ├── rawfile 
    │    │    ├── hiai.om               // 模型文件
    │    │    └── labels_caffe.txt      // 模型输出标签文件
```

## 具体实现

**从API12版本开始**，本示例展示的功能使用了在CANN和NNCore中定义的以下API：

* OH_NN_ReturnCode HMS_HiAIOptions_SetBandMode(OH_N


---
## cannkit_samplecode_add_custom_cpp
> 本示例通过Ascend C编程语言实现了AddCustom算子，并按照不同的算子调用方式分别给出了对应的端到端实现。

源码: https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_add_custom_cpp

## AddCustom自定义算子样例说明 
本样例通过Ascend C编程语言实现了AddCustom算子，并按照不同的算子调用方式分别给出了对应的端到端实现。
在开发者自研自定义算子AddCustom在端侧NPU上部署场景，可以使用本样例的AddCutom算子实现两个向量的加法计算。
如需扩展功能，请参考[《Ascend C算子开发》](https://developer.huawei.com/consumer/cn/doc/hiai-Guides/ascend-c-development-0000002119490598)。
- [FrameworkLaunch](./FrameworkLaunch)：使用框架调用AddCustom自定义算子。  
按照工程创建->算子实现->编译部署>算子调试>算子调用的流程完成算子开发。整个过程都依赖于算子工程：基于工程代码框架完成算子核函数的开发和Tiling实现，通过工程编译脚本完成算子的编译部署，继而实现单算子调用或第三方框架中的算子调用。

本样例中包含如下调用方式：
<table>
    <th>调用方式</th><th>目录</th><th>描述</th>
    <tr>
        <!-- 列的方向占据1个cell -->
        <td rowspan='1'><a href="./FrameworkLaunch"> FrameworkLaunch</td><td><a href="./FrameworkLaunch/Onnx"> Onnx</td><td>通过model_run_tool工具执行带AddCustom算子的模型。</td>
    </tr>
</table>   

## 算子描述
AddCustom算子对应的数学表达式为：  
$$
C = A + B
$$
$A$ 为计算输入
$B$ 为计算输入
$C$ 为计算输出
## 算子规格描述

| 向量  | 数据类型 | 数据格式 |
| :--- | :--- | :----- | 
| A    | fp16 | ND |
| B    | fp16 | ND | 
| C    | fp16 | ND |

## 支持的产品型号
本样例支持如下产品型号：
- Mate 70 Pro
- Mate 70 Pro+
- Mate 70 Pro RS
- Mate X6
- MateBook Pro
- MateBook Fold
## 目录结构介绍
```
└── FrameworkLaunch    //使用框架调用的方式调用AddCustom自定义算子工程。
```
## 环境安装<a name="envready"></a>
编译运行此样例前，请先完成开发运行环境部署。环境要求：
ubuntu版本(仅支持x86)>=22.0，3.7<=python版本<=3.10，gcc/g++版本>=7.0，cmake版本>=3.16.0。  
环境安装推荐使用docker，执行如下命令即可一键获得满足开发要求的环境：
```bash
docker pull hub.xzt.me/ponylang/ponyc-ci-x86-64-unknown-linux-ubuntu22.04-builder:20230829
docker run -itd --net=host --privileged --name ascendc_ubuntu_python -v /home/:/data/ 07c3ea016a90 


---
## cannkit_samplecode_lm_engine_cpp
> 基于CANN Kit大模型推理解决方案，CANN LM Engine调用CANN的模型加速能力，通过CANN 软硬协同实现最佳的大模型性能、能效、内存、系统占用。

源码: https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_lm_engine_cpp

# CANN_LM_Engine

# 介绍
 **CANN LM Engine** 是基于CANN Kit大模型推理解决方案，CANN LM Engine调用CANN的模型加速能力，通过CANN 软硬协同实现最佳的大模型性能、能效、内存、系统占用。

# CANN LM Engine 组件

* CANN LM Engine：CANN LM Engine为大模型业务提供计算链路的加速封装，提供[计算加速服务和API接口](CANN_LLM/CANN_LLM_Engine_Interface/CANN%20LLM%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88%E6%8E%A5%E5%8F%A3%E6%96%87%E6%A1%A3.md)。
* CANN 工具链：提供模型转换、量化、Ascend C等[工具链](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiaifoundation-preparations)。
* CANN LM Engine DEMO：提供端到端调用[DEMO参考范例](CANN_LLM/CANN_LLM_Engine_Demo/README.md)。
* CANN 硬件：基于NPU/GPU/CPU 加速。

![输入图片说明](CANN_LLM/CANN_LLM_Engine_Guide/images/img2.png)


# 使用说明
 **CANN LM Engine**  提供了端到端的业务集成[指导手册](CANN_LLM/CANN_LLM_Engine_Guide/CANN%20LLM%20%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88.md)，基于该手册，可以快速将业务部署到CANN硬件，获取最佳的业务性能，功耗收益。

 ## 快速入门

CANN LLM大语言模型解决方案基于CANN硬件加速能力，提供高性能，低功耗的运行LLM模型，助力用户基于CANN硬件环境，获得更好的用户体验  
用户通过如下的pipeline完成LLM模型在CANN硬件环境上的集成：

<img src="./CANN_LLM/CANN_LLM_Engine_Guide/images/img1.png" width="900" height="300">


*  **Step1** ：LLM模型量化；输入是用户原始模型，输出是量化后权重和量化系数文件。
*  **Step2** ：将模型结构导出到ONNX格式，输入是原始模型结构和step1的量化权重，输出是ONNX模型及模型结构NPU亲和适配。
*  **Step3** : 将ONNX模型转换为CANN模型结构格式；输入是step2的ONNX模型和step1的量化系数文件，输出是CANN格式定义模型。
*  **Step4** : 基于CANN LLMEngine集成LLM模型。

# 联系我们
当前demo处在实验室版本中，如果你感兴趣，可以联系我们hiaifoundation@huawei.com。


---
## car-kit-sample-code-client-demo-arkts
> 本示例通过@kit.CarKit接口，适配HiCar业务和导航流转业务，实现了手机与车机的互联场景。

源码: https://gitcode.com/HarmonyOS_Samples/car-kit-sample-code-client-demo-arkts

## 车联-车服务

## 介绍

本示例展示了导航信息服务和出行分布式引擎服务的接口用法

这些接口需要导入'@kit.CarKit'。

## 效果预览

|              **应用首页**               |                **导航信息交互页面**                |               **出行业务交互页面**                |
|:-----------------------------------:|:------------------------------------------:|:-----------------------------------------:|
|  <img src="screenshots/index.jpg">  | <img src="screenshots/NavInfoService.jpg"> | <img src="screenshots/TravelService.jpg"> |

使用说明：
1. 实例演示导航数据更新接口、导航信号监听接口及出行业务的使用,通过对应的按钮触发相关接口的调用，界面文本区域会显示相关状态

## 工程目录
```
├──entry/src/main/ets               // 代码区
│  ├──common
│  │  ├──CommonUtils.ets            // 工具类
│  │  └──Logger.ets                 // 日志类
│  ├──entryability
│  │  └──EntryAbility.ets           // 程序入口类
│  └──pages
│     ├──Index.ets                  // 程序入口类
│     ├──NavInfoServicePage.ets     // 导航信息交互接口用法类
│     └──TravelServicePage.ets      // 出行业务交互接口用法类
└──entry/src/main/resources         // 应用静态资源目录
```

## 具体实现

### 导航信息服务示例
* 获取导航管理者对象；
```
function getNavigationController(): NavigationController;
```
* 导航管理者对象，用于注册系统信号监听、解注册系统信号监听、更新导航状态（导航状态，包含导航类型，导航目的地，导航途径点，路线，地图主题等）、更新导航元数据（导航元数据，包含TBT信息，道路、电子眼等信息）
```
NavigationController
    // 注册系统信号监听
    registerSystemNavigationListener(listener: SystemNavigationListener): void;

    // 解注册系统信号监听
    unregisterSystemNavigationListener(): void;

    // 更新导航状态
    updateNavigationStatus(navigationStatus: NavigationStatus): void;

    // 更新导航元数据（导航元数据，包含TBT信息，道路、电子眼等信息）
    updateNa


---
## certificate-framework
> 本示例使用了@ohos.security.cert相关接口实现了对签名数据进行校验的功能。

源码: https://gitcode.com/HarmonyOS_Samples/certificate-framework

# 基于证书算法库接口实现签名数据校验

### 介绍

本示例使用证书算法库接口校验签名数据。场景包括：正确数据校验，服务端验证客户端证书和原始数据；错误数据校验，模拟攻击者篡改数据，服务端验证失败。确保数据完整性和身份可信，攻击者身份不可信或数据不完整则验证不通过。

### 效果预览

|   主页    |                   校验通过                   |             校验失败             |
|:-------:|:------------------------------------------:|:---------------------------------------:|
| ![](screenshots/device/index.png) | ![](screenshots/device/verify_success.png) | ![](screenshots/device/verify_fail.png) |

使用说明

1、点击**数据展示**按钮，页面文本框中分别显示正确的证书、原始和签名数据内容。

2、点击**签名校验**按钮，页面弹出弹窗，提示**校验通过**。

3、点击**修改原始数据**按钮，页面显示修改后的原始数据和正确的证书、签名数据；点击签名校验按钮，页面弹出弹窗，提示**校验失败**。

4、点击**修改签名数据**按钮，页面显示修改后的签名数据和正确的证书、原始数据；点击签名校验按钮，页面弹出弹窗，提示**校验失败**。

5、点击**数据展示**按钮，页面恢复正确证书、原始和签名数据的展示；点击**签名校验**按钮，页面弹出弹窗，提示**校验通过**。

### 工程目录

```
├──entry/src/main/ets                                  // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets       
│  ├──model
│  │  ├──CertFrameworkModel.ets                        // 证书算法库框架模型文件
│  │  └──Logger.ets                                    // 日志文件
│  └──pages
│     └──Index.ets                                     // 主界面
└──entry/src/main/resources                            // 应用资源目录
```

### 具体实现

* 使用证书公钥实现签名校验的功能接口Verify封装在CertFrameworkModel中
    * 获取证书公钥：首先调用cert.createX509Cert接口生成证书对象certObject，使用certObject对象的getPublicKey能力获取公钥pubKey；然后调用cryptoFramework.createAsyKeyGenerator接口创建密钥生成器keyGenerator，使用keyGenerator的convertKey能力将公钥pubKey转换为正确的格式。
    * 使用公钥校验签名：首先调用cryptoFramework.createVerify接口创建验签对象verifier，使用公钥pub


---
## character-recognition
> 本示例介绍使用Text组件的enableDataDetector属性实现文本特殊文字识别。

源码: https://gitcode.com/HarmonyOS_Samples/character-recognition

# 基于enableDataDetector属性实现文本特殊文字识别的功能

### 介绍

本示例通过Text组件的enableDataDetector属性，实现文本特殊文字识别，比如输入电话号码、链接、邮箱和地址的文本，文本自动变蓝并增加下划线。帮助开发者掌握文本的特殊识别能力。

### 效果图预览

![](./screenshots/device/word.gif)

##### 使用说明

进入页面，输入带有特殊文字的信息并发送，对话列表中文本会自动识别并标识特殊文字。目前支持识别的类型包括电话号码、链接、邮箱和地址，其中地址需要具体地址信息才会被识别，被识别的文字会变成蓝色并增加下划线。

### 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  └──CommonConstants.ets         // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets            // 程序入口类
│  ├──pages                  
│  │  └──Index.ets                   // 首页
│  └──viewmodel
│     ├──BasicDataSource.ets         // 数据源
│     └──MessageModel.ets            // 信息数据模型
└──entry/src/main/resources          // 应用静态资源目录
```

### 具体实现

1. 使用Text组件的enableDataDetector属性实现文本特定文字识别。

2. 使用Text组件的dataDetectorConfig属性设置允许识别的类型。

### 相关权限

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## cipher
> 本示例使用cryptoFramework接口的Cipher对象相关方法实现了字符串加解密算法，包括RSA加密算法与AES加密算法。

源码: https://gitcode.com/HarmonyOS_Samples/cipher

# 基于cryptoFramework实现字符串加解密

### 介绍

本示例通过cryptoFramework接口实现字符串加解密，主要用到2种加密算法，RSA加解密、AES加解密。帮助开发者掌握应用侧使用Cipher处理加解密，处理自己业务需要字符串加解密的场景。

### 效果预览

| 主页                                | 加密页面                                | 解密页面                                |
|-----------------------------------|-------------------------------------|-------------------------------------|
| ![](screenshots/device/index.png) | ![](screenshots/device/encrypt.png) | ![](screenshots/device/decrypt.png) |

使用说明

1.点击主页面的**加密**按钮，在加密界面中点击**Encryption Algorithm**下拉选择加密算法，在输入框中输入待加密的内容，点击**加密**
按钮，下方文本框中显示加密后内容。

2.点击**重置**按钮，清除文本框中内容。

3.点击主页面的**解密**按钮，在解密界面中点击**Decrypt Algorithm**下拉选择解密算法，在输入框中输入待解密的内容，点击**解密**
按钮，下方文本框中显示解密后内容。

4.点击**重置**按钮，清除文本框中内容。

### 工程目录
```
├──entry/src/main/ets                                  // 代码区
│  ├──common
│  │  ├──Decrypt.ets                                   // 解密页面
│  │  └──Encrypt.ets                                   // 加密页面
│  ├──entryAbility            
│  │  └──EntryAbility.ets            
│  ├──model            
│  │  ├──CipherModel.ts                                // 加密与解密方法
│  │  └──Logger.ts                                     // 日志工具
│  └──pages            
│     ├──Index.ets                                     // 首页
│     └──Second.ets                                    // 加密与解密页面
└──entry/src/main/resources                            // 应用资源目录
```

### 具体实现

* 本示例分成加密与解密两个模块
  * 加密模块
    * 使用到rsaEncrypt(RSA算法加密)与aesEncrypt(AES算法加密)两种加密方法进行加密操作。
    


---
## cloud-foundation-kit_-sample-code_-arkts
> 本示例主要实现了基于Cloud Foundation Kit在应用中使用云函数、云数据库、云存储等云端服务的功能。

源码: https://gitcode.com/HarmonyOS_Samples/cloud-foundation-kit_-sample-code_-arkts

# Cloud Foundation Kit（云开发服务）

## 介绍

本示例展示了开发云函数、云存储、云数据库、预加载的过程，包括：

1.云函数的创建、部署及调用。

2.云存储的上传下载功能。

3.云数据库的创建和增删改查功能。

4.安装预加载和周期性预加载的用法。

需要使用@kit.CloudFoundationKit。

## 效果预览

| **云函数页面**                              | **云存储页面**                             | **云数据库页面**                            |                    安装预加载页面                     | 周期性预加载页面                                        |
|----------------------------------------|---------------------------------------|---------------------------------------|:----------------------------------------------:|-------------------------------------------------|
| ![](./screenshots/device/function.png) | ![](./screenshots/device/storage.png) | ![](./screenshots/device/clouddb.png) | ![](./screenshots/device/install_prefetch.png) | ![](./screenshots/device/periodic_prefetch.png) |

## Sample工程的配置与使用

### 在DevEco中配置Sample工程的步骤如下

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
2. 打开Sample工程，使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)配置的应用包名替换app.json5文件中的bundleName属性值。
3. 该Sample应用已集成认证服务SDK，请将您的“agconnect-services.json”文件复制到“AppScope/resources/rawfile”目录下。 具体参考[添加应用配置文件](https://developer.huawei.com/consumer/cn/doc/app/agc-help-auth-integration-sdk-0000002236337006#section845671619187)。 
4. 使用华为认证服务SDK登录华为账号后获取用户凭据，开通华为账号认证后，使用您


---
## component-collection
> 本示例为ArkUI中组件、通用、动画、全局方法的集合。

源码: https://gitcode.com/HarmonyOS_Samples/component-collection

# 实现ArkUI组件功能

### 介绍

本示例集合了ArkUI组件库中组件类、通用类、动画类和全局类模块，帮助开发者掌握多种ArkUI组件和事件的使用方法。

### 效果预览

| 组件                                          | 通用                                            | 动画                                                         | 全局方法                                            |
|---------------------------------------------|-----------------------------------------------|------------------------------------------------------------|-------------------------------------------------|
| ![image](screenshots/devices/component.png) | ![image](screenshots/devices/general.png)     | ![image](screenshots/devices/animation.png)                | ![image](screenshots/devices/global.png)        |
| <center>Button 按钮</center>                  | <center>onClick 点击事件</center>                 | <center>元素共享转场</center>                                    | <center>警告弹窗</center>                           |
| ![image](screenshots/devices/button.png)    | ![image](screenshots/devices/click_event.png) | ![image](screenshots/devices/share_element_transition.png) | ![image](screenshots/devices/warning_popup.png) |

使用说明：

1.点击**组件**、**通用**、**动画**、**全局方法**四个按钮或左右滑动切换不同视图。

2.点击导航（如onClick点击事件、触摸事件等），跳转至详情页面。

### 工程目录

```
├──entry/src/main/ets                                  // 代码区
│  ├──application
│  │  └──MyAbilityStage.ets      
│  ├──common
│  │  ├──AttributeModificationTool.ets                 // 组件
│  │  ├──IntroductionTitle.ets                         // 首页介绍标题组件
│  │  ├


---
## component-reuse
> 实现组件复用

源码: https://gitcode.com/HarmonyOS_Samples/component-reuse

# 实现组件复用

### 介绍
本示例为开发者展示组件复用的典型开发场景，包括同一列表内的组件复用、多个列表间的组件复用。


### 效果预览

| 同一列表内-列表项结构类型相同                                                                    | 同一列表内-列表项结构类型不同                                  | 同一列表内-列表项内子组件可拆分组合                               | 
|------------------------------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------|
| <img src="screenshots/device/0.png" width="320"> | <img src="screenshots/device/1.png" width="320"> | <img src="screenshots/device/2.png" width="320"> |

| 多个列表间的组件复用                                       | 
|--------------------------------------------------|
| <img src="screenshots/device/3.png" width="320"> | 

使用说明
1. 启动应用，点击具体场景分类，进入对应列表场景中。
2. 上下滑动列表，观察体验组件复用效果，滑动时不丢帧。

### 工程目录

```
├──ets
│  ├──common
│  │  └──MockData.ets                      // mock数据源
│  ├──entryability
│  │  └──EntryAbility.ets                  // ability入口
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets            // ability恢复入口
│  ├──model
│  │  ├──ItemData.ets                      // 列表项数据模型
│  │  ├──ItemDataSource.ets                // 列表项数据源
│  │  └──TitleDataSource.ets               // 标签数据源
│  ├──pages
│  │  ├──ComposableItemPage.ets            // 子组件可组合布局的列表项页面
│  │  ├──DiffListReusePage.ets             // 多个列表间的组件复用页面
│  │  ├──Index.ets                         // 首页
│  │  ├──MultiTypeItemPage.ets             // 多种结构类型的列表项页面
│  │  ├─


---
## component-stack
> 本示例介绍运用Stack组件以构建多层次堆叠的视觉效果。通过绑定Scroll组件的onScrollFrameBegin滚动事件回调函数，精准捕获滚动动作的发生。当滚动时，实时地调节组件的透明度、高度等属性，从而成功实现了嵌套滚动效果、透明度动态变化以及平滑的组件切换。

源码: https://gitcode.com/HarmonyOS_Samples/component-stack

# 使用Stack组件构建多层次堆叠布局

### 介绍

本示例介绍运用Stack组件以构建多层次堆叠的视觉效果。通过绑定Scroll组件的onScrollFrameBegin滚动事件回调函数，精准捕获滚动动作的发生。当滚动时，实时地调节组件的透明度、高度等属性，从而成功实现了嵌套滚动效果、透明度动态变化以及平滑的组件切换。

### 效果图预览
|                               堆叠效果                               |
|:--------------------------------------------------------------:|
| <img src="./screenshots/phone.gif" width="320"/> |

### 使用说明

1. 加载完成后显示整个界面，超过一屏可以上下滑动可见堆叠效果。

### 目录结构

```
componentstack
├──entry/src/main/ets
│  ├──constant
│  │  └──StackConstant.ets                        // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets                         // 应用生命周期类
│  ├──model
│  │  └──IconModel.ets                            // 本地数据源
│  ├──pages
│  │  └──Index.ets                                // 组件堆叠主页面 
│  ├──view
│  │  ├──IconView.ets                             // 按钮快捷入口自定义组件 
│  │  └──ProductList.ets                          // 商品列表自定义组件
│  └──viewmodel
│     ├──DataSource.ets                           // 列表数据模型
│     └──IconViewModel.ets                        // 数据类型定义
└────entry/src/main/resources 
```

### 实现思路

1. 在向上滑动过程中观察到头部组件是处于层级底部，而其他组件覆盖在其上方，为此，选择Stack组件来获取堆叠效果。
2. 在顶部的可滚动区域，通过使用Scroll组件来获取堆叠效果。
3. 实现滚动过程中动态调整文本框高度的功能时，运用Scroll组件滚动事件回调函数onScrollFrameBegin在滚动时修改文本框的高度及组件的透明度。
4. 存在多层嵌套滚动的情况时，应该先滚动父组件，再滚动自身。只需要在内层的Scroll组件的属性nestedScroll设置向前向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。
5. 在商品列表区域，采用瀑布流（WaterFlow）容器进行布局，将商品信息动态分布并分成两列呈现，每列商品自上而下排列。

### 相关权限
不涉及。

### 依赖
不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyO


---
## concurrent-module
> 本示例通过@ohos.taskpool和@ohos.worker接口，展示了如何启动worker线程和taskpool线程。

源码: https://gitcode.com/HarmonyOS_Samples/concurrent-module

# 基于线程池实现多线程任务功能

### 介绍

本示例通过@ohos.taskpool和@ohos.worker接口，展示了如何启动worker线程和taskpool线程实现任务的多线程处理。帮助开发者掌握多线程的使用方法，提升多任务处理的效率和灵活性。

### 效果预览

| 首页                                | 拷贝文件                                 | 字符串排序                            | 任务池页面                           |
|-----------------------------------|--------------------------------------|----------------------------------| ------------------------------------ |
| ![](screenshots/device/index.png) | ![](screenshots/device/copyFile.png) | ![](screenshots/device/worker.png) | ![](screenshots/device/taskpool.png) |

使用说明

1. 在主界面，可以点击**字符串排序**和**拷贝文件**按钮进入对应的界面；

2. 点击**字符串排序**按钮进入多线程界面：

   worker：

    1. 选择**Worker**页签，输入待排序的字符串，并以逗号分割。

    2. 点击**字符串排序**按钮，会将排序前的字符串发送给worker线程，在worker线程实现字符串排序，然后将排序后的字符串发送给主线程，主线程中显示排序后的字符串。

    3. 点击**清除**按钮，清除字符串。

   taskpool：

    1. 选择**TaskPool**页签，输入待排序的字符串，并以逗号分割。

    2. 点击**立即执行**按钮，任务执行完成后将排序后的字符串显示出来。

    3. 点击**超时3s执行**按钮，任务延迟3s后执行，执行完成后将排序后的字符串显示出来。

    4. 点击**函数任务**按钮，直接调用执行操作，执行完成后将排序后的字符串显示出来。需要注意的是，通过**函数任务**创建的task任务不支持取消。

    5. 点击**取消任务**按钮，会取消最后一个未执行的task任务。需要注意的是，只有当任务数大于最大线程数且任务未开始执行时才可以取消成功。

    6. 点击**清除**按钮，清除字符串。

3. 点击**拷贝文件**按钮进入文件拷贝界面：

   选择需要拷贝的文件，然后点击**拷贝文件**按钮，文件拷贝成功，触发事件日志显示沙箱下文件个数以及显示部分拷贝成功的文件名。

### 工程目录

```
├──entry/src/main/ets                         // 代码区
│  ├──common
│  │  ├──Common.ets                           // 公共工具类
│  │  └──Logger.ets                           // 日志工具类
│  ├──component
│  │  ├──TaskPoolTab.ets     


---
## content-publisher
> 本示例通过RichEditor组件以及常用的ArkUI组件，实现一个图文内容发布器。

源码: https://gitcode.com/HarmonyOS_Samples/content-publisher

# 基于ArkUI实现内容发布器功能

## 项目简介

本示例基于ArkUI的基本能力和RichEditor组件，实现一个富文本编辑器应用。功能包括：支持用户从图库中选取图片添加到页面；正文输入框支持添加话题、联系人、图文标题、自定义表情信息；页面支持添加添加当前位置信息。

## 效果预览

![](screenshots/device/home.png)

## 使用说明

1. 点击“添加优质首图”，选择好图片后，图片显示在横向列表中。
2. 点击“正文”输入框，可以输入相应的信息。
3. 点击页面下方![](entry/src/main/resources/base/media/ic_symbol2.svg)按钮，下方显示“图文标题”列表，选择相应的“图文标题”后，“图文标题”会在正文中显示。
4. 点击页面下方“@”按钮，页面进入联系人页面，选择需要@的联系人，返回发帖页面，在正文输入框会显示选中联系人的昵称。
5. 点击页面下方“#”按钮，页面弹出话题列表内容,选择对应的话题，弹框关闭，在正文输入框会显示选中的话题。
6. 点击页面下方表情按钮，切换到表情面板，点击表情，在正文输入框会显示选中的表情。
7. 点击左下“添加位置”，“添加位置”下方区域会多出一行附近位置信息，选中后，“添加位置”会变成选中的位置信息。

## 工程目录

```
├──entry/src/main/ets                         // 代码区
│  ├──constants
│  │  └──CommonConstants.ets                  // 公共常量
│  ├──entryability
│  │  └──EntryAbility.ets       
│  ├──models
│  │  └──CommonModel.ets                      // 公共实体类       
│  ├──pages
│  │  ├──ContactListPage.ets                  // 联系人页面
│  │  └──Home.ets                             // 主页面       
│  ├──utils
│  │  ├──CommonUtil.ets                       // 通用工具类
│  │  ├──FileUtil.ets                         // 选择图片工具类
│  │  ├──LocationUtil.ets                     // 本地位置工具类
│  │  ├──PermissionManager.ets                // 权限管理类
│  │  └──Logger.ets                           // 日志文件
│  └──view
│     ├──ContactListView.ets                  // 联系人模块
│     ├──PictureListView.ets                  // 图片列表模块
│     ├──ToolbarView.ets                      // 底部工具模块
│     ├──EditorView.ets                       // 编辑输入模块
│     ├──Gr


---
## continue-progress
源码: https://gitcode.com/HarmonyOS_Samples/continue-progress

# 实现浏览进度接续功能

### 介绍

本示例基于应用接续和分布式能力实现了长列表浏览、媒体浏览和web页面浏览的进度接续。长列表是List嵌套WaterFlow组件，需要将currentOffset接续； 媒体进度接续使用Avplayer实现，接续其集数和播放时间，使用seek()接口实现；Web进度使用js语句获取进度。

### 效果预览

| 首页                              | 长列表                                | 媒体                              | web                           |
|---------------------------------|------------------------------------|---------------------------------|-------------------------------|
| ![image](screenshots/index.png) | ![image](screenshots/longlist.png) | ![image](screenshots/video.png) | ![image](screenshots/web.png) |

### 使用说明：

本示例提供3个按钮触发使用不同场景的进度接续：

1. 长列表进度：点击该按钮完成进入长列表浏览页面，点击对端接续图标，对端恢复页面到长列表页面并且浏览位置在源端离开的条目附近。
2. 媒体浏览进度接续：可以观看视频切换视频，点击对端接续图标，对端恢复视频播放页面，并且从源端当前播放的位置开始播放。
3. Web页面浏览进度接续：可以查看web页面，点击对端接续图标，对端恢复页面到web页面并且浏览位置在源端离开的条目附近。


### 工程目录

```
├───ets                                         
│   ├───constants                               
│   │   ├───BreakpointConstants.ets             // 断点相关常量
│   │   ├───CommonConstants.ets                 // 一般常量
│   │   └───HomeConstants.ets                   // 主页的常量
│   ├───entryability                            
│   │   └───EntryAbility.ets                    // 程序入口类
│   ├───entrybackupability                      
│   │   └───EntryBackupAbility.ets              // 备份恢复类
│   ├───pages                                   
│   │   └───Index.ets                           // 首页
│   ├───utils                                   
│   │   ├───BreakpointSystem.e


---
## core-speech-kit-sample-code-ark-ts-kit-asrdemo
> 本示例展示了将音频信息转换为文本的AI能力。

源码: https://gitcode.com/HarmonyOS_Samples/core-speech-kit-sample-code-ark-ts-kit-asrdemo

# 实现语音识别

## 介绍

本示例展示了使用基础语音服务提供的语音识别能力。

本示例展示了对一段音频流转换成文字的能力展示。

需要使用语音识别接口@hms.ai.speechRecognizer.d.ts.

## 效果预览

|           **桌面**            |         **主页面**          |         **录音播报**          |
|:---------------------------:|:------------------------:|:-------------------------:|
| ![](screenshots/launch.png) | ![](screenshots/asr.png) | ![](screenshots/play.png) | 

使用说明：

1. 在手机的主屏幕，点击”asrDemo“，启动应用。
2. 点击“CreateEngine”，进行能力初始化。
3. 可以选择以下其中一种方式进行操作,两者同时使用回调会发生异常：
   a)点击“startRecording”，开始录音识别。
   b)点击“audioToText”读取应用音频文件，写流进行识别。
   如选择后者则需开发者将PCM格式的音频信息存放在 entry\src\main\resources\resfile 路径下。
5. 点击“queryLanguagesCallback/queryLanguagesPromise”，查询支持的语种和音色。

### 工程目录
```
├─entry/src/main/ets                         // 代码区
│  ├─entryability
│  │  └─EntryAbility.ets       
│  └─pages
│     ├─AudioCapturer.ets                    // 录音器实现1
│     ├─FileCapturer.ets                     // 录音器实现2
│     └─Index.ets                            // 主界面
├─entry/src/main/resources                   // 应用资源目录
│  └─resfile
│     └─001.pcm
└─screenshots                                // 截图
```

## 具体实现

本示例展示了在@hms.ai.speechRecognizer.d.ts定义的API：
~~~
* createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback<SpeechRecognizerEngine>): void;
* setListener(listener: RecognizerListener): void;
* queryLanguages(params: LanguageQuery, callback: AsyncCallback<Array<string>>): void;
* startListening(params: StartParams): void;
* writeAudio(sessionId: string, audio: 


---
## core-speech-kit-sample-code-ark-ts-kit-ttsdemo
> 	
本示例展示了文本信息转换为语音并进行播报的AI能力。

源码: https://gitcode.com/HarmonyOS_Samples/core-speech-kit-sample-code-ark-ts-kit-ttsdemo

# 实现文本转语音

## 介绍

本示例展示了使用基础语音服务提供的文本转语音能力。

本示例展示了对一段文本，进行语音合成及播报的能力。

需要使用文本转语音接口@hms.ai.textToSpeech.d.ts.

## 效果预览

|           **桌面**            |            **主页面**            |          **播报**          |
|:---------------------------:|:-----------------------------:|:------------------------:|
| ![](screenshots/launch.png) | ![](screenshots/MainPage.png) | ![](screenshots/tts.png) | 

使用说明：

1. 在手机的主屏幕，点击”ttsDemo“，启动应用。
2. 点击“CreateEngine”按钮，进行能力初始化。
3. 点击“speak”按钮，试听文本播报。 
4. 点击“stop”等按钮对播报进行事件控制。

### 工程目录
```
├─entry/src/main/ets                         // 代码区
│  ├─entryability
│  │  └─EntryAbility.ets       
│  └─pages
│     ├─Index.ets                            // 主页界面
│     └─PcmPlayer.ets                        // PcmPlayer工具类
├─entry/src/main/resources                   // 应用资源目录
└─screenshots                                // 截图
```

## 具体实现

本示例展示了在@hms.ai.textToSpeech.d.ts定义的API：
~~~
* createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback<TextToSpeechEngine>): void;
* speak(text: string, speakParams: SpeakParams, listener: SpeakListener): void;
* stop(): void;
* isBusy(): boolean;
* shutdown(): void;
~~~
业务使用时，需要先进行import导入textToSpeech。
调用speak等接口，传入想要识别的文本，试听播报，观察日志等。参考entry/src/main/ets/pages/Index.ets.

## 相关权限

不涉及。

## 依赖

不涉及。

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机、华为平板、2in1。
2. HarmonyOS系统：HarmonyOS 5.0.0 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。





---
## core-vision-kit-sample-code-ark-ts-face-compare-demo
> 本示例展示了对比两张图片中的人脸并判断是否为同一个人的AI能力。

源码: https://gitcode.com/HarmonyOS_Samples/core-vision-kit-sample-code-ark-ts-face-compare-demo

# 实现人脸比对

## 介绍

本示例展示了使用基础视觉服务提供的人脸比对能力。

本示例模拟了在应用里，选择两张图片，计算两个图中最大人脸的相似度

需要使用人脸比对接口@hms.ai.face.faceComparator.d.ts。

## 效果预览

|         **主窗口**          |             **选择图片**             |             **开始比对**             |
|:------------------------:|:--------------------------------:|:--------------------------------:|
| ![](screenshots/app.png) | ![](screenshots/selectImage.png) | ![](screenshots/faceResult.png) | 

使用说明：

1. 在手机的主屏幕，点击”faceComparatorDemo“，启动应用。
2. 点击“Select images”按钮，用户可以在图库中选择图片，或者通过相机拍照。
3. 点击“Compare faces”按钮，比对人脸信息，结果通过文本展示。

## 工程目录
```
├─entry/src/main/ets
│  ├─entryability
│  │  ├─EntryAbility.ets            // 程序入口
│  └─pages
│     └─Index.ets                   // 应用主界面
└─entry/src/main/resources          // 资源文件目录
```

## 具体实现

本示例展示的控件在@hms.ai.face.faceComparator.d.ts定义了人脸比对API：
~~~
*     function compareFaces(visionInfo1: VisionInfo, visionInfo2: VisionInfo): Promise<FaceCompareResult>;
~~~
业务使用时，需要先进行import导入faceComparator
调用通用人脸比对接口，并传入想要比对的图片，接收处理返回的结果（文字信息）。参考entry/src/main/ets/pages/Index.ets.

## 相关权限

不涉及。

## 依赖

不涉及。

## 约束与限制

1. 本实例仅支持标准系统上运行，支持设备：华为手机、华为平板、2in1。
2. HarmonyOS系统：HarmonyOS 5.0.0 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。


---
## core-vision-kit-sample-code-ark-ts-face-detect-demo
> 本示例展示了检测图片中的人脸并返回各项数据的AI能力。

源码: https://gitcode.com/HarmonyOS_Samples/core-vision-kit-sample-code-ark-ts-face-detect-demo

# 实现人脸识别

## 介绍

本示例展示了使用基础视觉服务提供的人脸识别能力。

本示例模拟了在应用里，选择一张图片，识别其多个人脸信息并展示出来。包括人脸框、五官点位、置信度、人脸朝向（欧拉角）

需要使用人脸识别接口@hms.ai.face.faceDetector.d.ts。

## 效果预览

|         **主窗口**          |             **选择图片**             |             **开始识别**             |
|:------------------------:|:--------------------------------:|:--------------------------------:|
| ![](screenshots/app.png) | ![](screenshots/selectImage.png) | ![](screenshots/faceResult.png) | 

使用说明：

1. 在手机的主屏幕，点击”faceDetectorDemo“，启动应用。
2. 点击“Select image”按钮，用户可以在图库中选择图片，或者通过相机拍照。
3. 点击“Start detection”按钮，识别人脸信息，结果通过文本展示。

## 工程目录
```
├─entry/src/main/ets
│  ├─entryability
│  │  ├─EntryAbility.ets            // 程序入口
│  └─pages
│     └─Index.ets                   // 应用主界面
└─entry/src/main/resources          // 资源文件目录
```

## 具体实现

本示例展示的控件在@hms.ai.face.faceDetector.d.ts定义了人脸检测API：
~~~
*   function detect(visionInfo: VisionInfo): Promise<Array<Face>>;
~~~
业务使用时，需要先进行import导入faceDetector
调用通用人脸识别接口，并传入想要识别的图片，接收处理返回的结果（文字信息）。参考entry/src/main/ets/pages/Index.ets.

## 相关权限

不涉及。

## 依赖

不涉及。

## 约束与限制

1. 本实例仅支持标准系统上运行，支持设备：华为手机、华为平板、2in1。
2. HarmonyOS系统：HarmonyOS 5.0.0 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。


---
## core-vision-kit-sample-code-ark-ts-object-detect-demo
源码: https://gitcode.com/HarmonyOS_Samples/core-vision-kit-sample-code-ark-ts-object-detect-demo

# 实现多目标识别

## 介绍

本示例展示了使用基础视觉服务提供的多目标识别功能。

本示例模拟了在应用里，选择一张多目标图片，识别多个目标。

需要使用多目标识别接口@hms.ai.vision.objectDetection.d.ts。

## 效果预览

|          **主窗口**          |             **选择图片**              |             **开始比对**              |
|:-------------------------:|:---------------------------------:|:---------------------------------:|
| ![](screenshots/app.png) | ![](screenshots/selectImage.png) | ![](screenshots/objectResult.png) | 

使用说明：

1. 在手机的主屏幕，点击”objectDetectDemo“，启动应用。
2. 点击“Select image”按钮，用户可以在图库中选择图片，或者通过相机拍照。
3. 点击“Start multi-object detection”按钮，识别多目标信息，结果通过文本展示。

## 工程目录
```
├─entry/src/main/ets
│  ├─entryability
│  │  └─EntryAbility.ets            // 程序入口
│  ├─entrybackupability
│  │  └─EntryBackupAbility.ets
│  └─pages
│     └─Index.ets                   // 应用主界面
└─entry/src/main/resources          // 资源文件目录
```

## 具体实现

本示例展示的控件在@hms.ai.vision.objectDetection.d.ts定义了多目标识别API：
~~~
*     process(request: visionBase.Request): Promise<ObjectDetectionResponse>;
~~~
业务使用时，需要先进行import导入objectDetection
调用通用多目标识别接口，并传入想要识别的图片，接收处理返回的结果（文字信息）。参考entry/src/main/ets/pages/Index.ets.

## 相关权限

不涉及。

## 依赖

不涉及。

## 约束与限制

1. 本实例仅支持标准系统上运行，支持设备：华为手机、华为平板、2in1。
2. HarmonyOS系统：HarmonyOS 5.0.0 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。


---
## core-vision-kit-sample-code-ark-ts-ocr-demo
> 本示例展示了图像信息转换为字符信息的能力。

源码: https://gitcode.com/HarmonyOS_Samples/core-vision-kit-sample-code-ark-ts-ocr-demo

# 实现通用文字识别

## 介绍

本示例展示了使用基础视觉服务提供的通用文字识别能力。

本示例模拟了在应用里，选择一张图片，识别其文字信息并展示出来（可复制）。

需要使用通用文字识别接口@hms.ai.ocr.textRecognition.d.ts。

## 效果预览

|         **主窗口**          |             **选择图片**             |             **开始识别**             |
|:------------------------:|:--------------------------------:|:--------------------------------:|
| ![](screenshots/app.png) | ![](screenshots/selectImage.png) | ![](screenshots/ocrResult.png) | 

使用说明：

1. 在手机的主屏幕，点击”ocrDemo“，启动应用。
2. 点击“Select image”按钮，在图库中选择图片，或者通过相机拍照。
3. 点击“Start recognition”按钮，识别图本信息，文本展示并可复制。

## 工程目录
```
├─entry/src/main/ets
│  ├─entryability
│  │  └─EntryAbility.ets            // 程序入口
│  └─pages
│     └─Index.ets                   // 应用主界面
└─entry/src/main/resources          // 资源文件目录
```

## 具体实现

本示例展示的控件在@hms.ai.ocr.textRecognition.d.ts定义了文字识别API：
~~~
* recognizeText(visionInfo: VisionInfo, callback: AsyncCallback<TextRecognitionResult>): void
~~~
业务使用时，需要先进行import导入textRecognition。
调用通用文字识别接口，并传入想要识别的图片，接收处理返回的结果（文字信息）。参考entry/src/main/ets/pages/Index.ets.

## 相关权限

不涉及。

## 依赖

不涉及。

## 约束与限制

1. 本实例仅支持标准系统上运行，支持设备：华为手机、华为平板、2in1。
2. HarmonyOS系统：HarmonyOS 5.0.0 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。


---
## core-vision-kit-sample-code-ark-ts-skeleton-detector-demo
> 本示例展示了识别图片人像中的关键骨骼点的AI能力。

源码: https://gitcode.com/HarmonyOS_Samples/core-vision-kit-sample-code-ark-ts-skeleton-detector-demo

# 实现骨骼点识别

## 介绍

本示例展示了使用基础视觉服务提供的骨骼点识别功能。

本示例模拟了在应用里，选择一张人物全身图片，识别骨骼点。

需要使用骨骼点检测接口@hms.ai.vision.skeletonDetection.d.ts。

## 效果预览

|          **主窗口**          |             **选择图片**              |              **开始比对**               |
|:-------------------------:|:---------------------------------:|:-----------------------------------:|
| ![](screenshots/app.png) | ![](screenshots/selectImage.png) | ![](screenshots/skeletonResult.png) | 

使用说明：

1. 在手机的主屏幕，点击”skeletonDetectDemo“，启动应用。
2. 点击“Select image”按钮，用户可以在图库中选择图片，或者通过相机拍照。
3. 点击“Start skeleton detection”按钮，识别照片骨骼点信息，结果通过文本展示。

## 工程目录
```
├─entry/src/main/ets
│  ├─entryability
│  │  └─EntryAbility.ets            // 程序入口
│  ├─entrybackupability
│  │  └─EntryBackupAbility.ets
│  └─pages
│     └─Index.ets                   // 应用主界面
└─entry/src/main/resources          // 资源文件目录
```

## 具体实现

本示例展示的控件在@hms.ai.vision.skeletonDetection.d.ts定义了骨骼点识别API：
~~~
*     process(request: visionBase.Request): Promise<SkeletonDetectionResponse>;
~~~
业务使用时，需要先进行import导入skeletonDetection
调用骨骼点检测接口，并传入想要识别的图片，接收处理返回的结果（文字信息）。参考entry/src/main/ets/pages/Index.ets.

## 相关权限

不涉及。

## 依赖

不涉及。

## 约束与限制

1. 本实例仅支持标准系统上运行，支持设备：华为手机、华为平板、2in1。
2. HarmonyOS系统：HarmonyOS 5.0.0 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。


---
## core-vision-kit-sample-code-image-segmentation-demo-arkts
> 本示例展示了识别和提取图像中的主体的AI能力，帮助开发者用于前景目标检测和前景主体分离的场景。

源码: https://gitcode.com/HarmonyOS_Samples/core-vision-kit-sample-code-image-segmentation-demo-arkts

# 实现主体分割

## 介绍

本示例展示了使用基础视觉服务提供的主体分割能力。

本示例模拟了在应用里，选择一张图片，识别其图片中的显著性主体并展示出来主体的边界框的数据。

需要使用主体分割接口@hms.ai.vision.subjectSegmentation.d.ts。

## 效果预览

|         **主窗口**          |             **选择图片**             |             **开始识别**             |
|:------------------------:|:--------------------------------:|:--------------------------------:|
| ![](screenshots/app.png) | ![](screenshots/selectImage.png) | ![](screenshots/segResult.png) | 

使用说明：

1. 在手机的主屏幕，点击”imgSegDemo“，启动应用，默认自带一张图片。
2. 点击“Select image”按钮，用户可以在图库中选择图片，或者通过相机拍照。
3. 点击“Start subject segmentation”按钮，识别图片中的显著性主体，结果通过主体边界框的坐标显示。

## 具体实现

本示例展示的控件在@hms.ai.vision.subjectSegmentation.d.ts定义了主体分割API：
~~~
*   function doSegmentation(visionInfo: VisionInfo, config?: SegmentationConfig): Promise<SegmentationResult>;
~~~
业务使用时，需要先进行import导入subjectSegmentation
调用通用主体分割接口，并传入想要识别的图片，接收处理返回的结果（文字信息）。参考entry/src/main/ets/pages/Index.ets.

## 相关权限

不涉及。

## 依赖

不涉及。

## 约束与限制

1. 本实例仅支持标准系统上运行，支持设备：华为手机、华为平板、2in1。
2. HarmonyOS系统：HarmonyOS 5.0.0 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。


---
## crypto-collection
> 本示例使用cryptoFramework接口的相关方法实现字符串加解密算法。

源码: https://gitcode.com/HarmonyOS_Samples/crypto-collection

# 基于cryptoFramework实现加解密功能

### 介绍

本示例使用cryptoFramework接口的相关方法实现字符串加解密、签名验签、消息摘要、消息认证码等功能，使用了AES、3DES、SM4、RSA、SM2、ECDSA、SHA256、MD5、SM3、HMAC等算法。

### 效果预览

| 首页                                        | 加解密页面                                           | 加解密详情页                                         | 签名验签页面                                       | 签名验签详情页                                             |
|-------------------------------------------|-------------------------------------------------|------------------------------------------------|----------------------------------------------|-----------------------------------------------------|
| ![image](screenshots/devices/index.png)   | ![image](screenshots/devices/crypto.png)        | ![image](screenshots/devices/cryptoDetail.png) | ![image](screenshots/devices/signature.png)  | ![image](screenshots/devices/signatureDetail.png)   |
| <center>消息摘要页面</center>                   | <center>消息摘要详情页</center>                        | <center>消息认证码页面</center>                       | <center>消息认证码详情页</center>                    | <center>SM2密钥格式转换</center>                          |
| ![image](screenshots/devices/summary.png) | ![image](screenshots/devices/summaryDetail.png) | ![image](screenshots/devices/code.png)         | ![image](screenshots/devices/codeDetail.png) | ![image](screenshots/devices/format_conversion.png) |

### 使用说明

1. 点击按钮跳转到各个算法页面，点击列表项跳转到各个详情页面。
2. 加解密详情页：输入待加密字符串后点击加密即可加密字符串，输出加密后的Base64编码的字符串，点击解密将加密后的Base64编码的字符


---
## crypto-framework
> 本示例使用@ohos.security.cryptoFramework相关接口实现了对文本文件的加解密、签名验签操作。

源码: https://gitcode.com/HarmonyOS_Samples/crypto-framework

# 基于cryptoFramework实现文本文件加解密

### 介绍
本示例通过cryptoFramework接口实现文本加解密，主要用到2种加密算法，RSA加解密、AES加解密。帮助开发者掌握应用侧使用Cipher处理加解密，处理自己业务需要文本加解密的场景，对文件签名验签（本质也是加解密）的场景。

实现场景如下：

1）软件需要加密存储本地文本文件，需要调用加解密算法库框架选择密钥文本文件，对本地文本文件进行加密，其中密钥文本文件可由加解密算法库生成。

2）软件需要解密存储本地文本文件，需要调用加解密算法库框架选择密钥文本文件，对本地文本文件进行解密，其中密钥文本文件可由加解密算法库生成。

3）软件需要对存储本地文本文件签名，调用加解密算法库框架选择密钥文本文件，对本地文本文件进行完整性签名，其中密钥文本文件可由加解密算法库生成。

4）软件需要验证存储本地文本文件的签名完整性，需要调用加解密算法库框架选择密钥文本文件与签名文件，对文件进行验签，其中密钥文本文件可由加解密算法库生成。

### 效果预览

| 加密页面                                | 解密页面                                 | 签名页面                              | 验签界面                                |
|-------------------------------------|--------------------------------------|-----------------------------------|-------------------------------------|
| ![](screenshots/device/encrypt.png) | ![](screenshots/device/decrypt.png) | ![](screenshots/device/sign.png) | ![](screenshots/device/verify.png) |

使用说明

1.点击主页面tab栏的**加密**，在加密界面点击**打开文件**，通过文件选择器选择文本文件，选择完毕自动返回加密界面，
其内容显示在**文件内容**文本框中，
点击**选择密钥**，选择密钥文件，如果没有密钥文件，可以通过在加密界面点击**随机生成AES密钥**，生成并通过文件选择器保存密钥文件。
选择完文本文件和密钥文件后，点击**加密**按钮，完成加密，并通过文件选择器保存密文文件。
下方**加密内容**文本框中显示加密后的消息内容。

2.点击主页面tab栏的**解密**，在解密界面点击**打开文件**，通过文件选择器选择文本文件，选择完毕自动返回解密界面，
其内容显示在**文件内容**文本框中，
点击**选择密钥**，选择和**加密相同**的密钥文件。
选择完文本文件和密钥文件后，点击**解密**按钮，完成解密，并通过文件选择器保存明文文件。
下方**解密内容**文本框中显示解密后的消息内容。

3.点击主页面tab栏的**签名**，在签名界面点击**打开文件**，通过文件选择器选择文本文件，选择完毕自动返回签名界面，
其内容显示在**文件内容**文本框中，
点击**选择密钥**，选择密钥文件，如果没有密钥文件，可以通过在签名界面点击**随机生成RSA密钥**，生成并通过文件选择器保存密钥文件，注意RSA密钥


---
## crypto-sm2
> 本示例对使用@kit.CryptoArchitectureKit加密后的密文格式进行转换。

源码: https://gitcode.com/HarmonyOS_Samples/crypto-sm2

# 基于加解密算法库框架实现ASN.1密文转换

### 介绍

本示例对使用@kit.CryptoArchitectureKit加密后的密文格式进行转换。@kit.CryptoArchitectureKit加密后的密文格式默认为以base64显示的ASN.1格式问题，通过对密文进行base64变换后得到字符数组，以16进制数字显示，在此基础上进行密文格式转换，从ASN.1格式转换为c1c3c2格式的裸密文，再以c1c3c2格式的裸密文进行解密，以验证密文转换的正确性。

### 效果预览

| 首页                                     | 数据加密                                     | base64变换                           | 密文格式变换                                   | 数据解密                                     |
|----------------------------------------|------------------------------------------|------------------------------------|------------------------------------------|------------------------------------------|
| ![index](screenshots/device/index.png) | ![encode](screenshots/device/encode.png) | ![hex](screenshots/device/hex.png) | ![c1c3c2](screenshots/device/c1c3c2.png) | ![decode](screenshots/device/decode.png) |

使用说明

1. 点击主页面**加密**按钮，对原始数据使用SM2国密算法进行加密，其内容显示在**加密数据**文本框中，此时**解密**按钮和**base64转换**按钮使能。
2. 点击主页面**base64转换**按钮，对原始密文进行base64转换，在**加密数据**文本框中显示转换后的密文，此时**asn.1转换**按钮使能。
3. 点击主页面**asn.1转换**按钮，对密文进行asn.1转换，在**加密数据**文本框中显示转换后的密文，此时**加密**按钮和**base64转换**按钮去使能。
4. 点击主页面**解密**按钮，对密文进行解密，在**解密数据**文本框中显示解密后的文本，此时**解密**按钮去使能。

### 工程目录

```
entry/src/main/                          // 代码区
├──ets
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──pages
│  │  └──Index.ets                       // 主页界面
│  └──utils
│     ├──SM2.ets                         // SM2加解密
│     ├──SM2CipherText.ets               // 密文格式转换
│     └──SM2Se


---
## custom-canvas
源码: https://gitcode.com/HarmonyOS_Samples/custom-canvas

# 基于Canvas实现画布的功能

### 介绍

本示例通过Canvas实现了一个包括画笔粗细、颜色和透明度的选择、绘制、缩放、清楚等功能的画布功能。帮助开发者掌握Canvas的相关接口属性，绘制自己的业务UI。

### 效果图预览

![](./screenshots/device/canvas.gif)

##### 使用说明

1. 进入首页后，下方有五个按钮，画笔默认选中，可以在空白部分进行绘画，默认粗细是3，颜色是黑色不透明。
2. 进行绘制后，撤回按钮会高亮可点击，点击后可以撤回上一步的笔画；同时重做按钮会高亮可点击，点击重做后还原上一步撤销的笔画。
3. 点击橡皮擦按钮后，手指绘画就会实现擦除效果，画笔按钮取消高亮。
4. 点击清空按钮会清空整个画布的所有绘制，同时清空按钮高亮。
5. 点击画笔按钮，会弹出半模态弹窗，在弹窗内可以选择画笔的类型、颜色、不透明度和粗细。
6. 本示例只展示圆珠笔和马克笔两种类型，圆珠笔为默认类型，这里可以点击马克笔，关闭弹窗再次进行绘画，笔画就变为马克笔。
7. 再次点击画笔唤起弹窗，可以切换颜色、不透明度和粗细，不透明度只有马克笔可以切换，圆珠笔不可以切换。
8. 双指捏合画布缩小，双指外扩画布放大，缩放时画笔按钮取消高亮，缩放结束后，点击画笔就可以再次进行绘制。

### 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  └──CommonConstants.ets         // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets            // 程序入口类
│  ├──pages                  
│  │  └──Index.ets                   // 首页
│  ├──view   
│  │  └──myPaintSheet.ets            // 半模态页面
│  └──viewmodel
│     ├──DrawInvoker.ets             // 绘制方法
│     ├──IBrush.ets                  // 笔刷接口
│     ├──IDraw.ets                   // 绘制类
│     └──Paint.ets                   // 绘制属性类
└──entry/src/main/resources          // 应用静态资源目录
```

### 具体实现

1. 通过在Canvas上绑定onTouch事件获取触摸点的相对画布的x轴和y轴坐标，将坐标传入路径对象Path2D的moveTo和lineTo方法实现绘制功能。
2. 橡皮擦功能是通过修改CanvasRenderingContext2D的strokeStyle属性为白色来实现的。
3. 每条绘制路径都会通过add方法存放到绘制数组drawPathList中，撤回功能将drawPathList最后一项移除并存到重做数组redoList中，重做功能把redoList中最后一项清除并重新放回drawPathList中。
4. 清除功能是将drawPathList和redoList数组清空后重新绘制画布。
5. 笔刷中圆珠笔的globalAlpha属性值默认为1，且不可改变，马克笔的globalAlpha属性值默认为0.5，可以通过Slider组件调


---
## custom-common-event
> 本示例主要展示了公共事件相关的功能，实现了一个检测用户部分行为的应用。

源码: https://gitcode.com/HarmonyOS_Samples/custom-common-event

# 实现公共事件的订阅和发布

### 介绍

本示例主要展示了公共事件相关的功能，实现了一个检测用户部分行为的应用。具体而言实现了如下几点功能：

1.通过订阅系统公共事件，实现对用户操作行为（亮灭屏、锁屏和解锁屏幕、Wi-Fi状态变化）的监测；

2.通过在用户主动停止监测行为时发布自定义有序公共事件，实现对用户主动触发监听行为的持久化记录；

3.通过在用户设置对某一事件的监听状态时发布粘性事件，记录下本次应用运行期间允许监听的事件列表，同时在应用退出时将临时允许的修改为不允许。

### 效果预览

| 主页                                   | 监控页面                               | 设置页面                               | 历史记录页面                          |
|--------------------------------------|------------------------------------| -------------------------------------- | ------------------------------------- |
| <img src="screenshots/launch.jpg" /> | <img src="screenshots/main.jpg" /> | <img src="screenshots/settings.jpg" /> | <img src="screenshots/history.jpg" /> |

使用说明：

1.安装编译生成的hap包，桌面上显示应用图标如下，点击图标即可进入应用。

<img src="screenshots/icon.png" style="zoom:80%;" />

2.进入应用显示菜单页，可选择“进入”，“历史”，“设置”及“关于”几个选项。

3.点击“进入”后跳转至主页面，点击主页面“开始监控”按钮，将开始监听系统公共事件，并进行计时，此时按钮内容变更为“停止监听”；点击停止监听按钮，页面上将显示本次监听时长及监听期间收到的干扰信息汇总，并在页面右下角显示“查看详情”按钮，点击按钮将跳转至详情页，显示监听期间收到的干扰信息，应用当前仅监听了亮灭屏、锁屏和解锁屏幕、Wi-Fi状态变化等用户可操作的系统公共事件，后续可根据需求快速扩展。

4.返回至应用菜单页面，点击“历史”可查看用户操作监听的历史记录，当前支持每次运行期间最多存储10条历史记录，超过10条后将删除历史数据。

5.返回至应用菜单页面，点击“设置”可进行具体系统事件的监听配置，应用提供了“一直”、“仅本次”及“从不”三个选项，其中“仅本次”选项是指本次应用运行期间将监听特定系统公共事件，应用退出后该选项将自动调整为“从不”。

6.返回至应用菜单页面，点击“关于”可查看应用版本信息及本示例的说明。

### 工程目录
```
├──entry/src/main/ets                           // 代码区
│  ├──application
│  │  └──MyAbilityStage.ets                    
│  ├──component
│  │  └──Header.ets                             // 头部组件
│  ├──ent


---
## custom-dialog-gathers
> 本示例使用自定义弹窗(CustomDialog)、全屏模态转场(bindContentCover)、半模态转场(bindSheet)等实现多种自定义弹窗。

源码: https://gitcode.com/HarmonyOS_Samples/custom-dialog-gathers

# 实现多种自定义弹窗的效果

### 介绍

本示例通过CustomDialog、bindContentCover、bindSheet等接口，实现多种样式的弹窗。帮助开发者掌握自定义弹窗开发的步骤，灵活的实现自己业务需要用到的弹窗场景。

### 效果预览

| 滑动选择弹窗                                   | 模态弹窗                                      | 半模态弹窗                                      | toast弹窗                                |
|------------------------------------------|-------------------------------------------|--------------------------------------------|----------------------------------------|
| ![image](screenshots/device/slide.gif)   | ![image](screenshots/device/modality.gif) | ![image](screenshots/device/semimodal.gif) | ![image](screenshots/device/toast.gif) |
| 隐私协议弹窗                                   | 全屏弹窗                                      | 自定义日历选择器弹窗                                 | 两级半模态+全屏弹窗                             |
| ![image](screenshots/device/privacy.gif) | ![image](screenshots/device/screen.gif)   | ![image](screenshots/device/customize.gif) | ![image](screenshots/device/add.gif)   |

### 使用说明：

加载完成后显示首页的8个自定义弹窗类别，点击对应按钮，进入相应的弹窗页面：
1. 滑动选择弹窗：点击页面底部两个按钮，会弹出对应的12小时制的时间选择器弹窗和文本选择器弹窗。
2. 模态弹窗：点击页面底部选择乘车人，会弹出模态弹窗，点击模态弹窗底部确认按钮，关闭模态弹窗。
3. 半模态弹窗：点击页面中选择点餐口味和餐具按钮，弹出半模态弹窗，点击遮罩层关闭弹窗。
4. toast弹窗：点击底部按钮，会弹出登陆成功的toast弹窗，3s后弹窗淡出消失。
5. 隐私协议弹窗：点击底部按钮弹出隐私协议弹窗，弹窗内容可以滚动，橙色的隐私协议可以点击，点击后会跳转到新页面，点击新页面的返回按钮回到隐私弹窗页面，弹窗不会关闭，点击同意或不同意关闭弹窗。
6. 全屏弹窗：点击底部按钮弹出全屏弹窗，点击左上角向下箭头可直接关闭弹窗；通过向下滑动会有阻尼效果，当滑动距离大于300时，弹窗会关闭，否则回弹到原位置。
7. 自定义日历选择器弹窗：点击页面中的日期会弹出日期选择器弹窗，当前日期之前的日期不可选，之后的日期可选，选择完成后弹窗关闭，日期更改为选中的日期。
8. 


---
## custom-dialog-selection-and-development
> 本示例主要介绍如何给应用添加自定义样式的弹窗，包括非模态弹窗：文本提示、图文提示、操作提示等；以及模态弹窗：确认弹窗、隐私弹窗、进度条、操作列表、评论回复弹窗等。

源码: https://gitcode.com/HarmonyOS_Samples/custom-dialog-selection-and-development

# **自定义弹窗选型与开发**
## 介绍
本示例主要介绍如何给应用添加自定义样式的弹窗，包括非模态弹窗：文本提示、图文提示、操作提示等；以及模态弹窗：确认弹窗、隐私弹窗、进度条、操作列表、评论回复弹窗等。旨在帮助开发者了解
如何实现这些弹窗，给应用添加这些交互弹窗，也能提升用户体验。
## 预览效果
<img src='./screenshots/device/image.png' width='320'>

## 工程目录
``` 
├──entry/src/main/ets                                   // 代码区
│  ├──entryability
│  |  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  |  └──EntryBackupAbility.ets
│  ├──pages
│  |  ├──AgreementPage.ets                              // 隐私协议页面
│  |  ├──CommentList.ets                                // 评论回复弹窗
│  |  ├──Index.ets                                      // 首页
│  |  ├──NavigationDialog.ets                           // 导航弹窗
│  |  └──PrivacyDialog.ets                              // 隐私弹窗
|  ├──uiComponent.ets
│  |  ├──ItemHead.ets                                   // 首页标题
│  |  └──SubItemHead.ets                                // 首页副标题
|  └──utils.ets
│     └──PromptActionClass.ets                          // 自定义弹窗
└──entry/src/main/resources                             // 应用资源目录
``` 

## 相关概念

* 非模态弹窗：用户可忽略弹窗，继续操作其他内容。弹窗出现时，背景界面仍可点击或滚动。通常自动消失或手动轻触关闭。
* 模态弹窗：用户必须处理弹窗内容（点击按钮或关闭），否则无法操作其他界面。弹窗出现时，背景内容通常变暗或模糊（防止误触）。

## 使用说明
1. 打开应用首页，点击文本提示，展示文本提示弹框。
2. 打开应用首页，点击图文提示，展示图文提示弹框。
3. 打开应用首页，点击操作提示，展示操作提示弹框。
4. 打开应用首页，点击确认弹窗，展示确认弹窗，需点击确认按钮关闭。
5. 打开应用首页，点击隐私弹窗，跳转至二级页面，点击按钮打开隐私弹窗，点击隐私协议跳转到二级页面，返回后隐私弹窗不消失。
6. 打开应用首页，点击进度条，展示进度条弹框，点击暂停后，进度停止增长；点击开始后，进度继续增长。
7. 打开应用首页，点击操作列表，展示操作列表弹框。
8. 打开应用首页，点击可变高度操作列表，展示可变高度操作列表弹框，长按并上下滑动


---
## custom-input-text
> 本示例通过输入法框架实现自会编辑框，可以绑定输入法应用，从输入法应用输入内容，显示和隐藏输入法。

源码: https://gitcode.com/HarmonyOS_Samples/custom-input-text

# 实现自绘编辑框

### 介绍

本示例通过输入法框架实现一个自绘编辑框，该自绘编辑框能够绑定输入法应用，实现监听输入法事件，显示和隐藏输入法，发送光标和编辑框属性等功能。

### 效果预览

|                  主页                   |
|:-------------------------------------:|
| ![home](screenshots/devices/main.png) |

使用说明

1.点击编辑框可以绑定并拉起输入法，可以从输入法键盘输入内容到编辑框。

2.可以点击**attach**/**detach**、**show**/**hide**、**on**/**off**按钮来绑定/解绑、显示/隐藏、开启监听/关闭监听。

3.输入光标信息后点击**updateCursor**向输入法应用发送光标信息，发送成功会右toast提示。

4.输入选中文本的开始和结束位置，点击**changeSelection**可以选中文本。

5.选择文本输入类型和Enter键类型后，点击**updateAttribute**可以更新拉起的输入法的输入类型和Enter键类型，依赖输入法应用是否适配。

### 工程目录

```
├──entry/src/main/ets/
│  ├──entryability
│  ├──components                         //自定义组件
│  │  └──CustomInputText.ets             //自绘编辑框组件
│  ├──pages
│  │  └──Index.ets                       //主页
│  └──utils
│     ├──Logger.ets                      //日志工具类
│     └──InputAttributeInit.ets          //编辑框属性工具类
└──entry/src/main/resources              // 应用静态资源目录

```

### 具体实现

* 自绘编辑框
  * 使用输入法框架实现组件绑定输入法应用，监听输入法事件，显示和隐藏输入法，发送光标和编辑框属性到输入法应用功能。
  * 源码链接：[Index.ets](./entry/src/main/ets/pages/Index.ets)，[CustomInputText.ets](./entry/src/main/ets/components/CustomInputText.ets)
  * 参考接口：@ohos.inputMethod
### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## custom-notification-badge
> 本示例主要展示了设定应用的桌面图标角标的功能，使用@ohos.notificationManager接口，进行桌面角标的设置，通知的发送，获取等。

源码: https://gitcode.com/HarmonyOS_Samples/custom-notification-badge

# 实现自定义通知角标功能

### 介绍

本示例主要展示了设定应用的桌面图标角标的功能，使用@ohos.notificationManager接口，进行桌面角标的设置，通知的发送，获取等。帮助开发者实现桌面图标的角标展示及通知栏通知数量的展示。

### 效果预览

| 主页/通知列表                        | 通知发送界面| 通知栏                                             |
|--------------------------------|--------------------------------|-------------------------------------------------|
| ![image](screenshots/main.png) | ![image](screenshots/notification_send.png) | ![image](screenshots/notification_get_list.png) |

使用说明

1. 在主界面，可以看到当前应用的所有消息通知；
2. 点击右下角Tab页签进入通知发送页面，点击对应的通知即可发送相应类型的通知，点击几次发送几条；
3. 点击左下角Tab页签进入通知列表，可以查看刚才发送的通知，通知右边会显示通知数量，点击相应的通知可进行通知读取，取消相应通知数量；
4. 下拉通知栏，可以看到角标数量，对应的通知数量。

### 工程目录

```
├──entry/src/main/ets/
│  ├──components
│  │  ├──NotificationList.ets                 // 通知列表控件
│  │  ├──NotificationPublish.ets              // 通知发送控件
│  │  └──TitleBar.ets                         // 标题栏控件
│  ├──entryability
│  │  └──EntryAbility.ets                     // 程序入口类
│  ├──feature
│  │  └──NotificationOperations.ets           // 对外提供发布通知的接口
│  └──pages
│     └──Index.ets                            // 首页  
├──entry/src/main/resources                   // 应用静态资源目录
│
├──notification/src/main/ets/
│  ├──notification
│  │  ├──NotificationContentUtil.ets          // 封装各种通知的主体内容
│  │  ├──NotificationManagementUtil.ets       // 封装通知列表，角标设置的接口
│  │  ├──NotificationRequestUtil.ets          // 接收通知的主体内容，返回完整的通知
│  │  ├──NotificationUtil.ets                 // 封装允许发布通知、发布通知、关闭通知的接口
│  │  └──WantAgentUtil.ets        


---
## customizing-long-press-menu
> 本示例介绍了给Webview页面中可点击元素（超链接/图片）绑定长按/鼠标右击时的自定义菜单的方案。

源码: https://gitcode.com/HarmonyOS_Samples/customizing-long-press-menu

# 实现Web组件的交互功能

### 介绍

本示例通过Web组件的onContextMenuShow函数，实现了应用加载HTML文件，并给HTML文件中的内容增加与用户交互的功能。帮助开发者掌握Web组件的开发，学会应用内网页如何与用户交互的处理。

### 效果图预览

![](./screenshots/device/web.gif)

##### 使用说明

长按Web页面中的图片或者链接元素，弹出自定义的Menu菜单，创建自定义的操作，如复制图片、使用浏览器打开链接、复制链接等。

### 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  ├──CommonConstants.ets         // 公共常量类
│  │  └──Utils.ets                   // 工具函数
│  ├──entryability
│  │  └──EntryAbility.ets            // 程序入口类
│  └──pages                  
│     └──Index.ets                   // 首页
└──entry/src/main/resources          // 应用静态资源目录
```

### 具体实现

1. 创建Web组件，导入示例HTML文件，绑定弹出菜单组件。

2. 调用Web组件的onContextMenuShow函数，获取当前页面元素弹窗菜单的信息，如位置信息、当前链接、以及是否存在图片等媒体元素、获取事件来源等。

3. 创建自定义菜单，在onContextMenuShow事件中能够获取触发菜单元素的信息和事件，根据这些内容动态创建自定义的弹出菜单。

### 相关权限

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## data-base-upgrade
> 本示例展示了对关系型数据库的操作，包括对数据库的常规增删改查操作以及对数据库事务的操作。

源码: https://gitcode.com/HarmonyOS_Samples/data-base-upgrade

# 数据库的备份与恢复

### 介绍

本示例通过使用relationalStore模块，实现对于数据库的基本增删改查操作，并实现了数据库的备份与恢复功能，给开发者提供一个简单的数据库操作示例。


### 效果预览
![image](screenshots/device/DataBaseUpgrade.gif)

使用说明

1、使用下拉选择框的方式提供几个可添加的字段名，然后提示用户输入对应的字段值。

2、点击版本更新后，会拉取正在更新的进度条弹窗，当进度条100%前点击叉号取消，会事务性回滚导致下方用户信息不更新。

3、点击版本更新后，会拉取正在更新的进度条弹窗，当进度条达到100%后，会事务性提交并刷新下方用户信息并刷新备份数据库。

4、点击版本回退按钮，会查询备份数据库并恢复。

5、版本回退的背景是在数据库在执行出问题时，可以回退到上一个版本，所以版本回退仅能回退一个版本，但在有新的版本更新之后，即可进行新的回退。


### 工程目录
```
├──entry/src/main/ets/
│  ├──common
│  │  ├──constants
│  │  │  └──CommonConstants.ets             // 常量类
│  │  └──utils
│  │     ├──CommonUtils.ets                 // 文字弹窗实现类
│  │     ├──DBUtils.ets                     // 数据库操作类
│  │     └──Logger.ets                      // 日志打印类
│  ├──entryability
│  │  └──EntryAbility.ets                   // 程序入口类
│  ├──pages
│  │  └──Index.ets                          // 主页面
│  ├──view
│  │  └──ProgressDialog.ets                 // 进度条弹窗实现类
│  └──viewmodel
│     └──userInfo.ets                       // 用户信息类
└──entry/src/main/resources                 // 应用静态资源目录
```
### 具体实现

* 本示例的主要功能都基于关系型数据库。
* 添加字段值的操作主要基于executeSql。
* 关于数据库事务性的操作主要参考commit和rollback。
* 版本回退的实现主要利用对数据库的备份与恢复，在版本更新时，备份数据库，在版本回退时，恢复数据库。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## data_augmentation_kit_samplecode_localchat_qa_arkts
> 本示例基于端侧问答模型，展示了一个轻量高效、响应迅速的智能问答助手。

源码: https://gitcode.com/HarmonyOS_Samples/data_augmentation_kit_samplecode_localchat_qa_arkts

# 基于端侧问答模型实现智能问答

## 介绍

本示例基于端侧问答模型，专为自然聊天对话场景设计，旨在打造轻量高效、响应迅速的智能问答助手。模型部署于本地设备，无需依赖云端，保障数据隐私与安全，同时支持实时交互与离线运行。通过模拟人类对话习惯，具备上下文理解能力，可精准识别用户意图，实现多轮对话与个性化回复，广泛适用于客服、教育、生活助手等场景，提升用户体验与交互自然度。

## 效果预览

| 对话                                            | 
|-----------------------------------------------|
| <img src='./screenshots/index.png' width=320> | 
## 使用说明

### 编译安装

使用DevEco Studio打开工程，并进行编译安装。

### 白名单申请


### 应用使用

1. 打开应用，同时会拉起模型管理应用。
2. 模型管理应用首次被拉起，前台弹出模型管理应用界面，同意在HarmonyOS上管理本地AI模型后，下载Qwen模型。
3. 模型管理应用非首次被拉起，打开桌面右下角隐藏的图标菜单，点击AI字样图标，弹出模型管理应用界面，下载Qwen模型。
4. 等待模型下载完成后，开始进行端侧问答。

## 工程目录

```
├──LocalChat/src/main/ets/
│  ├──localchatability
│  │   └──LocalChatAbility.ets              // Ability的生命周期回调内容
│  ├──localchatbackupability
│  │   └──LocalChatBackupAbility.ets        // BackupAbility的生命周期回调内容
│  └──pages
│      └──Index.ets                         // 端侧模型问答界面
├──resource
└──module.json5

```

## 具体实现

1. 使用@kit.DataAugmentationKit 能力实现。
2. 使用Init接口实现拉起端侧大模型。
3. 使用Chat接口实现智慧问答。

## 相关权限

需要网络权限：ohos.permission.INTERNET

## 依赖

不涉及

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：PC/2in1。
2. HarmonyOS系统：HarmonyOS 6.0 Beta3及以上。
3. DevEco Studio版本：DevEco Studio 6.0 Beta3及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0 Bete3 SDK及以上。
5. 请参考[端侧问答模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataaugmentation-localchatmodel)中：[约束与限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataaugmentation-localchatmodel#section2323123112812)



---
## debug
> 本示例通过使用@ohos.hidebug接口来获取当前应用内存使用情况。

源码: https://gitcode.com/HarmonyOS_Samples/debug

# 基于hidebug接口获取应用内存使用情况

### 介绍

本示例通过使用@ohos.hidebug接口，来获取当前应用内存使用情况，并以数字的形式展示出当前内存的使用情况，包括私有内存、共享内存以及PSS内存等指标。

### 效果预览

| 主页                                |Debug数据|
|-----------------------------------|--------------------------------|
| ![](screenshots/device/index.png) |![](screenshots/device/data.png)|


使用说明

1.点击界面右上方Debug图标，弹出Debug信息界面，显示当前应用内存使用情况；

2.再次点击右上方Debug图标，Debug信息界面消失。

### 工程目录

```
├──entry/src/main/ets/
│  ├─application
│  │  └─MyAbilityStage.ets     
│  ├──component
│  │  └──DebugInfo.ets                  // Debug信息页面
│  ├──data
│  │  └──Logger.ts                      // 日志工具
│  ├─entryability
│  │  └─EntryAbility.ets
│  └──pages
│     └──Index.ets                      // 首页
└──entry/src/main/resources             // 应用静态资源目录
```
### 具体实现

* 本实例获取Debug信息的功能结主要封装在Index，源码参考:[Index.ets](entry/src/main/ets/pages/Index.ets) 。
    * 获取Debug信息：在Index页面中通过点击事件调用hidebug.getPss()、hidebug.getSharedDirty()、hidebug.getPrivateDirty()等方法能够获取应用进程实际使用的物理内存大小、进程的共享脏内存大小、进程的私有脏内存大小。
  
### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## device-management-collection
> 本示例集合设备管理相关（非系统特性）不需要复杂功能展示的模块，展示了各个模块的基础功能。

源码: https://gitcode.com/HarmonyOS_Samples/device-management-collection

# 实现设备管理功能

## 介绍

本示例集合设备管理相关（非系统特性）不需要复杂功能展示的模块，展示了各个模块的基础功能。帮助开发者了解设备管理相关（非系统特性）的模块功能。包含：

- @ohos.batteryInfo (电量信息)
- @ohos.runningLock (Runninglock锁)
- @ohos.power (系统电源管理)
- @ohos.settings (设置数据项名称)
- @ohos.thermal (热管理)
- @ohos.usbManager (USB管理)

## 效果预览

|                   **主页**                   |                  **电量信息**                  |                  **RunningLock锁**                   |               **系统电源管理**               |
|:------------------------------------------:|:------------------------------------------:|:---------------------------------------------------:|:--------------------------------------:|
|   ![home](screenshots/devices/home.png)    | ![battery](screenshots/devices/battery.png)  | ![runninglock](screenshots/devices/runninglock.png) | ![power](screenshots/devices/power.png) |
|                **设置数据项名称**                 |                   **热管理**                   |                      **USB管理**                      |
| ![settings](screenshots/devices/settings.png) |  ![thermal](screenshots/devices/thermal.png)   |        ![usb](screenshots/devices/usb.png)        |

使用说明

1.首页展示语言基础类库各个子模块菜单，点击进入对应的模块页面。

2.各个子模块界面中点击功能按钮完成各个功能。

3.电量信息：进入电量信息页面，展示设备电量相关信息。

4.RunningLock锁：点击按钮实现设备支持的休眠锁类型。

5.系统电源管理：点击按钮分别实现获取亮灭屏状态、获取电源模式功能。

6.设置数据项名称：点击按钮分别实现获取数据项uri。

7.热管理：进入热管理页面，展示当前设备热档位信息、设备过热时提示用户。

8.USB管理：打开监听开关后插入USB设备，会有提示并刷新设备列表，关闭监听后清空列表，再次插入USB设备不会提示和自动刷新，下拉设备列表可以手动刷新设备列表。

## 工程目录

```
├──common/src/main/ets/                      


---
## device-security-kit-sample-code-business-risk-intelligent-detection
> 本示例基于业务风险检测服务能力，提供场景（防作弊、反欺诈、违规内容检测等）的业务风险决策能力。

源码: https://gitcode.com/HarmonyOS_Samples/device-security-kit-sample-code-business-risk-intelligent-detection

# 实现业务风险检测（ArkTS）

## 介绍

本示例向您介绍如何在应用中使用业务风险检测接口进行涉诈剧本检测、模拟点击检测和模拟点击增强检测。

需要使用设备安全服务接口 **@kit.DeviceSecurityKit**。

## 效果预览
![效果图](screenshots/device/home_page.png)

## 工程的配置与使用

### 在DevEco中配置工程的步骤如下

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
2. 打开应用，使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)配置的应用包名替换app.json5文件中的bundleName属性值。
3. 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)开通涉诈剧本检测服务，具体参考[Device Security Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)。模拟点击检测、模拟点击增强检测无需开通服务。

#### 工程使用说明
1. 运行该应用前，先对设备进行联网。
2. 运行该应用：
   1. 点击 "FraudRiskDetect" 按钮获取涉诈剧本检测结果；
   2. 点击 "SimulatedClickRiskDetect" 按钮获取模拟点击检测结果；
   3. 点击 "SimulatedClickRiskEnhancedDetect" 按钮获取模拟点击增强检测结果。
   
   如果获取成功，页面会显示检测结果，如果获取失败，页面会显示相应的错误码。
3. 获取检测结果后：
   1. 涉诈剧本检测结果建议在服务端侧进行结果解析和签名验证；
   2. 模拟点击检测结果建议在服务端侧进行结果解析；
   3. 模拟点击增强检测结果建议在服务端侧进行结果解析和签名验证。

## 工程目录
```
└──entry/src/main/ets            // 代码区  
   └── entryability                    
   │   └── EntryAbility.ets          // 程序入口类  
   └── model                
   │   └── FraudRiskDetectModel.ets    // 涉诈剧本检测结果获取类  
   │   └── SimulatedClickRiskDetectModel.ets    // 模拟点击检测结果获取类
   |   └── SimulatedClickRiskEnhancedDetectModel.ets    // 模


---
## device-security-kit-sample-code-business-risk-intelligent-detection-server-demo-java
> 本示例基于业务风险检测服务能力，提供场景（防作弊、反欺诈、违规内容检测等）的业务风险决策能力。

源码: https://gitcode.com/HarmonyOS_Samples/device-security-kit-sample-code-business-risk-intelligent-detection-server-demo-java

# BusinessRiskIntelligentDetection Server Sample

## 目录

 * [介绍](#介绍)
 * [运行步骤](#运行步骤)
 * [支持环境](#支持环境)
 * [示例代码](#示例代码)
 * [许可证](#许可证)


## 介绍
BusinessRiskIntelligentDetection Server Sample 提供了在服务端验证结果的示例代码。
## 运行步骤
在运行BusinessRiskIntelligentDetection Server Sample前，请检查是否安装Java以及Maven。
1.使用maven工具构建工程。
2.运行main程序。
3.输入检测结果，即：JWS字符串。
4.输入证书文件路径。
5.如果验证成功，则输出payload内容，否则输出错误信息。

## 支持环境
Java 1.8 及以上

## 示例代码

### 涉诈剧本检测
1. 解析JWS，获取header，payload，signature。
2. 从header中获取证书链，使用[Huawei CBG Root CA](https://pki.consumer.huawei.com/ca/cer/RootCaG2Ecdsa.cer)证书对其进行验证。
3. 校验证书链中的叶证书域名，域名：riskopenapi.platform.hicloud.com。
4. 从signature中获取签名，校验其签名。
5. 从payload中获取涉诈剧本检测结果，格式和样例摘录如下：
```json
{
  "timestampMs": 9xxxxxxxxx,
  "nonce": "Rxxxxxxxxx",
  "appId": "xxxxxxxxx",
  "version": 1,
  "riskScore": 90,
  "tags": [
    "phishing",
    "malware",
    "interdiction",
    "control"
  ]
}
```
更多信息请访问[涉诈剧本检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-fraudriskdetection)

### 模拟点击增强检测
1. 解析JWS，获取header，payload，signature。
2. 从header中获取证书链，使用[Huawei CBG Device Attestation Root CA](https://pki.consumer.huawei.com/ca/cer/Huawei_CBG_ECC_Device_Attestation_Root_CA.cer)证书对其进行验证。
3. 校验证书链中的Common Name，Common Name：Harmony OS Device Attestation Service。
4. 从signature中获取签名，校验其签名。
5. 从payload中获取模拟点击检测结果，格式和样例摘录如下：
```json
{
  "timestampMs": 9860437986543,
  "version": 1,
  "riskDecision": "fake",
  "tags": ["AbnormalTap"]
}

```
更多信息请访问[模拟点击增强检测](https://developer.huawei


---
## device-security-kit-samplecode-safetydetect-serverdemo-java
源码: https://gitcode.com/HarmonyOS_Samples/device-security-kit-samplecode-safetydetect-serverdemo-java

# SafetyDetect SysIntegrity Server Sample

[English](readme_en.md) | 中文

## 目录

 * [介绍](#介绍)
 * [运行步骤](#运行步骤)
 * [支持环境](#支持环境)
 * [示例代码](#示例代码)
 * [许可证](#许可证)


## 介绍
SafetyDetect SysIntegrity Server Sample 提供了在服务端验证结果的示例代码。
## 运行步骤
在运行SafetyDetect SysIntegrity Server Sample之前，请检查是否安装Java以及Maven。
1.使用maven工具构建工程。
2.运行main程序。
3.输入系统完整性检测结果，即：JWS字符串。
4.输入root G2 证书文件路径。
5.如果验证成功，则输出payload内容，否则输出错误信息。

## 支持环境
Java 1.7 及以上

## 示例代码

1. 解析JWS，获取header，payload，signature。
2. 从header中获取证书链，使用[HUAWEI CBG root G2](https://h5hosting-drcn.dbankcdn.cn/cch5/crl/pki_CA_RootG2Ca/RootG2Ca.cer)证书对其进行验证。
3. 校验证书链中是否包含3级证书；校验证书链中x5c[0]证书的域名是否为sysintegrity.platform.hicloud.com。
4. 从signature中获取签名，校验其签名。
5. 从payload中获取完整性验证结果，格式和样例摘录如下：
```json
{
  "hapCertificateSha256": "xxx",
  "hapBundleName": "xxx",
  "appId": "xxx",
  "basicIntegrity": false,
  "detail": [
    "attack",
    "jailbreak",
    "emulator"
  ],
  "nonce": "xxx",
  "timestamp": 1604098577327
}
```
更多信息请访问[系统完整性检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-sysintegrity-check)
##  许可证
此代码已获得 [Apache License, version 2.0](http://www.apache.org/licenses/LICENSE-2.0).




---
## device-security-kit_-sample-code_-trusted-app-service-demo_-ark-ts
源码: https://gitcode.com/HarmonyOS_Samples/device-security-kit_-sample-code_-trusted-app-service-demo_-ark-ts

# 实现可信应用服务（ArkTS）

## 介绍

本示例向您介绍如何在应用中使用可信应用服务开发安全摄像头和安全地理位置功能。

需要使用可信应用服务接口 **@kit.DeviceSecurityKit**。

## 效果预览
![效果图](screenshots/device/home_page_cn.png)

## Sample工程的配置与使用

### 在DevEco中配置Sample工程的步骤如下

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
2. 打开Sample应用，使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)配置的应用包名替换app.json5文件中的bundleName属性值。
3. 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)开通可信应用服务，具体请参见[Device Security Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)。

#### Sample工程使用说明
1. 运行该Sample应用前，先对设备进行联网，并打开位置信息。
2. 运行该Sample应用，点击"打开安全相机"按钮打开安全摄像头，圆形组件中会显示前置摄像头采集到的安全图像，如果验证签名失败会显示文字提示，点击"关闭安全相机"按钮关闭安全摄像头。
3. 运行该Sample应用，点击"获取地理位置（速度优先）"按钮，文本框中会显示速度优先策略下获取到的位置信息，点击"获取地理位置（精度优先）"按钮，文本框中会显示速度优先策略下获取到的位置信息，如果获取位置信息失败，或者验证签名失败，会显示文字提示。

## 工程目录
```
├─entry/src/main/ets             // 代码区  
│ ├─common  
│ │ └─CertChain.ets              // 证书链相关操作类  
│ │ └─Permission.ets             // 权限相关操作类  
│ │ └─TrustedServiceOption.ets   // 可信应用服务接口参数  
│ ├─entryability  
│ │ └─EntryAbility.ets           // 程序入口类  
│ ├─entrybackupability  
│ │ └─EntryBackupAbility.ets  
│ ├─model  
│ │ └─SecureCamera.ets           // 安全相机类  
│ │ └─EntryBackupAbility.ets     // 安全地理位置类  
│ ├─pa


---
## distributed-view-show
源码: https://gitcode.com/HarmonyOS_Samples/distributed-view-show

# 基于应用接续实现分布式视频播放器功能

### 介绍

基于ArkTS扩展的声明式开发范式编程语言编写的一个分布式视频播放器，主要包括一个直播视频播放界面，实现视频播放时可以从一台设备迁移到另一台设备继续运行，来选择更合适的设备继续执行播放功能以及平板视频播放时协同调用手机编辑发送弹幕功能。

### 效果预览
![dia.gif](./screenshots/devices/dia.gif)

**使用说明**

1. 准备手机端与平板端两台设备，并且登录同一华为账号，双端设备打开WI-FI和蓝牙，建议双端设备接入同一个局域网，可提升数据传输的速度
2. 双端设备均安装此应用
3. 滑动浏览手机端视频，打开平板端应用
4. 点击平板端手机输入按钮，调起手机端输入内容，提交后平板端查看

### 工程目录

```
├──entry/src/main/ets             // 代码区
│  ├──common
│  │  └──Constants.ets            // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets         // 程序入口类
│  ├──inputability
│  │  └──InputAbility.ets         // 手机文本编辑入口类
│  ├──model
│  │  ├──LiveData.ets             // 直播视频相关数据
│  │  └──LiveDataModel.ets        // 直播视频类
│  ├──pages
│  │  ├──CommentPage.ets          // 弹幕显示界面
│  │  ├──InputPage.ets            // 手机评论编辑界面
│  │  └──LivePage.ets             // 视频播放界面
│  └──utils
│     ├──Logger.ets               // 日志类
│     └──WindowUtil.ets           // 界面控制类
└──entry/src/main/resource        // 应用静态资源目录
```

### 具体实现
1. 在实现协同接口前，应用需要申请协同所需的访问控制权ohos.permission.DISTRIBUTED_DATASYNC。
   在requestPermissions字段中增加权限声明ohos.permission.DISTRIBUTED_DATASYNC
2. 同时需要在应用首次启动时弹窗向用户申请授权，在用户手动允许授权后，应用才会真正获取相应权限，从而成功访问操作目标对象。
   打开“entry > src > entryability > EntryAbility.ets” 文件，在EntryAbility类中实现以下函数，从而在调用时动态弹窗向用户申请权限。
3. 获取目标设备的设备ID。
4. 在发起端设置目标组件参数，调用startAbilityForResult()接口启动目标端UIAbility，异步回调中的data用于接收目标端UIAbility停止自身后返回给调用方UIAbility的信息。
5. 在目标端UIAbility任务完成后，调用terminateSelfWithResult()方法，将数据返回给发起端的UIAbility。
6. 发起端UIAbility


---
## drawing-to-xcomponent
> 本篇Sample主要介绍如何使用Drawing绘制一个bitmap，然后通过NativeWindow贴图到XComponent的双缓冲实现。

源码: https://gitcode.com/HarmonyOS_Samples/drawing-to-xcomponent

# 基于XComponent组件实现双缓冲功能

## 简介

本篇Sample主要介绍如何使用Drawing绘制一个bitmap，然后通过NativeWindow贴图到XComponent的双缓冲实现。

双缓冲：在内存中创建一片内存区域，把将要绘制的图片预先绘制到内存中，在绘制显示的时候直接获取缓冲区的图片进行绘制。更具体一点来说：先通过Drawing方法将要绘制的所有的图形绘制到一个Bitmap上也就是先在内存空间完成，然后获取位图的像素地址、并将其拷贝到XComponent的NativeWindow地址。完成贴图，将图片显示在屏幕上。

界面如下所示：

![synchronized_operation](screenshots/device/img.png)

## 工程目录

```
├──entry/src/main/cpp                         // C++ 代码区
│  ├──common
│  │  └──log_common.h                         // 日志文件
│  ├──plugin                                  // 生命周期管理模块
│  │  ├──plugin_manager.cpp                   
│  │  └──plugin_manager.h                     
│  ├──samples                                 // samples渲染模块
│  │  ├──sample_bitmap.cpp                    
│  │  └──sample_bitmap.h  
│  ├──types
│  │  └──libentry                             // C++接口导出
│  │     ├──index.d.ts                        
│  │     └──oh-package.josn5                 
│  ├──CMakeLists.txt                          // CMake配置文件
│  └──hello.cpp                               // Native模块注册
├──entry/src/main/ets                         // ets 代码区
│  ├──common
│  │  └──CommonConstants.ets                  // 常量定义文件
│  ├──entryability
│  │  └──EntryAbility.ets       
│  ├──interface
│  │  └──XComponentContext.ts                 // 接口文件
│  └──pages
│     └──Index.ets                            // 主页界面
└──entry/src/main/resources                   // 应用资源目录
```

## 相关概念

- Drawing: 提供包括2D图形渲染、文字绘制和图片显示等功能函数。
- NativeWindow: 提供NativeWindow功能，


---
## easygo-parallel-shopping
> 本示例以Navigation路由实现的购物类应用为载体，通过easyGo兼容方案配置实现平行视界效果。

源码: https://gitcode.com/HarmonyOS_Samples/easygo-parallel-shopping

# easygo-parallel-shopping

本示例以Navigation路由实现的购物类应用为载体，通过easyGo兼容方案配置实现平行视界效果。


---
## effect-kit
> 本示例介绍使用Image库以及EffectKit库中的colorPicker对目标图片进行取色，将获取的颜色作为背景渐变色，通过Swiper组件对图片进行轮播。

源码: https://gitcode.com/HarmonyOS_Samples/effect-kit

# 基于ColorPicker实现自适应背景色功能

### 介绍

本示例介绍使用Image库以及EffectKit库中的colorPicker对目标图片进行取色，将获取的颜色作为背景渐变色，通过Swiper组件对图片进行轮播。基于该案例开发者可以熟练的使用ColorPicker相关接口以及图片的自动轮播设置。

### 效果图预览

<img src="screenshots/device/effect_kit.png" width=320>

**使用说明**

直接进入页面，对图片进行左右滑动，或者等待2s后图片自动轮播，图片切换后背景颜色会自动改变。

### 实现思路

1. 在事件onAnimationStart切换动画过程中通过Image模块相关能力，获取图片颜色平均值，使用effectKit库中的ColorPicker智能取色器进行颜色取值。
2. 同时通过接口animateTo开启背景颜色渲染的属性动画。全局界面开启沉浸式状态栏。
3. 通过属性linearGradient设置背景色渲染方向以及渲染氛围。

### 高性能知识点

**不涉及**

### 工程结构&模块类型
```
├──entry/src/main/ets                         // ets 代码区
│  ├──constants
│  │  └──CommonConstants.ets                  // 常量定义文件  
│  ├──entryability
│  │  └──EntryAbility.ets       
│  └──pages
│     └──Index.ets                            // 主页界面
└──entry/src/main/resources                   // 应用资源目录
```

### 模块依赖

**不涉及**

### 参考资料

**不涉及**

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## enterprise-data-guard-kit_-sample-code-arkts
源码: https://gitcode.com/HarmonyOS_Samples/enterprise-data-guard-kit_-sample-code-arkts

# 企业数据保护服务

## 介绍

本示例主要展示了数据保护服务相关的功能，使用@kit.EnterpriseDataGuardKit、@kit.CoreFileKit等接口，实现了打开读取文件、设置查询文件标签、扫描公共目录文件清单、删除文件、下发KIA文件清单、下发网络拦截策略和查询文件URI的功能。

仅供企业安全管控类MDM应用申请权限后使用。

## 效果预览

| 应用入口                                                  | 应用主页                                                   | 接口使用按钮                                                   | 日志输出                                                     |
|-------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| 点击图标打开应用                                              | 应用主页显示在设备屏幕                                            | 点击接口测试按钮调用接口                                             | 接口调用通过日志输出                                               |
| <img src="./screenshot/head.png" style="zoom:25%;" /> | <img src="./screenshot/index.png" style="zoom:25%;" /> | <img src="./screenshot/btnPage.png" style="zoom:25%;" /> | <img src="./screenshot/logPage.png" style="zoom:25%;" /> |

使用说明

1.在项目根目录下执行[test.bat](test.bat)脚本，发送[test.json](test.json)到设备上。

2.在应用中心选中应用"label"打开sample应用。

3.打开应用后应用界面会显示在屏幕上。

4.点击按钮调用对应接口，如点击"测试1：扫描公共目录"。

5.接口调用结果输出到日志中。

## 工程目录

```
├──entry/src/main/ets                         // 代码区
│  ├──svcability
│  │  ├──ScanFileGuard.ts                     // 文件扫描工具类
│  ├──entryAbility  
│  │  └──EntryAbility.ts                      


---
## enterprisespacekit_samplecode_filetransfer_arkts
> 本示例基于Enterprise Space Kit（企业数字空间服务）的文件传输能力，实现企业应用下发空间互传策略。

源码: https://gitcode.com/HarmonyOS_Samples/enterprisespacekit_samplecode_filetransfer_arkts

# 实现空间互传的策略下发

## 介绍

本示例主要展示了企业空间服务管理相关的功能，使用@kit.EnterpriseSpaceKit接口，实现了设置审计信息、获取审计信息的功能。

供企业管控类MDM应用申请权限后使用。

## 效果预览

| 应用入口                                                  | 应用主页                                                   | 接口使用按钮                                                           | 日志输出                                                     |
|----------------------------------------------------|-----------------------------------------------------|------------------------------------------------------------------|-------------------------------------------------------|
| 点击图标打开应用                                              | 应用主页显示在设备屏幕                                            | 点击接口测试按钮调用接口                                                     | 接口调用通过日志输出                                               |
| <img src="./screenshot/head.png" style="zoom:25%;" /> | <img src="./screenshot/SampleCode_0_cn.png" style="zoom:25%;" /> | <img src="./screenshot/SampleCode_1_cn.png" style="zoom:25%;" /> | <img src="./screenshot/logPage.png" style="zoom:25%;" /> |

使用说明

1.在应用中心选中应用"label"打开sample应用。

2.打开应用后应用界面会显示在屏幕上。

3.点击按钮调用对应接口，如点击"设置审计信息"。

4.接口调用结果输出到日志中。

## 工程目录

```
├──entry/src/main/ets               // 代码区
│  ├──entryability
│  │  └──EntryAbility.ts            // 程序入口类
│  ├──pages
│  │  └──Index.ets                  // 主界面
│  └──svcability
│     └──fileTransferService.ets    //接口调用
└──entry/src/main/resources         // 资源文件目录
```

## 具体实现（接口参考@hms.enter


---
## exception-handling
源码: https://gitcode.com/HarmonyOS_Samples/exception-handling

# 实现应用异常处理功能

### 介绍

本示例通过应用事件打点hiAppEvent获取上一次应用崩溃或应用卡死的异常信息，并将异常数据信息加载到页面上。帮助开发者掌握应用异常信息的获取方法，实现应用异常的快速定位和及时处理。

### 效果图预览
| 默认页面                                  | 构建异常事件                                | 捕获异常事件                                |
|---------------------------------------|---------------------------------------|---------------------------------------|
| ![](screenshots/device/Preview_1.png) | ![](screenshots/device/Preview_2.png) | ![](screenshots/device/Preview_3.png) |

**使用说明**

1. 点击构建应用崩溃事件，3s之后应用退出，然后打开应用进入应用异常页面，隔1min左右后，显示上次异常退出信息。 
2. 点击构建应用卡死事件，需手动退出，然后打开应用进入应用异常页面，隔1min左右后，显示上次异常退出信息。

### 实现思路

1. 构建应用异常。源码参考[Index.ets](./entry/src/main/ets/pages/Index.ets)。
2. 应用退出后，进入本页面，等待订阅消息通知，待收到订阅消息后，通过EventSubscription.ets中的onReceive函数，接收到异常信息数据，并通过AppStorage.setOrCreate('appEventGroups',异常信息数据)双向绑定异常信息，源码参考代码可参考[EventSubscription.ets](./entry/src/main/ets/model/EventSubscription.ets)。
3. @StorageLink('appEventGroups')接收订阅事件函数传递的事件组信息，调用getFaultMessage函数对信息进行处理，将处理后的信息通过 this.faultDataSource.pushData(message) 添加到懒加载数据源中，并通过this.faultDataSource.persistenceStorage()执行持久化存储，最后通过使用LazyForEach将数据信息加载到页面上。具体源码参考[Index.ets](./entry/src/main/ets/pages/Index.ets)。
4. 以上代码中有引用懒加载数据类和持久化存储类，源码可参考[DataSource.ets](./entry/src/main/ets/model/DataSource.ets)和[PreferencesManager.ets](./entry/src/main/ets/model/PreferencesManager.ets)。

### 工程结构&模块类型

   ```
    ├───entry/src/main/ets                             
    │   ├───entryability
    │   │   └──EntryAbility.ets     


---
## faqsnippets
源码: https://gitcode.com/HarmonyOS_Samples/faqsnippets

# FAQSnippets

#### 介绍
{**以下是 Gitee 平台说明，您可以替换此简介**
Gitee 是 OSCHINA 推出的基于 Git 的代码托管平台（同时支持 SVN）。专为开发者提供稳定、高效、安全的云端软件开发协作平台
无论是个人、团队、或是企业，都能够用 Gitee 实现代码托管、项目管理、协作开发。企业项目请看 [https://gitee.com/enterprises](https://gitee.com/enterprises)}

#### 软件架构
软件架构说明


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)



---
## fastkit_samplecode_rectpartition_cpp
> 本示例基于FAST Kit算法加速套件，利用矩形划分求解器接口实现矩形区域划分功能，展示FAST Kit在网格数据处理和空间几何计算等潜在场景中的算法加速能力。

源码: https://gitcode.com/HarmonyOS_Samples/fastkit_samplecode_rectpartition_cpp

# 基于FAST Kit实现矩形区域划分

## 介绍
本示例基于FAST Kit算法加速套件，利用矩形划分求解器接口实现矩形区域划分功能，展示FAST Kit在网格数据处理和空间几何计算等潜在场景中的算法加速能力。

矩形划分求解器接收若干个彼此不相交的矩形区域作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形区域数量尽可能少。

矩形划分求解器运行的时间复杂度为$O(N\log N)$，其中$N$为输入矩形数量。可以高效处理大规模输入数据。此示例处理的区域数据规模较小，仅作为演示目的。

## 效果预览
| 应用启动后默认界面                                       | 用户点击按钮后显示矩形划分结果                          |
| -------------------------------------------------------- | ------------------------------------------------------- |
| <img src="screenshots/device/beforeclick.png" width=320> | <img src="screenshots/device/afterclick.png" width=320> |

## 使用说明
1. 打开应用，显示默认界面。其中上方网格区域为算法输入的编辑区域（算法输入区域由橙色表示）。
1. 点击中间的按钮计算矩形区域划分。
1. 点击后，在下方的网格展示算法输出。可以看到算法将橙色输入区域被划分为若干矩形（输出矩形由随机颜色表示）。
1. 之后，用户可以继续点击上方网格自由编辑，然后点击中间按钮进行计算，查看矩形划分结果。

## 工程目录
```       
├──entry/src/main/cpp           // cpp代码区
│  ├──types                                
│  │  └──libentry        
│  │     └──Index.d.ts          // native层接口注册文件
│  ├──CMakeLists.txt            // native层编译配置
│  └──napi_init.cpp             // native api层接口的具体实现函数，包括矩形划分API调用
├──entry/src/main/ets           // ets代码区
│  ├──entryability 
│  │  └──EntryAbility.ets       // 程序入口
│  ├──entrybackupability 
│  │  └──EntryBackupAbility.ets // 程序备份恢复
│  └──pages 
│     └──Index.ets              // 主页界面
└──entry/src/main/resources     // 应用资源目录
```

## 具体实现

### UI部分

UI部分代码写在`Index.ets`主页界面中，其中网格部分使用ArkUI中的Grid网格容器组件实现。如何使用Grid组件不是本示例重点，如有需要请查阅相关官方文档，此处不进行赘述。

UI接受用户输入后，以跨语言调用的方式将输入矩形数据传入给Native层，在Native层调用


---
## file-compression
> 本示例介绍通过使用@ohos.file.fs和@ohos/commons-compress三方库等接口，实现不同资源路径下文件的压缩与解压，包含zip、gzip、tar、7z压缩格式。

源码: https://gitcode.com/HarmonyOS_Samples/file-compression

# 实现文件压缩与解压

### 介绍

本示例介绍通过使用@ohos.file.fs和@ohos/commons-compress三方库等接口，导入rawfile中文件，可以进行预览和压缩解压操作，开发者可以进行zip、gzip、tar、7z格式文件的操作。

### 效果图预览

![](screenshots/device/phone.gif)

### 使用说明

1. 点击预览预览文本内容，点击压缩选择压缩格式进行文件压缩。
2. 压缩后文件点击解压进行解压，解压后文件保存在在新目录/decompressedFile中，重复解压覆盖原有文件。
3. 点击从资源文件导入，导入rawfile中文件，可以进行预览和压缩解压操作。

### 目录结构

```
handletabs
│  ├──constant
│  │  └──FileConstants.ets
│  ├──entryability
│  │  └──EntryAbility.ets                        // 应用入口类
│  ├──model
│  │  └──FileItem.ets                            // 文件类
│  ├──pages
│  │  └──Index.ets                               // 首页
│  ├──utils
│  │  ├──CompressUtil.ets                        // 压缩工具类
│  │  ├──FileUtil.ets                            // 文件工具类
│  │  └──Logger.ets                              // 日志工具类
│  └──view
│     └──DialogView.ets                          // 弹窗视图
└────entry/src/main/resources 
```

### 相关权限
不涉及。

### 依赖
运行前需安装包common-compress，命令行执行"ohpm install @ohos/commons-compress"。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## fit-for-dark-mode
> 本示例通过@ohos.app.ability.ConfigurationConstant等接口，进行深色模式的设置。

源码: https://gitcode.com/HarmonyOS_Samples/fit-for-dark-mode

# 实现深色模式功能

## 简介
本示例采用深色模式适配相关技术，确保应用在系统深浅色模式切换时界面效果美观自然，实现颜色资源适配、媒体资源适配、状态栏适配等。应用内还提供用户可控的深浅色模式开关，满足用户个性化需求，实现应用在不同模式下的深浅色切换。

## 效果预览：
<img src="screenshots/phone.png" width=320>

## 工程目录

```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口
│  ├──pages   
│  │  ├──DarkModeSetting.ets            // 深色模式设置页面
│  │  ├──Home.ets                       // 主页
│  │  ├──Index.ets                      // 程序页面入口
│  │  └──Mine.ets                       // 我的页面
│  ├──view                  
│  │  ├──FinishedTodoItem.ets           // 已完成的Todo组件    
│  │  └──TodoItem.ets                   // Todo组件
│  └──viewmodel                  
│     ├──ColorModeChangeFunctions.ets   // 深浅模式切换功能函数封装
│     ├──Todo.ets                       // Todo类
│     └──TodoViewModel.ets              // Todo数据
└──entry/src/main/resources             // 应用静态资源目录
```
使用说明：
- 默认应用跟随系统深浅色进行切换，在设置->显示与亮度->深色模式->全天开启中进行打开关闭，应用会跟随进行深浅色显示。
- 应用内提供关闭跟随系统切换功能，在我的->深色模式中关闭跟随系统设置，应用将始终保持浅色模式。
- 应用内提供手动控制深浅色开关，在我的->深色模式中打开/关闭深色模式，应用会跟随设置的值选择深色/浅色显示。

## 具体实现

1. 颜色资源适配例如文本颜色，组件背景颜色等。有以下两种方案：
   1. 使用系统预留的颜色资源值。
   2. 开发者进行手动适配。需要开发者创建src/main/resources/dark/element目录，并在目录下创建color.json文件，在文件中设置页面元素在深色模式下的颜色值，并在src/main/resources/base/element/color.json文件中设置浅色模式下的页面元素颜色值。
2. 图片与图标资源适配。若需要应用在深色模式与浅色模式下呈现不同的图片/图标，需要开发者创建出src/main/resources/dark/media目录，用于放置应用在深色模式下的图片与图标资源，并在src/main/resources/base/media放入同名但不同的静态资源。
3. 系统状态栏适配。默认情况下若应用未启用沉浸式，则不会存在状态栏适配问题，若应用设置了沉浸式，可能会导致页面的背景色与状态栏文字颜色对比度过低，对


---
## fluent-blog
> 本示例介绍如何流畅刷页面。

源码: https://gitcode.com/HarmonyOS_Samples/fluent-blog

# 实现流畅刷文章功能

### 介绍

本示例实现了文章和媒体文件浏览的功能，通过设置组件的属性来控制屏幕刷新率，达到低功耗的目的，参考本示例可学习开发类似博客场景，并进行低功耗的适配。

### 效果预览

|                               主页                               |
|:--------------------------------------------------------------:|
| <img src="./screenshot/device/ltpo.png" width="320"/> |

##### 使用说明

1. 上下滑动页面，流畅刷文章；
2. 点击第一个视频，可进入视频播放界面。

### 工程目录

```

├──entry/src/main/ets/
│  ├──constant
│  │  └──Constant.ets                        // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets                    // 程序入口类
│  ├──pages
│  │  ├──Index.ets                           // 应用首页
│  │  └──NewPlayPage.ets                     // 视频页
│  ├──segment
│  │  └──segment.ets                         // 动画案例     
│  ├──view
│  │  ├──AVPlayerItem.ets                    // AVPlayer页
│  │  ├──ButtonItem.ets                      // Button Item页
│  │  ├──ImageModifier.ets                   // 图片页
│  │  ├──MuliGrid.ets                        // 布局页
│  │  ├──SampleUnitAVPlayView.ets            // AVPlayer样例页
│  │  ├──SampleUnitPicView.ets               // 图片样例页
│  │  ├──SampleUnitVideoSecondView.ets       // 视频样例页
│  │  ├──SampleUnitVideoView.ets             // 视频样例页
│  │  ├──SampleUnitView.ets                  // 样例展示页
│  │  └──TitleAreaItem.ets                   // 标题页
│  └──viewmodel
│     ├──BasicDataSource.ets                 // 数据源
│     ├──ButtonUnitItem.ets                  // 按钮item类型
│     ├──SampleUnitItem.ets                  // 案例item类型
│     └──TitleUnitItem.ets            


---
## fluent-news-homepage
> 本场景解决方案主要面向于新闻类页面开发人员，指导开发者从零开始构建一个新闻类的首页面，包含地址选择、tabs和tabContent切换的动态图标和流畅动效、下拉刷新上拉加载、首页feed流等常见功能，及功能的流畅体验。

源码: https://gitcode.com/HarmonyOS_Samples/fluent-news-homepage

# 基于原生组件实现新闻类首页流畅体验

### 介绍
本场景解决方案主要面向于新闻类页面开发人员，指导开发者从零开始构建一个新闻类的首页面，包含地址选择、tabs和tabContent切换的动态图标和流畅动效、下拉刷新上拉加载、首页feed流等常见功能，及功能的流畅体验。

### 效果预览

<img src='screenshots/device/NewsDemo.gif' width='320'>

使用说明

1. 获取地理位置的权限；
2. 点击位置信息，跳转地址页，可修改当前位置信息；
3. 点击顶部页签或者滑动切换页面，页签同步切换；
4. 点击底部页签切换页面，同步切换页签，触发页签切换的动画效果；
5. 下拉刷新页面信息；
6. 上拉加载页面信息；
7. 点击右下角按钮回弹至顶部。


### 工程目录
```
├──entry/src/main/ets/
│  ├──common
│  │  └──lottie                    // 动画
│  ├──constants
│  │  ├──BreakpointConstants.ets   // 断点常量
│  │  ├──CommonConstants.ets       // 常用常量
│  │  └──HomeConstants.ets         // 主页常量
│  ├──entryability
│  │  └──EntryAbility.ets          // Ability的生命周期回调内容
│  ├──pages
│  │  ├──CitySearch.ets            // 城市查询
│  │  └──Index.ets                 // 首页
│  ├──util                  
│  │  ├──BreakpointType.ets        // 断点类型
│  │  └──ResourceUtil.ets          // 路由数据
│  ├──view                  
│  │  ├──CityView.ets              // 城市列表组件
│  │  ├──Home.ets                  // 主页组件
│  │  ├──HomeContent.ets           // tab内容组件
│  │  ├──HomeHeader.ets            // 主页头部组件
│  │  ├──NewsChannel.ets           // 新闻渠道组件
│  │  ├──PullToRefreshNews.ets     // 拉取刷新新闻组件
│  │  ├──SearchView.ets            // 搜索组件
│  │  └──TabBar.ets                // 标签栏组件
│  └──viewmodel                  
│     ├──CityDetailData.ets        // 城市详细数据
│     ├──NewsData.ets              // 新闻数据
│     ├──NewsDataSource.ets        // 新闻数据源
│     ├──NewsTypeModel.ets         // 新闻类型模型
│     └──NewsViewModel.e


---
## form-game
> 本示例展示了如何通过Stage模型实现一个简单的游戏卡片。

源码: https://gitcode.com/HarmonyOS_Samples/form-game

# 基于Stage模型实现简单游戏卡片

### 介绍

本示例使用Stage模型和C++/ArkTS混合编程创建一个成语排序游戏卡片，通过点击事件让用户按正确顺序排列乱序的成语。C++负责随机数生成并通过NAPI接口与ArkTS交互，结合Form Kit增强卡片功能和交互体验。


### 效果预览

| 添加卡片                                               | 操作卡片                                                |
|----------------------------------------------------|-----------------------------------------------------|
| ![FormGameAdd](screenshots/device/FormGameAdd.png) | ![FormGameAdd](screenshots/device/FormGamePlay.png) |

使用说明：

1.部分设备的桌面不支持卡片，可以通过自己的开发卡片使用方，进行卡片的创建、更新和删除等操作。

2.安装应用，并在桌面上长按本应用的桌面图标，长按后弹出选项列表。

3.点击弹出列表中的**服务卡片**选项进入卡片添加界面。

4.点击正下方的**添加到桌面**按钮，卡片就会出现在桌面上。

### 工程目录
```
├──entry/src/main/cpp                         // cpp代码区，使用c++实现随机算法
├──entry/src/main/ets                         // ets代码区
│  ├──entryability                               
│  │  └──EntryAbility.ets                     // Ability的生命周期回调
│  ├──formability
│  │  └──FormAbility.ets                      // 定义卡片对象首次被创建时需要做的操作
│  ├──pages 
│  │  └──Index.ets                            // 应用首页
│  └──util
│     └──Logger.ets                           // 日志工具类
├──entry/src/main/js                          // js代码区
│  ├──common                                  // 卡片资源目录
│  ├──i18n                                    // 卡片国际化语言目录
│  └──widget/pages/index                      // 卡片内容目录                     
│     ├──index.css                            // 卡片样式
│     ├──index.hml                            // 卡片内容    
│     └──index.json                


---
## frame-generation-gles-samplecode-clientdemo-cpp
源码: https://gitcode.com/HarmonyOS_Samples/frame-generation-gles-samplecode-clientdemo-cpp

# 针对GLES的超帧

## 介绍

本示例展示了基于Graphics Accelerate Kit提供的OpenGL ES超帧API在图形绘制场景实现超帧功能。

需要编译依赖FrameGeneration的动态库libframegeneration.so。

## 效果预览

|            **桌面**             |                 **主界面**                 |
|:-----------------------------:|:---------------------------------------:|
| ![desk](screenshots/desk.png) | ![interface](screenshots/interface.png) |

使用说明：

1. 在手机的主屏幕，点击”FG Demo“，启动应用，进入图形绘制场景。
2. 点击左上角，可手动开启或关闭超帧功能。显示“超帧开启”表示超帧功能已开启，显示“超帧关闭”表示超帧功能已关闭。
3. 退出应用时，自动关闭超帧。

## 工程目录

```
└── entry/src/main                          // 代码区
    ├── cpp
    │    ├── types/libentry
    │    │     └── index.d.ts               // native层接口注册文件
    │    ├── napi_init.cpp                  // native api层接口的具体实现函数
    │    ├── CMakeLists.txt                 // native层编译配置
    │    ├── include                        // 头文件
    │    ├── source                         // C++代码区
    │    │    ├── core.cpp                  // 核心入口，管理生命周期
    │    │    ├── renderer.cpp              // 渲染管理类的实现
    │    │    ├── scene_base.cpp            // 超帧模式基类的实现
    │    │    ├── scene_extrapolation.cpp   // 外插模式类的实现
    │    │    ├── scene_interpolation.cpp   // 内插模式类的实现
    │    │    ├── opaque_layer_base.cpp     // 场景绘制基类的实现
    │    │    ├── opaque_layer.cpp          // 场景绘制派生类的实现
    │    │    ├── gui.cpp                   // UI绘制
    │    │    └── ...
    ├── ets
    │    ├── ability 
    │    │     └── EntryAbility.ts          // 程序入口类，可在此设置超帧模式
    │    ├── pages 
    │    │     └── I


---
## frame-generation-vulkan-samplecode-clientdemo-cpp
源码: https://gitcode.com/HarmonyOS_Samples/frame-generation-vulkan-samplecode-clientdemo-cpp

# 针对Vulkan的超帧

## 介绍

本示例展示了基于Graphics Accelerate Kit提供的Vulkan超帧API在图形绘制场景实现超帧功能。

需要编译依赖FrameGeneration的动态库libframegeneration.so。

## 效果预览

|            **桌面**             |                 **主界面**                 |
|:-----------------------------:|:---------------------------------------:|
| ![desk](screenshots/desk.png) | ![interface](screenshots/interface.png) |

使用说明：

1. 在手机的主屏幕，点击”VulkanFG“，启动应用，进入图形绘制场景。
2. 点击左上角，可手动开启或关闭超帧功能。显示“超帧开启”表示超帧功能已开启，显示“超帧关闭”表示超帧功能已关闭。
3. 退出应用时，自动关闭超帧。

## 工程目录

```
└── entry/src/main                          // 代码区
    ├── cpp
    │    ├── types/libentry
    │    │     └── index.d.ts               // native层接口注册文件
    │    ├── napi_init.cpp                  // native api层接口的具体实现函数
    │    ├── CMakeLists.txt                 // native层编译配置
    │    ├── Asset                          // Shader及资源加载类的实现
    │    ├── Begin                          // 程序入口
    │    │    ├── core.cpp                  // 核心入口，管理生命周期
    │    │    ├── hellovk.cpp               // vk渲染流程及超帧调用
    │    │    └── ...
    │    ├── Common                         // 通用类
    │    ├── third_party                    // 三方库
    │    ├── vulkan_utils                   // vk工具类的实现
    ├── ets
    │    ├── entryability 
    │    │     └── EntryAbility.ets         // 程序入口类，可在此设置超帧模式
    │    ├── pages 
    │    │     └── Index.ets                // 主界面
    └── resources
    │    ├── base/media                     // 图片资源
    │    │   └── ...
    │    ├── rawfile                  


---
## game-puzzle
> 该示例通过@ohos.multimedia.image和@ohos.file.photoAccessHelper接口实现获取图片，以及图片裁剪分割的功能。

源码: https://gitcode.com/HarmonyOS_Samples/game-puzzle

# 实现图片裁剪的功能

### 介绍

本示例通过@ohos.multimedia.image和@ohos.file.photoAccessHelper接口，实现一个类似“华容道游戏”的小游戏。
通过这个游戏，使得开发者学会如何获取系统相册资源文件，图片如何裁剪，运用到自己的业务当中。

### 效果预览
| 首页                                        | 运行                                       |
|-------------------------------------------|------------------------------------------|
| ![running](screenshot/device/running.png) | ![running](screenshot/device/change.png) |

### 使用说明：
1. 使用预置相机拍照后启动应用，应用首页会读取设备内的图片文件并展示获取到的第一个图片，没有图片时图片位置显示空白；由于规格限制，请勿选择过大图片，避免无法加载；
2. 点击开始按钮开始后，时间开始倒计时，在规定时间内未完成拼图则游戏结束。在游戏中，玩家点击重新开始进行游戏重置；
3. 点击开始游戏后，玩家可以根据上方的大图，点击黄格周围的图片移动，点击后图片和黄格交换位置,最终拼成完整的图片；
4. 不在游戏中时，玩家可以点击上方大图，选择自定义图片来进行拼图游戏。

### 工程目录
```
├──entry/src/main/ets                         // 代码区
│  ├──application
│  │  └──AbilityStage.ets
│  ├──common
│  │  ├──CommonConstants.ets                  // 常量类 
│  │  └──ImagePicker.ets                      // 图片选择
│  ├──entryability
│  │  └──EntryAbility.ets 
│  ├──model
│  │  ├──GameRules.ets                        // 游戏规则
│  │  ├──ImageModel.ets                       // 图片操作
│  │  ├──Logger.ets                           // 日志
│  │  └──PictureItem.ets                      // 分解的图片
│  └──pages
│     └──Index.ets                            // 首页
└──entry/src/main/resources                   // 应用资源目录
```
### 具体实现
+ 游戏中图片裁剪分割的效果实现在ImageModel中，源码参考[ImageModel](entry/src/main/ets/model/ImageModel.ets):
  + 获取本地图片：首先使用getPhotoAccessHelper获取相册管理模块实例，然后使用getAssets方法获取文件资源，最后使用getAllObjects获取检索结果中的所有文件资产方便展示


---
## game-service_-sample-code_game-performance_-client-demo
> 本示例主要基于游戏场景感知，完成游戏向系统发送数据和获取设备状态信息。


源码: https://gitcode.com/HarmonyOS_Samples/game-service_-sample-code_game-performance_-client-demo

# 基于场景感知实现游戏与系统交互（ArkTS）

## 简介
本示例集成了Game Service Kit，实现了一个简单的场景感知功能，供您参考使用，请注意，订阅设备和取消订阅设备仅演示接口调用示例。

## 预览图
![](./image/indexPage_cn.png)

## 工程目录
```
├──entry/src/main/ets                      // 代码区    
│  ├──entryability    
│  │  └──EntryAbility.ets                  // 程序入口类    
│  └──pages     
│     └──Index.ets                         // 主界面       
│        ├──gamePerformanceInit()          // 初始化接口      
│        ├──subscribeDeviceState()         // 订阅设备信息接口    
│        ├──unSubscribeDeviceState()       // 取消订阅设备信息接口    
│        ├──updateGameSceneInfo()          // 更新游戏场景信息  
│        └──queryDeviceInfo()              // 查询设备信息     
└──entry/src/main/resources                // 资源文件目录   
```

## 使用说明
1. 使用DevEco Studio打开工程目录。
2. 替换AppScope中app.json5文件和Index.ets文件中的bundleName。
3. 在build-profile.json5的signingConfigs中配置签名信息。
4. 在HarmonyOS设备上运行示例代码。

## 约束与限制
1. 本示例仅支持标准系统上运行，支持设备：华为手机、平板和PC/2in1。
2. HarmonyOS系统：HarmonyOS 5.0.2 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.2 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.2 Release SDK及以上。 


---
## game-service_-sample-code_game-player_-client-demo
> 本示例主要展示游戏联合登录、合规校验、玩家角色信息提交等功能的开发。


源码: https://gitcode.com/HarmonyOS_Samples/game-service_-sample-code_game-player_-client-demo

# 基础游戏服务

## 简介
本示例集成了Game Service Kit，实现了一个简单的游戏登录和账号切换功能，供您参考使用。

## 效果预览
![](./image/result_cn.png)

## 工程目录
```
├─entry/src/main/ets                // 代码区  
│  ├─common                          // API接口实现  
│  │  └─GameApi.ets  
│  ├─entryability  
│  │  └─EntryAbility.ets              // 程序入口类  
│  ├─entrybackupability  
│  │  └─EntryBackupAbility.ets  
│  └─pages                           // 存放页面文件目录  
│      └─Index.ets                     // 主页面，游戏登录场景、游戏号切换场景实现  
└─entry/src/main/resources          //应用资源目录  
```

## 使用说明
1. 使用DevEco Studio打开工程目录。
2. 替换AppScope中app.json5文件中的bundleName。
3. 在build-profile.json5的signingConfigs中配置签名信息，并在AppGallery Connect中配置签名证书指纹。
4. 替换entry/src/main/module.json5文件中的client_id和app_id。
5. 在HarmonyOS设备上运行示例代码。

## 相关权限
该Sample应用在调用游戏初始化、联合登录等接口需要访问网络，已在module.json5文件中添加网络权限"ohos.permission.INTERNET"。

## 约束与限制
1. 本示例仅支持标准系统上运行，支持设备：华为手机、平板、2in1、TV。
2. HarmonyOS系统：HarmonyOS NEXT Developer Beta1及以上。
3. DevEco Studio版本：DevEco Studio NEXT Developer Beta1及以上。
4. HarmonyOS SDK版本：HarmonyOS NEXT Developer Beta1 SDK及以上。


---
## gameservice_samplecode_game_performance_clientdemo_cpp
> 本示例主要基于游戏场景感知，完成游戏向系统发送数据和获取设备状态信息。

源码: https://gitcode.com/HarmonyOS_Samples/gameservice_samplecode_game_performance_clientdemo_cpp

# 基于场景感知实现游戏与系统交互（C++）

## 简介
本示例基于GameServiceKit，展示了一个简单的场景感知功能，供您参考使用：游戏场景感知初始化、更新游戏网络和场景等信息、注册和取消设备温度变化事件、查询设备gpu信息、查询设备温度信息。
开发者可以结合业务场景，通过向系统上报游戏信息，以及主动查询或是监听回调的方式感知设备的实时状态，以便于在游戏过程中进行性能调节。

## 预览图
![](./image/indexPage_cn.png)

## 工程目录
```
└──entry/src/main                      // 代码区
   ├──cpp
   │  ├──types/libentry
   │  │  └──Index.d.ts                 // native层接口注册文件
   │  ├──napi_init.cpp                 // native api层接口的具体实现函数
   │  ├──CMakeLists.txt                // native层编译配置
   │  ├──include                       // 头文件
   │  │  └──game_performance_sample.h  // 接口定义
   │  └──src                           // C++代码区
   │     ├──init.cpp                   // 初始化类的实现
   │     ├──thermallevel_callback.cpp  // 订阅温度变化事件类的实现
   │     ├──update_gameinfo.cpp        // 上报游戏信息类的实现
   │     ├──query_gpuinfo.cpp          // 查询设备GPU信息类的实现
   │     └──query_thermalinfo.cpp      // 查询设备温度信息类的实现
   ├──ets
   │  ├──entryability 
   │  │  └──EntryAbility.ets           // 程序入口类
   │  │──entrybackupability 
   │  │  └──EntryBackupAbility.ets     // 应用提供扩展的备份恢复能力     
   │  └──pages 
   │     └──Index.ets                  // 主界面
   └──resources                        // 资源文件目录
```

## 使用说明
1. 使用DevEco Studio打开工程目录；
2. 替换AppScope中app.json5文件的bundleName；
3. 在build-profile.json5的signingConfigs中配置签名信息；
4. 在HarmonyOS设备上运行示例代码。


## 约束与限制
1. 本示例仅支持标准系统上运行，支持设备：华为手机、平板和PC/2in1。
2. HarmonyOS系统：HarmonyOS 5.0.2 Beta1及以上。
3. DevEco Studio版本：DevEco Studio 5.0.2 Beta1及以上。
4. HarmonyOS SDK版本：H


---
## graphic-creation
> 本示例主要实现社交通讯类应用的图文内容编创流程，在该过程中接入自由流转、服务互动等HarmonyOS特性能力。

源码: https://gitcode.com/HarmonyOS_Samples/graphic-creation

# 基于AI能力实现图文内容高效编创

### 简介

本示例展示如何在图文编辑中接入HarmonyOS特性，包括照片选取、HDR
Vivid展示、图片AI识别文字与抠图、MovingPhoto拍摄、跨端操作等图文流转功能，适用于社交类应用，并提供详细技术实现。

### 效果展示

![](./screenshots/screen1.gif)

### 使用说明

1. 在平板和手机上都要安装该应用，主要用于测试图文流转能力。
2. 当前跨端能力仅能平板调用手机，无法实现手机调用平板。
3. 为了实现跨端拍照、跨端相册、图文流转能力，两台设备需要登录相同账号，连接WIFI网络，连接同一个局域网可以提高接续数据传输速度，同时开启蓝牙。
4. AI辅助图文内容高效编创，体现以下能力：系统Picker照片选取，HDR
   Vivid图片展示，图片AI智能识别文字及抠图，MovingPhoto拍摄，跨端拍照、扫描、相册选取，图文流转续编能力。

### 工程目录

```
├──ets
│  ├──common
│  │  └──CommonConstants.ets             // 常量配置
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──model
│  │  ├──CameraService.ets               // 相机服务
│  │  ├──ContentInfo.ets                 // 接续资产对象
│  │  ├──SelectedDataSource.ets          // picker photo后的数据源
│  │  └──WaterFlowDataSource.ets         // 首页瀑布流的数据源
│  ├──pages
│  │  ├──GraphicCreationPage.ets         // 图文编辑发布页
│  │  ├──ImageEditPage.ets               // 图片选择编辑页与自定义相机切换
│  │  ├──Index.ets                       // 主页
│  │  ├──PreviewMovingPhotoPage.ets      // 预览拍摄的Moving Photo
│  │  └──PreviewPhotoPage.ets            // 预览普通拍摄图片
│  ├──utils
│  │  ├──BreakpointSystem.ets            // 断点监听
│  │  ├──DataUtils.ets                   // 数据转换工具
│  │  ├──FileUtils.ets                   // 文件处理工具
│  │  ├──Logger.ts                       // 日志
│  │  └──UIUtils.ets                     // UI设置工具
│  └──view
│     ├──CameraView.ets                  // 相机视图
│     ├──FlowItemView.ets                // 瀑布流卡片组件
│     ├──HomeView.ets                    // 主页视图
│     ├──


---
## graphics-accelerate-kit-background-download-samplecode-arkts
> 基于游戏资源包预下载能力，完成资源包静默下载至用户设备中。

源码: https://gitcode.com/HarmonyOS_Samples/graphics-accelerate-kit-background-download-samplecode-arkts

# 基于游戏资源加速服务实现资源包后台下载（ArkTS）

## 介绍

本示例展示了基于Graphics Accelerate Kit提供的资源包后台下载能力，实现系统后台下载游戏资源（例如关卡包、3D角色模型、纹理等）到用户设备中，解决游戏启动慢的问题，为用户提供即开即玩的游戏体验。

## 效果预览

|             **通知栏**             |
|:------------------------------:|
| ![desk](screenshots/desk.png) |

操作说明：

1. 安装游戏应用，系统自动下载游戏资源。
2. 查看手机通知栏的游戏资源下载进度。
3. 等待游戏资源下载完成后，在手机的主屏幕点“资源预下载“，启动应用，查看游戏资源下载状态。

## 工程目录
```
└──entry/src/main                                   // 代码区
    ├──ets
    │    ├──common
    │    │    ├──AssetAccelManifest.ets             // 资源加速清单处理类
    │    │    └──CommonConstants.ets                // 常量定义类
    │    ├──entryability 
    │    │    └──EntryAbility.ets                   // 主程序入口类
    │    ├──extensionability 
    │    │    └──AssetAccelExtAbility.ets           // 资源加速扩展能力类
    │    ├──pages 
    │    │    └──Index.ets                          // 应用主页面
    │    ├──session 
    │    │    └──AssetSessionStorage.ets            // 存储类
    │    └──task
    │         ├──GameStepBase.ets                   // 游戏资源基类
    │         └──GameStepDetect.ets                 // 游戏资源检测类
    ├──resources                                    // 资源文件目录
    └──module.json5                                 // 模块的配置文件
```

## 使用说明
1. 使用DevEco Studio打开工程目录；
2. 替换AppScope中app.json5文件的bundleName；
3. 在build-profile.json5的signingConfigs中配置签名信息；
4. 在HarmonyOS NEXT设备上运行示例代码。更多内容请参见[Graphics Accelerate Kit（图形加速服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-kit-guide)。

## 相关权限
在module


---
## grid-drag-sort
源码: https://gitcode.com/HarmonyOS_Samples/grid-drag-sort

# 实现Grid网格元素拖拽交换排序能力

## 介绍

Grid网格元素拖拽交换功能是通过Grid容器组件、组合手势、显式动画结合来实现的。Grid容器组件用来构建网格元素布局、组合手势用来实现元素拖拽交换的效果、显式动画用来给元素拖拽交换过程中，添加动画效果。
本示例主要实现了四种网格元素拖拽交换的场景：网格元素相同大小时拖拽交换、网格元素不同大小时拖拽交换、网格元素直接拖拽交换、网格元素抖动。

## 预览效果
<img src='./screenshots/device/phone.png' width=320>

## 工程目录

``` 
├──entry/src/main/ets                                   // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  └──pages                              
│     ├──DifferentItemDrag.ets                          // 不同大小item拖拽交换页
│     ├──DirectDragItem.ets                             // 直接拖拽交换页
│     ├──Index.ets                                      // 首页
│     ├──JitterAnimation.ets                            // 抖动动画页
│     └──SameItemDrag.ets                               // 相同大小item拖拽交换页
└──entry/src/main/resources                             // 应用资源目录
``` 

## 使用说明
示例代码包含四个场景：
* 网格元素相同大小时拖拽交换

  在编辑九宫格等多图的场景中，长按图片（网格元素）可以拖拽交换排序，拖拽图片的过程中，旁边的图片也会即时移动，以产生新的宫格排布。
* 网格元素不同大小时拖拽交换

  在一些展示设备的场景中，会有大小不同的网格元素。当用户想改变设备排序时，可以长按设备图片（网格元素）拖拽交换排序，拖拽的过程中，也会改变排列顺序，以产生新的宫格排布。
* 网格元素直接拖拽交换

  在不需要长按拖拽的场景下，开发者可以将元素设置成直接拖拽，无需长按，即可完成元素的拖拽交换。
* 网格元素抖动

  在设备列表页面时，如果想要移除设备，在选中设备并长按后，可对网格元素进行编辑。此时，设备图片会有抖动的效果。

## 相关权限

无

## 约束与限制

* 本示例仅支持标准系统上运行，支持设备：华为手机。

* HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

* DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

* HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## grid-hybrid
> 本示例主要实现了Grid组件和List组件以及Swiper组件的嵌套混合布局。

源码: https://gitcode.com/HarmonyOS_Samples/grid-hybrid

## 基于Grid的嵌套混合布局

### 介绍

本示例介绍了两种嵌套混合布局，一种是通过Grid组件与List组件实现嵌套混合布局，另一种是Grid组件与Swiper组件实现嵌套混合布局。

### 效果预览

本示例在预览器中的效果：
#### 场景一：Grid与List相互嵌套
|                               Grid与List相互嵌套                               |
|:--------------------------------------------------------------:|
| <img src="./screenshots/Devices/image1.gif" width="320"/> |
#### 场景二：Grid与Swiper相互嵌套
|                               Grid与Swiper相互嵌套                               |
|:--------------------------------------------------------------:|
| <img src="./screenshots/Devices/image2.gif" width="320"/> |

使用说明：

1.可以在预览器中查看页面效果，也可在对应设备上查看页面效果。

### 工程目录

```
├──entry/src/main/ets                              // 代码区
│  ├──constants                                  
│  │  ├──CommonConstants.ets                       // 常用常量
│  │  └──ListDataConstants.ets                     // 列表数据常量
│  ├──entryability  
│  │  └──EntryAbility.ets 
│  ├──model  
│  │  ├──GridListDataSources.ets                   // 场景一Grid组件数据
│  │  ├──WaterFlowDataSource.ets                   // 瀑布流数据
│  ├──pages  
│  │  ├──GridNestListIndex.ets                     // Grid组件与List组件混合布局页
│  │  ├──GridNestSwiperIndex.ets                   // Grid组件与Swiper组件混合布局页                             
│  │  └──Index.ets                                 // 首页 
│  └──view
│     ├──GridComponent.ets                         // 场景一竖直方向的List子组件
│     ├──GridItemComponent.ets                     // GridItem子组件
│     └──MenuItemComponent.ets                  


---
## guide-snippets
> HarmonyOS 指南代码同源仓。

源码: https://gitcode.com/HarmonyOS_Samples/guide-snippets

# HarmonyOSGuideSnippets

#### 介绍
{**以下是 Gitee 平台说明，您可以替换此简介**
Gitee 是 OSCHINA 推出的基于 Git 的代码托管平台（同时支持 SVN）。专为开发者提供稳定、高效、安全的云端软件开发协作平台
无论是个人、团队、或是企业，都能够用 Gitee 实现代码托管、项目管理、协作开发。企业项目请看 [https://gitee.com/enterprises](https://gitee.com/enterprises)}

#### 软件架构
软件架构说明


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)



---
## hand-writing-to-image
> 本示例使用Drawing库的Pen和Path结合NodeContainer组件实现手写绘制功能，并通过Image库的packToFile和packing接口将手写板的绘制内容保存为图片。

源码: https://gitcode.com/HarmonyOS_Samples/hand-writing-to-image

# 实现手写绘制图片功能

### 介绍

本示例使用Drawing库的Pen和Path结合NodeContainer组件实现手写绘制功能，并通过Image库的packToFile和packing接口将手写板的绘制内容保存为图片。通过该示例，开发者可以掌握图片绘制相关接口的使用以及如何将画布保存为图片。

### 效果图预览

![](screenshots/device/HandWriteToImage.gif)

**使用说明**

1. 在虚线区域手写绘制，点击撤销按钮撤销前一笔绘制，点击重置按钮清空绘制。 
2. 点击箭头可以跳转到预览界，预览界面可以进行图片预览以及图片保存。 
3. 预览界面点击packToFile保存图片按钮和packing保存图片按钮可以将绘制内容保存为图片并写入文件，显示图片保存路径。

### 实现思路

1. 创建NodeController的子类MyNodeController，用于获取根节点的RenderNode和绑定的NodeContainer组件宽高。
2. 创建RenderNode的子类MyRenderNode，初始化画笔和绘制path路径。
3. 创建变量currentNode用于存储当前正在绘制的节点，变量nodeCount用来记录已挂载的节点数量。
4. 创建自定义节点容器组件NodeContainer，接收MyNodeController的实例，将自定义的渲染节点挂载到组件上，实现自定义绘制。 
5. 在NodeContainer组件的onTouch回调函数中，手指按下创建新的节点并挂载到rootRenderNode，nodeCount加一，手指移动更新节点中的path对象，绘制移动轨迹，并将节点重新渲染。 
6. rootRenderNode调用getChild方法获取最后一个挂载的子节点，再使用removeChild方法移除，实现撤销上一笔的效果。 
7. 使用clearChildren清除当前rootRenderNode的所有子节点，实现画布重置，nodeCount清零。
8. 使用componentSnapshot.get获取组件NodeContainer的PixelMap对象，用于保存图片。 
9. 使用Image库的packToFile()和packing()将获取的PixelMap对象保存为图片。

### 高性能知识点

不涉及

### 工程结构&模块类型

```
├──entry/src/main/ets                         // ets 代码区
│  ├──constants
│  │  └──CommonConstants.ets                  // 常量定义文件  
│  ├──entryability
│  │  └──EntryAbility.ets       
│  ├──model
│  │  └──RenderNodeModel.ets                  // MyRenderNode类模版页面
│  └──pages
│     ├──SavePages.ets                        // 预览保存界面
│     └──Index.ets                            // 绘制界面
└──entry/src/main/resources                   // 应用资源目录
```

### 参考资料

1. Draw


---
## handle-tabs
> 本示例介绍使用了Tab组件实现自定义增删Tab页签的功能。该场景多用于浏览器等场景。

源码: https://gitcode.com/HarmonyOS_Samples/handle-tabs

# 基于Tab组件实现增删Tab的功能

### 介绍

本示例通过修改Tab组件的barHeight高度，隐藏组件自带的TabBar，自定义一个可以增删Tab页签的场景，该场景多用于浏览器等场景。帮助开发者掌握Tab组件的相关接口属性，灵活的实现自己业务需要用到的Tab场景。

### 效果图预览

![](./screenshots/phone.gif)

### 使用说明

1. 点击新增按钮，新增Tab页面。
2. 点击删除按钮，删除Tab页面。

### 目录结构

```
handletabs
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──model
│  │  └──ConstantsData.ets                       // 数据类
│  └──pages
│     ├──Index.ets                               // 增删tab页签功能实现页面
│     ├──MenuBar.ets                             // 工具栏
│     └──TabSheetComponent.ets                   // 自定义TabBar组件
└────entry/src/main/resources 
```

## 实现思路

1. 设置Tab组件的barHeight为0，隐藏组件自带的TabBar。
2. 使用@Link修饰符，将自定义TabBar组件和Tab组件通过focusIndex和tabArray进行双向绑定。
3. 在自定义TabBar中修改focusIndex和tabArray的值时，Tab组件根据数据变化进行对应UI变更。

### 相关权限
不涉及。

### 依赖
不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## hdr2sdr
> 本示例基于Surface模式实现高效视频编解码，支持HDR视频录制及HDR转SDR转码功能，通过硬件加速和色彩空间优化技术，提升视频质量处理效率。

源码: https://gitcode.com/HarmonyOS_Samples/hdr2sdr

# 实现HDR视频转码SDR视频功能

## 项目简介

本示例基于Surface模式实现高效视频编解码，支持HDR视频录制及HDR转SDR转码功能，通过硬件加速和色彩空间优化技术，提升视频质量处理效率。

## 效果图预览

| 首页                                                       | 播放页                                                          |
|----------------------------------------------------------|--------------------------------------------------------------|
| <img src="screenshots/devices/MainPage.png" width=320>   | <img src="screenshots/devices/PlayerPage.png" width=320>     |
| 录制页                                                      | 转码页                                                          |
| <img src="screenshots/devices/RecordPage.png" width=320> | <img src="screenshots/devices/TranscoderPage.png" width=320> | 

## 使用说明

1. 打开应用，点击AVRecorder或AVCodec进行HDR视频录制。
2. 点击录制视频，完成录制后返回，点击视频播放或暂停视频。
3. 点击保存视频，确认保存。
4. 返回首页，点击HDR视频转码。
5. 点击屏幕选择视频，点击AVCodec或Video_Processing进行SDR转码并送显。

> **注意**：
> 1. AVRecorder录制不支持设置AVMetadata音视频元数据的HDR类型。
> 2. 在使用转码的功能时，请选择HDR类型的视频，HDR视频在相册中有HDR标识。

## 工程目录

```
├──entry/src/main/cpp                    // Native层
│  ├──capbilities                        // 接口能力实现
│  │  ├──include                         // 编解码模块接口定义
│  │  ├──AudioCapturer.cpp               // 音频采集实现
│  │  ├──AudioDecoder.cpp                // 转码音频解码实现
│  │  ├──AudioEncoder.cpp                // 音频编码实现
│  │  ├──Demuxer.cpp                     // 解封装实现
│  │  ├──Muxer.cpp                       // 封装实现
│  │  ├──VideoDecoder.cpp                // 转码视频解码实现
│  │  ├──VideoEncoder


---
## health_-service_-kit_-sample-code
> 本示例基于运动健康服务开放能力，实现运动健康数据的管理和运动联动。


源码: https://gitcode.com/HarmonyOS_Samples/health_-service_-kit_-sample-code

# 实现运动健康数据管理

## 介绍

本示例展示了使用华为运动健康数据服务提供的授权管理，数据源管理，运动健康采样数据、锻炼记录、健康记录的管理，运动联动服务。

需要使用华为运动健康数据服务接口 **@kit.HealthServiceKit**。

## 效果预览

| **示例应用主页面**                         | **授权管理页面**                         | **数据源管理页面**                        |
|-------------------------------------|------------------------------------|------------------------------------|
| ![avatar](./screenshots/img_zh.png) | ![avatar](./screenshots/img_1_zh.png) | ![avatar](./screenshots/img_2_zh.png) | 

| **运动健康采样数据管理页面**                   | **锻炼记录管理页面**                       | **健康记录管理页面**                       |
|------------------------------------|------------------------------------|------------------------------------|
| ![avatar](./screenshots/img_3_zh.png) | ![avatar](./screenshots/img_4_zh.png) | ![avatar](./screenshots/img_5_zh.png) |

| **运动联动页面**                         |
|------------------------------------|
| ![avatar](./screenshots/img_6_zh.png) |

## Sample工程的配置与使用

### 在DevEco中配置Sample工程的步骤如下

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
2. [申请运动健康服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-apply-0000001770425225)。
3. 打开Sample应用，使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)配置的应用包名替换AppScope\app.json5文件中的bundleName属性值。
4. 使用[AppGallery Connect](https://develo


---
## hmosworld
源码: https://gitcode.com/HarmonyOS_Samples/hmosworld

# HMOS世界

### 简介

本示例基于"端云一体化"的开发方式，端侧采用分层架构和模块化的设计方案，使用HarmonyOS"一次开发，多端部署"和多个HarmonyOS特性服务能力；云侧采用AppGallery Connect云开发框架的云函数和云数据库服务。实现了一款承载了多个HarmonyOS技术特性的应用，赋能HarmonyOS开发者。

| 探索                                     | 学习                                         | 溪村挑战赛                                       | 活动                                           | 我的                                     |
|----------------------------------------|--------------------------------------------|---------------------------------------------|----------------------------------------------|----------------------------------------|
| ![image](screenshots/devices/home.jpg) | ![image](screenshots/devices/learning.jpg) | ![image](screenshots/devices/challenge.jpg) | ![image](screenshots/devices/conference.jpg) | ![image](screenshots/devices/mine.jpg) |

### 使用说明

1. 本示例目录结构如下：

```
├──HMOSWorld
│  ├──Application（客户端工程文件）
│  │  ├──AppScope
│  │  ├──feature
│  │  ├──hvigor
│  │  └──products
│  └──CloudProgram（服务端工程文件）
│     ├──clouddb（云数据库数据）
│     └──cloudfunvtions（云函数）
├──README.md（HMOS世界项目介绍）
├──SETUP.md（HMOS世界端云一体化搭建指导文档）
└──screenshots（README.md和SETUP.md图片资源文件）
  
```

2. 本示例使用前，需完成端云一体化配置，要求客户端工程与服务端工程协同配置，具体配置过程请参见第[SETUP.md](SETUP.md)1-5章。本示例用到了地图服务、华为账号登录、推送消息和推送卡片功能，如果想完整体验这四项功能，需要进一步完成手动签名和端云一体化配置，具体配置过程请参见[SETUP.md](SETUP.md)的第6章，如不想体验可忽略此章节。

3. 本示例完成端云一体化配置后，数据请求使用的是[AGC](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)云函数，运行安装时请保证AGC服务端和客户端的配置信息是与bundleName一一对应


---
## http
> 本示例通过@ohos.net.http等接口，实现了根据URL地址和相关配置项发起http请求的功能。

源码: https://gitcode.com/HarmonyOS_Samples/http

# 基于Http实现网络请求功能

### 介绍

本示例通过@ohos.net.http等接口，实现了根据URL地址和相关配置项发起http请求的功能。帮助开发者实现使用http获取网络请求的场景。

### 效果预览

|首页|结果页|
|--------------------------------|--------------------------------|
|![](screenshots/device/index.png)|![](screenshots/device/result.png)|

使用说明

1.启动应用可配置网络请求，设置网址、请求方式、请求参数；

2.点击确认按钮，跳转请求结果页面；

3.点击返回按钮，返回配置页面；

4.支持将本示例中的http模块编译成tgz包。

### 工程目录

```
├──entry/src/main/ets/
│  ├──Application
│  │  └──MyAbilityStage.ets
│  ├──MainAbility
│  │  └──MainAbility.ets          // 项目入口，请求相关权限
│  ├──page
│  │  └──Index.ets                // 首页
│  └──util                        // 日志文件
│     └──Logger.ets               // 日志文件
├──entry/src/main/resources       // 应用静态资源目录
│
├──httprequest/src/main/ets/
│  └──components
│     ├──MainPage
│     │  └──MainPage.ets          // 首页主体内容
│     └──model
│        └──http.ts               // 封装了http参数和发起请求的接口
└──http/src/main/resources        // 应用静态资源目录
```

### 具体实现

* 本示例将发送http请求的接口封装在Http模块，源码参考：[http.ts](httprequest/src/main/ets/components/model/http.ts)
  * 发起请求：在[MainPage.ets](httprequest/src/main/ets/components/MainPage/MainPage.ets)
  通过TextInput组件获取参数，点击“确认”按钮后通过Http.request()方法调用http.createHttp().request()接口向指定的地址发送请求。

### 相关权限

ohos.permission.INTERNET

### 依赖

不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## iapkit-sample-clientdemo-arkts
> 此示例实现了接入IAP Kit消耗型商品、非消耗型商品、自动续期订阅商品购买能力。


源码: https://gitcode.com/HarmonyOS_Samples/iapkit-sample-clientdemo-arkts

# 实现应用内支付服务-客户端

## 介绍
IAP Kit（应用内支付服务）为开发者提供便捷的应用内支付体验和简便的接入流程，让开发者聚焦应用本身的业务能力，助力开发者的商业变现。开发者应用可通过使用IAP Kit提供的系统级支付API快速启动IAP收银台，即可实现应用内支付。
通过IAP Kit，用户可以在应用内购买各种类型的数字商品（虚拟商品），包括消耗型商品、非消耗型商品、自动续期订阅商品和非续期订阅商品。
- 消耗型商品：使用一次后即消耗掉，随使用减少，需要再次购买的商品。例：游戏货币，游戏道具等。
- 非消耗型商品：一次性购买，永久拥有，无需消耗。例：游戏中额外的游戏关卡、应用中无时限的高级会员等。
- 自动续期订阅商品：用户购买后在一段时间内允许访问增值功能或内容，周期结束后自动续期购买下一期的服务。例：应用中有时限的自动续期高级会员，如视频连续包月会员。
- 非续期订阅商品：用户购买后在一段时间内允许访问增值功能或内容，周期结束后禁止访问，除非再次购买自动续期订阅或非续期订阅商品。例：应用中有时限的高级会员，如：视频一个月会员。

本示例展示了使用应用内支付服务提供的接入支付的能力，需要使用应用内支付服务接口 @kit.IAPKit。

## 效果预览

<img src="screenshots/cn/entryPage.png" alt="demo entry page" height="360"/>
<img src="screenshots/cn/consumablePage.png" alt="demo entry page" height="360"/>
<img src="screenshots/cn/cashierPage.png" alt="demo entry page" height="360"/>


## 工程的配置与使用
### 工程配置说明
1. 完成应用开发准备。其中配置签名信息时，请使用手动签名方式。详情请参见：[应用开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview)。
   - 如果开发者应用的compatibleSdkVersion>=14，则接入IAP Kit不要求开发者[添加公钥指纹](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview#section1726913517284)以及[配置应用身份信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-config-app-identity-info#section96781336145618)。
2. 开通商户服务。详情请参见：[开通商户服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-enable-merchant-service)。
3. 开启和激活应用内购买服务。详情请参见：[开启和激活应用内购买服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-enable-in-app-purchases)。
4. 在AppGalle


---
## icon-main-color
> 本示例将介绍如何根据图片设置自适应的背景色。

源码: https://gitcode.com/HarmonyOS_Samples/icon-main-color

# 实现根据图标自适应背景色功能

### 介绍

本示例通过Image相关接口将Icon图标的解码为PixelMap对象，然后取出所有像素值，接着通过自定义算法遍历所有像素值，查找到出现次数最多的像素用于设置背景颜色。通过该案例开发者可以了解根据图片最多的像素点设置自适应背景色的具体方法。

### 效果图预览

![](screenshots/device/IconMainColor.png)

**使用说明**

1. 转换图片为PixelMap，取出所有像素值。
2. 遍历所有像素值，查找到出现次数最多的像素，即为图片的主要颜色。
3. 适当修改图片的主要颜色，作为自适应的背景色。

### 实现思路

**实现步骤**

1. 解码图片，转换为PixelMap对象，便于提取像素值。
2. 提取所有像素值，转换为整数，放入数组中。
3. 遍历数组，将所有像素值放入一个Map中，key为像素值，value为个数。
4. 遍历Map，找出出现次数最多的像素值。
5. 将整数格式的像素值转换为RGB格式，再转换为HSV格式。
6. 将HSV格式转换为RGB格式，就得到了背景色。

### 高性能知识点

1. 解码图片时，分辨率设为40*40，既可以加快计算背景颜色的速度，又可以保证准确性。
2. 提取像素时，由于HarmonyOS中的颜色是用{red,green,blue,alpha}来表示，直接放入数组或者Map中会影响计算出现次数最多的像素的速度，所以需要使用rgbToNumber方法转换为整数。

### 工程结构&模块类型

   ```
├──entry/src/main/ets                         // ets 代码区
│  ├──constants
│  │  └──CommonConstants.ets                  // 常量定义文件  
│  ├──entryability
│  │  └──EntryAbility.ets       
│  ├──utils
│  │  ├──ImageUtils.ets                       // 图片处理工具类
│  │  └──ColorUtils.ets                       // 颜色处理工具类  
│  ├──pages
│  │  ├──IconItem.ets                         // Icon组件布局
│  │  └──Index.ets                            // 主页界面
│  └──viewmodel
│     ├──AppInfoModel.ets                     // App信息类
│     └──MockDataModel.ets                    // 列表信息类
└──entry/src/main/resources                   // 应用资源目录
   ```

### 模块依赖

**不涉及**

### 参考资料

**不涉及**

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK


---
## image-canvas-edit
> 构建Surface输入输出的图片编辑

源码: https://gitcode.com/HarmonyOS_Samples/image-canvas-edit

# 基于PixelMap与Canvas实现图片编辑

## 项目简介

- 基于PixelMap 编解码技术与 Canvas 画布实现高效图像处理。支持裁剪、旋转、缩放、平移等基础编辑，提供亮度、透明度、饱和度调节功能，内置多种滤镜效果及文字水印工具。
- 操作实时预览，编辑后可直接保存处理结果，满足日常图片美化与调整需求。

## 效果预览

|                           裁剪                            |                           图片信息                           |                            水印                            |                            调节                            |
|:-------------------------------------------------------:|:--------------------------------------------------------:|:--------------------------------------------------------:|:--------------------------------------------------------:|
|  <img src="./screenshots/device/cai.png" width="320"/>  |  <img src="./screenshots/device/msg.png" width="320"/>   |  <img src="./screenshots/device/shui.png" width="320"/>  |  <img src="./screenshots/device/tiao.png" width="320"/>  |
|                           滤镜                            |                            平移                            |                            缩放                            |                                                          |
|  <img src="./screenshots/device/lv.png" width="320"/>   |  <img src="./screenshots/device/ping.png" width="320"/>  |  <img src="./screenshots/device/suo.png" width="320"/>   |                                                          |

## 功能特性
- **原图信息**：查看解码原图数据。
- **基础编辑**：裁剪、旋转、镜像。
- **图像调节**：亮度、透明度、饱和度调节。
- **图像变换**：平移、缩放。
- **滤镜效果**：黑白、模糊、高亮等多种滤镜。
- **水印功能**：支持添加文字。
- 


---
## image-comment
> 本示例通过拉起系统相机实现发布图片评论。

源码: https://gitcode.com/HarmonyOS_Samples/image-comment

# 实现发布图片评论功能

### 简介

本示例通过拉起系统相机实现发布图片评论，便于用户了解系统相机接口的调用方式。

### 效果预览
|                               Image                               |
|:--------------------------------------------------------------:|
| <img src="screenshots/ImageComment.png" width="300px"> |

使用说明：

1.启动后点击文本框，再点击相机按钮，拉起系统相机。

2.拍照后返回，点击发布按钮。

### 工程目录
```
├──entry/src/main/ets
│  ├──commmon
│  │  └──CommonConstants.ets       // 常量类                             
│  ├──entryability  
│  │  └──EntryAbility.ets          // 程序入口
│  ├──model
│  │  ├──CommentModel.ets          // 评论类
│  │  └──MockCommentData.ets       // 评论数据
│  ├──pages                                     
│  │  └──Index.ets                 // 首页
│  ├──utils                                 
│  │  └──CameraUtils.ets           // 拉起相机
│  └──view
│     ├──CommentInputDialog.ets    // 发布评论弹窗
│     ├──CommentItemView.ets       // 评论组件
│     └──ImageListView.ets         // 评论图片列表
└──entry/src/main/resources        // 应用资源目录
```

### 相关权限

不涉及

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## image-compression
> 本示例通过@ohos.multimedia.image等接口，通过二分法进行图片压缩。

源码: https://gitcode.com/HarmonyOS_Samples/image-compression

# 实现图片压缩

### 简介
本示例通过Image kit相关接口，实现了对图片进行压缩的功能，主要是通过二分法进行图片压缩，参考本示例可实现选择图片目标大小进行压缩的功能。

### 效果预览：

|           **图片压缩**            |
|:-----------------------------:|
| ![home](screenshots/main.png) |

使用说明：

1.启动应用后，首页正常显示界面。

2.输入图片压缩目标大小，点击图片压缩。

3.出现压缩后的图片，实际压缩大小小于等于输入的目标压缩大小。

### 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  └──Constants.ets                  // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  └──pages                  
│     └──Index.ets                      // 首页
└──entry/src/main/resources             // 应用静态资源目录
```

### 相关权限

- 无权限涉及

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## image-depth-copy
> 在图片开发过程中经常会涉及到PixelMap的深拷贝，本例通过使用PixelMap的readPixelsToBuffer方法来实现深拷贝。在创建源PixelMap的时候，需要将解码参数设置为RGBA_8888，而在深拷贝创建目标PixelMap的时候需要将解码参数设置为RGBA_8888。

源码: https://gitcode.com/HarmonyOS_Samples/image-depth-copy

# 实现PixelMap图片裁剪和深拷贝功能

### 介绍

本示例主要展示了通过图片获取到PixelMap格式数据，然后根据该原始PixelMap初始化出一个深拷贝的目标PixelMap，然后调用crop方法对图片进行裁剪。通过该示例开发者可以学习图片处理相关接口的使用以及图片裁剪的方法。

### 效果图预览

![](screenshots/device/ImageDepthCopy.gif) 

**使用说明**

1. 进入页面，显示的即为rawfile中图片的PixelMap经过深拷贝过后的PixelMap对象。
2. 点击底部的按钮，对原始PixelMap进行深拷贝后再根据相应的比例进行裁剪。
3. 点击顶部的保存图标，可以保存当前图片。

### 实现思路
1. PixelMap深拷贝方法。通过readPixelsToBuffer读取图片资源的PixelMap到ArrayBuffer，再通过createPixelMap得到目标PixelMap。
2. 初始化时，通过深拷贝从原始PixelMap创建目标PixelMap。
3. 调用crop方法对图片进行裁剪。
4. 通过FileIO接口方法保存图片到具体路径。

### 高性能知识点

**不涉及**

### 工程结构&模块类型
```
├──entry/src/main/ets                         // ets 代码区
│  ├──constants
│  │  └──CommonConstants.ets                  // 常量定义文件  
│  ├──entryability
│  │  └──EntryAbility.ets       
│  ├──util
│  │  ├──CopyObj.ets                          // 业务层-图片深拷贝处理
│  │  └──FileUtil.ets                         // 业务层-图片保存
│  ├──model
│  │  └──AdjustData.ets                       // 裁剪选项资源
│  └──pages
│     └──Index.ets                            // 主页界面
└──entry/src/main/resources                   // 应用资源目录
```

### 模块依赖

**不涉及**

### 参考资料

1. 位图操作。
2. packing。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## image-filter
> ArkUI中Image组件colorFilter使用，提供多种滤镜效果和图像增强功能，适用于简易照片编辑等领域。

源码: https://gitcode.com/HarmonyOS_Samples/image-filter

# 基于colorFilter实现图片滤镜效果

## 项目简介

本示例是一个基于`Image`和`Swiper`组件开发的图片滤镜示例应用。该应用不仅演示了如何使用`ColorFilter`对图片进行色彩处理，还实现了一个具有平滑缩放动画的图片轮播功能，支持对每一张图片独立设置滤镜效果。

## 效果预览
|                     原图                     |                     复古                     |                     反色                     |
| :------------------------------------------: | :------------------------------------------: | :------------------------------------------: |
| <img src='./screenshots/pic1.png' width=320> | <img src='./screenshots/pic2.png' width=320> | <img src='./screenshots/pic3.png' width=320> |

|                     增艳                     |                     美白                     |
| :------------------------------------------: | :------------------------------------------: |
| <img src='./screenshots/pic4.png' width=320> | <img src='./screenshots/pic5.png' width=320> |

## 使用说明

安装运行应用之后，分别点击图片下方的“Retro”、“Invert”、“Enhance”和“Whiten”单选框，会显示对应的滤镜效果，滑动图片可以对不同的图片添加滤镜效果。

## 工程目录

```
├──entry/src/main/ets/
│  ├──constants
│  │  └──CommonConstants.ets              // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets           // 数据备份恢复类
│  └──pages
│     └──Index.ets                        // 应用入口页
└──entry/src/main/resources               // 应用静态资源目录
```

## 具体实现

使用 `colorFilter`实现为图像设置颜色滤镜效果，有如下两种方式：

- **4×5颜色矩阵**: 通过传入一个4x5的RGBA转换矩阵，给图像设置颜色滤镜效果，如 `RETRO_COLOR_MATRIX` 通过修改 RGB 权重实现怀旧色调。
- **颜色滤波器**: 通过传入一个创建指定的颜色和混合


---
## image-reading-saving
> 图片读取与保存

源码: https://gitcode.com/HarmonyOS_Samples/image-reading-saving

# 基于Media Library Kit实现图片读取与保存

## 介绍

本示例介绍了如何使用安全控件、授权弹窗、以及获取系统权限的方式实现图片的读取与保存功能。

## 效果预览

<img src="./screenshots/device/preview.gif" width="320">

## 工程目录

```
├──entry/src/main/ets                     // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──component                           // 公共组件
│  │  ├──ReadBtn.ets                      // 读取组件
│  │  └──WriteBtn.ets                     // 写入组件
│  ├──pages
│  │  └──Index.ets                        // 应用主界面
│  ├──view
│  │  ├──PhotoPicker.ets                  // 使用PhotoPicker访问相册视图
│  │  ├──PhotoViewPicker.ets              // 使用PhotoViewPicker访问相册视图
│  │  ├──Preview.ets                      // 预览界面
│  │  ├──ReadView.ets                     // 读取视图界面
│  │  └──WriteView.ets                    // 写入视图界面
│  └──utils                               // 工具类
│     └──AuthorizationTools.ets           // 授权工具类
└──entry/src/main/resources               // 应用静态资源目录
```

## 使用说明

1. 主界面点击三种读取相册的方式任意一种，选择图片。
2. 预览界面查看图片相关信息，随后点击保存按钮，跳转到保存界面。
3. 保存界面点击三种保存方式任意一种，保存到相册。

## 实现说明

1. 通过[PhotoPickerComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-photopickercomponent)组件实现PhotoPicker读取图片。
2. 通过[PhotoViewPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker#select)的select属性拉起选择界面，实现PhotoViewPicker读取图片。
3. 通过[requestPermissionsFromUser](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abi


---
## intents-kit-samplecode-clientdemo-arkts
源码: https://gitcode.com/HarmonyOS_Samples/intents-kit-samplecode-clientdemo-arkts

# 意图框架服务

## 介绍
- 本示例基于意图框架，使用`@kit.IntentsKit`实现意图共享，使用`@kit.AbilityKit`的`InsightIntentExecutor`实现意图调用。

## 效果预览

### 意图共享
1. 共享界面展示。

   ![界面展示](images/page.jpg "界面展示")

2. 按`获取insightIntents`获取insightIntent示例数据，获取的示范数据将显示在共享界面上方输入框内。

   ![获取示范数据](images/getInsightIntent.jpg "获取示范数据")

3. 按`shareIntent`进行数据共享，并在共享界面下方的结果栏内获取意图共享结果。

   ![意图共享](images/shareIntentAndResult.jpg "意图共享")

### 意图调用

- 待共享的意图完成处理后，将会在小艺建议的卡片内展示共享的意图，点击展示的对应卡片，执行意图调用逻辑。

#### 使用小艺建议模板卡片实现意图调用
1. 小艺建议展示模板卡片，此项目内使用音乐类模板卡片。

   ![小艺建议展示界面0](images/display0.jpg "小艺建议展示界面0")

2. 点击模板卡片，按照意图注册配置内逻辑，执行对应跳转。此项目内跳转至共享界面，并在共享界面下方结果栏内展示意图调用回传参数。

   ![意图调用0](images/returnParam0.jpg "意图调用0")

### SID获取
1. 点击`getSid`获取SID，并在结果栏内展示（优先获取缓存）。

   ![SID获取](images/sid.jpg "SID获取")

2. 点击`getSidRenew`强制获取新的SID，并在结果栏内展示。

   ![SID刷新](images/sidRenew.jpg "SID刷新")

## 工程目录
```
entry/src/main/
| --- ets
|     | --- entryability
|     |     | --- EntryAbility.ets                                  // 共享界面Ability
|     |     | --- InsightIntentExecutorImpl.ets                     // 意图调用逻辑
|     | --- pages
|     |     | --- Index.ets                                         // 共享界面UI
|     | --- utils
|     |     | --- FileReader.ets                                    // 意图示例数据文件读取
|     |     | --- InsightIntentSharer.ets                           // 意图共享与getSid API调用
|     |     | --- Logger.ets                                        // 日志打印
| --- resources
|     | --- base
|     |     | --- profile
|     |     |     | --


---
## international
> 本示例主要展示了国际化模块的相关功能，使用@ohos.i18n接口，实现简单日历展示、字符类型判断、文本断点处理功能。

源码: https://gitcode.com/HarmonyOS_Samples/international

# 实现国际化功能

### 介绍

本示例主要展示了国际化模块的相关功能，使用@ohos.i18n接口，实现简单日历展示、字符类型判断、文本断点处理功能;

### 效果预览

| 首页                            | 日历                                   | 字符、文本处理                                               | 字符、文本处理效果                                            |
|-------------------------------|--------------------------------------|-------------------------------------------------------|------------------------------------------------------|
| ![main](sceenshots/main.png) | ![calendar](sceenshots/calendar.png) | ![text_processing1](sceenshots/text_processing1.png) | ![text_processing1](sceenshots/text_processing2.png) |

使用说明
1. 在主界面，可以点击日历、字符文本处理按钮进入对应功能界面；
2. 在日历界面，点击“<” “>”按钮，可以查看上/下月公历信息；
3. 在字符、文本处理界面，上方输入框输入一个字符，点击字符类型判断可以查看当前输入的字符类型，下方输入框输入长文本，点击文本断点可以查看文本断点结果，断点处用红色/标记；

### 工程目录

```
├──entry/src/main/ets/
│  ├──component
│  │  ├──OperationView.ets                  // 主页item组件
│  │  └──TitleBar.ets                       // 标题栏组件
│  ├──entryability
│  │  └──EntryAbility.ets                   // 程序入口类
│  ├──pages
│  │  ├──Calendar.ets                       // 日历页面
│  │  ├──Index.ets                          // 首页
│  │  └──TextProcessing.ets                 // 字符、文本断点处理页面
│  └──util
│     └──ResourceUtil.ts                    // 资源管理工具
└──entry/src/main/resources                 // 应用静态资源目录
```

### 具体实现
1. 日历功能使用@ohos.i18n模块中Calendar实现，全部逻辑处于Calendar，源码参考：[Calendar.ets](entry/src/main/ets/pages/Calendar.ets)。
2. 字符类型判断功能使用@ohos.i18n模块中Unicode实现，全部逻辑处于TextPr


---
## js-unit
> 本示例展示测试框架中单元测试框架的使用示例。

源码: https://gitcode.com/HarmonyOS_Samples/js-unit

# 基于JsUnit实现单元功能测试

### 介绍
本示例展示测试框架中单元测试框架的使用示例，便于开发者正确使用单元测试框架。

本实例用到了自动化测试框架代码部件仓arkXtest，如需日志打印调试，需要引入日志打印接口@ohos.hilog。

单元测试用例相较于UI自动化测试用例而言更偏重于接口返回数据的校验及逻辑处理。

### 效果预览
不涉及

使用说明
- 将JsUnit目录下的项目工程整体导入到DevEco Studio开发工具中。
- 查看ohostest目录下的测试代码实现。
- 在DevEco Studio中执行测试用例代码查看执行效果，执行方式请参考官网指南的测试框架章节。

### 工程目录

```
├──entry/src/ohosTest/ets                         // 代码区
│  ├──test
│  │  ├──assertExampleTest                        
│  │  │  └──assertExample.test.ets                // 断言自动化测试脚本
│  │  ├──basicExampleTest                        
│  │  │  └──basicExample.test.ets                 // 基础自动化测试脚本
│  │  ├──callBackExampleTest                        
│  │  │  └──callBackExample.test.ets              // 回调自动化测试脚本
│  │  ├──coverExampleTest                        
│  │  │  └──coverExample.test.ets                 // 嵌套自动化测试脚本
│  │  ├──customExampleTest                        
│  │  │  └──customExample.test.ets                // 通用自动化测试脚本
│  │  ├──paramExampleTest                        
│  │  │  └──paramExample.test.ets                 // 参数自动化测试脚本
│  │  ├──data.json                                // json数据文件
│  │  └──List.test.ets                            // 测试脚本列表
│  ├──testability
│  │  ├──pages
│  │  │  └──Index.ets                             // 首页页面
│  │  └──TestAbility.ets   
│  ├──testrunner                       
│  │  └──OpenHarmonyTestRunner.ets                
│  └──util                       
│     └──Logger.ets                                // 日志工具类
└──


---
## keyboard
> 本示例展示了输入框在顶部和底部时软键盘弹出对页面布局的影响。

源码: https://gitcode.com/HarmonyOS_Samples/keyboard

# 实现软键盘弹出功能

### 介绍

本示例展示了输入框分别在屏幕顶部和底部时软键盘弹出对页面布局的影响，通过设置软键盘的避让模式为KeyboardAvoidMode.RESIZE、设置NavDestination的mode为NavDestinationMode.DIALOG和设置toast的showMode为ToastShowMode.TOP_MOST等方式实现布局的避让，帮助开发者在多种软件盘弹出场景下实现合理的页面布局。

### 效果预览
| 聊天列表页面                        | 聊天页面                          | 邮件页面                          |
|-------------------------------|-------------------------------|-------------------------------|
| ![](screenshots/device/1.png) | ![](screenshots/device/2.png) | ![](screenshots/device/3.png) |
| 评论页面                          | 
| ![](screenshots/device/4.png) | 

使用说明

1、点击搜索按钮，顶部栏变为搜索框，点击搜索框在下方弹出软键盘，中间列表不变形。

2、点击任一联系人，进入聊天页面，点击下方输入框弹出软键盘，中间列表被挤压，顶部栏不动。

3、进入邮件页面，点击发件人，弹出软键盘，通过设置软键盘的避让模式为KeyboardAvoidMode.RESIZE（压缩模式），来解决底部操作栏被遮挡的问题。

4、进入评论页面，点击输入框，弹出软键盘，通过设置NavDestination的mode为NavDestinationMode.DIALOG弹窗类型，并设置软键盘避让模式为压缩模式，解决页面上抬的距离过多的问题。

### 工程目录
```
├──entry/src/main/ets
│  ├──common
│  │  └──constants
│  │     └──CommonConstants.ets             // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets                   // 程序入口类
│  ├──pages
│  │  ├──ChatListPage.ets                   // 聊天列表页面
│  │  ├──Comment.ets                        // 评论页面
│  │  ├──ContactPage.ets                    // 聊天页面
│  │  ├──CustomDialogAvoid.ets    
│  │  ├──ExamplePage.ets    
│  │  ├──ExamplePageMode.ets   
│  │  ├──GetKeyboardHeightDemo.ets
│  │  ├──GetSafeAreaHeightDemo.ets
│  │  ├──GetSafeAreaHeightDemoMode.ets         
│  │  ├──Index.ets                          // 主页


---
## knock-share
> 碰一碰分享示例代码

源码: https://gitcode.com/HarmonyOS_Samples/knock-share

# 基于Share Kit实现碰一碰视频快速分享

### 介绍

本示例利用Share Kit与App Linking的结合，实现了快速跨设备分享视频并直接进入应用内视频播放页面的功能。通过harmonyShare.on()
方法注册碰一碰监听事件，并在回调中使用sharableTarget.share()方法分享App Linking链接，从而提供了一步直达的流畅用户体验。

### 效果图预览

| 首页                         | 播放页面                      | 碰一碰分享预览                      |
|----------------------------|---------------------------|------------------------------|
| ![](screenshots/index.png) | ![](screenshots/play.png) | ![](screenshots/preview.png) |

**使用说明**

1. 在运行项目前，需要完成App Linking的配置，以及对应用进行手动签名，具体可以参考[使用App Linking实现应用间跳转](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startup)。
2. 在完成App Linking的配置后，请前往[KnockController.ets](entry/src/main/ets/controller/KnockController.ets)文件，将share()方法中的content参数替换为真实可用的链接地址，同时将[module.json5](./entry/src/main/module.json5)文件中uris的host修改为可用的域名。
3. 设备A和设备B均安装运行示例代码，在亮屏、解锁的状态下并且都已开启华为分享服务（系统默认开启）
4. 设备A进入视频播放页面，和设备B顶部轻碰触发碰一碰分享。
5. A设备在分享界面上滑预览图，设备B接收到图片，并且直接拉起应用视频播界面。

### 工程结构

```
├──entry/src/main/ets
│  ├──controller         
│  │  ├──AVPlayerController.ets             // 视频播放控制类             
│  │  └──KnockController.ets                // 碰一碰分享控制类
│  ├──entryability                        
│  │  └──EntryAbility.ets                   // 程序入口类
│  ├──entrybackupability                  
│  │  └──EntryBackupAbility.ets             // 数据备份恢复类
│  ├──model                               
│  │  └──VideoData.ets                      // 视频数据
│  ├──pages                               
│  │  ├──Index.


---
## language-base-class-library
> 本示例集合语言基础类库的各个子模块，展示了各个模块的基础功能。

源码: https://gitcode.com/HarmonyOS_Samples/language-base-class-library

# 实现语言基础类库功能

### 介绍
本示例集合ArkTS语言基础类库的各个子模块，展示了各个模块的基础功能，帮助开发者掌握ArkTS语言基础类库各子模块的使用方法。包含：

- @ohos.convertxml (xml转换JavaScript)
- @ohos.taskpool (启动任务池)
- @ohos.uri (URI字符串解析)
- @ohos.util (util工具函数)
- @ohos.ArkTSUtils (ArkTSUtils工具函数)
- @ohos.util.ArrayList (线性容器ArrayList)
- @ohos.util.Deque (线性容器Deque)
- @ohos.util.HashMap (非线性容器HashMap)
- @ohos.util.HashSet (非线性容器HashSet)
- @ohos.util.LightWeightMap (非线性容器LightWeightMap)
- @ohos.util.LightWeightSet (非线性容器LightWeightSet)
- @ohos.util.LinkedList (线性容器LinkedList)
- @ohos.util.List (线性容器List)
- @ohos.util.PlainArray (非线性容器PlainArray)
- @ohos.util.Queue (线性容器Queue)
- @ohos.util.Stack (线性容器Stack)
- @ohos.util.TreeMap (非线性容器TreeMap)
- @ohos.util.TreeSet (非线性容器TreeSet)
- @ohos.xml (xml解析与生成)
- @ohos.convertxml (xml转换JavaScript)

### 效果预览

|                **主页**                 |               **Util**                |
|:-------------------------------------:|:-------------------------------------:|
| ![home](screenshots/devices/home.png) | ![util](screenshots/devices/util.png) |

使用说明

1. 首页展示语言基础类库各个子模块菜单，点击进入对应的模块页面。
2. 各个子模块界面中点击功能按钮完成各个功能。
3. Util中有二级菜单，点击进入对应的二级界面，包含：
   * StringCode：字符串编解码，点击功能按钮完成各个功能。
   * RationnalNumber：有理数比较，点击功能按钮完成各个功能。
   * LRUCache：LRU缓冲区，点击功能按钮完成各个功能。
   * ScopeHelper：范围判断，点击功能按钮完成各个功能。
   * Base64Helper：Base64编解码，点击功能按钮完成各个功能。
   * TypeCheck：类型检查，点击功能按钮完成各个功能。
   * JsonFunction：Json常用方法，点击功能按钮完成各个功能。
4. ArkTSUtil中有二级菜单，点击进入对应的二级界面，包含：
   * AsonFunction：将ISendable数据类型序列化和反序列化。
5. Xml & ConvertXml界面


---
## large-file-copy
> 文件拷贝是应用开发中的一个常见场景，通常有两种方式，一是直接读写文件的全部内容，二是使用buffer多次读写。前者的优点在于使用简单，但是在大文件场景下，内存占用较高，影响应用性能；后者的优点在于内存占用较小，但是编程稍显复杂。本例将展示如何使用buffer来将大文件的rawfile复制到应用沙箱。

源码: https://gitcode.com/HarmonyOS_Samples/large-file-copy

# 基于定长buffer的大文件拷贝解决方案

### 介绍

文件拷贝是应用开发中的一个常见场景，通常有两种方式，一是直接读写文件的全部内容，二是使用buffer多次读写。前者的优点在于使用简单，但是在大文件场景下，内存占用较高，影响应用性能；后者的优点在于内存占用较小，但是编程稍显复杂。本例将展示如何使用buffer来将大文件的rawfile复制到应用沙箱。

### 效果预览
![Index](screenshot/LargeFileCopy.gif)

### 工程目录
```
├──entry/src/main/ets               
│  ├──constants
│  │  └──BigFileCopyConstants.ets        // 常量类               
│  ├──entryability  
│  │  └──EntryAbility.ets               // 程序入口
│  └──view                              
│     └──Index.ets                      // 首页
└──entry/src/main/resources             // 应用资源目录
```

**使用说明**

1. 点击拷贝按钮开始复制。
2. 当复制进度达到100%之后，点击预览按钮进行文件的预览，以验证文件复制的正确性。
3. 如果要反复验证本场景，请在复制完成之后，点击重置按钮，重置进度，再进行后续验证。

### 相关权限

不涉及

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## list-exchange
> 本示例主要实现了List列表项的交换与删除功能。

源码: https://gitcode.com/HarmonyOS_Samples/list-exchange

## 通过组合手势实现List组件中列表项交换排序

### 介绍

本示例介绍了如何通过组合手势结合List组件，来实现对List组件中列表项的交换排序。

### 效果预览

|                               List                               |
|:--------------------------------------------------------------:|
| <img src="./screenshots/Devices/image1.gif" width="320"/> |


使用说明：

1.可以在预览器中查看页面效果，也可在对应设备上查看页面效果。

### 工程目录

```
├──entry/src/main/ets                              // 代码区
│  ├──constants                                  
│  │  └──CommonConstants.ets                       // 常用常量
│  ├──entryability  
│  │  └──EntryAbility.ets 
│  ├──pages                             
│  │  └──Index.ets                                 // 首页 
│  ├──utils
│  │  └──Logger.ets                                // 日志打印类       
│  └──viewModel
│     ├──AttributeModifier.ets                     // 列表样式类
│     ├──ListExchangeCtrl.ets                      // 列表行为控制类
│     └──ListInfo.ets                              // 列表项信息类    
└──entry/src/main/resources                        // 应用资源目录

```

### 具体实现


本示例通过组合手势：长按、拖动，以及拖动的距离判断列表项是否需要交换，并使用ListItem组件的swipeAction属性设置划出的删除组件。



### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## list-item-edit
> 本示例基于List组件，实现待办事项管理、文件管理、备忘录的等场景列表编辑效果。

源码: https://gitcode.com/HarmonyOS_Samples/list-item-edit

# 基于List组件实现待办事项列表编辑效果

### 介绍

本示例基于List组件，实现待办事项管理、文件管理、备忘录的等场景列表编辑效果。

### 效果预览
|                               List                               |
|:--------------------------------------------------------------:|
| <img src="./screenshots/device/listitem_edit.gif" width="320"/> |

##### 使用说明

- 点击添加按钮，选择需要添加的待办事项。
- 点击左侧checkbox按钮，待办事项状态变更为已完成。
- 左滑单个待办事项，点击删除按钮后，当前待办事项被删除。

### 工程目录

```

├──entry/src/main/ets/
│  ├──common
│  │  └──Constants.ets               // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets            // 程序入口类
│  ├──model
│  │  └──ToDo.ets                    // 待办事项数据
│  ├──pages
│  │  └──Index.ets                   // 首页
│  └──view
│     └──TodoListItem.ets            // 待办选项
└──entry/src/main/resources          // 应用静态资源目录
```

### 具体实现

1. List组件绑定@State修饰的数组变量toDoData。

2. ListItem组件设置左滑动效swipeAction属性，使得单个ListItem可以进行左右滑动，并显示自定义的UIBuilder。

3. 新增/删除列表项，更新数组变量toDoData，并同时更新List组件UI。

### 相关权限

不涉及

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## list-optimization
> 本示例分别使用ForEach与LazyForEach实现了长列表，并在LazyForEach懒加载的基础上实现了缓存列表项与组件复用，旨在不同大小的数据下，对比ForEach与LazyForEach的性能，包括完全显示所用时间、丢帧率等性能指标。

源码: https://gitcode.com/HarmonyOS_Samples/list-optimization

# 基于ForEach和LazyForEach实现长列表

### 介绍
本示例分别使用ForEach与LazyForEach实现了长列表，并在LazyForEach懒加载的基础上实现了缓存列表项与组件复用，旨在不同大小的数据下，对比ForEach与LazyForEach的性能，包括完全显示所用时间、丢帧率等性能指标。

### 效果预览：
| ForEach页面                           | LazyForEach页面                                  | 
|-------------------------------------|-----------------------------------------|
| ![](screenshots/device/ForEach.png) | ![](screenshots/device/LazyForEach.png) | 


使用说明：

1.启动应用后，在DevEco Studio启动Profiler中的Frame用来记录应用在ForEach和LazyForEach的丢帧率等数据；

2.分别点击【ForEach】和【LazyForEach】后，分别记录完全显示所用时间。完全显示所用时间可以通过Launch进行录制分析，详情操作可以参考[Launch分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-launch-overview)。

3.分别点击【ForEach】和【LazyForEach】后，分别记录滑动的丢帧率。滑动丢帧可以通过Frame进行录制分析，详情操作可以参考[Frame分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-frame)。

4.为方便对比实验，本Sample在src/main/resources/rawfile中提供了不同大小的数据文件。开发者可以在getArticleModelObjFromJSON方法中更换数据文件来对比不同数据量下ForEach和LazyForEach的性能。


### 工程目录
```
├──entry/src/main/ets/
│  ├──components
│  │  ├──ArticleCardView.ets            // 文章列表项组件
│  │  └──ReusableArticleCardView.ets    // 可复用文章列表项组件
│  ├──constants 
│  │  └──Constants.ets                  // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──model
│  │  ├──ArticleListData.ets            // 列表的DataSource
│  │  └──LearningResource.ets           // 列表数据类
│  ├──pages
│  │  ├──basicPre.ets                   // 预加载页面
│  │  ├──ForEachListPage.ets            


---
## live-view-kit_-sample-code_-clientdemo_-arkts
> 基于HarmonyOS实现了即时配送场景下实况窗的创建、更新和结束功能。


源码: https://gitcode.com/HarmonyOS_Samples/live-view-kit_-sample-code_-clientdemo_-arkts

# 实现多场景实况窗展示功能

## 简介

本示例基于Live View Kit（实况窗服务）实现即时配送场景、航班出行等场景下实况窗的创建、更新和结束功能。

## 相关概念

- 实况窗：实况窗是一种帮助用户聚焦正在进行的任务，方便快速查看和即时处理的通知形态。实况窗具有时效性、时段性、变化性的特点。
- 组件：Demo中主要使用了Text、Image等组件。
- liveViewManager：本模块提供Live View Kit的基础能力，包括创建、更新和停止实况窗、获取实况窗和检查实况窗开关的功能。

## 实际效果

### 界面展示

在应用主页面中有多个场景的卡片，点击对应卡片，即可跳转到该场景的页面。
通过场景页面中的各个按钮，可以进行实况窗的创建、更新与结束，查看该场景中实况窗更新的流程（流程仅供参考，用户可自行定义）。

| 应用主页面                            | 场景页面(以即时配送为例)               | 实况窗样例(以即时配送为例)                      |
|----------------------------------|-----------------------------|-------------------------------------|
| ![](./screenshots/main_page.png) | ![](./screenshots/page.png) | ![](./screenshots/notification.png) |

左右文本模板(适用于航班场景/高铁场景)：赏月/夕阳/雨雪天气等卡片背景效果展示

| 赏月卡片背景                             | 夕阳卡片背景                               | 雨雪天气卡片背景                           |
|------------------------------------|--------------------------------------|------------------------------------|
| ![](./screenshots/flight_moon.png) | ![](./screenshots/flight_sunset.png) | ![](./screenshots/flight_snow.png) |

### 场景与状态

- 即时配送：待支付、待商家接单、待骑手接单、骑手已接单、骑手已到店、商品配送中、商品放入取餐柜和商品已送达
- 打车出行：呼叫车辆中、行程即将开始、司机正在赶来、司机已到达上车点、正在去往目的地、行程结束、待支付
- 高铁旅行：计划出发、已安检、检票提醒、已检票、停止检票、已出发、列车运行中、已到达
- 排队叫号：取号、排队中、即将到号、叫号中、排队完成
- 赛事比分：第一节开始、更新进展（进展一/进展二/进展三）、暂停、暂停结束、中场休息、第二节开始、比赛结束
- 导航：导航开始、提供导向（导向一/导向二）、路线变更、导航结束
- 航旅出行：计划出发、待值机、已值机、已安检、开始登机、催促登机、已登机、结束登机、即将起飞、已起飞、已到达、提醒行李转盘、结束提醒、用户退票、航班取消、航班晚点、改签
- 计时：正计时、倒计时、暂停计时、继续计时、结束计时
- 共享租赁：提交订单、更新进展、结束订单、暂停


---
## location-service
源码: https://gitcode.com/HarmonyOS_Samples/location-service

# 基于位置服务获取设备定位信息

### 介绍

本示例通过@kit.LocationKit中的geoLocationManager实现获取缓存位置、获取当前位置和持续定位功能，并结合@kit.BackgroundTasksKit中的backgroundTaskManager开启长时任务，实现后台定位功能，同时运用map.Marker将位置信息标记在地图上。开发者可以在需要用到设备位置信息的开发场景中，如查看所在城市天气、出行打车、旅行导航以及观察运动轨迹等，集成本示例代码实现定位功能。

### 效果预览
| 首页                                            |
|-----------------------------------------------|
| ![](screenshots/devices/location_service.png) |

## 使用说明

使用前请先参考[应用开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview)完成基本准备工作及公钥指纹配置后，参考地图服务开发指南 “配置AppGallery Connect” 章节[开通地图服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc)，并参考应用/元服务[手动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)章节对应用进行签名。

1. 进入主页，点击"获取缓存位置"按钮获取缓存位置信息，并将其标记在地图上。

2. 进入主页，点击"获取当前位置"按钮获取当前位置信息，并将其标记在地图上。

3. 进入主页，点击"持续定位"按钮，地图上会显示相关位置信息，并持续更新位置信息；再次点击"持续定位"按钮，停止持续更新位置信息。

4. 进入主页，点击"后台定位"按钮，地图上会显示相关位置信息，将应用退至后台后仍可持续更新位置信息；应用回到前台，再次点击"后台定位"按钮后将应用退至后台，停止持续更新位置信息。说明：如果手机长时间处于绝对静止，资源管理会冷冻应用。系统针对冷冻的应用会停止定位，解冻之后应用正常恢复定位。解冻措施：将应用返回前台；移动手机退出静止状态（若移动手机没有立即恢复定位功能，可能是移动的距离不够，系统没有判定手机移动或位置发生变化；应用解冻在息屏状态可能会有一段时间的延迟，导致定位功能延迟恢复）。

### 工程目录

```
├──entry/src/main/ets/                    // 代码区
│  ├──common
│  │  └──CommonConstants.ets              // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──model
│  │  └──LocationInter.ets                // 位置经纬度信息
│  └──pages
│     └──Index.ets                        // 主


---
## logger
> 本示例使用hilog日志系统，提供日志打印类，使应用/服务可以按照指定级别、标识和格式字符串输出日志内容，帮助开发者了解应用/服务的运行状态，更好地调试程序。

源码: https://gitcode.com/HarmonyOS_Samples/logger

# 基于hilog实现日志打印功能

### 介绍

本示例使用hilog日志系统，提供日志打印类，使应用/服务可以按照指定级别、标识和格式字符串输出日志内容，帮助开发者了解应用/服务的运行状态，更好地调试程序。

### 效果预览
| 首页                                     |
|----------------------------------------|
| ![image](screenshots/device/index.png) |

使用说明：

1.进入应用会自动生成一个空的日志文件。

2.点击log按钮即可输出日志，并将日志生成到日志文件当中。

### 工程目录
```
├──entry
│  ├──src/main/ets
│  │  ├──entryability
│  │  │  └──EntryAbility.ets           // 程序入口类
│  │  └──pages           
│  │     └──Index.ets                  // 主页面
│  └──src/main/resources               // 应用静态资源目录
└──log
   ├──src/main/ets
   │  └──components	                    
   │     └──mainpage                 
   │  	    ├──Configure.ets		   // 日志打印配置项
   │        ├──Configure.ts            // 配置项类型
   │        ├──Logger.ets              // 日志打印类
   │        ├──LoggerModel.ts          // 封装日志打印类
   │        └──LogLevel.ts             // 日志等级枚举值
   └──src/main/resources              
```

### 具体实现
+ 日志输出功能封装在Logger，源码参考:[Logger.ets](log/src/main/ets/components/mainpage/Logger.ets):
    + 日志输出：Logger类根据Configure的types参数将日志分为三个类型，其中file类型会将日志写入本地文件，console类型调用ConsoleLoggerStrategy类输出，hilog类型调用HilogLoggerStrategy类输出;
    + 日志文件写入本地：FileLoggerStrategy类使用@ohos.file.fs将日志写入本地文件中，本示例只是展示了文件写入文件操作的使用方法，在实战场景中，建议把耗时操作放入子线程中运行。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。





---
## login-and-logout
> 本示例是基于Navigation实现导航跳转，采用PromptAction实现弹窗。模拟登录和注销的场景实现，且界面满足一多适配。

源码: https://gitcode.com/HarmonyOS_Samples/login-and-logout

# 基于Navigation组件实现模拟登录和注销的场景

## 介绍

基于Navigation组件实现导航跳转，采用PromptAction实现弹窗。模拟登录和注销的场景实现，且界面满足一多适配。应用登录符合隐私要求，实现正确的跳转逻辑，满足更好的用户体验。

## 预览效果
手机运行效果图如下：

![](/screenshots/image1.png)

折叠屏运行效果图如下：

![](/screenshots/image4.png)

tablet运行效果图如下：

![](/screenshots/image7.png)

## 工程目录

``` 
├──entry/src/main/ets                                   // 全屏登录代码区
│  ├──common
│  │  └──CommonConstants.ets                            // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages                              
│  │  ├──AuthorizedDialog.ets                           // 隐私授权弹窗
│  │  ├──Index.ets                                      // 首页
│  │  ├──Login.ets                                      // 登录页
│  │  └──Logout.ets                                     // 退出登录页
│  └──utils.ets
│     └──JudgeHasNet.ets                                // 判断网络是否连接
└──entry/src/main/resources                             // 应用资源目录
├──login/src/main/ets                                   // 全屏登录代码区
│  ├──common
│  │  └──CommonConstants.ets                            // 常量类
│  ├──loginability
│  │  └──LoginAbility.ets                               // 程序入口类
│  ├──pages                              
│  │  ├──AuthorizedDialog.ets                           // 隐私授权弹窗
│  │  ├──Index.ets                                      // 首页
│  │  ├──Login.ets                                      // 登录页
│  │  └──Logout.ets   


---
## low-power-player-play-formatted-audio
> 该示例展示了使用LPP低功耗播放器播放格式化音频

源码: https://gitcode.com/HarmonyOS_Samples/low-power-player-play-formatted-audio

# LowPowerPlayerPlayFormattedAudio

#### 介绍
该示例展示了使用LPP低功耗播放器播放格式化音频

#### 软件架构
软件架构说明


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)



---
## manage-audio-output-devices
> 本示例基于媒体场景和通话场景，展示如何获取输出设备信息、切换输出设备、响应设备变更。

源码: https://gitcode.com/HarmonyOS_Samples/manage-audio-output-devices

# 实现音频输出设备管理功能

## 项目简介

本示例基于AVSession、AudioRender、AudioRoutingManager、AudioSessionManager等能力，通过媒体场景和通话场景，展示如何获取输出设备信息、切换输出设备、响应设备变更。

## 效果预览

| 应用主界面                               | 媒体设备                                | 通话设备                                |           
|-------------------------------------|-------------------------------------|-------------------------------------|
| ![image](screenshots/effect_01.png) | ![image](screenshots/effect_02.png) | ![image](screenshots/effect_03.png) |

## 使用说明

1. 点击首页"媒体设备"按钮进入音乐播放页面，点击右上角AVCastPicker投播组件切换输出设备，点击播放按钮播放音乐，点击暂停按钮暂停播放。
2. 点击首页"通话设备"按钮进入通话模拟页面，显示可选择输出设备列表，点击设置按钮选择默认输出设备，点击通话按钮开始通话。 
3. 打开AVCastPicker系统组件开关，点击右下角图标按钮，使用AVCastPicker投播组件切换输出设备； 
4. 关闭AVCastPicker系统组件开关，点击右下角图标按钮，使用audioRenderer切换输出设备。

## 工程目录

```
├───entry/src/main/ets
│   ├───common                        
│   │   ├───AudioRenderering.ets            // 音频播放控制器
│   │   ├───AVSessionController.ets         // 音频会话控制器
│   │   ├───OutputDevicesOperation.ets      // 输出设备管理
│   │   └───Utils.ets      	                // 工具类
│   ├───constants                               
│   │   └───CommonConstants.ets             // 常量
│   ├───viewModel                        
│   │   ├───SongData.ets                    // 音乐数据
│   │   └───SongItem.ets      	            // 音乐定义类
│   ├───entryability                        
│   │   └───EntryAbility.ets                // Ability的生命周期回调内容
│   ├───entrybackupability                  
│   │   └───EntryBackupAbility.ets     


---
## managing-audio-input-devices
> 本示例基于媒体场景和通话场景，展示如何获取输入设备信息、切换输入设备、响应设备变更。

源码: https://gitcode.com/HarmonyOS_Samples/managing-audio-input-devices

# 实现音频输入设备管理功能

## 项目简介
本示例基于AudioCapturer、AudioRender、AudioRoutingManager、AudioSessionManager等能力，通过媒体场景和通话场景，展示如何获取输入设备信息、切换输入设备、响应设备变更。

## 效果预览

| 应用主界面                               | 音频录制                                | 音频播放                                |           
|-------------------------------------|-------------------------------------|-------------------------------------|
| ![image](screenshots/effect_01.png) | ![image](screenshots/effect_02.png) | ![image](screenshots/effect_03.png) |

## 使用说明
1. 点击"媒体设备"按钮进入"录制和播放"页面，显示可选择输入设备列表，点击设置按钮切换音频输入设备。
2. 点击红色录制按钮开始录音，等待录音完毕或等待5s后手动点击录制按钮结束录音，
3. 显示录音结果后，点击播放按钮播放音频。
4. 点击"通话设备"按钮进入"录制和播放"页面，显示可选择输入设备列表。
5. 点击红色录制按钮开始录音，等待录音完毕或等待5s后手动点击录制按钮结束录音，点击播放按钮播放音频。
6. 显示录音结果后，点击播放按钮播放音频。

## 工程目录

```
├───entry/src/main/ets
│   ├───common                        
│   │   ├───AudioRecording.ets              // 音频录制控制器
│   │   ├───AudioRenderering.ets            // 音频播放控制器
│   │   ├───InputDevicesOperation.ets       // 音频设备管理
│   │   └───Utils.ets      	                // 工具类
│   ├───constants                               
│   │   └───CommonConstants.ets             // 常量
│   ├───entryability                        
│   │   └───EntryAbility.ets                // Ability的生命周期回调内容
│   ├───entrybackupability                  
│   │   └───EntryBackupAbility.ets          // 程序备份和恢复
│   ├───pages                               
│   │   └───Index.ets                       // 首页
│   └───view                                
│       └───R


---
## map-kit_-sample-code_-demo-arkts
> 本示例展示了使用地图服务提供的地图展示、移动地图、添加Marker/MapCircle/MapPolyline/MapPolygon、静态图、位置搜索、地点详情和选点高级控件的能力。


源码: https://gitcode.com/HarmonyOS_Samples/map-kit_-sample-code_-demo-arkts

# 地图服务

## 介绍

本示例展示了使用地图服务提供的地图展示、移动地图、添加Marker/MapCircle/MapPolyline/MapPolygon、静态图、位置搜索、地点详情和选点高级控件的能力。

需要使用地图服务接口@hms.core.map.map.d.ts、@hms.core.map.mapCommon.d.ts、@hms.core.map.MapComponent.d.ets、@hms.core.map.sceneMap.d.ts、@hms.core.map.site.d.ts、@hms.core.map.staticMap.d.ts、@hms.core.map.navi.d.ts。

## 效果预览


| **应用首页**                   |         **基础功能页面**         |        **移图效果展示1**         |              **移图效果展示2**               |    
|:---------------------------|:--------------------------:|:-------------------------:|:------------------------------------:|
| ![](screenshots/Index.png) | ![](screenshots/MapController.png) | ![](screenshots/moveCamera1.png) | ![](screenshots/moveCamera2.png) |  


| **应用首页**                   |         **基础功能页面**         |        **我的位置**         |              **修改位置样式**               |    
|:---------------------------|:--------------------------:|:-------------------------:|:------------------------------------:|
| ![](screenshots/Index.png) | ![](screenshots/MapController.png) | ![](screenshots/setLocation.png) | ![](screenshots/setLocationStyle.png) |  


| **应用首页**                   |          **覆盖物添加页面**           |            **添加标记**             |            **添加多边形**             |    
|:---------------------------|:-----------------------------:|:-------------------------------:|:--------------------------------:|
| ![](screenshots/Index.png) | ![](screenshots/overlay.png) | ![](screenshots/addMarker.png) | ![](scree


---
## media-provider
> 本示例主要展示了媒体会话（媒体提供方）的相关功能，使用@ohos.multimedia.avsession等接口实现媒体提供方与媒体播控中心自定义信息的交互功能。

源码: https://gitcode.com/HarmonyOS_Samples/media-provider

# 实现音频应用作为媒体会话提供方接入媒体会话

## 介绍

本示例主要展示了媒体会话（媒体提供方）的相关功能，使用@ohos.multimedia.avsession等接口实现媒体提供方与媒体播控中心自定义信息的交互功能。

> 注意：
> 此示例仅展示媒体提供方的相关功能，如果需要媒体会话提供的完整的自定义信息交互功能，请将本示例与系统播控中心共同使用。

## 效果预览

![Index](screenshot/device/media_provider.gif) 

## 使用说明

### 基础操作

1. 打开媒体提供方示例应用。
2. 点击播放按钮，应用的播放状态发生变化，进度开始刷新。
3. 点击暂停按钮，应用的播放状态开始变化，进度停止刷新。
4. 点击上一首按钮，应用界面展示播放列表中的上一首歌曲的信息。
5. 点击下一首按钮，应用界面展示播放列表中的下一首歌曲的信息。
6. 点击播放，拖动进度条，播放进度改变。
7. 点击收藏，收藏按钮点亮。
8. 点击播放模式，可以切换不同的播放模式（注：播放模式未实现功能，仅实现与播控中心状态同步）。

### 进阶操作（与媒体播控中心一起使用）

1. 点击本应用播放、暂停、上一首、下一首按钮，可以发现媒体播控中心中，该会话的状态同步改变。
2. 点击媒体播控中心的对应按钮，可以发现本应用中按钮状态同步改变。
3. 媒体播控中心可以获取到本应用的正在播放内容、播放模式、歌词、进度、收藏状态、媒体资源金标、历史歌单等信息。

## 工程目录

给出项目中关键的目录结构并描述它们的作用，示例如下：

```
├──entry/src/main/ets/
│  ├──common
│  │  ├──constants
│  │  │  └──Constants.ets                       // 常量类
│  │  └──utils
│  │     ├──GlobalContextUtils.ets              // 全局上下文封装
│  │     ├──Logger.ets                          // 日志打印封装
│  │     └──MediaData.ets                       // 歌曲相关信息
│  ├──entryability
│  │  └──EntryAbility.ets  
│  ├──model
│  │  ├──IntentExecutorImpl.ets                 // 意图调用执行实现类
│  │  └──mediaData.ets                          // 媒体数据类型  
│  ├──pages
│  │  └──Index.ets                              // 界面实现
│  └──viewmodel
│     └──ProviderManager.ets                    // 媒体提供方状态管理
└───entry/src/main/resources                    // 应用资源目录
```

## 具体实现

* 界面相关的实现都封装在pages/Index.ets下，源码参考：[pages/Index.ets](./entry/src/main/ets/pages/Index.ets)
  
  * 使用`@Storag


---
## multi-columns
> 本示例分别展示了多场景下，一多分栏控件的响应式变化效果。

源码: https://gitcode.com/HarmonyOS_Samples/multi-columns

# 一次开发，多端部署-分栏控件

### 介绍

本示例分别展示了多场景下，一多分栏控件的响应式变化效果。

本示例分别用到了SideBarContainer组件与Navigation组件，对应使用场景如下：

* A+B+C：即SideBarContainer组件组合Navigation组件
* A+C：SideBarContainer组件
* B+C：Navigation组件

### 效果预览

本示例在预览器中的效果：

**A+B+C**:

| 360vp                               | 600vp                               | 840vp                               |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| ![](screenshots/Devices/image3.png) | ![](screenshots/Devices/image2.png) | ![](screenshots/Devices/image1.png) |

**A+C**:

| 360vp                               | 600vp                               |
| ----------------------------------- | ----------------------------------- |
| ![](screenshots/Devices/image8.png) | ![](screenshots/Devices/image7.png) |

**B+C**:

| 360vp                                | 600vp                               |
| ------------------------------------ | ----------------------------------- |
| ![](screenshots/Devices/image10.png) | ![](screenshots/Devices/image9.png) |

使用说明：

1.在预览器中查看页面效果

2.在预览器中开启窗口拖拽模式，拖动窗口变化，可以查看组件的响应式变化，如下图所示： 
 
![](screenshots/Devices/image11.png)

### 工程目录

```
├──entry/src/main/ets                         // 代码区
│  ├──application                                  
│  │  ├──MailBox.ets                          // 邮箱
│  │  ├──PhotoAlbum.ets                       // 图库
│  │  └──Settings.ets                         // 设置
│  ├──common  
│  │  ├──BreakpointSystem.ets   


---
## multi-convenient-life
> 本篇Sample基于自适应布局和响应式布局，实现一次开发，多端部署的便捷生活页面，并根据手机、折叠屏、平板以及2in1不同的设备尺寸实现对应页面。

源码: https://gitcode.com/HarmonyOS_Samples/multi-convenient-life

# 多设备便捷生活界面

## 简介

本篇Sample基于自适应布局和响应式布局，实现一次开发，多端部署的便捷生活页面，并根据直板机、双折叠、平板不同的设备尺寸实现对应页面。

| 直板机                             | 双折叠                           | 平板                             |
|--------------------------------|--------------------------------|--------------------------------|
| ![](screenshots/device/phone.png) | ![](screenshots/device/foldable.png) | ![](screenshots/device/2in1.png) |

## 工程目录结构

```
├──entry/src/main/ets                               // 代码区
│  ├──constants  
│  │  ├──BreakpointConstants.ets                    // 断点常量类
│  │  ├──CommonConstants.ets                        // 公共常量类 
│  │  ├──DishDetailConstants.ets                    // 商品详情页常量类
│  │  ├──FoodListConstants.ets                      // 美食列表页常量类                                  
│  │  └──ShopDisplayConstants.ets                   // 店铺页常量类
│  ├──entryability  
│  │  └─EntryAbility.ets 
│  ├──pages  
│  │  ├──DishDetails.ets                            // 商品详情页
│  │  ├──FoodList.ets                               // 美食列表页
│  │  ├──GraphicText.ets                            // 图文详情页
│  │  ├──Index.ets                                  // 首页 
│  │  ├──Living.ets                                 // 直播页                                  
│  │  └──ShopDisplay.ets                            // 店铺页
│  ├──utils  
│  │  ├──BreakpointType.ets                         // 断点类型类                                  
│  │  └──Logger.ets                                 // 日志打印类
│  ├──view  
│  │  ├──DishComme


---
## multi-device-interaction
> 本实例依托系统级交互归一化能力，实现了跨多端设备的统一交互体验。支持触控屏、触控板、鼠标、键盘等多种输入方式，涵盖基础输入事件、手势识别、拖拽操作及焦点管理等核心交互功能，为多设备交互提供完整示例。

源码: https://gitcode.com/HarmonyOS_Samples/multi-device-interaction

# 实现多设备交互功能

## 项目简介

本实例依托系统级交互归一化能力，实现了跨多端设备的统一交互体验。支持触控屏、触控板、鼠标、键盘等多种输入方式，涵盖基础输入事件、手势识别、拖拽操作及焦点管理等核心交互功能，为多设备交互提供完整示例。

## 效果预览
| 输入设备选择                                            | 交互事件选择                                               | 交互体验                                                |
|---------------------------------------------------|------------------------------------------------------|-----------------------------------------------------|
| <img src='./screenshots/device/page1.png' width=320> | <img src='./screenshots/device/page2.png' width=320> | <img src='./screenshots/device/page3.png' width=320> |

## 使用说明

1. 直板机、双折叠（Mate X系列）、阔折叠、三折叠、平板、PC/2in1、智慧屏设备运行default模块，智能穿戴设备运行wearable模块。
2. 在首页选择要交互的输入设备，进入该输入设备支持的交互事件页。
3. 选择要体验的交互事件，进行交互并查看交互效果。

## 工程目录

```
├───default                                                
│   ├───src/main/ets                               
│   │   ├───common                                        
│   │   │   ├───constants
│   │   │   │   └───Constants.ets                         // 常量类
│   │   │   └───utils
│   │   │       ├───ResourceConversion.ets                // 资源转换类
│   │   │       ├───Utils.ets                             // 通用方法
│   │   │       ├───WidthBreakpointType.ets               // 断点工具类
│   │   │       └───WindowUtil.ets                        // 窗口工具类
│   │   ├───entryability                            
│   │   │   └───EntryAbility.ets                          // Ability的生命周期回调内容
│   │   ├───entrybackupability  


---
## multi-file-download
> 本示例为开发者展示常见的多文件下载，介绍如何使用request模块实现多个文件下载进度和状态的监听管理。

源码: https://gitcode.com/HarmonyOS_Samples/multi-file-download

# 多文件下载监听

### 介绍

本示例为开发者展示常见的多文件下载，介绍如何使用request模块实现多个文件下载进度和状态的监听管理。

### 效果预览
![](./screenshots/device/download.png)

### 使用说明
1. 在源码Index.ets的downloadUrlArray变量中填入要下载的文件数组，编译安装。
2. 打开首页，点击下载队列中某一项下载按钮，或者点击"全部开始"按钮。
3. 文件在下载时，会显示下载进度，点击按钮，暂停下载；再次点击，恢复下载。
4. 文件下载成功后，会显示下载完成；下载失败或错误，会提示。

### 工程目录

```
├──entry/src/main/ets/
│  ├──constants
│  │  └──Constants.ets                  // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──pages                 
│  │  └──Index.ets                      // 首页
│  └──view     
│     ├──FileDownloadItem.ets           // 列表item项            
│     └──ProgressButton.ets             // 进度条按钮
└──entry/src/main/resources             // 应用静态资源目录
```

### 具体实现

1. Index页面中使用List实现下载列表（在downloadUrlArray变量中输入要下载的url数组）。
2. FileDownloadItem中实现列表项视图。
3. 在每个列表项中配置下载参数，创建下载任务，注册相关监听，在监听回调中获取文件的下载状态，将数据绑定到相应组件上。
4. 针对每个下载任务提供启动、暂停、恢复的功能操作。

### 相关权限

1. 网络使用权限：ohos.permission.INTERNET。

### 依赖
不涉及

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。 

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## multi-hap
> 本示例展示多HAP开发，简单介绍了多HAP的使用场景，应用包含了一个entry HAP和两个feature HAP，两个feature HAP分别提供了音频和视频播放组件，entry中使用了音频和视频播放组件。 三个模块需要安装三个hap包，最终会在设备上安装一个主entry的hap包。

源码: https://gitcode.com/HarmonyOS_Samples/multi-hap

# 实现多Hap构建功能

### 介绍

本示例展示多HAP开发，简单介绍了多HAP的使用场景，应用包含了一个entry HAP和两个feature HAP，两个feature HAP分别提供了音频和视频播放组件，entry中使用了音频和视频播放组件。 三个模块需要安装三个hap包，最终会在设备上安装一个主entry的hap包。

本示例用到了应用上下文Context接口 @ohos.app.ability.common媒体服务接口@ohos.multimedia.media。

### 效果预览

| 主页                               | 音频HAP                              | 视频HAP                              |
|----------------------------------|------------------------------------|------------------------------------|
| ![](screenshots/device/home.png) | ![](screenshots/device/audio.png) | ![](screenshots/device/video.png) |

使用说明：

1.第一步：点击Build->Build Hap(s)/APP(s)->Build Hap(s)，构建三个模块的hap包。

2.第二步：使用IDE安装多Hap包。

| 1、点击 entry -> Edit Configurations 打开编辑页 | 2、选择 Deploy Multi Hap 勾选 Deploy Multi Hap Packages 后勾选 audioFeature 和 videoFeature，点击 Apply 后运行项目 |
|-----------------------------------------|---------------------------------------------------------------------------------------------------|
| ![Edit](screenshots/device/edit.png)    | ![deploy](screenshots/device/deploy.png)                                                          |

3.第三步：点击audio，进入audio播放页面，可点击PlayAudio按钮，播放音频。

4.第四步：点击video，进入video播放页面，可点击播放按钮播放视频。

### 工程目录

```
├──audioFeature/src/main/ets/
│  ├──application
│  │  └──MyAbilityStage.ets
│  ├──audioAbility
│  │  └──AudioAbility.ets
│  ├──pages
│  │  └──index.ets                            // audio组件的实现页面
│  └──util
│     └──Logger.ts                            // 日志工具
├──audioFeature/src/main/mod


---
## multi-mobile-payment
> 本篇Sample基于Scan Kit中的默认界面扫码能力与码图生成能力实现移动支付应用中常见的扫一扫和收付款功能。

源码: https://gitcode.com/HarmonyOS_Samples/multi-mobile-payment

# 多设备移动支付界面

## 介绍

本篇Sample基于Scan Kit中的默认界面扫码能力与码图生成能力实现移动支付应用中常见的扫一扫和收付款功能。

## 效果预览
手机运行效果图如下：

<img src="screenshots/device/phone.png" width="320"/>

折叠屏运行效果图如下：

<img src="screenshots/device/foldable.png" width="480"/>

tablet运行效果图如下：

<img src="screenshots/device/tablet.png" width="800"/>


## 使用说明

1. 点击扫一扫可体验扫码能力，扫码结果将以应用日志形式打印。
2. 点击收付款可体验码图生成能力（不涉及实际支付业务），该能力可用于生成包含自定义信息的二维码，可使用其他设备扫码查看生成的码图信息。


## 工程目录结构

```
├──entry/src/main/ets                                   // 代码区
│  ├──common
│  |  └──Constants.ets                                  // 常量
│  ├──entryability
│  |   └──EntryAbility.ets
│  ├──pages
│  |  ├──Home.ets                                       // 首页界面
│  |  ├──Index.ets                                      // 入口界面
│  |  ├──ReceivePaymentPage.ets                         // 收付款界面
│  |  └──ScanQRCodePage.ets                             // 自定义扫码界面
│  ├──view
│  |  ├──CashFlowCenterCard.ets                         // 收款界面底部功能条组件
│  |  ├──FunctionCard.ets                               // 功能卡片
│  |  ├──QuickFunctionCardCircle.ets                    // 快捷功能（圆形）
│  |  ├──QuickFunctionCardSquare.ets                    // 快捷功能（矩形）
│  |  ├──ScanQRCodeDialog.ets                           // 自定义扫码弹窗
│  |  └──XComponentView.ets                             // 扫码能力封装组件
│  └──viewmodel
│     ├──FortunePicksViewModel.ets                      // 财富精选数据
│     ├──PayHubViewModel.ets                            // 支付中心数据
│     ├──QuickFunctionsViewModel.ets                  


---
## multi-nav-bar
> 本示例展示了导航组件在不同设备形态下的样式。

源码: https://gitcode.com/HarmonyOS_Samples/multi-nav-bar

# 一次开发，多端部署-分级导航栏

### 简介

本示例基于自适应布局和响应式布局，实现多设备上的分级导航栏效果。在sm、md断点下，展示为底部页签和顶部页签；在lg断点下，展示为侧边页签和顶部页签；在xl断点下，展示为侧边栏分级导航。为开发者提供分级导航栏的开发方案。

### 预览效果

| 直板机                             | 双折叠                           | 平板                             | PC/2in1                        |
|--------------------------------|--------------------------------|--------------------------------|--------------------------------|
| ![](screenshots/device/sm.png) | ![](screenshots/device/md.png) | ![](screenshots/device/lg.png) | ![](screenshots/device/xl.png) |

### 使用说明

1. 分别在直板机、双折叠（Mate X系列）、平板、PC/2in1设备上安装并打开应用，不同设备的应用页面通过响应式布局和自适应布局呈现不同的效果。
2. 首页内容，支持上下滑动。
3. 点击顶部页签/侧边栏中二级目录切换内容区信息。
4. 点击底部/侧边页签/侧边栏一级目录切换不同功能页面。

### 工程目录
```
├──entry/src/main/ets                     // 代码区
│  ├──common
│  │  └──utils
│  │     ├──BreakpointType.ets            // 断点工具类
│  │     └──WindowUtils.ets               // 窗口工具类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──model
│  │  ├──TabDataModel.ets                 // 导航目录数据类
│  │  └──VideoDataModel.ets               // 内容区数据类
│  ├──pages
│  │  └──Index.ets                        // 首页
│  ├──view
│  │  ├──Home.ets                         // 主页
│  │  ├──SideBarView.ets                  // 侧边栏
│  │  ├──TopTabView.ets                   // 顶部页签
│  │  └──VideoInfoView.ets                // 内容区域页
│  └──viewmodel
│     ├──TabViewModel.ets                 // 导航目录数据
│     └──VideoV


---
## multi-news-read
> 本示例基于自适应布局和响应式布局，实现一次开发，多端部署的新闻阅读页面。根据手机、折叠屏以及平板不同的设备尺寸实现对应页面。

源码: https://gitcode.com/HarmonyOS_Samples/multi-news-read

# 多设备新闻阅读界面

## 介绍

本示例基于自适应布局和响应式布局，实现一次开发，多端部署的新闻阅读页面。根据手机、折叠屏以及平板不同的设备尺寸实现对应页面。

## 效果预览

| 直板机                             | 折叠屏                           | 平板                             |
|--------------------------------|--------------------------------|--------------------------------|
| ![](screenshots/device/phone.png) | ![](screenshots/device/foldable.png) | ![](screenshots/device/tablet.png) |

## 使用说明

1. 点击第一个按钮，布局将根据设备尺寸自动调整列数。
2. 点击第二个按钮，布局在实现响应式列数调整的基础上，会进一步控制内容的显隐：在小尺寸设备上自动隐藏新闻详情，在非小尺寸设备中完整展示。
3. 点击第三个按钮，在小尺寸设备下，新闻将以列表形式展示，在非小尺寸设备下，新闻将以宫格的方式进行展示。


## 工程目录结构

```
├──entry/src/main/ets                                   // 代码区
│  ├──common                                            // 媒体查询工具类
│  |  └──Constants.ets                                  // 常量
│  ├──entryability
│  |   └──EntryAbility.ets
│  ├──pages
│  |  ├──Index.ets                                      // 主页界面
│  |  ├──MediaNews.ets                                  // 媒体新闻
│  |  ├──NewsChannel.ets                                // 新闻频道
│  |  └──NewsListPage.ets                               // 新闻列表界面
│  ├──view
│  |  ├──Header.ets                                     // 页签头部组件
│  |  ├──HotList.ets                                    // 热门列表组件
│  |  ├──LeftTextRightImageBgGray.ets                   // 左文右图组件1
│  |  ├──LeftTextRightImageBgWhite.ets                  // 左文右图组件2
│  |  ├──NewsWithImages.ets                             // 上文下图组件
│  |  ├──TopImageBottomText.ets                         // 上图


---
## multi-short-video
> 本示例基于自适应布局和响应式布局，实现一次开发，多端部署的短视频页面。通过“三层工程架构”实现代码复用，并根据手机、折叠屏以及2in1不同的设备尺寸实现对应页面。

源码: https://gitcode.com/HarmonyOS_Samples/multi-short-video

# 多设备短视频界面

## 介绍

本示例基于自适应布局和响应式布局，实现一次开发，多端部署的短视频页面。通过“三层工程架构”实现代码复用，并根据直板机、双折叠、平板以及PC/2in1不同的设备尺寸实现对应页面。

## 效果预览
![image](screenshots/device/phone.png)

## 使用说明

点击分享按钮，拉起分享弹窗。在手机上是半模态弹窗，双折叠上是居中弹窗，而平板上是跟手弹窗。

## 工程目录
```
├──commons
│  └──base/src/main/ets
│     └──constants
│        └──BreakpointConstants.ets       // 常量类
├──features
│  ├──home/src/main/ets
│  │  ├──constants
│  │  │  └──HomeConstants.ets             // 常量类
│  │  └──view
│  │     └──Home.ets                      // 主页面view
│  └──home/src/main/resources             // 应用静态资源目录
└──products
   ├──entry/src/main/ets
   │  ├──common
   │  │  └──constants
   │  │     └──CommonConstants.ets        // 常量类
   │  ├──entryability
   │  │  └──EntryAbility.ets              // 程序入口类
   │  └──pages
   │     └──MainPage.ets                  // 主页面
   └──entry/src/main/resources            // 应用静态资源目录
```
## 具体实现

* 使用Share Kit（分享服务）实现分享功能。

## 相关权限

不涉及。

## 依赖

不涉及。

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：直板机、双折叠（Mate X系列）、平板、PC/2in1。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## multi-tab-navigation
> 本示例为开发者提供常见的Tab导航的UI样式，包括底部导航，顶部导航，侧边导航等典型场景。

源码: https://gitcode.com/HarmonyOS_Samples/multi-tab-navigation

# 基于Tabs组件实现常见导航样式

### 介绍

Tabs组件可以让用户能聚焦于当前显示的内容，对页面内容进行分类，提高页面空间利用率。本示例基于Tabs组件，为开发者提供不同场景下的导航样式，如：常见底部导航、舵式底部导航、可滑动+更多按钮样式、侧边导航等。

### 效果预览
| 常见底部导航                                                 | 舵式底部导航                                                 | TabContent视频内容滑动                                        | 可滑动+更多按钮样式                                            |                         
|--------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------|-------------------------------------------------------|
| <img src='screenshots/device/bottom.gif' width=320>    | <img src='screenshots/device/rudder.gif' width=320>    | <img src='screenshots/device/tabcontent.gif' width=320> | <img src='screenshots/device/button.gif' width=320>   |      
| 下划线样式                                                  | 背景高亮样式                                                 | 文字样式                                                    | 双层嵌套样式 1                                              |
| <img src='screenshots/device/underline.gif' width=320> | <img src='screenshots/device/highlight.gif' width=320> | <img src='screenshots/device/writing.gif' width=320>    | <img src='screenshots/device/nesting1.gif' width=320> |
| 双层嵌套样式 2                                               | 常见侧边导航                                                 | 抽屉式侧边导航                                                 | 居


---
## multi-ticket-class
> 本示例主要使用栅格布局和List组件相结合的方式，实现了股票类差异化的多场景响应式变化效果。

源码: https://gitcode.com/HarmonyOS_Samples/multi-ticket-class

# 多设备股票类界面

## 介绍

本篇Sample基于自适应布局和响应式布局，实现一次开发，多端部署的股票交易应用。根据不同设备尺寸（如直板机、双折叠（Mate X系列）、阔折叠、三折叠、平板），实现了相应的页面布局。该Sample支持在双折叠（Mate X系列）、三折叠和平板设备上分屏显示，便于对比股票详情。

## 效果预览

本示例分为两个页面和两个弹框。鉴于三折叠与平板横向断点均为lg，在效果预览页面中，仅展示平板设备的效果示意图。

**自选首页**:

| 阔折叠                                 | 直板机                                          | 折叠屏（展开态）                           | 平板                        |
|-------------------------------------|----------------------------------------------|------------------------------------|-----------------------------------|
| ![](screenshots/devices/home-page-purax.png) | ![](screenshots/devices/home-page-phone.png) | ![](screenshots/devices/home-page-foldablescre.png) | ![](screenshots/devices/home-page-tablet.png) |

**股票详情页**:

| 阔折叠                                 | 直板机                                 | 折叠屏（展开态）                           | 平板（全屏）                             |
|-------------------------------------|------------------------------------|------------------------------------|------------------------------------|
| ![](screenshots/devices/detail-page-purax.png) | ![](screenshots/devices/detail-page-phone.png) | ![](screenshots/devices/detail-page-foldablescre.png) | ![](screenshots/devices/detail-page-tablet.png) |

**多股比价**:

|             | 折叠屏分屏-双股比价                                             | 折叠屏全景多窗-三股比价                                     |
|-------------|--------------------------------------------------------|-----------------------


---
## multi-travel-accommodation
> 本示例主要使用栅格布局和List组件相结合的方式，实现了旅行住宿差异化的多场景响应式变化效果。

源码: https://gitcode.com/HarmonyOS_Samples/multi-travel-accommodation

# 多设备旅行订票界面

### 介绍

本示例主要使用栅格布局和List组件相结合的方式，实现了旅行住宿差异化的多场景响应式变化效果。

### 效果预览

本示例在预览器中的效果：

**酒店详情页**:

| 直板机                               | 双折叠（展开态）                                | 平板                                     |
|----------------------------------|-----------------------------------------|---------------------------------------------|
| ![](screenshots/Devices/phone_hotel_page.PNG) | ![](screenshots/Devices/fold_hotel_page.png) | ![](screenshots/Devices/pad_hotel_page.png) |

**低价日历效果**:

| 直板机                                | 双折叠（展开态）                                  | 平板                                        |
|------------------------------------|-------------------------------------------|------------------------------------------------|
| ![](screenshots/Devices/phone_calendar_page.png) | ![](screenshots/Devices/fold_calendar_page.png) | ![](screenshots/Devices/pad_calendar_page.png) |

**查询车票页**:

| 直板机                                 | 双折叠（展开态）                                       | 平板                                       |
|-------------------------------------|------------------------------------------------|----------------------------------------------|
| ![](screenshots/Devices/phone_search_page.png) | ![](screenshots/Devices/fold_search_page.png) | ![](screenshots/Devices/pad_search_page.png) |

使用说明：

1.可以在预览器中查看页面效果，也可在对应设备上查看页面效果。

2.在首页点击酒店详情页及低价日历按钮，会跳转至酒店详情页，直板机的顶部图片会在滚动至最顶部展开，离开顶部收起， 双折叠左侧下方的小图可滚动，点击小图会更换大图，平板为左侧可滑动切换图片的布局。

3.在酒店详情页点击低价日


---
## multi-travel-navigation
源码: https://gitcode.com/HarmonyOS_Samples/multi-travel-navigation

# 多设备地图导航界面

### 介绍

本示例主要使用Map Kit的相关能力实现多端上地图的查看、搜索地点、路径规划及服务卡片和实况胶囊等典型场景。

### 效果预览

首页运行效果图如下：

| 手机                                  | 折叠屏                                 |
|-------------------------------------|-------------------------------------|
| ![](screenshots/device/sm/home.png) | ![](screenshots/device/md/home.png) |

搜索结果页运行效果如下：

| 手机                                    | 折叠屏                                   |
|---------------------------------------|---------------------------------------|
| ![](screenshots/device/sm/search.png) | ![](screenshots/device/md/search.png) |

路线规划页运行效果如下：

| 手机                                   | 折叠屏                                  |
|--------------------------------------|--------------------------------------|
| ![](screenshots/device/sm/route.png) | ![](screenshots/device/md/route.png) |

服务卡片运行效果如下：

| 手机                                  | 折叠屏                                 |
|-------------------------------------|-------------------------------------|
| ![](screenshots/device/sm/form.png) | ![](screenshots/device/md/form.png) |

实况窗运行效果如下：

| 手机（通知中心）                            | 折叠屏（通知中心）                           |
|-------------------------------------|-------------------------------------|
| ![](screenshots/device/sm/live.png) | ![](screenshots/device/md/live.png) |

### 相关概念

- 一次开发，多端部署：一套代码工程，一次开发上架，多端按需部署。支撑开发者快速高效的开发支持多种终端设备形态的应用，实现对不同设备兼容的同时，提供跨设备的流转、迁移和协同的分布式体验。
- 自适应布局：当外部容器大小发生变化时，元素可以根据相对关系自动变化以适应外部容器变化的布局能力。


---
## native-multi-threads
> 本示例以生产者-消费者模型为案例来介绍如何进行Native多线程开发以及线程间通信。Native侧通过调用C++标准库实现生产者-消费者模型，并分别使用了多种线程间通信的方式来进行ArkTS应用侧数据传输，以实现UI界面图片刷新。

源码: https://gitcode.com/HarmonyOS_Samples/native-multi-threads

# 基于Native实现多线程开发以及线程间通信功能

### 简介

本示例以生产者-消费者模型为案例来介绍如何进行Native多线程开发以及线程间通信。Native侧通过调用C++标准库实现生产者-消费者模型，并分别使用了多种线程间通信的方式来进行ArkTS应用侧数据传输，以实现UI界面图片刷新。界面效果如图所示：

![synchronized_operation](screenshots/device/readme.png)

### 工程目录
```
├──entry/src/main/common                      
│  └──constans
│     └──CommonConstants.ets                  // 常量定义文件
├──entry/src/main/cpp                         // C++ 代码区                   
│  ├──types
│  │  └──libentry                             // C++接口导出
│  │     ├──index.d.ts                        
│  │     └──oh-package.josn5                 
│  ├──CMakeLists.txt                          // CMake配置文件
│  ├──MultiThreads.cpp                        // Native模块注册
│  ├──ProducerConsumer.cpp                    // 业务功能实现
│  └──ProducerConsumer.h                      
├──entry/src/main/ets                         // ets 代码区
│  ├──entryability
│  │  └──EntryAbility.ets       
│  ├──images                                  // 自定义png图片
│  └──pages
│     └──Index.ets                            // 主页界面
└──entry/src/main/resources                   // 应用资源目录
```

### 相关概念

- **NAPI：** NAPI提供的接口名与三方Node.js一致，目前支持部分接口。

- **NAPI中支持的标准库：** 目前支持标准C库、C++库、OpenSL ES、zlib。

- **NAPI接口说明：** 包含napi相关函数的用法、参数解释、以及一些应用示例。

- **生产者-消费者模型：** 某个模块负责产生数据，这些数据由另一个模块来负责处理。产生数据的模块，就形象地称为生产者；而处理数据的模块，就称为消费者。本示例中，Native侧通过C++线程、信号量以及条件变量等关键特性来实现生产者-消费者模型。生产者线程负责从字符串数组中搜索目标文件路径。搜索到后，放入缓冲队列中。消费者线程负责从缓冲队列中取出目标文件路径，并通过线程通信的方式将结果返回给ArkTS应用侧。

- **Native侧子线程与ArkTS主线程通信方式**

  


---
## native-progress-notify
> 本示例通过模拟下载场景介绍如何将Native的进度信息实时同步到ArkTS侧。

源码: https://gitcode.com/HarmonyOS_Samples/native-progress-notify

# 基于Native实现进度通知功能

### 介绍

本示例通过模拟下载场景介绍如何将Native的进度信息实时同步到ArkTS侧。通过在Native侧创建线程安全函数将Native侧子线程中的进度数据实时同步给ArkTS侧，用于界面显示。通过该示例开发这个可以了解Native线程安全函数相关接口以及Native侧进度条实时同步实现方案。

### 效果图预览

![](screenshots/device/native_progress_notify.gif)

**使用说明**

1. 点击“Start Download“按钮后，Native侧启动子线程模拟下载任务。
2. Native侧启动子线程模拟下载，并通过ArkTS的回调函数将进度信息实时传递到ArkTS侧。

### 高性能知识点

本例中，在Native侧使用子线程执行下载任务，从而避免对主线程资源的占用，能有效提升性能。

### 工程结构&模块类型

```
├──entry/src/main/cpp                         // C++ 代码区
│  ├──types
│  │  └──libentry                             // C++接口导出
│  │     ├──index.d.ts                        
│  │     └──oh-package.josn5                 
│  ├──CMakeLists.txt                          // CMake配置文件
│  └──napi_init.cpp                           // Native模块注册
├──entry/src/main/ets                         // ets 代码区
│  ├──constants
│  │  └──CommonConstants.ets                  // 常量定义文件  
│  ├──conversionability
│  │  └──ConversionAbility.ets       
│  └──pages
│     └──Index.ets                            // 主页界面
└──entry/src/main/resources                   // 应用资源目录
```

### 相关权限

**不涉及**

### 参考资料

1. [Progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress)
2. [使用Node-API实现跨语言交互](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-napi-interaction-with-cpp)

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。 
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。 
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。 
4. HarmonyOS SDK版本：Harmony


---
## native-save-pic-to-sand-box
> 本示例主要介绍Native如何将网络上的图片及Rawfile中的图片保存到应用沙箱中。

源码: https://gitcode.com/HarmonyOS_Samples/native-save-pic-to-sand-box

# 基于Native实现保存图片到应用沙箱功能

### 介绍

本示例主要介绍如何在Native侧将图片保存到应用沙箱中，主要包括保存网络图片和保存Rawfile中的图片两种场景。保存网络图片主要利用Curl三方库能力实现，保存Rawfile中的图片主要通过资源管理器以及字节流的方式保存图片。通过该案例开发者可以了解到两种不同场景下获取图片并保存的详细方法。

### 效果图预览

![](screenshots/device/native_image_to_sandbox.gif)

**使用说明**

1. rawfile路径下存有一张图片IMG_4558.JPG。

2. 设备连接上网络。

3. 点击"保存Rawfile图片"，前端通过调用Native侧暴露的saveImageOfRawfileCallback接口将rawfile中的图片IMG_4558.JPG保存到应用沙箱中并返回沙箱路径到前端进行显示；点击“保存网络图片”，前端通过调用Native侧暴露的saveImageOfInternetCallback接口将网络图片保存到应用沙箱中并返回沙箱路径到前端进行显示。

### 工程结构&模块类型

```
│  ├──entry/src/main/cpp                      // C++ 代码区
│  ├──types
│  │  └──libentry                             // C++接口导出
│  │     ├──index.d.ts                        
│  │     └──oh-package.josn5                 
│  ├──CMakeLists.txt                          // CMake配置文件
│  └──napi_init.cpp                           // Native模块注册
├──entry/src/main/ets                         // ets 代码区
│  ├──constants
│  │  └──CommonConstants.ets                  // 常量定义文件  
│  ├──conversionability
│  │  └──ConversionAbility.ets       
│  └──pages
│     └──Index.ets                            // 主页界面
└──entry/src/main/resources                   // 应用资源目录
```

### 模块依赖

本实例依赖开源库libcurl。

### 相关权限

网络访问权限：ohos.permission.INTERNET。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## natural-language-kit-sample-code-client-demo-arkts
> 本示例展示了文本语义理解相关的AI能力，帮助开发者更好地处理和分析文本数据。

源码: https://gitcode.com/HarmonyOS_Samples/natural-language-kit-sample-code-client-demo-arkts

# 实现分词、实体抽取

## 介绍

本示例展示了基于自然语言处理服务的分词、实体抽取功能。

本示例模拟了在应用里，输入一段文字，调用分词、实体抽取能力后得到的结果。

需要使用通用文字识别接口@hms.ai.nlp.textProcessing.d.ts。

## 效果预览

|         **主页面**          |             **分词**             |             **实体抽取**             |
|:------------------------:|:--------------------------------:|:--------------------------------:|
| ![](screenshots/app.png) | ![](screenshots/wordSeg.png) | ![](screenshots/getEntity.png) | 

使用说明：

1. 在手机的主屏幕，点击”nlpDemo“，启动应用。
2. 输入一段文字。
3. 点击“Get Word Segmentation Result”按钮，展示出分词结果，点击"Get Entity Results"，展示出实体抽取结果。

### 工程目录
```
├─entry/src/main/ets                         // 代码区
│  ├─entryability
│  │  └─EntryAbility.ets       
│  └─pages
│     └─Index.ets                            // 主页界面
├─entry/src/main/resources                   // 应用资源目录
└─screenshots                                // 截图
```

## 具体实现

本示例展示的控件在@hms.ai.nlp.textProcessing.d.ts定义了分词和实体抽取的API：
~~~
*   function getWordSegment(text: string): Promise<Array<WordSegment>>;
*   function getEntity(text: string, entityConfig?: EntityConfig): Promise<Array<Entity>>;
~~~
输入一段文本后点击分词、实体结果按钮，接收处理返回的结果（文字信息）。参考entry/src/main/ets/pages/Index.ets.

## 相关权限

不涉及。

## 依赖

不涉及。

## 约束与限制

1. 本实例仅支持标准系统上运行，支持设备：华为手机、华为平板、2in1。
2. HarmonyOS系统：HarmonyOS 5.0.0 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。


---
## navigation-router
> 通过设计单独的路由模块和动态加载方法，解决一个Navigation组件下多har/hsp间路由跳转依赖耦合问题。

源码: https://gitcode.com/HarmonyOS_Samples/navigation-router

# 基于路由模块和动态加载实现应用页面路由导航功能

## 介绍

通过设计单独的路由模块和动态加载方法，将路由功能抽取为单独的模块供其他模块使用，实现业务模块间的解耦。帮助开发者在页面跳转开发场景中，解决了一个Navigation组件下多har/hsp间路由跳转依赖耦合问题。

## 效果预览

![路由导航效果预览](screenshots/device/demonstration.gif)

## 使用说明

点击页面按钮，路由跳转至对应页面。

## 工程目录

```
├──entry                                          // 入口模块
│  ├──build-profile.json5                         // 编译配置文件，其中arkOptions需配置动态import依赖的包名
│  ├──oh-package.json5                            // 依赖配置，需依赖全部子业务模块和RouterModule模块
│  ├──src/main/ets
│  │  ├──entryability
│  │  │  └──EntryAbility.ets
│  │  └──pages
│  │     └──Index.ets                             // 首页
│  └──src/main/resources                          // 资源目录
├──harA                                           // 子业务模块
│  ├──Index.ets                                   // 入口文件，对外暴露模块方法
│  ├──oh-package.json5                            // 依赖配置，需依赖RouterModule模块
│  ├──src/main/ets/components/mainpage
│  │  ├──A1.ets                                 
│  │  └──A2.ets                                 
│  └──src/main/resources
├──harB                                           // 子业务模块
│  ├──Index.ets                                   // 入口文件，对外暴露模块方法
│  ├──oh-package.json5                            // 依赖配置，需依赖RouterModule模块
│  ├──src/main/ets/components/mainpage
│  │  ├──B1.ets
│  │  ├──B2.ets
│  │  └──B3.ets
│  └──src/main/resources
├──harC                                           // 子业务模块
│  ├──Index.ets                                   // 入口文件，对外暴露模块方法
│  ├──oh-package.json5  


---
## nbody
> 在本示例中，使用ArkTS编程语言开发了业界编程语言基准测试项目Benchmarks Game中的N体问题模拟程序，实现类木星体轨道计算。

源码: https://gitcode.com/HarmonyOS_Samples/nbody

# 基于多线程实现N-Body模拟程序

### 介绍

在本示例中，使用ArkTS编程语言中的@ohos.taskpool和@ohos.worker 等接口开启多线程任务，实现了业界编程语言基准测试项目Benchmarks Game中的N体问题模拟程序，完成类木星体轨道计算，可以用于AOT(Ahead Of Time)等性能测试。

### 效果预览
| 主页                                       |计算中|重复点击|计算结果|
|------------------------------------------|-------|-------|-------|
| ![](screenshots/device/n-body_entry.png) |![](screenshots/device/n-body_calculating.png)|![](screenshots/device/n-body_reClick.png)|![](screenshots/device/n-body_result.png)|

使用说明

1.点击按钮Calculate By TaskPool，会从任务池创建一个任务，进行N-Body计算。

2.点击按钮Calculate By Worker，会创建一个Worker，进行N-Body计算。

### 工程目录
```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets                 // 封装整个模块启用
│  ├──model
│  │  ├──CalculateUtil.ets                // worker和taskpool都在这里调用            
│  │  └──NBody_ETS_6.ts                   // 天体轨道计算
│  ├──pages
│  │  └──Index.ets                        // 首页
│  ├──utils
│  │  ├──Constants.ts                     // 封装只读常量
│  │  └──Logger.ts                        // 封装整个日志
│  └──worker
│     └──CalculateWorker.ts               // worker线程
└──entry/src/main/resources               // 应用静态资源目录        
                                            
```
### 相关概念

AOT(Ahead Of Time)，即预先编译，在应用程序运行前，将代码预先编译成高性能机器代码，避免在运行时的编译性能消耗和内存消耗，让程序在首次运行就能通过执行高性能机器码获得性能收益。

### 具体实现

- 使用TaskPool开启子线程运行，计算50万次时间推移天体运行轨道，源码参考[CalculateUtil.ets ](entry/src/main/ets/model/CalculateUtil.ets )
  - 通过调用computeNBodyByTaskPool()创建一个task任务，并向taskpool线程池派发子线程任务。
  - 等待子线程执


---
## ndk-opengl
> XComponent控件常用于相机预览流的显示和游戏画面的绘制,在HarmonyOS上，可以配合Native Window创建OpenGL开发环境，并最终将OpenGL绘制的图形显示到XComponent控件。

源码: https://gitcode.com/HarmonyOS_Samples/ndk-opengl

# 多设备游戏界面

## 介绍

XComponent控件常用于相机预览流的显示和游戏画面的绘制，在HarmonyOS上，可以配合Native Window创建OpenGL开发环境，并最终将OpenGL绘制的图形显示到XComponent控件。本示例基于"Native C++"模板，调用OpenGL(OpenGL ES)图形库相关API绘制3D图形（三棱锥），并将结果渲染到页面的XComponent控件中进行展示。同时，点击自动旋转按钮可以自动旋转，点击阻尼旋转可以减速旋转直至停止旋转，还可以在屏幕上通过触摸滑动手势对三棱锥进行旋转，最终得到不同角度的图形并显示到页面。

## 效果预览

|  直板机   |               双折叠（Mate X系列）               | 平板                                 |
|:-----:|:-------------------------------:|------------------------------------|
| ![](screenshots/device/图片1.png) | ![](screenshots/device/图片4.png) | ![](screenshots/device/tablet.png) |

使用说明

应用界面中展示了XComponent相关控件的使用，及采用OpenGL (OpenGL ES)相关标准API绘制3D图形（三棱锥，3D渲染的光源用的是简单的线性光源）。

可在屏幕触摸滑动旋转三棱锥，或点击按钮使三棱锥进行自动或阻尼旋转，其中主要采用了napi接口来更新3D图形的旋转角度。

此外，增加了一多适配能力，OpenGL绘制三棱锥区域可自适应直板机、双折叠（Mate X系列）、平板设备，同时，支持竖屏旋转，且自动避让摄像头区域。

## 工程目录

```
├──entry/src/main/cpp/
│  ├──CMakeLists.txt                       // cmake编译配置
│  ├──app_napi.cpp                         // 调用native接口
│  ├──include
│  │  ├──app_napi.h
│  │  ├──tetrahedron.h
│  │  ├──frame_handle.h
│  │  └──util
│  │     ├──log.h
│  │     ├──napi_manager.h
│  │     ├──napi_util.h
│  │     └──native_common.h
│  ├──module.cpp                           // napi模块注册
│  ├──napi_manager.cpp
│  ├──napi_util.cpp
│  ├──frame_handle.cpp
│  ├──tetrahedron.cpp                      // OpenGL (ES) 三棱锥实现
│  └──type
│     └──libentry
│        ├──oh-package.json5
│        └──tetrahedron_napi.d.ts          // 接口导出
├──entry/src/main/ets
│  ├──entryability
│  │  └──Entry


---
## ndk-rawfile
> 本示例中主要介绍在TaskPool子线程中使用dlopen加载so库，以及如何使用Native Rawfile接口操作Rawfile目录和文件。功能包括文件列表遍历、文件打开、搜索、读取和关闭Rawfile。

源码: https://gitcode.com/HarmonyOS_Samples/ndk-rawfile

# 基于dlopen实现加载so库获取Rawfile资源功能

## 介绍

本示例中主要介绍在TaskPool子线程中使用dlopen加载so库，以及如何使用Native Rawfile接口操作Rawfile目录和文件。功能包括文件列表遍历、文件打开、搜索、读取和关闭Rawfile。

## 效果预览

| 主页                                   |
| ------------------------------------ |
| ![main](screenshots/device/main.png) |

使用说明

应用界面中展示了Rawfile相关的接口调用，包括获取resources/rawfile目录下的文件、对应的rawfile文件内容、对应rawfile文件的descriptor。其中使用到的功能包括文件列表遍历、文件打开、搜索、读取和关闭Rawfile。

## 工程目录

```
├──entry/libs/                             // 需要加载的.so文件
│  ├──arm64-v8a
│  │  └──libentry.so
│  └──x86_64
│     └──libentry.so
├──entry/src/main/cpp/                     // native侧代码
│  ├──include
│  │  └──global_handlers.h                 // 包含全局对象global_handlers的头文件
│  ├──types
│  │  ├──libentry
│  │  │  ├──index.d.ts                     // 接口导出
│  │  │  └──oh-package.json5
│  │  └──libpreloadso
│  │     ├──index.d.ts                     // 接口导出
│  │     └──oh-package.json5
│  ├──CMakeLists.txt                       // 编译脚本
│  ├──global_handlers.cpp                  // 定义全局对象global_handlers
│  ├──preloadso.cpp                        // preload接口
│  └──rawfile_demo.cpp                     // 调用native接口
├──entry/src/main/ets                      // ArkTS侧代码
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──pages
│  │  └──Index.ets                         // 首页
│  └──utils
│     ├──Constants.ets                     // 预加载的so文件数组
│     ├──Logger.ets                        // 日志工具
│     └──TaskPool.ets                      // TaskPool子线程加载so库
└──entry/src/mai


---
## ndk-xcomponent
> 本示例中主要介绍开发者如何使用Native XComponent接口来获取NativeWindow实例、获取布局/事件信息、注册事件回调、通过OpenGL/EGL实现在页面上绘制形状、渲染YUV图像文件。功能主要包括点击按钮绘制一个五角星，并可以通过点击XComponent区域改变五角星的颜色；点击按钮渲染YUV图像文件。

源码: https://gitcode.com/HarmonyOS_Samples/ndk-xcomponent

# 基于XComponent组件实现OpenGL图形绘制及YUV图像渲染功能

## 介绍

本示例中主要介绍开发者如何使用Native XComponent接口来获取NativeWindow实例、获取布局/事件信息、注册事件回调、通过OpenGL/EGL实现在页面上绘制形状、渲染YUV图像文件。功能主要包括:

1. 点击按钮绘制一个五角星，并可以通过点击XComponent区域改变五角星的颜色。

2. 点击按钮渲染YUV图像文件。

## 效果预览

| 绘制五角星                                    | 改变颜色                                             | 图像渲染                                            |
| ---------------------------------------- | ------------------------------------------------ | ----------------------------------------------- |
| ![main](screenshots/device/drawStar.png) | ![draw star](screenshots/device/changeColor.png) | ![change color](screenshots/device/loadYUV.png) |

使用说明

1. 安装编译生成的hap包，并打开应用。

2. 点击页面底部“Draw Star”按钮，页面将绘制一个五角星。

3. 点击XComponent组件区域（页面中白色区域）改变五角星颜色。

4. 切换页签，点击“Load YUV”按钮，页面渲染YUV文件。

## 工程目录

```
├──entry/src/main/cpp            // C++代码区
│  ├──common
│  │  └──common.h                // 常量定义文件
│  ├──manager                    // 生命周期管理模块
│  │  ├──plugin_manager.cpp
│  │  └──plugin_manager.h
│  ├──render                     // 渲染模块
│  │  ├──egl_core.cpp
│  │  ├──egl_core.h
│  │  ├──plugin_render.cpp
│  │  └──plugin_render.h
│  ├──CMakeLists.txt             // CMake配置文件
│  └──napi_init.cpp              // Napi模块注册
├──entry/src/main/ets            // ets代码区
│  ├──common
│  │  └──CommonConstant.ets      // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets        // 程序入口类
│  ├──interface
│  │  └──XComponentContext.ets   // 接口类
│  ├──pages                      // 页面文件
│


---
## ndkcreate-ui
> 本示例是通过DNK接口构建UI界面

源码: https://gitcode.com/HarmonyOS_Samples/ndkcreate-ui

# 通过NDK方式构建UI界面

## 介绍

ArkUI开发框架提供了一系列NDK接口，能够在应用中使用C和C++代码构建UI界面，这些接口包括UI组件创建、UI树操作、属性设置和事件监听等。
用户可以通过本工程学习相关NDK接口的用法。

## 效果预览

<img src="./screenshots/device/1.gif" width="320">


## 工程目录

```
|──entry/src/main/cpp
|  |──classdef
|  |  |──include
|  |  |  |──ArkUIBaseNode.h                          // 组件树操作的基类
|  |  |  |──ArkUICustomContainerNode.h               // 实现自定义容器组件的封装类
|  |  |  |──ArkUICustomNode.h                        // 实现自定义UI组件的封装类
|  |  |  |──ArkUIListItemAdapter.h                   // 懒加载封装类
|  |  |  |──ArkUIListItemGroupNode.h                 // 懒加载文本
|  |  |  |──ArkUIListItemNode.h                      // 列表项的封装
|  |  |  |──ArkUIListNode.h                          // 列表组件的封装
|  |  |  |──ArkUIMixedNode.h                         // 混合模式封装类
|  |  |  |──ArkUIMixedRefresh.h                      // Refresh组件的封装类
|  |  |  |──ArkUINode.h                              // 通用组件的封装
|  |  |  |──ArkUITextNode.h                          // 实现文本组件的封装类
|  |  |  └──NativeModuleInstance.h                   // ArkUI在Native侧模块的封装接口
|  |  └──src
|  |  |  |──ArkUIBaseNode.cpp                        // 组件树操作的基类
|  |  |  |──ArkUICustomContainerNode.cpp             // 实现自定义容器组件的封装类
|  |  |  |──ArkUICustomNode.cpp                      // 实现自定义UI组件的封装类
|  |  |  |──ArkUIListItemAdapter.cpp                 // 懒加载封装类
|  |  |  |──ArkUIListItemGroupNode.cpp               // 懒加载文本
|  |  |  |──ArkUIListItemNode.cpp                    // 列表项的封装
|  |  |  |──ArkUIListNode.cpp               


---
## nested-list
> 本示例通过List组件scrollToIndex方法实现List组件嵌套滑动。

源码: https://gitcode.com/HarmonyOS_Samples/nested-list

# 实现List组件嵌套滑动的效果

### 介绍

本示例通过List组件的scrollToIndex接口，实现两个List组件（ListA、ListB）嵌套时，ListA滑动到某一位置，ListB跟随滑动至业务期望的位置。帮助开发者掌握两个List嵌套滑动时的场景如何处理。

### 效果预览

|                   主页                   |
|:--------------------------------------:|
| ![home](screenshots/devices/phone.gif) |

使用说明

1.运行后滑动页面。

### 工程目录

```
├──entry/src/main/ets/
│  ├──constants                         
│  │  └──CommonConstants.ets            // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 入口类
│  ├──pages
│  │  └──Index.ets                      // 主页
│  ├──view
│  │  └──CardItemComponent.ets          // 自定义子组件
│  └──viewmodel
│     ├──CardItem.ets                   // 卡片实体类
│     ├──ClassifyModel.ets              // 列表实体类
│     └──ClassifyViewModel.ets          // 数据类
└──entry/src/main/resources             // 应用静态资源目录

```

### 具体实现

通过List接口scrollToIndex方法实现一个List滑动时另一个List跟随滑动到相应的位置。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## network-boost-kit-sample-code-arkts
源码: https://gitcode.com/HarmonyOS_Samples/network-boost-kit-sample-code-arkts

# 基于网络感知和预测能力实现网络加速

## 简介

Network Boost Kit（网络加速服务）提供网络加速能力以及网络感知、网络质量预测等能力，通过软、硬、芯、端、管、云等全方位的协同解决方案实现网络资源的调优和加速，从而构筑更可靠、更流畅、更高速的上网体验。

## 开发前准备

- 在开发HarmonyOS应用前，先进行对应的开发环境安装与调试。
- 了解网络加速服务代码结构。

## 效果预览

| 主页效果图                                | 网络质量评估                               | 网络场景识别                   |
|--------------------------------------|--------------------------------------|----------------------------------------|
| ![image](screenshots/renderings.png) | ![image](screenshots/networkQos.png) | ![image](screenshots/networkScene.png) |

| 传输体验反馈                                | 连接迁移通知                               | 迁移模式设置                   |
|--------------------------------------|--------------------------------------|----------------------------------------|
| ![image](screenshots/reportQoe.png) | ![image](screenshots/netHandover.png) | ![image](screenshots/setHandoverMode.png) |
## 工程目录

```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets             // 程序入口Ability
│  └──pages
│     ├──MainPage.ets                 // 主界面
│     ├──NetworkQos.ets               // 网络质量评估测试页面
│     ├──NetworkScene.ets             // 网络场景识别测试页面
│     ├──ReportQoe.ets                // 传输体验反馈测试页面
│     ├──NetworkHandover.ets          // 连接迁移通知测试页面
│     └──SetHandoverMode.ets          // 迁移模式设置测试页面
└──entry/src/main/resources           // 应用静态资源目录
```

## 具体实现

本示例主要展示的网络质量评估、网络场景识别、应用传输体验反馈功能对应的接口在@hms.networkboost.netquality.d.ts中，连接迁移通知、迁移模式设置功能对应的接口在@hms.


---
## network-manager
> 此Demo展示如何查询网络详情、域名解析、网络状态监听等功能。

源码: https://gitcode.com/HarmonyOS_Samples/network-manager

# 实现网络管理的功能

### 介绍
本示例通过@ohos.net.connection接口实现网络的详情、域名解析、网络监听等功能，注意需要申请ohos.permission.GET_NETWORK_INFO和ohos.permission.INTERNET权限。帮助开发者掌握如何处理检查网络、监听网络等的网络相关场景。

### 效果预览：
![image](screenshots/network.gif)


使用说明：

1.启动应用，在点击**检查网络**、**网络详情**、**网络连接信息**后，展示对应的信息；

2.在域名解析的模块下，输入对应的域名后，点击**域名解析**，展示解析的域名ip地址；

3.在网络监听模块下，开启网络监听后，展示当前监听的网络信息；关闭网络监听后，停止监听网络信息。


### 工程目录
```
├──entry/src/main/ets/
│  ├──common 
│  │  └──Constant.ets
│  ├──entryability
│  │  └──EntryAbility.ets                      
│  ├──pages
│  │  └──Index.ets
└──entry/src/main/resources                              
```

### 具体实现
使用@ohos.net.connection（网络连接管理）接口实现网络的详情、域名解析、网络监听等功能。


### 相关权限
允许应用获取数据网络信息：ohos.permission.GET_NETWORK_INFO

允许使用Internet网络：ohos.permission.INTERNET

### 依赖

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 6.0.0 Beta5及以上。

3. DevEco Studio版本：DevEco Studio 6.0.0 Beta5及以上。

4. HarmonyOS SDK版本：HarmonyOS 6.0.0 Beta5 SDK及以上。


---
## network-performance-timing
> 本示例为开发者展示http数据请求的性能分析API：PerformanceTiming，以表格的形式展示从request到对应阶段完成的耗时。

源码: https://gitcode.com/HarmonyOS_Samples/network-performance-timing

# 实现网络性能分析功能

### 介绍

本示例为开发者展示http数据请求的性能分析API：PerformanceTiming，以表格的形式展示从request到对应阶段完成的耗时，包括DNS、TCP、TLS、FirstSend、FirstReceive、TotalFinish等阶段耗时。

### 效果预览
![](./screenshots/device/network.png)

### 使用说明
打开首页，在输入框中填写http或https的测试地址，点击请求，查看表格中的各阶段网络性能耗时数据。

### 工程目录

```
├──entry/src/main/ets/
│  ├──constants
│  │  └──Constants.ets                  // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  └──pages                 
│     └──Index.ets                      // 首页
└──entry/src/main/resources             // 应用静态资源目录
```

### 具体实现

1. 创建http，设置监听回调headersReceive。
2. 设置请求参数，包括但不限于method、header等。
3. 发起请求request。
4. 解析结果response，其中performanceTiming是请求过程各阶段的耗时。

### 相关权限

网络连接权限 ohos.permission.INTERNET

获取网络状态权限 ohos.permission.GET_NETWORK_INFO

修改网络状态权限 ohos.permission.SET_NETWORK_INFO

### 依赖
不涉及

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。 

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## network-query
> 本示例使用 Network Kit 和 Telephony Kit 实现了四个常用的网络查询功能。开发者可参考这些实现，快速完成网络状态判断、MAC地址查询、WiFi列表查询、蜂窝网络相关数据的获取以及监听网络服务与质量变化等常见功能。

源码: https://gitcode.com/HarmonyOS_Samples/network-query

# 实现常见网络信息查询

### 介绍

本示例使用 Network Kit 和 Telephony Kit
实现了四个常用的网络查询功能。开发者可参考这些实现，快速完成网络状态判断、MAC地址查询、wifi列表查询、蜂窝网络相关数据的获取以及监听网络服务与质量变化等常见功能。

### 效果预览

| 连接到指定网络                                  | 网络状态感知                                   | WLAN定位                                   | 网络故障诊断                                   |
|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|
| ![image](screenshots/devices/Scene1.png) | ![image](screenshots/devices/Scene2.png) | ![image](screenshots/devices/Scene3.png) | ![image](screenshots/devices/Scene4.png) |

**使用说明**
1. 启动应用，点击首页按钮分别进入对应的场景页面。
2. 连接到指定网络场景：首先点击底部“获取系统扫描wifi”按钮获取wifi列表，然后点击列表中的项，在弹出窗中输入密码以连接wifi。由于wifi列表数据依赖于系统扫描，可能存在延时，开发者可以进入设置页面刷新wifi列表。
3. 网络状态感知场景：视频播放过程中，变化网络环境，如断开和连接网络，wifi和数据网络切换。
4. WLAN定位场景：点击底部按钮，页面显示wifi的mac地址。
5. 网络故障诊断场景：点击底部的按钮，显示网络类型、路由信息等等；若需通过网速和信号强度来检测网络问题，则需修改[NetworkDiagnostics.ets](entry/src/main/ets/view/NetworkDiagnostics.ets)文件中的文件下载地址TEST_DOWNLOAD_URL，10秒后将显示网络检测结果。

### 工程目录

```
├──entry/src/main/ets                           // 代码区
│  ├──common
│  │  ├──Logger.ets                             // 日志打印类   
│  │  ├──NetworkUtil.ets                        // 网络工具类 
│  │  ├──TimeUtil.ets                           // 时间格式转化工具类
│  │  └──ToastUtil.ets                          // Tost工具类
│  ├──component
│  │  ├──NetInfoItem.ets                        // 网络信息列表项  
│  │  └──WlanItem.et


---
## observer
> 本示例通过@ohos.telephony.observer等接口订阅网络状态、信号状态、蜂窝数据、sim状态等事件，并获取状态变化返回的结果。

源码: https://gitcode.com/HarmonyOS_Samples/observer

# 基于Observer实现事件订阅功能

### 介绍

本示例通过@ohos.telephony.observer等接口订阅网络状态、信号状态、蜂窝数据、sim状态等事件，并获取状态变化返回的结果。帮助开发者实现监听手机网络、信号、通话、sim卡等状态的场景。

### 效果预览

|主页|
|--------------------------------|
|![](screenshots/device/observer.png)|

使用说明

1.打开应用，开启所有订阅事件开关。

2.开关一次移动网络，触发网络状态变化。

3.插拔一次sim卡，触发sim卡状态变化和信号状态变化。

4.点击**查看详情**按钮，跳转详情页，显示监听到的数据结果。

### 工程目录
```
├──entry/src/main/ets/
│  ├──application
│  │  └──AbilityStage.ets
│  ├──mainability
│  │  └──MainAbility.ets
│  ├──model
│  │  ├──DetailData.ts                  // 详情数据
│  │  └──Logger.ts                      // 日志工具
│  └──pages
│     ├──Deatil.ets                     // 详情页面
│     └──Index.ets                      // 首页
└──entry/src/main/resources             // 应用静态资源目录
```
### 具体实现

* 该示例使用NetworkState方法获取网络注册状态，SignalInformation方法获取网络信号强度信息，RadioTechnology方法获取无线接入技术，DataConnectState方法描述蜂窝数据链路连接状态，DataFlowType方法描述蜂窝数据流类型，SimStateData方法获取SIM卡类型和状态等方法提供订阅管理功能。
* 源码链接：[DetailData.ts](entry/src/main/ets/modle/DetailData.ts)，[Index.ets](entry/src/main/ets/pages/Index.ets)
* 接口参考：@ohos.telephony.radio，@ohos.telephony.data，@ohos.telephony.observer

#### 相关概念

observer: 通过注册相关监听事件，来监听手机网络、信号、通话、sim卡等状态，并返回相应的结果。

### 相关权限

1.获取网络状态权限：ohos.permission.GET_NETWORK_INFO

### 依赖

不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## ohaudio-play-pcm
> 该示例用于展示如何使用OHAudio播放PCM音频

源码: https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm

# 基于OHAudio播放PCM音频

## 项目简介

本场景解决方案主要面向前台音频开发人员。指导开发者基于OHAudio开发音频播放功能，OHAudio用于播放PCM（Pulse Code Modulation）音频数据，播放其他格式的音频文件会产生杂音。功能包括后台播放、和播控中心的交互、适配不同类型的焦点打断策略、切换输出设备、倍数播放、音量调节等基础音频常见功能。

## 使用说明

1. 播放功能：运行工程，进入首页后，点击底部播放按钮，可播放音乐。
2. 切歌功能：播放按钮两侧有切歌按钮，点击切换上一首下一首。
3. 进度跳转功能：推动播放按钮上面的播放条，可以调整歌曲进度。
4. 循环模式：点击进度条上部，左侧第一个图标，可以切换不同播放模式，支持的模式有“顺序播放”、“单曲循环”、“随机播放”。
5. 歌单列表：点击进度条上部，左侧第二个图标，可以打开歌曲列表，点击歌曲名称，可以切换播放歌曲。
6. 静音播放：点击进度条上部，左侧第三个图标，可以打开静音播放功能。
7. 倍数设置：点击进度条上部，左侧第四个图标，可以调整歌曲播放速度。
8. 音量设置：点击进度条上部，左侧第五个图标，可以调整歌曲播放音量。
9. 收藏：点击页面“爱心”图标，将歌曲变成已收藏状态，可以同步至播控中心。

## 效果预览

| 主页面                                                | 歌词页                                                | 歌单列表                                                  | 倍数设置                                               |
|----------------------------------------------------|----------------------------------------------------|-------------------------------------------------------|----------------------------------------------------|
| <img src="screenshots/device/index.png" width=320> | <img src="screenshots/device/lyric.png" width=320> | <img src="screenshots/device/songList.png" width=320> | <img src="screenshots/device/speed.png" width=320> |

## 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  ├──constants                                        // 常量
│  │  │  ├──BreakpointConstants.ets                       // 断点常量
│  │  │  ├──ContentConstants.ets                          // 内容常量
│  │  │  ├──LyricConst.ets       


---
## ohaudio-record-pcm
> 该示例展示了使用OHAudio录制PCM音频

源码: https://gitcode.com/HarmonyOS_Samples/ohaudio-record-pcm

# OHAudioRecordPCM

#### 介绍
该示例展示了使用OHAudio录制PCM音频

#### 软件架构
软件架构说明


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)



---
## online-authenticationkit-sample-ifaaclientdemo-arkts
> 本示例主要展示IFAA的移动端的免密身份认证能力。

源码: https://gitcode.com/HarmonyOS_Samples/online-authenticationkit-sample-ifaaclientdemo-arkts

# 基于在线认证服务实现IFAA免密认证功能

## 介绍

本示例展示了IFAA免密身份认证接口的使用方法，IIFAA协议具体功能请参考[IIFAA本地免密技术规范](https://www.iifaa.org.cn/technical#paper)

通过从 @kit.OnlineAuthenticationKit 导入IFAA API接口，可实现基于IIFAA协议提供的端侧免密开通，认证和注销功能。


## 效果预览

| 应用入口 | 应用主页| 接口使用按钮 |
| --------------- | --------------- | -------------- |
| 点击图标打开应用 | 应用主页显示在设备屏幕   | 点击接口测试按钮调用接口  |
| <img src=".\image\startIcon.png" style="zoom:50%;" /> | <img src=".\image\homepage_cn.jpeg" style="zoom:25%;" /> | <img src=".\image\results_cn.jpeg" style="zoom:25%;" /> |

## 工程目录

```
├── entry/src/main/ets               // 代码区
│    ├── entryability
│    │    └── EntryAbility.ets       // 程序入口类
│    ├── model
│    │    └── IfaaModel.ets          // 开通、认证、关闭功能实现
│    └── pages
│         └── Index.ets              // 主页面入口
│    └── util
│         └── Util.ets               // 工具类
```



## 使用说明

1. 使用指纹/3D人脸进行免密身份认证，移动端设备需要录入对应的生物特征信息。
2. 在设备录入指纹/3D人脸后，点击开启按钮，页面弹出弹窗进行认证，提示开启成功。
3. 点击认证按钮，可使用生物特征（人脸/指纹）进行IFAA免密身份认证。
4. 点击关闭按钮，关闭IFAA生物特征（人脸/指纹）免密身份认证。


## 具体实现
以IFAA认证功能为例，业务使用时，需要先进行import导入如下IFAA API:

import { ifaa } from '@kit.OnlineAuthenticationKit'
* function preAuthSync(): Uint8Array;
* function auth(authToken: Uint8Array, authData: Uint8Array):Promise&lt;Uint8Array&gt;

业务使用时，首先需要在设备中存入指纹或3D人脸；首先通过调用preAuth()接口获取本次验证临时challenge参数，该数值需与生物认证所用challenge保持一致，IFAA服务会进行时效校验，获取参数后长时间未使用会导致验证失败；
通过调用User Authentication Kit成功获取指纹/人脸信息后，使用auth()接口进行身份认证，认证成功返回签名报文，失败会抛出异常。
具体用例请参考Index.ets


## 相关权限

1. 获取生物识别权限：ohos.permission.ACCESS_BIOMETR


---
## online-authenticationkit_sample_-fidoclientdemo_-arkts
> 本示例主要展示FIDO的移动端的免密身份认证能力。

源码: https://gitcode.com/HarmonyOS_Samples/online-authenticationkit_sample_-fidoclientdemo_-arkts

# 基于在线认证服务实现FIDO免密认证功能

## 介绍

本示例展示了FIDO免密身份认证接口的使用方法

通过从 @kit.OnlineAuthenticationKit 导入FIDO API接口，可实现基于FIDO协议提供的端侧免密开通，认证和注销功能。

## 效果预览

| 应用入口 | 应用主页| 接口使用按钮 |
| --------------- | --------------- | -------------- |
| 点击图标打开应用 | 应用主页显示在设备屏幕   | 点击接口测试按钮调用接口  |
| <img src="./image/startIcon.png" style="zoom:50%;" /> | <img src="./image/homepage_cn.png" style="zoom:25%;" /> | <img src="./image/results.png" style="zoom:25%;" /> |

## 工程目录
```
├── entry/src/main/ets
│    ├── bean
│    │    ├── FidoAuth.ets        // 认证数据结构
│    │    ├── FidoDereg.ets       // 注销数据结构
│    │    └── FidoReg.ets         // 注册数据结构
│    ├── ConnectService.ets       // 连接FIDO服务器，获取注册、认证、注销报文
│    ├── entryability
│    │    └── EntryAbility.ets    // 程序入口类
│    ├── pages
│    │    └── Index.ets           // 注册、认证、注销接口调用示例
│    └── util
│         └── Util.ets            // 工具类
```



## 使用说明

1. 运行前需修改并指定服务器地址(entry/src/main/ets/ConnectService.ets)；
2. 在主界面，每次使用FIDO功能之前，需要首先点击discover初始化认证器数据；
3. 在设备录入指纹/人脸后，点击开启按钮，页面弹出弹窗进行生物特征认证，提示开启成功；
4. 点击check policy可查询FIDO服务开通状态；
5. 在开启后点击认证按钮，页面弹出弹窗进行认证，提示认证成功；
6. 点击关闭按钮，提示关闭成功。


## 具体实现（接口参考@hms.security.fido）
以FIDO开启功能为例，业务使用时，需要先进行import导入如下fido API:
* function discover(context: common.Context): Promise&lt;DiscoveryData&gt;;
* function processUAFOperation(context: common.Context, uafRequest: UAFMessage, channelBindings?: ChannelBinding):Promise&lt;UAFMessage&gt;;
* function notifyUAFResult(context: common.Context, uafResponse: UAFMessage): Promise&lt;void&


---
## online-authenticationkit_sample_fido2clientdemo_arkts
> 本示例主要展示通行密钥的移动端的线上快速身份认证能力。

源码: https://gitcode.com/HarmonyOS_Samples/online-authenticationkit_sample_fido2clientdemo_arkts

# 基于在线认证服务实现通行密钥功能（ArkTS）

## 介绍

本示例展示了通行密钥服务提供的ArkTS示例代码的使用方法，可实现基于FIDO2协议的通行密钥注册、本地免密认证和跨设备扫码认证能力。
1. 通行密钥注册：支持使用用户身份认证特征（如人脸、指纹、PIN码）作为平台认证器，在本设备上创建应用或网页的通行密钥。
2. 本地免密认证：支持使用用户身份认证特征（如人脸、指纹、PIN码）作为平台认证器，使用通行密钥在本设备上进行应用或网页的免密认证。
3. 跨设备扫码认证：支持使用已注册通行密钥的移动设备作为漫游认证器，使用跨设备扫码的方式，在其他设备上进行应用或网页的免密认证。

## 效果预览

| 应用主页                                                    | 接口使用按钮                                              |
|---------------------------------------------------------|-----------------------------------------------------|
| 应用主页显示在设备屏幕                                             | 点击接口测试按钮调用接口                                        |
| <img src="./image/homepage_cn.png" style="zoom:25%;" /> | <img src="./image/results.png" style="zoom:25%;" /> |

## 工程目录
```
└── entry/src/main/ets
     ├── Pages                                                // 连接FIDO服务器，获取注册、认证、注销报文
     │    └── Index.ets                                       // 程序入口类
     └── server
          ├── Fido2NetUtil.ets                                // 连接服务器工具类
          ├── ServerAuthenticationExtensionsClientOutputs.ets // 用于构造认证响应扩展的数据结构类
          ├── ServerAuthenticatorAssertionResponse.ets        // 用于构造认证器断言响应的数据结构类
          ├── ServerAuthenticatorAttestationResponse.ets      // 用于构造认证器证明响应的数据结构类
          ├── ServerPublicKeyCredentialCreation.ets           // 用于构造向服务器传递响应报文的数据结构体
          ├── ServerPublicKeyCredentialCreationOptions.ets    // 用于构造创建新身份验证凭据选项的数据结构类
          ├── ServerPublicKeyC


---
## online-authenticationkit_sample_fido2clientdemo_cpp
> 本示例主要展示通行密钥的移动端的线上快速身份认证能力。

源码: https://gitcode.com/HarmonyOS_Samples/online-authenticationkit_sample_fido2clientdemo_cpp

# 基于在线认证服务实现通行密钥功能（C++）

## 介绍

本示例展示了通行密钥服务提供的C++ API的使用方法，可实现基于FIDO2协议的通行密钥注册、本地免密认证和跨设备扫码认证能力。
1. 通行密钥注册：支持使用用户身份认证特征（如人脸、指纹、PIN码）作为平台认证器，在本设备上创建应用或网页的通行密钥。
2. 本地免密认证：支持使用用户身份认证特征（如人脸、指纹、PIN码）作为平台认证器，使用通行密钥在本设备上进行应用或网页的免密认证。
3. 跨设备扫码认证：支持使用已注册通行密钥的移动设备作为漫游认证器，使用跨设备扫码的方式，在其他设备上进行应用或网页的免密认证。

## 效果预览

| 应用主页                                                    | 接口使用按钮 |
|---------------------------------------------------------| -------------- |
| 应用主页显示在设备屏幕                                             | 点击接口测试按钮调用接口  |
| <img src="./image/homepage_cn.png" style="zoom:25%;" /> | <img src="./image/results.png" style="zoom:25%;" /> |

## 工程目录
```
├── entry/src/main/cpp
│    ├── hcts                                                // native C++调用FIDO2NDK代码
│    │    ├── include                                        // 头文件
│    │    │    ├── fido2_serializer.h                        // fido2报文与结构体互转头文件                  
│    │    │    ├── fido2_test.h                              // 函数导出头文件
│    │    │    └── log.h                                     // 日志打印的头文件
│    │    └── src 
│    │    │    ├── connect_service.cpp                       // 调用FIDO2NDK的实现
│    │    │    └── fido2_serializer.cpp                      // fido2报文与结构体互转的实现
│    ├── third_party                                         // nlohmann三方库
│    │    └── include/nlohmann                               // nlohmann三方库
│    ├── types/libentry/                                     // 
│    │    ├── Index.d.ts      


---
## online-authenticationkit_samplecode_-soterclientdemo_-arkts
> 本示例主要展示SOTER的移动端的免密身份认证能力。

源码: https://gitcode.com/HarmonyOS_Samples/online-authenticationkit_samplecode_-soterclientdemo_-arkts

# 基于在线认证服务实现SOTER免密认证功能

## 介绍

本示例展示了SOTER免密身份认证接口的使用方法，通过从 @kit.OnlineAuthenticationKit 导入SOTER API接口，从@kit.UserAuthenticationKit导入userAuth。在设备处于联网状态下，可实现基于SOTER 协议提供的端侧生成密钥，开通，认证和关闭功能。


## 效果预览

| 应用入口 | 应用主页| 接口使用按钮 |
| --------------- | --------------- | -------------- |
| 点击图标打开应用 | 应用主页显示在设备屏幕   | 点击接口测试按钮调用接口  |
| <img src=".\image\startIcon.png" style="zoom:50%;" /> | <img src=".\image\homepage_cn.jpeg" style="zoom:25%;" /> | <img src=".\image\results_cn.jpeg" style="zoom:25%;" /> |

## 工程目录

```
├──entry/src/main/ets                      // 代码区
│   ├──entryability
│   │   └──EntryAbility.ets                // 程序入口类
│   ├──model
│   │   └──SoterModel.ets                  // 生成密钥、签名、删除密钥功能 
│   └──pages
│       └──Index.ets                       // 主页面入口
└──entry/src/main/resources                // 应用资源目录
```



## 使用说明

1. 使用指纹/3D人脸进行免密身份认证，移动端设备需要录入对应的生物特征信息。
2. 在设备录入指纹/3D人脸后，点击生成AppSecureKey按钮，提示生成应用密钥成功。
3. 点击生成AuthKey按钮，提示生成AuthKey成功。
4. 点击认证按钮，可使用生物特征（人脸/指纹）进行SOTER免密身份认证。
5. 点击关闭按钮，关闭SOTER生物特征（人脸/指纹）免密身份认证.


## 具体实现
以SOTER认证功能为例，业务使用时，需要先进行import导入如下SOTER API:

import { soter } from '@kit.OnlineAuthenticationKit'
* function getChallenge(keyAlias: string): Uint8Array;
* function auth(keyAlias: string, authToken: Uint8Array, info: string): soter.SignedResult;

业务使用时，首先需要在设备中存入指纹或3D人脸；首先通过调用getChallenge()接口获取本次验证临时challenge参数，该数值需与生物认证所用challenge保持一致，SOTER服务会进行校验；通过使用UserAuthenticationKit提供的生物特征认证能力，使用auth()接口对业务数据进行认证签名，认证成功返回签名报文，失败会抛出异常。

具体用例请参考Index.ets


#


---
## open-gtx-samplecode-clientdemo-cpp
> 本示例主要展示基于图形加速服务（Graphics Accelerate Kit）的OpenGTX API实现自适应调整游戏的帧率、设备的SOC/DDR频率的功能

源码: https://gitcode.com/HarmonyOS_Samples/open-gtx-samplecode-clientdemo-cpp

# 游戏自适应帧率调节（OpenGTX）

## 介绍

本示例展示了基于Graphics Accelerate Kit提供的OpenGTX API在图形绘制场景功能集成。

需要编译依赖OpenGTX的动态库libopengtx.so。

## 效果预览

|             **桌面**             |                 **主界面**                  |
|:------------------------------:|:----------------------------------------:|
| ![desk](screenshots/desk.png) | ![interface](screenshots/interface.png) |

使用说明：

1. 在手机的主屏幕，点击”OpenGTX“，启动应用，进入图形绘制场景。
2. 点击左上角，可手动开启或关闭OpenGTX功能。显示“OpenGTX开启”表示功能已开启，显示“OpenGTX关闭”表示功能已关闭。
3. 退出应用时，自动关闭OpenGTX。

## 工程目录

```
└── entry/src/main                          // 代码区
    ├── cpp
    │    ├── types/libentry
    │    │     └── index.d.ts               // native层接口注册文件
    │    ├── napi_init.cpp                  // native api层接口的具体实现函数
    │    ├── CMakeLists.txt                 // native层编译配置
    │    ├── include                        // 头文件
    │    ├── source                         // C++代码区
    │    │    ├── core.cpp                  // 核心入口，管理生命周期
    │    │    ├── renderer.cpp              // 渲染管理类的实现
    │    │    ├── scene_base.cpp            // OpenGTX基类的实现
    │    │    ├── scene_opengtx.cpp         // OpenGTX类的实现
    │    │    ├── opaque_layer_base.cpp     // 场景绘制基类的实现
    │    │    ├── opaque_layer.cpp          // 场景绘制派生类的实现
    │    │    ├── gui.cpp                   // UI绘制
    │    │    └── ...
    ├── ets
    │    ├── ability 
    │    │     └── EntryAbility.ts          // 程序入口类
    │    ├── pages 
    │    │     └── Index.ets                // 主界面
    └── resources
   


---
## page-redirection
> 本示例基于ArkUI框架和Web实现了H5页面和ArkTS原生界面之间的相互跳转。

源码: https://gitcode.com/HarmonyOS_Samples/page-redirection

# 基于Web组件实现ArkTS页面与H5页面间跳转的功能

### 介绍

本示例基于ArkUI框架和Web实现了H5页面和ArkTS界面之间的相互跳转。帮助开发者在Web页面开发中掌握H5页面加载，H5页面跳转，H5页面与ArkTS页面参数传递等功能的实现方案。

### 效果预览

| 商品列表                                    | 商品详情                                     | 订单确认                                      |
| --------------------------------------- | ---------------------------------------- | ----------------------------------------- |
| ![image](screenshots/devices/index.png) | ![image](screenshots/devices/detail.png) | ![image](screenshots/devices/confirm.png) |

使用说明

1. 启动应用，查看商品列表。

2. 点击某个商品，查看商品详情。

3. 在商品详情页点击底部返回按钮或者首页按钮返回到商品列表，此时点击底部前进按钮进入商品详情。

4. 在商品详情页点击立即购买按钮，查看订单确认页面。

### 工程目录

```
├──entry/src/main/ets                           // 代码区
│  ├──common
│  │  ├──constants   
│  │  │  └──CommonConstants.ets                 // 常量
│  │  └──utils   
│  │     └──Logger.ets                          // 日志打印  
│  ├──entryability
│  │  └──EntryAbility.ets
│  ├──model
│  │  └──ProductModel.ets                       // 产品模型
│  └──pages
│     ├──IndexPage.ets                          // 首页页面
│     └──OrderConfirmPage.ets                   // 订单确认页面
└──entry/src/main/resources                     // 资源文件夹
```

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## pako-compression
> 本示例展示了对字符串的压缩以及解压操作，实现了将写入字符串压缩成为压缩文件，以及将压缩文件解压并读取出字符串并返回的功能。

源码: https://gitcode.com/HarmonyOS_Samples/pako-compression

# 基于pako三方库的文件压缩与解压

### 介绍

本示例通过使用pako三方库能力，实现了对字符串的压缩与解压能力，即将字符串保存至文件中并压缩，以及解压获取到原字符串，给开发者提供一个简单的字符串压缩解压示例。

## 下载安装

```
  ohpm install pako
  ohpm install @types/pako --save-dev  // import pako 的时候语法报错。其原因是pako包内不含类型声明，需要 @types/pako 下载这个包的声明文件，从而解决语法的报错。
```

### 效果预览
![image](screenshots/device/StreamCompression.gif)

使用说明

1、在输入框内输入内容并点击压缩字符串并保存按钮，会拉取文件管理页面并压缩字符串、创建压缩文件。

2、点击解压文件并读取按钮，会拉取文件管理页面，选择压缩文件后，会解压并返回字符串显示在界面中。


### 工程目录
```
├──entry/src/main/ets/
│  ├──common
│  │  ├──constants
│  │  │  └──CommonConstants.ets             // 常量类
│  │  └──utils
│  │     ├──CommonUtils.ets                 // 常用工具类
│  │     ├──CompressionUtils.ets            // 压缩解压工具类
│  │     └──Logger.ets                      // 日志打印类
│  ├──entryability
│  │  └──EntryAbility.ets                   // 程序入口类
│  └──pages
│     └──Index.ets                          // 主页面
└──entry/src/main/resources                 // 应用静态资源目录
```
### 具体实现

* 本示例主要实现了压缩与解压的功能，实现主要参考三方js库[pako](https://github.com/nodeca/pako)，pako提供gzip和deflate等格式压缩解压码功能。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## pasteboard
源码: https://gitcode.com/HarmonyOS_Samples/pasteboard

# 实现剪贴板复制粘贴的功能

### 介绍

本示例使用PasteButton和@ohos.pasteboard实现剪贴板基本的复制粘贴功能，帮助开发者掌握系统控件PasteButton的使用，了解@ohos.pasteboard接口的相关用法。

### 效果预览

| 首页                                                | 复制分享链接                                             | 多数据混排页                                             | 进度条接入页                                                |
|---------------------------------------------------|----------------------------------------------------|----------------------------------------------------|-------------------------------------------------------|
| <img src='screenshots/device/home.png' width=320> | <img src='screenshots/device/pageB.png' width=320> | <img src='screenshots/device/paste.png' width=320> | <img src='screenshots/device/progress.png' width=320> |

### 工程目录

```
├──entry/src/main/ets                     // 代码区
│  ├──common
│  │  ├──CommonConstants.ets              // 常量类
│  │  └──Logger.ets                       // 日志类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets           
│  └──pages
│     ├──Home.ets                         // 首页
│     ├──PageA.ets                        // PageA
│     ├──PageB.ets                        // PageB
│     ├──PasteBoard.ets                   // 多数据混排粘贴页
│     ├──ProgressBar.ets                  // 进度条接入页
│     └──ShareDitect.ets                  // 粘贴分享直达页
└──entry/src/main/resources               // 应用静态资源目录
```

### 使用说明

1. 进入首页，点击多数据


---
## pattern-lock
> 本示例展示了图案密码锁组件的使用，实现了密码设置、验证和重置功能。

源码: https://gitcode.com/HarmonyOS_Samples/pattern-lock

# 实现图案密码锁功能

### 介绍

本示例展示了图案密码锁组件的使用，实现了密码设置、验证和重置功能。

图案密码锁组件：以宫格图案的方式输入密码，用于密码验证。手指触碰图案密码锁时开始进入输入状态，手指离开屏幕时结束输入状态并向应用返回输入的密码。  

使用到用户首选项接口@ohos.data.preferences 异步获取用户设定过的密码。


### 效果预览
| 设置密码页                                        | 输入密码页                                 | 主页                                   |
|----------------------------------------------|---------------------------------------|--------------------------------------|
| ![main](screenshots/device/set_password.png) | ![main](screenshots/device/input.png) | ![main](screenshots/device/home.png) |

使用说明：

1.首次进入时需要设置密码，需要两次输入密码相同后点击**设置密码**进行设置，如果第二次输入密码和第一次输入密码不同，会提示重新输入。

2.设置密码后，需要输入密码解锁，退出应用后重新进入应用，需要再次输入密码验证，密码验证成功进入主页。

3.设置密码后，在输入密码界面有**重置密码**按钮，点击后需要输入旧密码，旧密码验证成功后开始设置新的密码。  

### 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  └──CommonConstants.ets             // 常量    
│  ├──entryability
│  │  └──EntryAbility.ets   
│  ├──pages
│  │  ├──Home.ets                        // 输入密码成功后进入的首页页面
│  │  └──Index.ets                       // 密码锁页面，定义密码验证逻辑
│  ├──utils
│  │  ├──Logger.ets                      // 日志文件
│  │  └──PreferencesUtils.ets            // 定义用户存过的密码
│  └──view
│     └──TitleBar.ets                    // 标题栏组件
└──entry/src/main/resources              // 应用静态资源目录
```

### 具体实现
* 在pages/Home.ets中定义密码锁组件，通过定义两个变量isHasPass：是否已经设过密码;isReset：是否需要重置密码;
* 密码验证分为几种情况：[源码](entry/src/main/ets/pages/Home.ets) 参考。
  1. 首次进入页面， 通过aboutToAppear()初始化调用preferences.getPreferences()获取密码，此时defaultPassword=


---
## payment-kit-sample-code-clientdemo-arkts
> 华为支付服务客户端示例主要展示华为支付服务的单次支付能力入口。


源码: https://gitcode.com/HarmonyOS_Samples/payment-kit-sample-code-clientdemo-arkts

# 实现应用实物支付能力-客户端

## 介绍

本示例展示了使用鸿蒙支付服务提供的单次支付，签约代扣。

需要使用鸿蒙支付服务接口 **@kit.PaymentKit**。

## 效果预览

| **示例应用主页面**           | **支付页面**             |
|-----------------------|-------------------------|
| ![img_2.png](img_2.png) | ![img_3.png](img_3.png) |

## Sample工程的配置与使用

### 在DevEco中配置Sample工程的步骤如下

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-createproject-0000001100334664)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-createapp-0000001146718717)。
2. 打开Sample应用，使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)应用的包名替换app.json5文件中的bundleName属性值。
3. 使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)应用的配置更新module.json5文件相关配置，配置client_id及app_id属性值。
4. 详细可参见指南[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-preparations)。

## 工程目录
```
entry
  └─src                     
    ├─main                
    │  ├─ets              
    │  │  ├─entryability      // 程序入口类
    │  │  └─pages             // 入口界面
    │  └─resources        
    │      ├─base         
    │      │  ├─element       // 颜色、字体、字符串等资源
    │      │  ├─media         // 图片等资源  
    │      │  └─profile       // 页面配置
```  

## 具体实现
单次支付：
- 商户服务器按照商户模型调用Payment Kit提供的[直连商户预下单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-prepay)或[服务商/平台类商户预下单](https://developer.huawei.com/consumer/cn/doc/harmonyos-reference


---
## paymentkit-sample-code-serverdemo-java
> 华为支付服务服务端示例展示了单次支付下单和订单管理能力。


源码: https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java

# 实现应用实物支付能力-服务端

## 介绍
华为支付云侧接口 Java SDK Sample。

官方 Java 语言开发库`pay-java`由 `core` 和 `service` 组成：
- `core` 为基础库。包含自动签名和验签的 HTTP 客户端、回调处理、加解密库。
- `service` 为业务服务。基于业务场景提供不同的业务类，其下的方法为对应的http接口。

本示例展示通过`pay-java`请求支付`预下单`，`预签约`API接口并对`回调通知`和`敏感信息加解密`等其他内容进行说明。

需要使用到的接口：
1. 预下单:/api/v2/aggr/preorder/create/app  （参考[直连商户-预下单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-prepay)）
2. 预签约:/api/v2/contract/presign/app （参考[直连商户-预签约](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-presign)）
3. 更多接口详细查看：[鸿蒙支付服务API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-rest)

## 效果预览

| **运行成功日志输出**      |
|------------------------|
| ![run_log.png](run_log.png) |

## demo工程的配置与使用

### 配置demo工程的步骤如下

1. 配置好java环境：JDK 1.8及以上。
2. 配置好Maven集成环境。
3. 获取商户配置后将配置添加到配置文件petalpayconfig.properties。
4. 启动demo工程：src/main/java/com.huawei.petalpay.paymentservice.example/ExampleApplication.java
5. 详细可参见指南[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-server-connect)。

## 工程目录
```
pay-example
    └─src
        ├─main
        │  ├─java
        │  │  └─com
        │  │      └─huawei
        │  │          └─petalpay
        │  │              └─paymentservice
        │  │                  └─example
        │  │                      ├─common        // 通用类包
        │  │                      └─controller    // 程序接口类包
        │  └─resources           


---
## paymentkit-samplecode-uxcodeproject-arkts
> 本示例按照鸿蒙收银台UI设计实现支付收银台。协助外部开发者自建收银台界面能够和鸿蒙支付服务的收银台外观设计、用户体验上保持一致。

源码: https://gitcode.com/HarmonyOS_Samples/paymentkit-samplecode-uxcodeproject-arkts

# 实现支付收银台功能
## 介绍
本示例按照鸿蒙收银台UI设计实现支付收银台。协助外部开发者自建收银台界面能够和鸿蒙支付服务的收银台外观设计、用户体验上保持一致。

开发者可在应用项目中实现支付收银台。应用项目由配置文件(module.json5)、页面代码(ets文件)以及资源文件（图片、字符串等）组成，实现的收银台包含以下功能：展示商户信息、金额、支付方式列表（用户选择的支付方式会变成选中状态）和支付按钮。

## 效果预览
实现效果如下：

![](./screenshots/device/cashier_run_result.png)

## 工程目录
项目目录结构如下：
```
├───entry/src/main/ets                        // 根目录
│   ├───data                                 // 数据结构根目录
│   │   ├───CustPayType.ets                  // 支付类型枚举
│   │   ├───PaymentType.ets                  // 支付方式
│   │   └───TestData.ets                     // 测试数据
│   ├───entryability                         // 生命周期根目录
│   │   └───EntryAbility.ets                 // 生命周期入口
│   ├───pages                                // 页面根目录
│   │   └───Index.ets                        // 页面入口
│   ├───ui                                   // 收银台组件根目录
│   │   ├───Amount.ets                       // 金额组件
│   │   ├───CashierBindSheetContainer.ets    // 收银台容器
│   │   ├───CashierComponent.ets             // 收银台首页组件
│   │   ├───ConfirmButton.ets                // 按钮组件
│   │   ├───PaymentItemComp.ets              // 支付方式组件
│   │   └───PaymentOrderComp.ets             // 商户订单组件
│   └───util                                 // 工具类根目录
│       └───PaymentUtil.ets                  // 支付工具
└───entry/src/main/resources                 // 资源根目录
```

## 具体实现

### 页面结构
一个页面通常由自定义组件、自定义构建函数、样式和逻辑交互组成。

1.在ArkUI中，UI显示的内容均为组件，由框架直接提供的称为系统组件，由开发者定义的称为[自定义组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-gui


---
## pdfkit_-sample-code_-arkts
> 本示例向您介绍如何使用PDF Kit（PDF文件服务）进行基本PDF文件阅读及编辑能力。

源码: https://gitcode.com/HarmonyOS_Samples/pdfkit_-sample-code_-arkts

# 实现PDF文件的查看与编辑功能
## 介绍
本示例展示了如何使用PDFKit提供的能力进行PDF文件内容查看与编辑等相关操作，相关能力通过PDFKit服务接口@kit.PDFKit引入。
## 使用说明
将示例代码用DevEco打开，点击运行按钮，选择相应的PDF资源文件打开即可。<br />
![img](images/index_cn.png)
![img](images/PreviewPDF_cn.png)
![img](images/PdfView_cn.png)
## 工程目录
```
entry
  |——src
     |——main
     |   |——ets
     |   |   ├──entryability
     |   │   |  |── EntryAbility.ets // 本地启动ability
     |   |   ├──pages
     |   |   |  |── Index.ets // 文件选择界面
     |   |   |  |── PDFPreview.ets // PDF示例界面
     |   |   |  |── PDFView.ets // PdfView组件预览界面
```


## 具体实现
在@kit.PDFKit中定义了PDF服务的接口API，示例接口如下：


```
    /**
     * Load a file with a specified file path or uri.
     * @param { string } path - file path.
     * @param { string } password - File encryption password.
     * @param { (progress: number) => number } onProgress - Progress bar callback function.
     * @returns { ParseResult } ParseResult enum type.
     * @throws { BusinessError } 401 - invalid input parameter.
     * @syscap SystemCapability.OfficeService.PDFService.Core
     * @since 5.0.0(12)
     */
    loadDocument(path: string, password?: string, onProgress?: (progress: number) => number): ParseResult;

    /**
     * Release PDF documents.
     * @syscap SystemCapability.OfficeService.PDFService.Core
     * @since 5.0.0(12)
     */
    releaseDocument(): void;
    
    /**
     * Save document to specified file path.
     * @param { string } path - file path.
     * @param { (progress: number) => number } onProgress - Progres


---
## pen-kit_-sample-code_-arkts
> 本示例展示了利用Pen Kit(手写笔服务)能力实现应用集成手写功能。

源码: https://gitcode.com/HarmonyOS_Samples/pen-kit_-sample-code_-arkts

手写笔服务
===============================

## 目录

* [简介](#简介)
* [效果预览](#效果预览)
* [工程结构](#工程结构)
* [使用说明](#使用说明)
* [相关权限](#相关权限)
* [约束与限制](#约束与限制)


简介
------------
手写笔服务（Pen Kit）是华为提供的一套手写套件，提供笔刷效果、笔迹编辑、报点预测和一笔成形功能，为开发者提供丰富而便捷的手写能力，开发者可以轻松集成实现手写功能，享受优质的手写体验，创造更多的手写应用场景。
另外还单独提供了全局取色、一笔成形、报点预测的能力。
本示例展示了如何接入PenKit手写套件的能力。

效果预览
------------
![img_cn.png](img_cn.png)


工程结构
-------
    ├── entryability
    │   └── EntryAbility.ets        // 本地启动ability，可通过loadContent任意切换以下四个demo
    └── pages
        └── HandWritingDemo.ets          // 手写套件界面
        └── ImageFeaturePicker.ets       // 全局取色界面
        └── InstantShapeGenerator.ets    // 一笔成形界面
        └── PointPredictor.ets           // 报点预测界面
    └── utils 
        └── ContextConfig.ts      // 上下文配置

使用说明
-------

业务使用时，需要导入相应模块，使用`import{ HandwriteComponent, HandwriteController }from '@kit.Penkit' `引入。
初始化HandwriteController。 通过callback回调的方式获取HandwriteController数据加载动作已完成的时机，
调用HandwriteController组件，传入已初始化后的HandwriteController，
并传入初始化完成后的callback和缩放后onScale的回调响应。
```c
import { HandwriteComponent, HandwriteController } from '@kit.Penkit';

@Entry
@Component
struct HandWritingComponent {
  controller: HandwriteController = new HandwriteController();
  // 根据应用存储规则，获取到手写文件保存的路径，此处仅为实例参考
  initPath: string = this.getUIContext().getHostContext()?.filesDir + '/aa';

  aboutToAppear() {
    // 加载时设置保存动作完成后的回调。
    this.controller.onLoad(this.callback);
  }

  // 手写文件内容加载完毕渲染上屏后的回调,通知接入用户,可在此处进行自定义行为
  callback = () => {
    // 自定义行为,例如文件加载完毕


---
## perf-test
> 本示例展示测试框架中白盒性能测试框架的使用示例。

源码: https://gitcode.com/HarmonyOS_Samples/perf-test

# 测试框架
### 介绍
本示例展示测试框架中白盒性能测试框架的使用示例。

测试框架arkxtest的详细介绍请[参考](https://docs.openharmony.cn/pages/v5.1/zh-cn/application-dev/application-test/arkxtest-guidelines.md) 。

本实例需要引入PerfTest接口[@ohos.test.PerfTest](https://gitee.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-test-kit/js-apis-perftest.md) 。  

### 效果预览
不涉及

使用说明
- 将perftest目录下的项目工程整体导入到DevEco Studio开发工具中。
- 查看ohosTest目录下的测试代码实现。
- 在DevEco Studio中执行测试用例代码查看执行效果，执行方式请[参考](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/application-test/arkxtest-guidelines.md)  

### 工程目录

```
perfTest 
|-----entry 
          |-----src/main/pages
                |-----index.ets                         // 页面组件 
          |-----ohosTest                                // 自动化测试用例
                |-----ets/test
                      |-----PerfTest.test.ets        // 自动化测试脚本，其中it()就是一个测试用例
|-----AppScope
          |-----app.json5                               // 定义应用唯一的包名："bundleName": "com.samples.test.perftest",
```
 须知

* 前提：引入PerfTest依赖：import { PerfMetric, PerfTest, PerfTestStrategy, PerfMeasureResult } from '@ohos.test.PerfTest';  

### 具体实现

#### PerfTest测试框架示例内容
* 1）测试函数执行期间的应用性能。
* 2）在ohosTest的test/PerfTest.test.ets中it()定义一条测试用例，支持三个参数：用例名称，过滤参数和用例函数。用例操作的行为以异步的形式编写。
* 3）指定唯一的ability即entry：通过want()中指定bundleName和abilityName：EntryAbility。
* 4）启动指定ability(相当于手动运行hap)：通过abilityDelegatorRegistry.getAbilityDelegator.startAbility(want)。
* 5）获取当前应用最顶层的ability对象：通过abilityDelegatorRegistry.getAbilit


---
## picker
> 应用使用@ohos.file.picker、@ohos.file.fs等接口，实现了picker拉起文档编辑保存、拉起系统相册图片查看、拉起视频并播放的功能。

源码: https://gitcode.com/HarmonyOS_Samples/picker

# 实现选择和查看文件功能

### 介绍

应用使用@ohos.file.picker、@ohos.file.photoAccessHelper、@ohos.file.fs等接口，实现了拉起文档编辑保存、拉起系统相册图片查看、拉起视频并播放的功能。

### 效果预览

| 首页                                                        | 查看并编辑文档界面                          | 查看图片界面                                | 查看视频界面                              |
|-----------------------------------------------------------|------------------------------------|---------------------------------------|-------------------------------------|
| <img src='./screenshots/device/Index.png' width=320> | ![](./screenshots/device/Edit.png) | ![](./screenshots/device/Picture.png) | ![](./screenshots/device/Video.png) |

使用说明：

1. 在首页，应用显示查看最近打开文档功能的跳转按钮，点击后进入文件管理页面，可以通过最近页面，查看最近打开的文档。通过点击右上方的三个按钮，可以分别实现新建文档、选择图片或视频并打开预览、选择文档并打开的功能。
2. 在查看文档界面，点击右上方左一按钮，可以实现当前文档另存为的功能；点击右上方中间的按钮，开启文档的编辑功能，textArea变成可编辑状态，用户输入数据后点击右上方第三个按钮，可以将当前文档内容进行保存操作（系统文档没有保存权限）。
3. 在查看图片界面，拉起系统相册，用户至多可选择三张图片查看，点击图片可以切换所显示的图片名及大小信息。
4. 在查看视频界面，拉起系统相册，用户至多可选择三个视频查看，点击视频播放并且可以显示的视频名及大小信息。

### 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  ├──Common.ts
│  │  ├──Constants.ets                  // 常量
│  │  ├──Logger.ts                      // 日志工具
│  │  └──Utils.ts						
│  ├──entryability
│  │  └──EntryAbility.ets               // ability类
│  ├──media
│  │  └──MediaFileUri.ets               // 媒体文件相关函数
│  ├──pages
│  │  ├──EditFile.ets                   // 查看并编辑文档界面
│  │  ├──Index.ets                      // 首页
│  │  └──ViewMedia.ets                  // 查看图片和视频界面
│  └──


---
## preferences
> 本示例使用@ohos.data.preferences接口，展示了使用首选项持久化存储数据的功能。

源码: https://gitcode.com/HarmonyOS_Samples/preferences

# 实现首选项数据持久化功能

### 简介

本示例使用@kit.ArkData中的@ohos.data.preferences接口，展示了使用首选项持久化存储数据的功能。帮助开发者实现主题切换且主题数据缓存读取的场景。

### 效果预览 

|default主题|pomelo主题|simplicity主题|
|---|---|---|
|![](screenshots/devices/default.png)|![](screenshots/devices/pomelo.png)|![](screenshots/devices/simplicity.png)|

使用说明

1.点击顶部titleBar的右侧**切换**按钮，弹出主题菜单，选择任意主题则切换相应的主题界面；

2.退出应用再重新进入，显示上一次退出前的主题界面。

### 工程目录
```
├──entry/src/main/ets/
│  ├──application
│  │  └──AbilityStage.ets
│  ├──common
│  │  └──ThemeDesktop.ets             // 首页主体内容
│  ├──mainability
│  │  └──MainAbility.ets
│  ├──pages
│  │  └──Index.ets                    // 首页，所有的接口和数据都封装在这里
│  └──util
│     ├──DataSource.ets               // 数据懒加载
│     └──Logger.ets                   // 日志文件
└──entry/src/main/resources           // 应用静态资源目录
```

### 具体实现

* 切换主题：在首页预先设置好几套主体数据，使用preferences.getPreferences获取使用Preferences对象，调用Preferences.get()
读取缓存中的参数，得到当前应该展示哪一套主体。每次点击切换按钮都会调用Preferences.put()来重新修改参数，然后使用
Preferences.flush()保存并刷新文件内容。
源码参考:[Index.ets](entry/src/main/ets/pages/Index.ets) 。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。






---
## preview-kit-samplecode-clientdemo-arkts
> 本示例主要展示Preview Kit（文件预览服务）的预览文件功能。

源码: https://gitcode.com/HarmonyOS_Samples/preview-kit-samplecode-clientdemo-arkts

# 基于Preview Kit实现预览文件能力
## 介绍
本示例展示了使用文件预览服务提供的接入预览功能
需要使用文件预览服务接口@kit.PreviewKit
## 效果预览
使用说明
1.在手机的主屏幕，点击 “预览文件” 或者 “预览文件夹” 按钮，启动预览应用

![](screenshots/device/demoIndex.png)
![](screenshots/device/demo.png)
![](screenshots/device/demo_folder.png)

## 工程目录
├─entry/src/main/ets    
│ ├─entryability                
│ │ └─EntryAbility.ets // 本地启动ability     
│ ├─pages                
│ │ └─Index.ets // 基础预览界面

## 具体实现
在@kit.PreviewKit定义了文件预览的接口API：
使用了如下接口进行业务实现：


```
openPreview(context: Context, file: PreviewInfo, info?: DisplayInfo): Promise<void>;
canPreview(context: Context, uri: string): Promise<boolean>;
```

业务使用时，需要先进行import导入
import { filePreview } from '@kit.PreviewKit';
参考entry\src\main\ets\pages\Index.ets文件

## 相关权限
无

## 依赖
依赖于文件预览应用

## 约束与限制
1.设备类型：华为手机、平板和2in1。

2.HarmonyOS系统：HarmonyOS NEXT Developer Beta1及以上。

3.DevEco Studio版本：DevEco Studio NEXT Developer Beta1及以上。

4.HarmonyOS SDK版本：HarmonyOS NEXT Developer Beta1 SDK及以上。


---
## push-kit-sample-code-client-atomic-arkts
> 本示例基于HarmonyOS实现了在元服务中发起基于账号的订阅请求。

源码: https://gitcode.com/HarmonyOS_Samples/push-kit-sample-code-client-atomic-arkts

# 客户端推送服务（元服务）

## 简介
本示例基于HarmonyOS实现了元服务发起基于账号的订阅请求。


## 相关概念
- Push Kit：Push Kit（推送服务）是华为提供的消息推送平台，建立了从云端到终端的消息推送通道。所有HarmonyOS应用可通过集成Push Kit，实现向应用实时推送消息，使消息易见，构筑良好的用户关系，提升用户的感知度和活跃度。
- serviceNotification：本模块提供服务通知的基础能力，包括请求订阅通知授权。

## 效果预览

| 首页                                  | 订阅服务通知页面                             | 发起订阅                                   | 点击通知进入应用内页                         |
|---------------------------------|--------------------------------------|----------------------------------------|------------------------------------|
| ![](./screenshots/homePage.png) | ![](./screenshots/subscribePage.png) | ![](./screenshots/subscribeDialog.png) | ![](./screenshots/landingPage.png) |

## 工程目录

```
├─entry/src/main/ets               // 代码区  
│ ├─abilities
│ │ ├─ClickActionAbility.ets       // 通知栏点击事件能力类
│ │ └─EntryAbility.ets             // 主程序入口类
│ ├─pages                          // 存放页面文件目录                
│ │ ├─ClickActionInnerPage.ets     // 点击通知落地页面            
│ │ ├─Index.ets                    // 应用主页面
│ │ └─SubscribePage.ets            // 订阅服务通知页面
│ ├─utils                          // 存放工具类文件目录
│ │ └─Logger.ets                   // 日志类，管理系统日志
└─entry/src/main/resources         // 资源文件目录
```

## 开发准备
1. 将app.json5文件中的包名替换为您自己的元服务包名。
2. 开通推送服务，详情请参考[指导](https://developer.huawei.com/consumer/cn/doc/atomic-guides/push-as-prepare)。
3. 开通服务通知并选用订阅模板，详情请参考[指导](https://developer.huawei.com/consumer/cn/doc/atomic-guides/push-as-service-noti)。
4. 将SubscribePag


---
## push-kit-sample-code-clientdemo-arkts
> 本示例基于HarmonyOS实现了申请Push Token和接收Push场景化消息的功能。

源码: https://gitcode.com/HarmonyOS_Samples/push-kit-sample-code-clientdemo-arkts

# 消息通知-推送服务-客户端

## 简介
本示例基于HarmonyOS实现了申请Push Token和推送场景化消息功能。


## 相关概念
- Push Kit：Push Kit（推送服务）是华为提供的消息推送平台，建立了从云端到终端的消息推送通道。所有HarmonyOS应用可通过集成Push Kit，实现向应用实时推送消息，使消息易见，构筑良好的用户关系，提升用户的感知度和活跃度。
- Push Token：Push Token标识了每台设备上每个应用，开发者可以调用场景化消息接口，根据Token来推送消息。
- 组件：Demo中主要使用了Text、Button、Image等组件。
- pushService：本模块提供Push Kit的基础能力，包括获取和删除Push Token、绑定和解绑账号和接收场景化消息的功能。

## 效果预览
| 首页                                                           | 申请Token页面                                            | 成功申请Token                                           | 点击通知进入应用内页                                                |
|--------------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------------|
| <img src="./screenshots/clickLandingPage.png" width="300px"> | <img src="./screenshots/getToken.png" width="300px"> | <img src="./screenshots/success.png" width="300px"> | <img src="./screenshots/extendedToast.png" width="300px"> |

## 工程目录

```
├─entry/src/main/ets               // 代码区  
│ ├─abilities
│ │ ├─PushMessageAbility.ets       // 消息监听事件能力类
│ │ └─TestAbility.ets              // 通知栏点击事件能力类
│ ├─component                      // 组件
│ │ └─CallComponent.ets            // VOIP组件
│ ├─entryability                   // 应用入口
│ │ ├─EntryAbility.ets             // 主程序入口类
│ │ ├─VoIPUIAbility.ets          // 处理应用内通话消息
│ │ └─RemoteNotificationExtAb


---
## push-kit-service-sample-code-timeline-java
> 本示例基于Java语言实现了向元服务推送基于账号的服务动态消息。

源码: https://gitcode.com/HarmonyOS_Samples/push-kit-service-sample-code-timeline-java

# 服务动态 服务端 代码示例
- 本demo为面向Java的元服务服务动态消息推送示例代码。
## 支持的java版本
java 8+
## 快速开始
### 下载
下载此demo并在IDE中打开。
### 开发准备
1. 元服务服务动态消息权益申请
   - 服务动态消息是提供给开发者的B2C（Business-to-Customer）消息能力，通过服务动态消息，开发者可以基于订单向用户推送关键节点的动态消息，及时提醒用户订单进度。\
     开发者可以参考[基于账号的服务动态消息](https://developer.huawei.com/consumer/cn/doc/atomic-guides/push-as-timeline)开通动态消息服务。

2. 获取Service Account凭据文件，具体步骤如下：
   - 创建服务账号密钥文件\
     您需要在华为开发者联盟的[API Console](https://developer.huawei.com/consumer/cn/console/overview)上，在左侧”API服务“页签中点击”凭证“页面，创建并下载推送服务API的服务账号密钥文件，相关创建步骤请参见[API Console操作指南-服务账号密钥](https://developer.huawei.com/consumer/cn/doc/start/api-0000001062522591#section3554194116341)。\
     您申请后的服务账号密钥样例文件形式可参考（文件内容已经经过脱敏处理）：
     ~~~json
     {
       "project_id": "*****",
       "key_id": "*****",
       "private_key": "-----BEGIN PRIVATE KEY-----\n**********************************==\n-----END PRIVATE KEY-----\n",
       "sub_account": "*****",
       "auth_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/authorize",
       "token_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
       "auth_provider_cert_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/certs",
       "client_cert_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/x509?client_id="
     }
     ~~~
3. 推送服务动态消息的参数示例如下，更多详情请见[服务动态推送API接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-api-service-timeline-send)。
   - [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service


---
## push-kit_-sample-code_-server-demo_-java
> 本示例基于Java语言提供了推送Push场景化消息的功能。

源码: https://gitcode.com/HarmonyOS_Samples/push-kit_-sample-code_-server-demo_-java

# Push Kit 服务端 demo

本 demo 为面向 Java 的鸿蒙场景化消息推送示例代码。

## 支持发送的消息

- [通知消息](src/main/java/com/huawei/push/NotificationExamples.java)
  - 点击消息动作
    - 点击消息进入应用首页并传递数据
    - 点击消息进入应用内页并传递数据
  - 通知样式
    - 普通通知
    - 通知角标
    - 通知大图标
    - 多行文本样式
- [卡片刷新消息](src/main/java/com/huawei/push/FormUpdateExamples.java)
  - 推送卡片刷新消息
- [语音播报消息](src/main/java/com/huawei/push/ExtensionExamples.java)
  - 推送语音播报消息
- [消息撤回](src/main/java/com/huawei/push/RevokeExamples.java)
  - 撤回通知消息
- [实况窗消息](src/main/java/com/huawei/push/LiveViewExamples.java)
  - 推送实况窗消息
- [应用内通话消息](src/main/java/com/huawei/push/VOIPExamples.java)
  - 推送应用内通话消息

## 支持的 Java 版本

Java 8+

## 快速开始

### 下载

下载此 demo 并在 IDE 中打开。

### 开发准备

1. 参考[Push Kit 开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-kit-guide)，开通推送服务，并获取 Push Token。
2. 获取 Service Account 凭据文件，具体步骤如下：

- 登录华为开发者联盟，进入[API Console](https://developer.huawei.com/consumer/cn/console/overview)。
- 点击左侧导航栏中“API服务->API库”，确保在项目名下已启用推送服务，若无请点击“未启用”，进入详情页面申请启用：![image](src/main/resources/screenshots/1.png)
- 点击左侧导航栏中“API服务->凭证”，在项目下点击”服务帐号密钥“下的”创建凭证“：![image](src/main/resources/screenshots/2.png)
- 填写必填项，并点击“生成公私钥”、“创建并下载 JSON”，下载后的文件就是您的 Service Account 凭据文件：![image](src/main/resources/screenshots/3.png)
- 将下载好的文件重命名为“service_account.json”，并替换工程中的[Service Account 凭据文件](src/main/resources/service_account.json)

#### 推送通知消息
1. 推送通知消息前，请先完成[申请通知消息自分类权益](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-apply-right#section151736231558


---
## readerkit_samplecode_arkts
> 本示例基于Reader Kit提供的能力，实现了电子书的阅读功能。为开发者展示了借助Reader Kit，如何快速构建书籍阅读能力。详细展示了电子书解析、目录展示及跳转、设置字体、翻页方式、背景色、字体大小、行间距等功能。

源码: https://gitcode.com/HarmonyOS_Samples/readerkit_samplecode_arkts

# 使用Reader Kit进行电子书阅读（ArkTS）
## 介绍
基于Reader Kit（阅读服务）提供的能力，实现了电子书的阅读功能。为开发者展示了多种格式电子书的解析、排版、阅读交互能力，以及如何借助Reader Kit的能力和组件快速构建书籍阅读能力。

## 效果预览
| **首页（初始状态）**                            | **首页（导入书籍后状态）**                              | **阅读页**                                |
|-----------------------------------------|----------------------------------------------|-----------------------------------------|
| ![avatar](screenshots/device/main1_page.png) | ![avatar](screenshots/device/main2_page.png) | ![avatar](screenshots/device/reader_page.png) | 

| **目录页**                            | **设置页**                           |
|-----------------------------------------|----------------------------------------|
| ![avatar](screenshots/device/catalog_page.png) | ![avatar](screenshots/device/settings_page.png) |

### 本示例工程使用说明

1. 运行本示例，开发者需要先将txt、epub、mobi、azw、azw3格式的书籍文件下载到设备本地目录中。
2. 运行本示例，开发者需要先去[下载](https://github.com/adobe-fonts/source-han-serif/tree/release?tab=readme-ov-file)“思源宋体”文件，并放到“rawfile\fonts”目录。
3. 运行项目成功后，开发者先通过“导入书籍”按钮将书籍文件导入到应用沙箱目录，然后再点击“去阅读器”按钮跳转到阅读页阅读书籍。
4. 在阅读页，开发者可左右横滑进行翻页。也可点击屏幕中间弹出菜单栏，在菜单栏可点击“目录”按钮跳转到目录页查看书籍目录列表，也可点击“设置”按钮跳转到设置页更改阅读设置项。
5. 在目录列表页，将会按目录层级展示书籍的目录列表。开发者可以上下滑动进行查看书籍目录，也可点击目录列表项跳转到对应章节进行阅读。
6. 在设置页，开发者可更改字体、翻页方式、背景色或背景图片、字体大小以及行间距。

## 工程目录
````
├──entry/src/main/ets	            // 代码区
│  ├──common
│  │  ├──BookParserInfo.ets         // 导入书的信息
│  │  ├──FontFileInfo.ets           // 字体信息
│  │  └──LocalBookImporter.ets      // 本地书籍导入工具类
│  ├──entrya


---
## remote-communication-kit_-sample-code_-arkts
> 本示例主要展示了如何实现基础URL测试、超时测试、断点续传的功能。

源码: https://gitcode.com/HarmonyOS_Samples/remote-communication-kit_-sample-code_-arkts

# 基于RCP实现远场HTTP通信功能（ArkTS）

## 简介

Remote Communication Kit是华为推出的一款专业的网络通信SDK，它通过对HTTP/HTTPS协议的封装实现了高效的数据请求功能。该服务为开发者提供了标准化的接口，支持应用系统快速、稳定、安全地与服务器进行数据交互。

## 开发前准备

- 开发HarmonyOS应用前，需先安装并配置开发环境。
- 了解远场通信服务代码结构。

## 效果预览

![效果图](./screenshots/Main.png)
![基础URL测试](./screenshots/BaseAddress.png)
![超时测试](./screenshots/TimeOut.png)
![断点续传测试](./screenshots/TransferRange.png)
![拦截器测试](./screenshots/Interceptor.png)
![上传文件测试](./screenshots/UploadFile.png)
![使用证书测试](./screenshots/Certificate.png)

## 工程目录

```
└── entry/src/main/ets
    ├── entryability
    │   └── MainAbility.ets        // UI Ability
    ├── pages
    │   ├── BaseAddress.ets      // 基础URL测试页面
    │   ├── Certificate.ets      // 使用证书测试页面
    │   ├── Interceptor.ets      // 拦截器测试页面
    │   ├── MainPage.ets      // 主界面
    │   ├── TimeOut.ets      // 超时测试页面
    │   ├── TransferRange.ets      // 断点续传页面
    │   └── UploadFile.ets      // 上传文件测试页面
    └── utils
        └── FileSelectUtils.ets      // 选择文件的工具
```

## 具体实现

本示例主要展示的基础URL测试、超时测试、断点续传、拦截器、上传文件、使用证书功能，其相关接口均定义在 **@hms.collaboration.rcp.d.ts** 中。

- 基础URL(BaseAddress)：SessionConfiguration{baseAddress?: URLOrString;}。
- 超时测试(TimeOut)：TransferConfiguration{timeout?: Timeout;}。
- 断点续传(TransferRange)：TransferRange{from?: number; to?: number;}。
- 拦截器(Interceptor)：SessionConfiguration{interceptors?: Interceptor[];}。
- 上传文件(UploadFile)：uploadFromFile(url: URLOrString, uploadFrom: UploadFromFile): Promise<Response>。
- 使用证书(Certificate)：SecurityConfiguration {remoteValid


---
## remote-communication-kit_-sample-code_-c
源码: https://gitcode.com/HarmonyOS_Samples/remote-communication-kit_-sample-code_-c

# 基于RCP实现远场HTTP通信功能（C++）

## 简介

Remote Communication Kit是华为推出的一款专业的网络通信SDK，它通过对HTTP/HTTPS协议的封装实现了高效的数据请求功能。该服务为开发者提供了标准化的接口，支持应用系统快速、稳定、安全地与服务器进行数据交互。

## 开发前准备

- 开发HarmonyOS应用前，需先安装并配置开发环境。
- 了解远场通信服务代码结构。

## 效果预览

![效果图](./AppScope/resources/base/media/Main.png)
![基础URL测试](./AppScope/resources/base/media/BaseAddress.png)
![超时测试](./AppScope/resources/base/media/TimeOut.png)
![断点续传测试](./AppScope/resources/base/media/TransferRange.png)

## 工程目录

```
├── entry/src/main
    ├── cpp
    │   ├── CMakeLists.txt			// C文件编译脚本
    │   ├── napi_init.cpp			// C接口封装为ArkTs
    │   └── types 
    │       └── libentry
    │           ├── Index.d.ts		// 导出封装的ArkTs接口
    │           └── oh-package.json5	// ArkTs与动态库映射
    └── ets
        ├── entryability
        │   └── MainAbility.ets               //UI Ability
        └── pages
            ├── BaseAddress.ets		// 基础URL测试页面
            ├── MainPage.ets		// 主界面
            ├── TimeOut.ets			// 超时测试页面
            └── TransferRange.ets   	// 断点续传页面
```

## 具体实现

本示例主要演示了基础URL测试、超时测试和断点续传功能，相关接口均定义在 **rcp.h** 文件中，并在 **napi_init.cpp** 中进行调用。

- 基础URL(BaseAddress)：先配置基础URL，然后在Rcp_Request中将URL设置为相对地址。
- 超时测试(TimeOut)：通过Rcp_Timeout的connectMs和transferMs参数来设置连接超时和传输超时。
- 断点续传(TransferRange)：使用Rcp_TransferRange的from和to参数为请求设置数据传输范围。

在使用以上功能时，请确保先包含头文件 **#include "RemoteCommunicationKit/rcp.h"**，然后根据实际需求扩展使用相关接口。详细实现可以参考本用例中 **“entry/src/main/pages”** 下的三个接口实现。

## 相关权限

This example requires Internet access permissions. Please add the following per


---
## resizable-image
> 本示例基于Image组件的resizable属性，分别通过设置slice和lattice实现了聊天消息气泡和可拉伸占位图。

源码: https://gitcode.com/HarmonyOS_Samples/resizable-image

# 基于resizable实现图片拉伸效果

## 项目简介

本示例基于Image组件的[resizable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#resizable11)属性，分别通过设置slice和lattice实现了聊天消息气泡和可拉伸占位图。其中聊天消息气泡拉伸效果为四周圆角固定不变，中间内容区域可拉伸；可拉伸占位实现的效果是中间的内容不可拉伸，四周可以拉伸。

## 效果预览

| 聊天消息气泡                           | 可拉伸占位图                                  |   
|----------------------------------|-----------------------------------------|
| ![](screenshots/device/chat.png) | ![](screenshots/device/placeholder.png) |   

## 使用说明

1. 安装运行应用之后分别点击按钮“聊天消息气泡”和“可拉伸占位图”跳转到聊天页面和可拉伸占位图页面。
2. 在聊天页面，可以看到不同内容长度的气泡消息，气泡背景图片自适应不同的宽度和高度的聊天内容。
3. 在可拉伸占位图页面，点击图片右下角的操作按钮，图片会进行拉伸或收缩。

## 目录结构

```
├──entry/src/main/ets/
│  ├──common
│  │  └──Constants.ets                    // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets           // 数据备份恢复类
│  ├──pages
│  │  └──Index.ets                        // 应用首页
│  └──view
│     ├──ChatMessageView.ets              // 聊天消息页面
│     └──PlaceholderImgView.ets           // 可拉伸占位图页面
└──entry/src/main/resources               // 应用静态资源目录
```

## 具体实现

* 使用Image组件resizable属性的slice参数，实现聊天信息气泡效果。
* 使用Image组件resizable属性的lattice参数实现可拉伸占位图。

## 相关权限

不涉及。


## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 6.0.1 Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.1 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.1 Release SDK及以上。


---
## ringtone-kit_-sample-code_-demo
> 本示例基于铃声服务能力，提供了将音频设置为铃声的服务。

源码: https://gitcode.com/HarmonyOS_Samples/ringtone-kit_-sample-code_-demo

# 实现铃声设置功能

## 简介

Ringtone Kit（铃声服务）是一个用于设置铃声的工具库。通过使用Ringtone Kit，开发者可以在鸿蒙应用中提供铃声设置的功能，为用户提供简单一致、安全高品质的铃声设置体验。

|                         **应用首页**                         |
| :----------------------------------------------------------: |
| <img src="./screenshots/main.jpg"  width="250" align="middle" /> |

## 使用说明

使用前需要`先打开DEMO`，再使用 `hdc` 命令，将音频文件推入手机。

```bash
// 推送音乐命令
hdc file send 音乐文件.mp3 /storage/media/100/local/files/Docs/Download/com.example.uiextension
```

打开铃声设置Demo页面。

- 输入音乐文件名称，例如`6.mp3`，点击按钮`设为铃声`。
- 拉起设置铃声弹窗。
- 点击相应的设置按钮，设置不同的铃声类型。
- 点击我的铃声，跳转到系统设置铃声。

## 工程目录结构

```bash
├──entry/src/main
│  └──ets                           // 代码区
│     ├──entryability
│     │  └──EntryAbility.ets        // 程序入口类
│     └──pages                      // 页面文件
│        └──Index.ets               // 主界面
└──entry/src/main/resources         // 资源文件目录
```

## 约束与限制

1. 本实例仅支持标准系统上运行，支持设备：华为手机、华为平板。
2. HarmonyOS系统：HarmonyOS NEXT Developer Beta3及以上。
3. DevEco Studio版本：DevEco Studio NEXT Developer Beta3及以上。
4. HarmonyOS SDK版本：HarmonyOS NEXT Developer Beta3 SDK及以上。


---
## run-js-in-web
> 本示例基于H5游戏，通过arkui的button实现对游戏实现基本控制，展示webview的JS注入与执行能力，及native应用与H5的通信能力。

源码: https://gitcode.com/HarmonyOS_Samples/run-js-in-web

# 基于WebView实现Native与H5通信的能力

### 介绍

本示例基于H5游戏，通过ArkUI的Button实现对游戏实现基本控制，展示Webview的JS注入与执行能力，及Native应用与H5的通信能力，主要用在有H5页面交互的场景。帮助开发者掌握应用与H5页面内容交互处理。

### 效果预览

| 主页                               |
|----------------------------------|
| ![](screenshots/device/main.png) |

使用说明

1.设备连接热点，可访问互联网。

2.打开应用，通过界面中按钮进行游戏控制。

### 工程目录
```
├──entry/src/main/ets
│  ├──entryability
│  │  └──EntryAbility.ets                // 弹窗组件
│  ├──model
│  │  └──Logger.ets                      // 日志工具
│  └──pages
│     └──Index.ets                       // 首页
└──entry/src/main/resources              // 资源文件夹
```

### 具体实现

* 本示例分成一个模块
  * 通过button实现对游戏的基本控制，WebviewController方法控制Web组件各种行为，使用webview注入JS与执行能力。
  * 源码链接：[EntryAbility.ets](entry/src/main/ets/entryability/EntryAbility.ets)，[Index.ets](entry/src/main/ets/pages/Index.ets)
  * 接口参考：@ohos.window，@ohos.web.webview

### 相关权限

网络访问权限: ohos.permission.INTERNET

### 依赖

不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS NEXT 5.0.5 Release SDK及以上。




---
## sample-code_-aicaption-arkts
> 本示例基于场景化语音服务能力，提供了将音频文件识别为文字的服务。

源码: https://gitcode.com/HarmonyOS_Samples/sample-code_-aicaption-arkts

# 实现AI字幕

### 介绍
本示例展示了语音类AI能力中的AI字幕能力。

本示例模拟了在应用里，通过依次点击"切换字幕显示状态"->"读取pcm音频"按钮，拉起AI字幕控件并对音频进行实时语音转文字的场景。

需要使用HiAI引擎框架中的@kit.SpeechKit.d.ts接口。

### 效果预览
<img src="screenshots/AICaption.png" height="820">

### 工程目录
```
├─entry/src/main/ets                         // 代码区
│  ├─entryability
│  │  └─EntryAbility.ets                     // EntryAbility
│  └─pages
│     └─Index.ets                            // 主页界面
├─entry/src/main/resources                   // 应用资源目录
│  └─chineseAudio.pcm                        // pcm音频文件
└─screenshots                                // 截图
```

### 具体实现

本示例模拟了在应用里，通过依次点击"切换字幕显示状态"->"读取pcm音频"按钮，拉起AI字幕控件并对音频进行实时语音转文字的场景。
业务使用时，需要先进行import导入Speech kit: `import { AICaptionComponent, AICaptionOptions, AICaptionController, AudioData } from '@kit.SpeechKit';`

涉及接口：
* `writeAudio(audioData: AudioData): void` [链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-aicaptioncomponent#section272302165)
* `AudioData` [链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-aicaptioncomponent#section1869988122518)
* `AICaptionOptions` [链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-aicaptioncomponent#section15787428226)

涉及组件：
* `AICaptionComponent` [链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-aicaptioncomponent#section7266241469)
* `AICaptionController` [链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-aicaptioncomponent#s


---
## sample-plugin
> 本插件可在DevEco Studio中安装使用，提供Sample案例代码展示，一键拉取Sample案例源代码到本地直接引用。

源码: https://gitcode.com/HarmonyOS_Samples/sample-plugin

# Sample自动导入插件

## 介绍

本插件可在DevEco Studio中安装使用，提供Sample仓案例，可拉取Sample仓案例源代码到本地直接引用。

## 使用说明

### 安装插件

1. 通过[下载地址](plugin/sample_plugin-1.0.7-Alpha.zip)下载插件zip，无需解压。

2. 在DevEco Studio中，选择左上角File→Setting。

3. 找到Plugins，点击齿轮图标，选择Install Plugin from Disk。

4. 选择插件所在路径，进行安装。

5. 安装成功后点击OK按钮，即可通过鼠标右键使用插件。

   ![install](doc/image/install.gif)



### 自动获取sample仓案例源代码

1. 在光标处点击鼠标右键，选择Import HarmonyOS Sample。

2. 弹出对话框，选择源代码。

3. 选择需要下载的案例，点击OK，等待源代码下载完成。

4. 点击右上角Sync Now按钮，同步工程。

5. 同步结束后，编译安装即可查看效果。

   ![](doc/image/pull_code.gif)

##  约束限制条件

1. 需要在DevEco Studio中安装使用。
2. 需要连接互联网下载插件及源代码。

## 版本号

2025/6/18：v1.0.7-Alpha

2025/5/15：v1.0.6-Alpha

2025/4/30：v1.0.5-Alpha

2024/3/21：v1.0.1-Alpha

## Releate Note

v1.0.7-Alpha：

1.修复下载异常无法继续问题

2.优化体验问题

v1.0.6-Alpha：

1.修复图片下载失败问题

2.优化体验问题

v1.0.5-Alpha：

1.增加版本更新功能。

2.优化体验问题。

##  链接地址

[下载地址](plugin/sample_plugin-1.0.7-Alpha.zip)


---
## sample_in_harmonyos
> 「HarmonyOS代码工坊」汇聚优质代码案例，覆盖多场景开发需求，通过标准化、模块化的代码实践，帮助开发者快速掌握鸿蒙应用开发技巧，加速项目落地进程，开启鸿蒙开发新征程！

源码: https://gitcode.com/HarmonyOS_Samples/sample_in_harmonyos

# HarmonyOS代码工坊
## 一、「HarmonyOS代码工坊」APP尝鲜上线了！
为了帮助广大开发者更高效的完成鸿蒙应用开发，华为官方重磅打造了一款名为「HarmonyOS代码工坊」的开源APP。「HarmonyOS代码工坊」汇聚华为官方优质代码案例，覆盖多场景开发需求，通过标准化、模块化的代码实践，帮助开发者快速掌握鸿蒙应用开发技巧，加速项目落地进程，开启鸿蒙开发新征程！

【应用开发最佳实践】 

「HarmonyOS代码工坊」承载鸿蒙应用架构最佳实践，支持1+8设备运行，全方位体现鸿蒙应用的精致、流畅、智能、易用、安全、全场景互联等特点，并持续迭代鸿蒙新特性。

【示例代码一键获取】 

其中内置集成华为官方优质Samples示例代码，覆盖高频的鸿蒙应用开发场景，并支持源码的一键分享，给开发者提供所见即所得的样例代码，支撑开发者高效完成鸿蒙应用的开发。

【应用市场下载】 
- 下载地址：

  ![image](hmosword-build/image/download_small.png)

【代码开源地址】
- 「HarmonyOS代码工坊」源码地址：https://gitcode.com/HarmonyOS_Samples/sample_in_harmonyos
- 示例代码汇总地址：https://gitcode.com/HarmonyOS_Samples

【效果图】
![image](hmosword-build/image/9.png)
![image](hmosword-build/image/10.PNG)
@联系我们 

「HarmonyOS代码工坊」相关开发案例正在陆续更新中，您还期待我们为您提供什么样的开发案例，或还有什么宝贵意见，欢迎联系我们，非常期待您的反馈和建议，以促进我们不断改进！
- 官方邮箱：hmosworld@huawei.com
- 意见反馈：https://www.wjx.cn/vm/rXBoIC0.aspx

## 二、功能介绍（手机、折叠屏、平板、PC/2in1）
### 组件库首页
组件首页作为APP的入口页面，负责展示组件卡片，给用户提供不同组件的展示入口。主要包括页签区和内容区，内容区包括banner海报位与卡片入口。

| 手机                     | 平板                              | PC/2in1                               |
|------------------------|---------------------------------------|---------------------------------------|
| ![](hmosword-build/screenshots/1.png) | ![](hmosword-build/screenshots/2.png) | ![](hmosword-build/screenshots/3.png) |

### 组件库详情页
组件详情页承载全套符合HarmonyOS设计规范的ArkUI组件和开箱即用的特性能力。页面包括预览区、属性调整区、代码区和推荐列表四块，手动调整属性，可以看到预览区与代码区会发生相应的变化。

| 手机                                     | 平板                               | PC/2in1              


---
## scan-kit_-sample-code_-clientdemo_-arkts
> 本示例主要展示统一扫码服务（Scan Kit）的识码、扫码和生成码三大模块功能，包括图片识码能力、默认界面扫码能力、自定义界面扫码能力和码图生成能力。

源码: https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts

# 统一扫码服务

## 介绍

本示例展示了使用统一扫码提供的“扫码直达”服务、默认界面扫码能力、自定义界面扫码能力、图像识码能力、码图生成能力。

需要使用统一扫码服务接口 import { scanCore, scanBarcode, customScan, detectBarcode, generateBarcode } from '@kit.ScanKit';

## 效果预览

|               **控制中心**               |             **扫一扫扫码**             |          **直达服务页**           |
| :--------------------------------------: | :------------------------------------: | :-------------------------------: |
| ![](entry/screenshots/controlCenter.png) | ![](entry/screenshots/scanSuccess.png) | ![](entry/screenshots/access.png) |

|          **应用首页**           | **默认界面扫码**                       |               **扫码结果单码**               |              **扫码结果多码**              |           **默认界面扫码结果**           |
| :-----------------------------: | -------------------------------------- | :------------------------------------------: | :----------------------------------------: | :--------------------------------------: |
| ![](entry/screenshots/home.png) | ![](entry/screenshots/defaultScan.png) | ![](entry/screenshots/defaultSingleScan.png) | ![](entry/screenshots/defaultMutiScan.png) | ![](entry/screenshots/defaultResult.png) |

|          **应用首页**           | **自定义界面扫码**                       |              **扫码结果单码**               |             **扫码结果多码**              |          **自定义界面扫码结果**          |
| :-----------------------------: | ---------------------------------------- | :-----------------------------------------: | :-------------------------------------


---
## scankit-samplecode-clientdemo-arkts
> 本示例主要展示统一扫码服务（Scan Kit）的识码、扫码和生成码三大模块功能，包括图片识码能力、默认界面扫码能力、自定义界面扫码能力和码图生成能力。

源码: https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts

# 统一扫码服务

## 介绍

本示例展示了使用统一扫码提供的“扫码直达”服务、默认界面扫码能力、自定义界面扫码能力、图像识码能力、码图生成能力。

需要使用统一扫码服务接口 import { scanCore, scanBarcode, customScan, detectBarcode, generateBarcode } from '@kit.ScanKit';

## 效果预览

|               **控制中心**               |             **扫一扫扫码**             |          **直达服务页**           |
| :--------------------------------------: | :------------------------------------: | :-------------------------------: |
| ![](entry/screenshots/controlCenter.png) | ![](entry/screenshots/scanSuccess.png) | ![](entry/screenshots/access.png) |

|          **应用首页**           | **默认界面扫码**                       |               **扫码结果单码**               |              **扫码结果多码**              |           **默认界面扫码结果**           |
| :-----------------------------: | -------------------------------------- | :------------------------------------------: | :----------------------------------------: | :--------------------------------------: |
| ![](entry/screenshots/home.png) | ![](entry/screenshots/defaultScan.png) | ![](entry/screenshots/defaultSingleScan.png) | ![](entry/screenshots/defaultMutiScan.png) | ![](entry/screenshots/defaultResult.png) |

|          **应用首页**           | **自定义界面扫码**                       |              **扫码结果单码**               |             **扫码结果多码**              |          **自定义界面扫码结果**          |
| :-----------------------------: | ---------------------------------------- | :-----------------------------------------: | :-------------------------------------


---
## scenario-fusion-kit_-sample-code_-auto-fill
> 本示例展示了使用融合场景服务（Scenario Fusion Kit）的智能填充服务提供场景化的输入建议，实现复杂表单一键填充。

源码: https://gitcode.com/HarmonyOS_Samples/scenario-fusion-kit_-sample-code_-auto-fill

# 基于融合场景服务实现智能推荐数据填充

## 介绍

本示例展示了使用智能填充服务提供场景化的输入建议，实现复杂表单一键填充，帮助用户轻松地完成表单填写。

使用时需要引用程序框架服务接口@kit.AbilityKit

## 效果预览


| **主页**                                     | **剪贴板推荐**                                       | **华为账号推荐**                                    |
|--------------------------------------------|-------------------------------------------------|-----------------------------------------------|
| <img src=screenshots/main.jpg width="250"> | <img src=screenshots/clipboard.jpg width="250"> | <img src=screenshots/account.jpg width="250"> |

| **历史表单输入保存**                                       | **历史表单输入更新**                                         | **历史表单输入推荐**                                       |
|----------------------------------------------------|------------------------------------------------------|----------------------------------------------------|
| <img src=screenshots/history_save.jpg width="250"> | <img src=screenshots/history_update.jpg width="250"> | <img src=screenshots/history_form.jpg width="250"> |

## 前提条件

1. 设备智能填充开关必须处于打开状态。请前往“设置”->“隐私和安全”->“智能填充”打开智能填充功能。
2. 应用/元服务的输入组件的[ContentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-intelligentfilling-appendix)属性配置对应场景，即可触发智能填充功能。 
3. 智能填充服务开放能力接入需要申请与审批，详见[申请接入](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-introduction-to-smart-fill#section1167564853816)。 
4. 填充数据来源请参考[推荐数据源及推荐逻辑说明](https://developer.huawei.com/consumer/cn/do


---
## scenario-fusion-kit_-sample-code_-functional-api_-arkts
> 本示例展示了使用融合场景服务（Scenario Fusion Kit）提供的场景化API，主要用于获取系统信息和设备位置。

源码: https://gitcode.com/HarmonyOS_Samples/scenario-fusion-kit_-sample-code_-functional-api_-arkts

# 基于融合场景服务实现API获取系统属性

## 介绍

本示例展示了使用华为融合场景服务提供的场景化API，主要用于获取系统信息和设备位置。

需要使用华为融合场景服务接口 **@kit.ScenarioFusionKit**。

## 效果预览


| **示例应用主页面**                                    | **点击效果示意**                                     |
|------------------------------------------------|------------------------------------------------|
| <img src="SampleImg/API_img1.png" width="250"> | <img src="SampleImg/API_img2.png" width="250"> |

## 示例工程的配置与使用

### 在DevEco中配置本示例工程的步骤如下

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
2. 详细可参见开发指南-[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-preparations)。

## 工程目录
```
entry
  └─src                     
    ├─main                
    │  ├─ets              
    │  │  ├─entryability           // 程序入口类
    │  │    ├──EntryAbility.ets    // 本地启动ability
    │  │  └─pages             
    │  │     ├─Index.ets           // 入口界面
    │  │     ├─GetSystemInfoSync.ets      // 系统信息同步接口
    │  │     ├─GetSystemInfo.ets          // 系统信息异步接口
    │  │     └─GetSystemSetting.ets       // 系统设置接口
    │  └─resources        
    │      ├─base         
    │      │  ├─element       // 颜色、字体、字符串等资源
    │      │  ├─media         // 图片等资源  
    │      │  └─profile       // 页面配置
```  

## 具体实现
场景化API：
- 开发者调用 Scenario Fusion Kit 提供的 atomicService.getSystemSetting()接口，获取定位/蓝牙/wifi是否可用、设备方向等系统


---
## scenario-fusion-kit_-sample-code_-functional-btn_-arkts
> 本示例展示了使用融合场景服务（Scenario Fusion Kit）提供的场景化Button。

源码: https://gitcode.com/HarmonyOS_Samples/scenario-fusion-kit_-sample-code_-functional-btn_-arkts

# 基于融合场景服务构建场景化组件

## 介绍

本示例展示了使用华为融合场景服务提供的场景化组件，主要用于获取快速验证手机号Button、地图选点Button、选择头像Button、打开APP Button、选择收货地址Button、选择发票抬头Button、权限设置Button和省市区选择器Input的能力。

使用时需要引用场景化组件接口'@kit.ScenarioFusionKit'。

## 效果预览

| 主页                                        |
|--------------------------------------------|
| <img src=screenshots/main.jpg width="250"> |


使用说明

1. 在主界面可以点击快速验证手机号、地图选点、选择头像、打开APP、选择收货地址、选择发票抬头、权限设置和省市区选择器Input按钮验证对应场景的功能。
2. 可以通过设置styleOption中的属性值来配置按钮的基本样式。
3. 可以通过设置styleOption中styleConfig来设置更多按钮的样式。

## 示例工程的配置与使用

### 在DevEco中配置Codelab工程的步骤如下

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
2. 详细可参见开发指南-[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-preparations)和[场景化Button](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button)、[场景化Input](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-input)的前提条件。

## 工程目录
```
entry
  └─src                     
    ├─main                
    │  ├─ets              
    │  │  ├─entryability          // 程序入口类
    │  │    ├──EntryAbility.ets   // 本地启动ability
    │  │  └─pages
    │  │    ├──Index.ets                     // 基础预览界面
    │  └─resources        
    │      ├─base         
    │      │  ├─element       // 颜色、字体、字符串等资源
    │      │  ├─media         // 图片等资源  
    │      │  └─profile


---
## scenariofusionkit_samplecode_filepathconversion_arkts
> 本示例主要介绍如何使用Scenario Fusion Kit（融合场景服务）提供的文件路径转换的API，在HarmonyOS 4.x到HarmonyOS 5.0.x的升级场景和克隆场景，调用该接口可以将源文件路径转换为目标文件路径。

源码: https://gitcode.com/HarmonyOS_Samples/scenariofusionkit_samplecode_filepathconversion_arkts

# 基于融合场景服务实现文件路径转换

## 介绍

本示例展示了使用华为融合场景服务提供的文件路径转换接口，主要用于在HarmonyOS 4及以下到HarmonyOS 5及以上的升级场景和克隆场景通过调用文件路径转换接口（convertFileUris），获取升级后目标文件路径和文件类型。

需要使用华为融合场景服务接口 **@kit.ScenarioFusionKit**。

## 效果预览

文件路径转换接口：

| **示例应用主页面**                                    | **点击效果示意**                                                 |
|------------------------------------------------|------------------------------------------------------------|
| <img src="screenshots/device/API_img1_cn.jpg" width="250"> | <img src="screenshots/device/API_img2_cn.jpg" width="250"> |

## 示例工程的配置与使用

### 在DevEco中配置本示例工程的步骤如下

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-project-0000002242804048)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
2. 详细可参见开发指南-[文件路径转换API](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-api-path-conversion)。

## 工程目录
```
├──entry/src/main/ets	        // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets	// 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets // 备份能力类
│  └──pages
│     └──Index.ets		// 主界面	
└──entry/src/main/resources	// 资源文件目录  
``` 

## 具体实现
文件路径转换接口：
- 开发者调用 Scenario Fusion Kit 提供的 fileUriService.convertFileUris接口，系统文件路径转换，包括转换后文件类型。

参考
1. 文件路径转换接口：[entry\src\main\ets\pages\Index.ets](./Entry/src/main/ets/pages/Index.ets)

## 相关权限

无

## 依赖

无

## 约束与限制
1. 本示例仅支持标准系统上运行，支持设备:手机、平板。
2. HarmonyOS系统: HarmonyOS 5.0.2 Release 及以上。
3. DevEco Studio版本: Dev


---
## screentimeguard_kit_samplecode_appscontrol_arkts
> 本示例主要介绍Screen Time Guard Kit（屏幕时间守护服务）在应用里如何进行屏幕使用时间管控和应用使用限制，包括请求用户授权、安全拉起应用列表picker页、应用访问限制、解除应用访问限制、添加管控策略、查询管控策略、修改管控策略、启动管控策略、停止管控策略、删除管控策略。

源码: https://gitcode.com/HarmonyOS_Samples/screentimeguard_kit_samplecode_appscontrol_arkts

# 实现应用访问限制功能

## 介绍

Screen Time Guard Kit提供了屏幕使用时间管控、应用使用限制等开放能力。

本示例主要介绍在应用里如何进行屏幕使用时间管控和应用使用限制，包括请求用户授权、安全拉起应用列表picker页、应用访问限制、解除应用访问限制、添加管控策略、查询管控策略、修改管控策略、启动管控策略、停止管控策略、删除管控策略。

需要使用Screen Time Guard Kit接口 **@kit.ScreenTimeGuardKit**。

## 效果预览

| **请求用户授权页**                             | **拉起应用列表picker页** | **配置管控策略页** | **拦截页** |  **结束管控**  | **许可应用跳转页**  |
|-----------------------------------------|------------------------|-----------------|-------------|-------------|-------------|
| ![avatar](screenshots/device/img_1.png) |![avatar](screenshots/device/img_2.png)|![avatar](screenshots/device/img_3.png)|![avatar](screenshots/device/img_4.png)|![avatar](screenshots/device/img_5.png)|![avatar](screenshots/device/img_7.png)|


## 相关权限
 
本示例需要调用Screen Time Guard Kit接口的相关接口，已在 module.json5 文件中添加管理屏幕使用时间权限"ohos.permission.MANAGE_SCREEN_TIME_GUARD"。


## 本示例工程的配置与使用

### 在DevEco中配置本示例工程的步骤如下

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-createproject-0000001100334664)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-createharmonyapp-0000001945392297)。
2. 申请应用证书（.cer）、Profile（.p7b）文件，具体操作请参见[调试Harmony OS应用/元服务](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-app-0000001914423098)。
3. 在添加Profile时，需要申请权限"ohos.permission.MANAGE_SCREEN_TIME_GUARD"。
   请在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)“添加Profile”页“申请权限 ”标签后选中“受限ACL权限（HarmonyOS API9及以上）”，点击下方的“选择”，在弹出的“申请使用受限ACL权限”选择框里选择权


---
## scroll-component-nested-sliding
> 该示例通过nestedScroll属性，实现了上滑Scroll容器，滑至Tabs子组件处，Tabs吸顶，List子组件中内容可继续滑动的功能。

源码: https://gitcode.com/HarmonyOS_Samples/scroll-component-nested-sliding

# 实现Scroll组件嵌套滑动的效果

### 介绍

本示例通过Scroll组件的滑动能力和List组件的nestedScroll属性，实现当Scroll嵌套List滑动时，优先滑动最外层的Scroll，当Scroll滑动至末端时，List再继续滚动。帮助开发者掌握Scroll嵌套List滑动时的场景如何处理。

### 效果预览
|                               首页                               |
|:--------------------------------------------------------------:|
| <img src="./screenshots/device/ceiling.gif" width="320"/> |

使用说明：
1. 启动应用，向上滑动，Tabs组件会吸顶。
2. 再向上滑动，List组件的内容会继续向上滚动。
3. 点击tab导航栏栏可以左右切换不同的内容。

### 工程目录

```
├──entry/src/main/ets/
│  ├──common/constant
│  │  └──CommonConstants.ets            // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──page                  
│  │  └──Index.ets                      // 首页
│  └──viewmodel                  
│     └──InitData.ets                   // 数据
└──entry/src/main/resource              // 应用静态资源目录
```

### 具体实现

* 页面在List组件上添加nestedScroll属性，对它的两个参数scrollForward和scrollBackward分别设置PARENT_FIRST和SELF_FIRST ，从而实现往末尾端滚动时父组件先滚动，往起始端滚动时自身先滚动的效果，源码参考[index.ets](entry/src/main/ets/pages/Index.ets)。


### 相关权限
不涉及

### 依赖
不涉及

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## securities-keyboard
> 本示例是一款可一键输入“300”、“600”等证券代码的自定义键盘应用。

源码: https://gitcode.com/HarmonyOS_Samples/securities-keyboard

# 实现自定义证券代码键盘

### 介绍

本示例基于ArkUI框架实现一款能够一键输入诸如“300”、“600”等证券代码的自定义键盘应用。该应用不仅支持证券数字键盘与英文键盘之间的切换，在英文键盘模式下，提供了“英文大小写切换”功能。

### 效果预览

![image](screenshots/device/keyboard.gif)

使用说明

1. 点击搜索框，页面弹出证券数字键盘。

2. 证券数字键盘，输入“600”和“001”，搜索框内容显示“600001”。

3. 证券数字键盘，点击“清空”按钮，搜索框内容清空。

4. 证券数字键盘，点击“ABC”按钮，切换到英文键盘。

5. 英文键盘，输入“n”，“i”，“H”，“a”，“o”，搜索框内容显示“niHao”。

6. 英文键盘，点击左下的“英文大小写切换”按钮，键盘中英文由小写切换到大写。

7. 点击键盘“关闭”按钮，键盘关闭。

8. 点击搜索框右边的“x”按钮，搜索框内容清空。

### 工程目录

```
├──entry/src/main/ets	                 // 代码区
│  ├──common
│  │  ├──constants
│  │  │  └──CommonConstants.ets          // 公共常量类
│  │  └──utils
│  │     └──Logger.ets	                 // 日志文件
│  ├──entryability
│  │  └──EntryAbility.ets                // 程序入口类
│  ├──model
│  │  └──MenuData.ets                    // 键盘类
│  ├──pages
│  │  └──Index.ets                       // 主页面
│  ├──view
│  │  ├──DeleteKey.ets                   // 键盘删除子组件
│  │  ├──EnglishKeyboard.ets             // 英文键盘组件
│  │  ├──EnglishKeyItem.ets              // 英文键盘子组件
│  │  ├──NumberKeyboard.ets              // 数字键盘组件
│  │  ├──NumberKeyItem.ets               // 数字键盘子组件
│  │  └──ShiftKey.ets                    // 英文大小写切换子组件
│  └──viewmodel
│     └──KeyEventListen.ets              // 公共键盘接口
└──entry/src/main/resources              // 资应用资源目录
```

### 具体实现 

- 点击Search组件，会弹出自定义键盘customKeyboard。 当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。
- 以Flex弹性布局方式实现自定义键盘。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Releas


---
## service-collaboration-kit-sample-code-arkts
> 本示例中介绍了如何集成服务互通的能力。

源码: https://gitcode.com/HarmonyOS_Samples/service-collaboration-kit-sample-code-arkts

# 实现跨设备互通功能（ArkTS）

## 介绍

本示例展示了使用分布式协同框架提供的跨设备互通的能力。

本示例模拟了在备忘录的应用里，唤起另一个设备的拍照应用，并将拍照的结果传回给备忘录。

同时您也可以使用跨设备互通中的文档扫描和图库能力，实现跨端操作。

需要使用协同框架跨设备互通接口@kit.ServiceCollaborationKit。

## 代码结构说明

```
├──entry/src/main/ets                         // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets                     // 程序入口
│  └──pages
│     └──Index.ets                            // 主要页面
└──entry/src/main/resources                   // 应用资源目录
```

## 效果预览

|       **主窗口**       |      **应用首页**      |      **发现设备**      |      **拍照**      |
| :---------------------------------------: | :---------------------------------------: |:----------------------------------:|:----------------------------------:|
| ![](screenshots/devices/app_cn.jpg) | ![](screenshots/devices/main_cn.jpg) | ![](screenshots/devices/Pad_mean_item_cn.jpg) | ![](screenshots/devices/Pad_take_photo_cn.jpg) |
| **文档扫描** | **图库** | **图片回传** |  |
| ![](screenshots/devices/Pad_Scan_cn.jpg) | ![](screenshots/devices/Pad_ImagePicker_cn.jpg) | ![](screenshots/devices/getphoto_cn.jpg) |                                             |



使用说明：

1. 前置步骤：
   * 准备一台2in1(或平板)和一台手机，2in1(或平板)安装此示例，手机安装具有跨端拍照能力的相机应用。
   * 在设置里面，两台设备登录**相同**的华为账号。

1. 在2in1(或平板)的主屏幕，点击”备忘录Mock“，启动应用，在主界面可见“使用远端设备插入图片”按钮。
2. 点击“使用远端设备插入图片”按钮，弹出菜单，在菜单里会列出可用的具有拍照能力的远端设备：手机。
3. 点击相应设备的"拍照"按钮，就会唤起手机的相机应用。
4. 在手机进行拍照，然后选择确认，照片就会回传到2in1类设备上并显示在应用的界面上。

## 具体实现

本示例展示的控件在@hms.collaboration.service.d.ets定义了跨端拍照生态API：

* createCollaborationServiceMenuItems(bus


---
## share-kit_-sample-code_-clientdemo_-arkts
> 本示例展示了利用Share Kit分享能力，实现向目标应用分享数据和应用内的文件分享。

源码: https://gitcode.com/HarmonyOS_Samples/share-kit_-sample-code_-clientdemo_-arkts

# 实现华为分享功能
## 简介
系统分享服务为应用提供文本、图片、视频等内容跨应用分享能力，用于将内容发送到其他应用甚至其他应用的用户。应用把需要分享的内容和预览样式配置给系统分享服务，系统分享服务将根据分享的数据类型、数量等信息构建分享面板，为用户提供内容预览、推荐分享联系人、关联应用及操作界面，便于用户快速选择分享应用或操作，将内容分发到目标应用。

## 效果图
![](./screenshots/device/share_tab1.png)
![](./screenshots/device/share_tab2.png)
![](./screenshots/device/share_tab3.png)
![](./screenshots/device/share_tab4.png)
![](./screenshots/device/share_tab5.png)
![](./screenshots/device/share_demo1.jpg)
![](./screenshots/device/share_demo2.jpg)
![](./screenshots/device/share_demo3.jpg)

## 相关概念
- [Stage模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stage-model-development-overview)：Stage模型的设计，主要是为了解决[FA模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fa-model-development-overview)无法解决的开发场景问题，方便开发者更加方便地开发出分布式环境下的复杂应用。从API Version 9开始支持。
- [UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-overview)：UIAbility组件是一种包含UI的应用组件，主要用于和用户交互。UIAbility组件是系统调度的基本单元，为应用提供绘制界面的窗口。一个应用可以包含一个或多个UIAbility组件。
- [UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)：UIAbilityContext是需要保存状态的UIAbility所对应的context，继承自Context。提供UIAbility的相关配置信息以及操作UIAbility和ServiceExtensionAbility的方法。
- [UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)：UIExtensionContext是UIExtensionAbility的上下文环境，继承自ExtensionContext，提供UIExtensionAbility的相关配置信息以及操作UIAbility的方法，如启动UIAbili


---
## short-video
> 本示例基于Swiper组件实现了短视频的滑动上下切换。

源码: https://gitcode.com/HarmonyOS_Samples/short-video

# 基于Swiper组件实现短视频切换功能

### 简介

本示例基于Swiper组件实现了短视频的滑动上下切换，便于用户进行基础的视频切换功能开发。

### 效果预览
<img src="screenshots/ShortVideo.png" width="300px">

使用说明：

1.启动应用后显示短视频界面。

2.上下滑动切换短视频。

### 工程目录
```
├──entry/src/main/ets               
│  ├──common
│  │  └──CommonConstants.ets       // 常量类               
│  ├──entryability  
│  │  └──EntryAbility.ets          // 程序入口
│  ├──model
│  │  ├──BasicDataSource.ets       // 懒加载DataSource
│  │  └──DataModel.ets             // 数据类
│  ├──pages                                     
│  │  └──Index.ets                 // 首页
│  └──view
│     ├──Side.ets                  // 视频信息
│     └──VideoSwiper.ets           // 视频滑动组件
└──entry/src/main/resources        // 应用资源目录
```

### 相关权限

不涉及

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## simple-chat-list
> 实现简单聊天列表

源码: https://gitcode.com/HarmonyOS_Samples/simple-chat-list

# 实现简单聊天列表功能

## 介绍

本示例基于List组件实现简单聊天列表功能，包含联系人页面和聊天页面。主要涉及左滑删除、置顶、回到顶部、拖拽排序、新增聊天记录以及下拉加载等功能。

## 预览效果
<img src='./screenshots/device/effect.gif' width='320'>

## 工程目录

```
├──entry/src/main/ets       // 代码区
│ ├──common
│ |  └──CommonConstants.ets // 列表数据
│ ├──entryability
│ |  └──EntryAbility.ets    // 程序入口类
│ ├──entrybackupability
│ |  └──EntryBackupAbility.ets
│ └──pages
│    ├──ChatPage.ets        // 聊天页面
│    └──Index.ets           // 联系人页面
└──entry/src/main/resources // 应用资源目录
```

## 使用说明

1. 打开应用首页，左滑List列表，展示置顶和删除按钮，点击可分别实现列表项ListItem置顶和删除功能。
2. 往下滑动，出现回到顶部按钮，点击后可跳转至顶部。
3. 长按ListItem进行手势拖拽，可实现列表拖拽排序功能。
4. 点击ListItem进入聊天页面，默认显示底部消息，下拉可以加载更多聊天记录。
5. 点击输入框并输入消息，然后点击发送按钮，页面会实时展示最新的消息。

## 相关权限

不涉及。

## 约束与限制

* 本示例仅支持标准系统上运行，支持设备：华为手机。

* HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

* DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

* HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## socket-communication
> 本示例通过Socket监听“127.0.0.1”实现跨进程通信。

源码: https://gitcode.com/HarmonyOS_Samples/socket-communication

# 基于Socket实现跨进程通信

## 介绍

本示例通过Socket监听接口，实现跨进程通信。客户端应用连接服务端。输入消息数据，发送给对端；客户端、服务端接受到发送过来的信息，并展示在页面上。

## 效果预览

![](screenshots/device/SocketCommunication.gif)

## 使用说明

1. 打开服务端应用，点击“初始化”按钮，对服务端进行初始化。
2. 打开客户端应用，点击“连接服务端”按钮，连接服务端。
3. 返回服务端应用，输入框输入“123456”，点击“发送”图标按钮。
4. 返回客户端应用，客户端接收到服务端发送过来的信息，并展示在页面上。
5. 客户端页面，输入框输入“456789”，点击“发送”图标按钮。
6. 返回服务端应用，服务端接收到客户端发送过来的信息，并展示在页面上。

## 相关权限

- 允许应用使用Internet网络权限:ohos.permission.INTERNET。

## 依赖

不涉及

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## soundpool-play-short-audio
> 该示例展示了使用SoundPool播放短音频

源码: https://gitcode.com/HarmonyOS_Samples/soundpool-play-short-audio

# 基于SoundPool播放短音频

## 项目简介
本场景解决方案主要面向前台音频开发人员，指导开发者基于SoundPool开发短音频播放功能。

## 效果预览
| 主页面                              | 
|----------------------------------|
| <img src="screenshots/device/index.png" width="320"  />|

## 使用说明
1. 运行工程，进入首页后，点击底部播放按钮，可听见应用播放短音。
2. 点击底部循环播放按钮，可以听见循环播放短音三次。
3. 点击底部0.5倍速度播放，可以听见短音以0.5倍速度播放。
4. 点击底部2倍速度播放，可以听见短音以2倍速度播放。
5. 点击底部0.5倍音量播放，可以听见短音以0.5倍音量播放。


## 工程目录
```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets                                 // Ability的生命周期回调内容
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                           // EntryBackupAbility的生命周期回调内容
│  └──pages
│     └──Index.ets                                        // 首页
└──entry/src/main/resources                               // 应用静态资源目录
```

## 具体实现
使用系统接口SoundPool实现播放短音功能，短音文件来源于项目rawfile目录下的ogg文件。

## 相关权限
不涉及

## 约束与限制
1. 本示例仅支持标准系统上运行，支持设备：直板机。
2. HarmonyOS系统：HarmonyOS 6.0.0 Release Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。










---
## special-window-shape
源码: https://gitcode.com/HarmonyOS_Samples/special-window-shape

# 实现PC/2in1异形窗口功能

### 介绍

本示例通过使用setWindowMask()等接口，实现了在PC/2in1设备上创建圆形、三角形、图片形状等异形子窗口的功能，帮助开发者掌握非矩形窗口的场景开发。

### 效果预览
|                              | 
|-----------------------------------|
| 圆形子窗口                             | 
| ![](screenshots/device/c.png)     | 
| 三角形子窗口                            | 
| ![](screenshots/device/t.png)     | 
| 图片形状子窗口                           | 
| ![](screenshots/device/i.png)     | 


### 使用说明

进入应用后，点击创建圆形子窗口/创建三角形子窗口/创建图片形状子窗口，创建并显示对应形状子窗口，点击子窗口中关闭按钮，子窗口关闭。


### 工程目录

   ```
    ├───entry/src/main/ets                             
    │   ├───common
    │   │   └───Constants.ets                            // 公用常量
    │   ├───entryability
    │   │   └───EntryAbility.ets                         // Ability生命周期
    │   ├───pages
    │   │   ├───Index.ets                                // 主页面
    │   │   └───SubPage.ets                              // 子窗口页面
    │   └───utils
    │       ├───ImageUtils.ets                           // 图片工具类
    │       └───WindowUtils.ets                          // 窗口工具类
    └───entry/src/main/resources                         // 应用资源目录
   ```

### 具体实现

1. 在模块/src/main目录下，配置syscap.json文件，添加"SystemCapability.Window.SessionManager"。
2. 代码中使用createSubWindow()创建子窗口，设置窗口位置、大小及其他属性等，使用setUIContent()接口设置加载的page页面。
3. 根据要实现的异形窗口形状，计算二维数组掩码windowMask，使用setWindowMask(windowMask)，设置窗口形状。
4. 使用showWindow()接口显示异形子窗口。

### 相关权限

不涉及

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：PC/2in1。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3


---
## speech-kit-sample-TextReader_-arkts
> 基于场景化语音能力，提供AI模型可对文本内容进行朗读。

源码: https://gitcode.com/HarmonyOS_Samples/speech-kit-sample-TextReader_-arkts

# 实现朗读控件

### 介绍
本示例展示了语音类AI能力中的朗读控件能力。

本示例模拟了在应用里，通过点击朗读听筒，跳转朗读控件播放面板并对文章进行朗读的场景。

需要使用HiAI引擎框架中的@kit.SpeechKit.d.ts接口。

### 效果预览

|                               主页                               |
|:--------------------------------------------------------------:|
| <img src="./screenshots/TextReader.png" width="320"/> |

### 工程目录
```
├─entry/src/main/ets                         // 代码区
│  ├─entryability
│  │  └─EntryAbility.ets       
│  ├─model
│  │  ├─Article.ets                          // 文章数据结构
│  └─pages
│     └─Index.ets                            // 主页界面
├─entry/src/main/resources                   // 应用资源目录
└─screenshots                                // 截图
```

### 具体实现

本示例模拟了在应用里，通过点击朗读听筒，跳转朗读控件播放面板并对文章进行朗读的场景。
业务使用时，需要先进行import导入Speech kit: `import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';`

涉及接口：
* `init(context: common.BaseContext, readParams: ReaderParam): Promise<void>` [链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreader-api#section173751154134515)
* `start(readInfoList: ReadInfo[], articleId?: string): Promise<void>` [链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreader-api#section143611912403)
* `on(type: 'setArticle', callback: Callback<string>): void` [链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreader-api#section19795822172419)
* `on(type: 'clickArticle' | 'clickAuthor' | 'clickNotification', callback: Callback<string>


---
## stage-model
> 本示例基于AbilityKit展示了Satge模型Ability管理的相关能力。

源码: https://gitcode.com/HarmonyOS_Samples/stage-model

# 基于AbilityKit实现Stage模型Ability管理的相关能力

### 介绍

本示例基于AbilityKit实现Stage模型Ability管理的相关能力，实现跳转AbilityContent页面、AbilityAccessCtrl页面、Window页面等功能。

### 效果预览

| 主页                                        |
|-------------------------------------------|
| ![](./screenshots/device/stage_mode.png) |

使用说明：

1.点击**AbilityContext**按钮，跳转到AbilityContext页面，测试UIAbilityContext相关内容；

2.点击**AbilityAccessCtrl**按钮，跳转到AbilityAccessCtrl页面，测试abilityAccessCtrl相关内容；

3.点击**Window**按钮，跳转到Window页面,测试窗口相关内容；

### 工程目录

```
├──entry/src/main/ets/
│  ├─Application
│  │  └──MyAbilityStage.ts                   
│  ├─feature
│  │  ├──AbilityAccessCtrlController.ts      // 访问控制             
│  │  ├──AbilityContextController.ts         // Context控制                    
│  │  └──WindowController.ts                 // 窗口管理                  
│  ├─JumpAbility
│  │  └──JumpAbility.ts                      // 跳转
│  ├─MainAbility
│  │  └──MainAbility.ts                      
│  ├─pages
│  │  ├──component
│  │  │  ├──IndexTitleBar.ets                // 单个页面标题组件
│  │  │  └──PublicTitleBar.ets               // 通用的标题组件
│  │  ├──AbilityAccessCtrlPage.ets           // 程序访问控制
│  │  ├──AbilityContextPage.ets              // 提供允许访问特定于ability的资源的能力
│  │  ├──Index.ets
│  │  ├──TestPage.ets
│  │  └──WindowPage.ets                      // 窗口               
│  └──util
│     └──Logger.ts    
└──entry/src/main/resources                              
```

### 具体实现

Stage模型的设计基于如下三个出发点：

- **应用的能力与系统总体功能和功耗的平衡**

  在系统运行过程中，前台应用的资源占用会被优先保障，


---
## state-management
> 本示例通过使用页面级的状态变量和应用级的状态变量来实现应用的状态管理。

源码: https://gitcode.com/HarmonyOS_Samples/state-management

# 实现应用的状态管理功能

### 介绍

本示例通过ArkUI状态管理@State、@Prop、@Link、@Observed等装饰器，实现不同页面之间状态同步情景和应用的数据状态管理情景。帮助开发者掌握应用的数据状态同步处理。

### 效果预览

| 主页                               | 子组件同步父组件部分内容                                              | 爷孙组件之间状态同步                                    | 应用内全局数据与UI之间的状态同步                               |
|----------------------------------|-----------------------------------------------------------|-----------------------------------------------|-------------------------------------------------|
| ![](screenshots/device/Home.png) | ![](screenshots/device/ParentChildPartialContentSync.png) | ![](screenshots/device/DeepNestComponent.png) | ![](screenshots/device/ApplyGlobalDataSync.png) |

使用说明

1.点击首页中的基本类型进入对应页面，点击按钮可以更改圆形的颜色；点击查看源码可以展示基本类型功能效果的源码。

2.点击首页中的数组类型进入对应页面，点击新增元素可以添加数据；点击删除元素可以删除数据，当数据为空时，点击删除会弹出一个提示窗；点击更新数组中的某个元素，可以更改第一条数据的age属性，当数据为空时，同样会弹出一个提示窗；点击查看源码可以展示数组类型功能效果的源码。

3.点击首页中的类对象类型进入对应页面，点击更新对象可以更改对象属性和对象属性中的属性；点击更新对象属性，对象属性数据发生变化；点击更新属性中的属性，对象属性的属性数据发生变化；点击查看源码可以展示类对象类型功能效果的源码。

4.点击首页中的只更新所绑定的组件进入对应页面，点击修改标题和内容，标题和内容数据都发生变化，页面更新标题数据，内容数据不刷新；点击查看源码可以展示类对象类型功能效果的源码。

5.点击单、双向同步进入对应页面，点击设置为粉色按钮，父组件圆形颜色更新，两个子组件颜色同步更新；点击设置为蓝色按钮，子组件A圆形颜色更新，父组件和子组件B颜色不更新；点击设置为红色按钮，子组件B圆形颜色更新，父组件和子组件A圆形颜色同步更新，点击查看源码可以展示单、双向同步功能效果的源码。

6.点击子组件同步父组件的部分内容进入对应页面，点击父组件中的属性1修改数据，子组件中的属性1数据同步，点击子组件的属性1修改数据，父组件中的属性1数据同步，点击查看源码可以展示子组件同步父组件的部分内容功能效果的源码。

7.点击爷孙组件之间状态同步进入对应页面，点击爷组件下拉框组件选择颜色，下拉框文本和圆形颜色改变，孙组件下拉框文本和圆形颜色同步刷新；点击孙组件下拉框选择颜色，下拉框文本和圆形颜色改变，爷组件下拉框文本和圆形颜色同步刷新，点击查看源码可以展示爷孙组


---
## status-bar-extension-kit-samplecode
> 本示例展示了应用通过Status Bar Extension Kit接口接入状态栏的能力。

源码: https://gitcode.com/HarmonyOS_Samples/status-bar-extension-kit-samplecode

# 状态栏开放服务
## 介绍
本示例展示了应用如何接入状态栏，将图标添加到状态栏中显示
需要使用状态栏管理服务@kit.StatusBarExtensionKit

## 效果预览

### 添加图标

![addToStatusBar](pictures/addToStatusBar.jpeg)

### 移除图标

![removeFromStatusBar](pictures/removeFromStatusBar.jpeg)

## 使用说明

1.运行demo

2.点击demo运行界面中的“Add to status bar”按键，demo中自定义的图标被添加到状态栏中

3.点击demo运行界面中的“Remove from status bar”按键，状态栏中的图标被移除

## 工程目录

```
├─entry/src/main/ets    
│ ├─entryability    
│ │ └─EntryAbility.ets  // 本地启动ability     
│ ├─pages                
│ │ └─Index.ets  // demo展示界面                 
│ │ └─StatusBarPage.ets   // 状态栏左键弹窗显示页面                
│ ├─statusbarviewextensionability   
│ │ └─MyStatusBarViewAbility.ets  // 自定义StatusBarViewExtensionAbility  
├─entry/src/main/resources
│ ├─rawfile
│ │ └─testBlack.svg  // 浅色壁纸下展示的图标
│ │ └─testWhite.svg  // 深色壁纸下展示的图标
```

## 具体实现
在@kit.StatusBarExtensionKit定义了状态栏管理服务的接口API：
使用了如下接口进行业务实现：


```
addToStatusBar(context: common.Context, statusbarItem: StatusBarItem): void;
removeFromStatusBar(context: common.Context): void;
```

自定义StatusBarExtensionAbility时，需要导入对应模块：
import { StatusBarViewExtensionAbility } from '@kit.StatusBarExtensionKit';
参考 entry\src\main\ets\statusbarviewextensionability\MyStatusBarViewAbility.ets 文件

使用添加移除等功能时，需要导入statusBarManager模块：
import { statusBarManager } from '@kit.StatusBarExtensionKit';
参考 entry\src\main\ets\pages\Index.ets 文件

## 相关权限
无

## 依赖
无

## 约束与限制
1.设备类型：2in1。

2.HarmonyOS系统：HarmonyOS NEXT Developer Beta1及以上。

3.DevEco Studio版本：DevEco Studio NEXT Developer Beta1及以上


---
## store-kit-sample-code-clientdemo-arkts
> 本示例实现了应用详情展示、元服务加桌以及按需加载HAP包等功能。

源码: https://gitcode.com/HarmonyOS_Samples/store-kit-sample-code-clientdemo-arkts

# 应用市场服务（ArkTS）

## 介绍

基于Stage模型，实现了展示应用详情页下载安装目标应用、展示元服务详情页添加至桌面、查询广告验签标签版本、获取模块安装信息和添加按需加载模块、应用市场更新和应用归因服务、查询隐私链接、查询隐私签署结果以及停止隐私协议等功能。

## 效果预览
![](screenshots/device/sample.png)
![](screenshots/device/loadproduct.png)
![](screenshots/device/loadService.png)
![](screenshots/device/getVersion.png)
![](screenshots/device/getCode.png)
![](screenshots/device/installService_cn.png)
![](screenshots/device/update_cn.png)
![](screenshots/device/registersource.png)
![](screenshots/device/registertrriger.png)
![](screenshots/device/validatesource.png)
![](screenshots/device/setpostback.png)
![](screenshots/device/flushpostbacks.png)
![](screenshots/device/getAppPrivacyMgmtInfo.png)
![](screenshots/device/getAppPrivacyResult.png)
![](screenshots/device/disableService.png)

## 工程目录

```
├─Attribution/src/main/ets
│                       │  
│                       ├─attributionability/AttributionAbility.ets  // 本地启动应用归因ability 
│                       ├─common/utils/SignUtil.ets     // 生成签名方法    
│                       └─pages
│                           └─Attribution.ets  // 应用归因服务及应用归因接入调试功能接口页面
├─entry/src/main/ets
                   ├─common/bean/EntryItemInfo.ets   // 页面入口工具类
                   ├─entryability/EntryAbility.ets   // 本地启动ability   
                   │              
                   └─pages
                       ├─ CheckUpdatePage.ets           // 应用检查更新
                       ├─ DisableService.ets            // 停止隐私协议
                       ├─ GetAdsVerificatio


---
## styledtext
> 本示例通过自定义Span类型，在Text组件中使用ForEach遍历，根据不同的Span类型生成不同样式和功能的Span组件，实现部分文本高亮和超链接。此外还可以通过属性字符串灵活设置文本样式实现同样效果。

源码: https://gitcode.com/HarmonyOS_Samples/styledtext

# 实现富文本信息的显示

### 介绍

本示例针对高亮显示的超链接文本、自定义表情、图标与文本的组合元素、自定义的图文元素四个场景的富文本信息的效果实现。

### 效果预览

<img src="./screenshots/device/result.gif" style="width:320px">

**使用说明**

1. 点击按钮跳转到不同的页面。
2. 点击话题、@用户、视频可以跳转到对应的详情页。

### 工程目录

   ```  
   ├──entry/src/main/ets
   │  ├──common 
   │  │  └──HandleData.ets           // 公共处理方法    
   │  ├──components 
   │  │  └──MyDrawCustomSpan.ets     // 自定义组件    
   │  ├──mock 
   │  │  └──MockData.ets             // mock测试模拟数据          
   │  ├──model                                
   │  │  └──MyCustomSpan.ets         // 数据类型定义
   │  └──pages                       // 视图层
   │     ├──CustomizeEmoji.ets       // 自定义表情页面 
   │     ├──Home.ets                 // 主页面
   │     ├──ImageText.ets            // 自定义的图文元素页面
   │     ├──TitleDetail.ets          // 跳转页面-#话题点击跳转页面
   │     ├──TitleLink.ets            // 高亮显示的超链接文本页面
   │     ├──UserDetails.ets          // 跳转页面-@用户点击跳转页面            
   │     └──VideoLink.ets            // 图标与文本的组合元素页面
   └──entry/src/main/resources       // 应用资源目录                                                     
   ```

### 具体实现

TextAndSpanComponent 组件通过自定义Span对象区分不同类型的文本，在Text组件中遍历自定义Span对象数组并检查字符长度，根据自定义Span对象的类型生成不同样式和功能的Span组件。

1. 遍历 spans 中的 MyCustomSpan 对象，根据不同的 Span 类型生成不同样式功能和事件的属性。
2. 通过设置点击回调linkClickCallback，可以根据点击的span类型，执行对应操作，例如跳转详情页或视频页。

### 相关权限
不涉及

### 依赖
不涉及

### 约束与限制
1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.1.0 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.1.0 Release及以上。
4. HarmonyOS S


---
## sub-window-floating-window
> 本示例通过子窗口实现悬浮窗以及画中画功能实现视频小窗，介绍子窗口相关操作以及画中画功能。

源码: https://gitcode.com/HarmonyOS_Samples/sub-window-floating-window

# 基于子窗口实现悬浮窗

### 介绍
本示例通过子窗口和画中画接口实现悬浮窗和视频小窗功能，便于用户进行子窗口以及画中画相关操作。

### 效果预览

|                   主页                   |
|:--------------------------------------:|
| ![home](screenshots/devices/phone.gif) |

使用说明

1. 运行点击子窗口-悬浮窗按钮跳转到子窗口功能展示页面。
2. 点击四个按钮查看子窗口四种不同的操作。
3. 点击画中画-视频小窗跳转到画中画功能展示页面。
4. 点击启动画中画生成视频小窗。

### 工程目录

```
├──entry/src/main/ets/
│  ├──constants                         
│  │  └──CommonConstants.ets                 // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets                    // 入口类
│  ├──pages
│  │  ├──Index.ets                           // 主页
│  │  ├──MiniWindowPage.ets                  // 子窗口显示隐藏页面
│  │  ├──NavigationRedirectPage.ets          // 子窗口通过Nacigation跳转到画中画页面
│  │  ├──ResizeWindowPage.ets                // 调整子窗口大小页面
│  │  ├──RouterRedirect.ets                  // 控制创建子窗口通过Router返回首页页面
│  │  └──RouterRedirectPage.ets              // 子窗口通过Router返回首页
│  ├──utils
│  │  └──Logger.ets                          // 日志类
│  ├──view
│  │  ├──MiniWindowComponent.ets             // 控制创建子窗口显示隐藏自定义组件
│  │  ├──NavigationRedirectComponent.ets     // 控制创建子窗口通过Nacigation跳转到画中画自定义组件
│  │  ├──PipWindowComponent.ets              // 画中画功能实现自定义组件
│  │  ├──ResizeWindowComponent.ets           // 控制创建调整子窗口大小自定义组件
│  │  └──SubWindowComponentRouter.ets        // 悬浮窗功能展示路由自定义组件
│  └──viewmodel
│     ├──AVPlayerDemo.ets                    // 视频播放控制类
│     └──WindowPosition.ets                  // 子窗口位置类
└──entry/src/main/resources                  // 应用静态资源目录
```

###


---
## system-router-map
> 本项目提供系统路由的验证，运用系统路由表的方式，跳转到模块(HSP/HAR)的页面，可以不用配置不同跳转模块间的依赖。

源码: https://gitcode.com/HarmonyOS_Samples/system-router-map

# 基于系统路由表实现页面跳转

## 介绍

本项目提供系统路由的验证，运用系统路由表的方式，跳转到模块(HSP/HAR)的页面，可以不用配置不同跳转模块间的依赖。当发生页面跳转时，未跳转页面不会加载，已经加载过的页面不会再次加载。 解决了不同模块依赖耦合的问题，以及首页加载时间长的问题。

## 效果预览

![image](screenshots/device/navigation_router.gif)

## 使用说明

1. 主页会提供一个NavIndex的导航页，点击按钮会跳转到不同的来自HAR和HSP包的页面。

2. 每个HAR和HSP包的页面也存在跳转到别的页面的按钮。

## 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  └──utils
│  │     └──Logger.ets                          // 日志打印封装
│  ├──entryability
│  │  └──EntryAbility.ets                       // 程序入口  
│  └──pages
│     ├──EntryPageOne.ets                       // 页面1
│     ├──EntryPageTwo.ets                       // 页面2
│     └──Index.ets                              // 界面实现
├──entry/src/main/resources                     // 应用资源目录
├──harA
├──harB
├──hspA
└──hspB
```

## 具体实现

1.创建hapA harA hspA hspB。

2.在跳转目标模块的配置文件module.json5添加路由表配置。

3.添加完路由配置文件地址后，需要在工程resources/base/profile中创建route_map.json文件。

4.在跳转目标页面中，需要配置入口Builder函数，函数名称需要和router_map.json配置文件中的buildFunction保持一致。

5.应用通过调用pushDestinationByName等方式，可以获取跳转目标页面的错误信息。

## 相关权限

不涉及

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。

### 注意

运行时需设置引用所有HSP模块。设置运行后，点击Run > entry来启动应用/服务的编译构建。



---
## text-display-font
源码: https://gitcode.com/HarmonyOS_Samples/text-display-font

# 实现字体设置功能

#### 简介

本示例基于ArkUI提供的字体控制能力，实现了自定义字体显示文本、自定义字体恢复为系统字体、字体大小跟随系统设置、字体大小不跟随系统设置等功能。

#### 效果预览

| 是否跟随系统设置                                                    | 自定义字体大小和字重                                                | 自定义字体                                              |
|-------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------|
| <img src='screenshots/device/follow_system.webp' width=320> | <img src='screenshots/device/size_weight.webp' width=320> | <img src='screenshots/device/font.webp' width=320> |

#### 工程目录

```
├──entry/src/main/ets                                   // 代码区
│  ├──common
│  │  ├──CommonData.ets                                 // 列表数据
│  │  └──CommonUtils.ets                                // 工具类/工具函数
│  ├──entryability
│  │  └──EntryAbility.ets                               // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets
│  ├──pages                              
│  │  └──Index.ets                                      // 入口页
│  └──view  
│     ├──HomePage.ets                                   // 首页
│     └──SettingsPage.ets                               // 设置页
└──entry/src/main/resources                             // 应用资源目录
```

#### 相关权限

无

#### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 R


---
## text-effects
> 本示例基于Text组件及通用属性实现多种文字特效。

源码: https://gitcode.com/HarmonyOS_Samples/text-effects

# 基于Text组件及通用属性实现文字特效

### 介绍

本示例基于Text组件及通用属性实现多种文字特效。帮助开发者在ArkTS页面开发中实现文字渐变、歌词滚动、文字倒影、跑马灯渐变等多种文字效果。

### 效果预览
|                               文字特效                               |
|:--------------------------------------------------------------:|
| <img src="./screenshots/device/text_effects.gif" width="320"/> |

**使用说明**

1. 启动应用，查看多种文字特效，包含文字渐变、歌词滚动、文字倒影、跑马灯渐变等效果。

### 工程目录

```
├──entry/src/main/ets/
│  ├──constants
│  │  └──Constants.ets                  // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──page                  
│  │  └──Index.ets                      // 首页
│  └──view
│     ├──TextGradientView.ets           // 文字渐变     
│     ├──TextMarqueeView.ets            // 跑马灯渐变
│     ├──TextReflectionView.ets         // 文字倒影       
│     └──TextScrollingView.ets          // 歌词滚动
└──entry/src/main/resource              // 应用静态资源目录
```

### 具体实现

1. 文字渐变效果通过blendMode混合属性及linearGradient线性渐变属性实现。
2. 歌词滚动效果使用blendMode混合属性及linearGradient线性渐变属性及显式动画实现。
3. 文字倒影效果使用rotate旋转属性及linearGradient线性渐变属性实现。
4. 跑马灯渐变效果使用Text组件textOverflow超长文本显示属性及linearGradient线性渐变属性实现。

### 相关权限

不涉及

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



---
## timebar
> 可缩放时间轴UI效果

源码: https://gitcode.com/HarmonyOS_Samples/timebar

# 实现可缩放时间轴功能

## 项目介绍

本项目是一个基于Canvas和Video组件实现的时间轴联动视频播放Sample，核心功能是通过手势（平移、捏合缩放）控制视频时间轴，从而实现视频播放进度的快进、快退联动效果。

## 效果图预览
| 时间轴缩放                                   | 时间轴扩张                                   | 样式调整                                         |
| -------------------------------------------- | -------------------------------------------- |----------------------------------------------|
| <img src='./screenshots/pic1.png' width=320> | <img src='./screenshots/pic2.png' width=320> | <img src='./screenshots/pic3.png' width=320> |

## 功能特性

- **手势控制时间轴**: 支持平移手势（拖动时间轴）和捏合缩放手势（调整时间轴刻度）。
- **视频播放与时间轴同步**: 视频播放进度与时间轴上的当前时间点实时同步，用户拖动时间轴时，视频播放会相应跳转。
- **多视频片段管理**: 能够加载并按时间顺序播放多个视频文件。
- **时间刻度动态调整**: 时间轴的刻度（小时/分钟模式）会根据用户的缩放手势自动或平滑切换，提供合适的视图粒度。
- **播放状态反馈**: 视频播放状态（播放、暂停）与时间轴同步，提升用户体验。

## 使用说明

1. 将独立的应用示例工程导入DevEco Studio进行编译构建及运行调试。
2. 安装运行后，即可在设备上查看应用示例运行效果，以及进行相关调试。

## 工程目录

```
├───entry/src/main/ets
│   ├───common                              
│   │   ├───contants                        
│   │   │   └───CommonConstants.ets             // 常量
│   │   └───utils                           
│   │       └───CommonUtils.ets                 // 通用工具类
│   ├───components
│   │   └───VideoView.ets                       // 视频播放组件
│   ├───entryability                        
│   │   └───EntryAbility.ets                    // 程序入口类
│   ├───entrybackupability                  
│   │   └───EntryBackupAbility.ets              // 备份恢复类 
│   ├───model
│   │   ├───SegmentIndexInfo.ets        


---
## transitions-collection
> 本示例基于基础组件、通用属性、显式动效，实现多种常见转场动效案例。

源码: https://gitcode.com/HarmonyOS_Samples/transitions-collection

# 实现转场动效功能合集

### 介绍

本示例基于基础组件、通用属性、显式动效，实现多模态页面转场动效以及多种常见一镜到底转场动效，便于用户进行常见的转场动效场景开发。

### 效果预览

|               多模态页面转场动效                |               搜索一镜到底转场动效                |              卡片一镜到底转场动效               |
|:--------------------------------------:|:---------------------------------------:|:-------------------------------------:|
| ![image](screenshots/device/model.gif) | ![image](screenshots/device/search.gif) | ![image](screenshots/device/card.gif) |
|             **图片一镜到底转场动效**             |             **视频一镜到底转场动效**              |            **列表一镜到底转场动效**             |
| ![image](screenshots/device/image.gif) | ![image](screenshots/device/video.gif)  | ![image](screenshots/device/list.gif) |
|            **图书翻页一镜到底转场动效**            |
| ![image](screenshots/device/book.gif)  |

**使用说明**

点击各个模块下的选项进行跳转，进入到对应的转场动效场景：
1. 点击多模态页面转场动效实现案例，跳转半模态登录页面。在半模态窗口中选中同意协议键，并点击获取验证码按钮，跳转至手机验证码登录页面。通过点击手机验证码登录页面中的"账号密码登录"，向右切换跳转至账号密码登录页面，通过点击账号密码登录页面中的"手机验证码登录"，向左切换跳转至手机验证码登录页面。
2. 点击搜索一镜到底，进入搜索页面。点击搜索框后进行一镜到底的动效进入搜索页。
3. 点击卡片一镜到底，进入卡片页面。点击页面中的卡片后进行一镜到底的动效进入详情页。
4. 点击图片一镜到底，会弹出菜单选项：双指放大、查看大图和半模态。点击双指放大进入页面，在图片使用双指外扩的手势，图片会放大。点击查看大图进入页面会看到9张图片，点击图片后可以查看大图。点击半模态进入页面，点击页面中的图片会进入到半模态弹窗内。
5. 点击视频一镜到底，进入视频页面。点击视频进入到视频详情页，播放视频。
6. 点击列表一镜到底，进入列表页面。点击列表中的某一项进入详情页。
7. 点击图书翻页一镜到底，进入书架页面。点击书籍进入书籍详情页。

### 具体实现
```
├──entry/src/main/ets/
│  ├──common
│  │  ├──Constants.ets                                     // 公共常量类
│  │  └──CustomExceptions.ets                              // 自定义异常


---
## turbo-trans-protobuf
> 高性能 Protobuf 序列化库使用案例Sample

源码: https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf

# TurboTransProtobuf

## 简介
本示例展示了使用TurboTransProtobuf实现高性能Protobuf序列化反序列化操作，覆盖场景包括：
- 跨线程数据传递场景
- 反序列化为业务对象
- proto大数据解析场景
## 效果预览
<img src='./screenshots/device/sample.png' width='320'>


## 工程目录

```
├── entry/                                      // 应用入口
│   ├── protofile/                              // Proto文件定义
│   │   ├── DanmuMessage.proto                  // DanmuMessage数据结构定义
│   │   └── UserProfile.proto                   // UserProfile数据结构定义
│   └── src/main/ets                            // 代码区
│       ├── common                              
│       │   ├── components                      // 公共组件
│       │   │   ├── interface/                  
│       │   │   │   └── MainPageListItem.ets    // 单个菜单的数据结构定义
│       │   │   ├── CardContainer.ets           // 功能模块卡片-案例描述，示例代码，执行结果
│       │   │   ├── CellComponent.ets           // 单个功能模块菜单
│       │   │   ├── CellGroupComponent.ets      // 功能模块卡片
│       │   │   ├── LayoutContainer.ets         // 页面根布局组件
│       │   │   └── NavBar.ets                  // 页面标题
│       │   ├── constants                       
│       │   │   ├── CodeExampleConstants.ets    // 示例代码
│       │   │   ├── DanmuMessageConstants.ets   // DanmuMessage相关常量
│       │   │   ├── MenuConstants.ets           // 首页菜单目录
│       │   │   ├── PageConstant.ets            // 页面公共样式常量定义
│       │   │   └── PageRouteConstants.ets      // 路由常量定义
│       │   ├── styles                          
│       │   │   ├── BaseContentStyles.ets       // 页面基础样式
│    


---
## two-dimension-list
> 该示例通过组件嵌套滚动实现一个响应左右滑动以及上下滑动的列表。

源码: https://gitcode.com/HarmonyOS_Samples/two-dimension-list

# 实现两个Scroll组件嵌套滑动的效果

### 介绍

本示例通过两个Scroll嵌套，实现可左右和上下滑动的效果，多用于商品类、新闻类页面。帮助开发者掌握多个Scroll嵌套时，解决滑动冲突处理。

### 效果预览
![running](screenshots/device/list.gif)


### 工程目录
```
├──entry/src/main/ets                         // 代码区
│  ├──common
│  │  └──CommonConstants.ets                  // 常量类 
│  ├──entryability
│  │  └──EntryAbility.ets 
│  ├──model
│  │  ├──ListDataSource.ets                  
│  │  ├──MessageList.ets                      // 列表数据
│  │  └──TitleList.ets                        // 表头数据
│  └──pages
│     └──Index.ets                            // 首页
└──entry/src/main/resources                   // 应用资源目录
```

### 使用说明
进入首页后上下滑动列表，左右滑动列表。

### 具体实现
+ 本示例通过定义多个自定义组件，封装到Scroll组件中，通过懒加载的方式加载列表数据的方式实现上下左右滑动效果。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## ui-test
> 本示例展示测试框架中UI测试框架的使用示例。

源码: https://gitcode.com/HarmonyOS_Samples/ui-test

# 基于Uitest实现单元功能测试

## 介绍

本示例展示测试框架中UI测试框架的使用示例。便于开发者正确使用UI测试框架。

本实例需要引入UiTest接口@ohos.UiTest。

如需日志打印调试，需要引入日志打印接口@ohos.hilog。

## 效果预览

不涉及

使用说明

- 将uitest目录下的项目工程整体导入到DevEco Studio开发工具中。
- 查看ohostest目录下的测试代码实现。
- 在DevEco Studio中执行测试用例代码查看执行效果，执行方式请参考官网的测试框架。
- 本工程执行测试用例代码的结果，根据实际开发设备不同会有变更。请根据具体的开发设备修改代码中对应参数。

## 工程目录

```
├──entry/src/main/ets                             // 代码区
│  ├──clickability  
│  │  └──ClickAbility.ets                         // 点击入口类
│  ├──dragability  
│  │  └──DragAbility.ets                          // 拖拽入口类
│  ├──entryability  
│  │  └──EntryAbility.ets                         // 主程序入口类
│  ├──flingability  
│  │  └──FlingAbility.ets                         // 惯性滚动入口类
│  ├──inputability  
│  │  └──InputAbility.ets                         // 输入入口类
│  ├──mouseability  
│  │  └──MouseAbility.ets                         // 鼠标入口类
│  ├──pages  
│  │  ├──Click.ets                                // 点击页面
│  │  ├──Drag.ets                                 // 拖拽页面
│  │  ├──Fling.ets                                // 惯性滚动页面
│  │  ├──Fourth.ets                               // 第四页面
│  │  ├──Index.ets                                // 首页页面
│  │  ├──Input.ets                                // 输入页面
│  │  ├──Mouse.ets                                // 鼠标页面
│  │  ├──Pinch.ets                                // 捏合页面
│  │  ├──Scroller.ets                             // 滑动页面
│  │  ├──Swipe.ets                                // 滑块页面
│  │  └──Third.ets                


---
## uidesign-kit_-sample-code_-arkts
源码: https://gitcode.com/HarmonyOS_Samples/uidesign-kit_-sample-code_-arkts

# UI Design Kit（UI设计套件）

### 介绍
本示例主要展示了UI Design Kit（UI设计套件）相关的功能。
使用ArkUI、Localization Kit、Image Kit等接口，实现了图标合成、剪切、缩放、描边等功能。

### 相关概念
UI Design Kit是华为提供的符合华为HarmonyOS Design System定义的UI界面开发套件集合，包含HarmonyOS Design System设计定义的扩展UI组件及其多样化的组件样式、丰富多样的UI界面场景下的光影效果，支撑应用实现跟随HarmonyOS Design System高端精致设计效果UI界面，达成应用界面与华为HarmonyOS多设备UI设计风格完美融合。

### 相关权限
不涉及

### 使用说明
本示例展示了分层图标和单层图标的处理效果。

### 效果预览

<span style="border: 3px solid #ddd; padding: 10px 42px 10px 42px; margin: 10px 0;">
&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;分层图标&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;
</span>

<span style="border: 3px solid #ddd; padding: 10px 42px 10px 42px; margin: 10px 0;">
&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;单层图标&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;
</span>

<img src="screenshots/device/layeredIconProcessedScreen.png" width="296" height="640" /><img src="screenshots/device/iconProcessedScreen.png" width="296" height="640" />

### 工程目录
```
├─entry/src/main/ets                         // 代码区
│  ├─entryability
│  │  └─EntryAbility.ets       
│  └─pages
│     ├─GetHdsIcon.ets                       // 单层应用图标处理页面
│     ├─GetHdsLayeredIcon.ets                // 分层应用图标处理页面
│     └─Index.ets                            // 主页界面
├─entry/src/main/resources                   // 应用资源目录
└─screenshots                                // 截图
```

## 具体实现

在@kit.UIDesignKit中定义了图标处理接口API，示例接口如下：

```
  /**
   * Returns processed layered icon.
   *
   * @param { string } bundleName - Indicates the bundle n


---
## unit-test
> 本示例展示测试框架中单元测试框架的使用示例。

源码: https://gitcode.com/HarmonyOS_Samples/unit-test

# 测试框架

### 介绍
本示例展示测试框架中单元测试框架的使用示例。

本实例用到了自动化测试框架代码部件仓arkXtest，测试框架的详细介绍[arkXtest](https://docs.openharmony.cn/pages/v5.1/zh-cn/application-dev/application-test/arkxtest-guidelines.md)。   

如需日志打印调试，需要引入日志打印接口[@ohos.hilog](https://gitee.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-performance-analysis-kit/js-apis-hilog.md) 。  

单元测试用例相较于UI自动化测试用例而言更偏重于接口返回数据的校验及逻辑处理。


### 效果预览
不涉及

使用说明
- 将jsunit目录下的项目工程整体导入到DevEco Studio开发工具中。
- 查看ohostest目录下的测试代码实现。
- 在DevEco Studio中执行测试用例代码查看执行效果，执行方式请[参考](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/application-test/arkxtest-guidelines.md) 。

### 工程目录

```
jsunit
|-----entry 
          |-----src/main/pages
                |-----index.ets                         // 放页面组件 
          |-----ohosTest                                // 放自动化测试用例
                |-----ets/test/basicExampleTest
                      |-----basicExampleTest.ets        // 放自动化测试脚本，其中it()就是一个测试用例
|-----AppScope
          |-----app.json5                               // 定义应用唯一的包名："bundleName": "com.samples.test.jsunit",
```

### 具体实现

#### jsunit单元测试框架示例内容
* 1）在entry的index.ets中放页面组件。
* 2）在ohosTest的test/basicExample.test.ets中it()定义一条测试用例，支持三个参数：用例名称，过滤参数和用例函数。用例操作的行为以异步的形式编写。
* 3）通过Want配置指定唯一的ability即entry：通过want()中指定bundleName：com.samples.test.jsunit和abilityName：EntryAbility。
* 4）启动指定ability(相当于手动运行hap)：通过abilityDelegatorRegistry.getAbilityDelegator.startAbility(want)。
* 5）获取当前应用最顶层的ability对象：通过abilityDelegatorRegis


---
## upload-and-down-load
> 本示例使用@ohos.request接口创建上传和下载任务，实现上传、下载功能，hfs作为服务器，实现了文件的上传和下载和任务的查询功能。

源码: https://gitcode.com/HarmonyOS_Samples/upload-and-down-load

# 实现上传和下载功能

### 介绍
本示例使用@ohos.request接口创建上传和下载任务，实现上传、下载功能，hfs作为服务器，实现了文件的上传和下载和任务的查询功能。帮助开发者实现上传、下载文件并查询的场景。

### 效果预览

|                    主页                    |                     上传                     |                         下载                         |
|:----------------------------------------:|:------------------------------------------:|:--------------------------------------------------:|
| ![home](screenshots/devices/home.png) | ![util](screenshots/devices/upload.png) | ![convertxml](screenshots/devices/download.png) |

使用说明

1. 本示例功能需要先配置服务器环境后使用，具体配置见[上传下载服务配置](./environment/README.md)（仅支持Windows系统）。

2. 首页展示上传和下载两个入口组件，点击进入对应的页面，如果要使用后台下载任务，请开启后台任务开关。

3. 上传页面(请先在图库中确定已开启图库权限)：

    3.1 点击**+**，**从相册选择**拉起图库选择照片，图片选择页面支持拍照，选择照片后点击发表进行上传。 
   
    3.2 在首页中打开后台任务开关后，上传页面开启的是后台上传任务，后台任务在应用退出到后台时可以在通知栏看到任务状态。

4. 下载页面：

    4.1 点击文件列表选择要下载的文件后，点击**下载**选择指定路径后开始下载。

    4.2 点击**查看下载文件**进入下载文件页面，点击文件夹查看文件夹内的文件。

    4.3 在首页中打开后台任务开关后，下载页面开启的是后台下载任务，后台任务在应用退出到后台时可以在通知栏看到任务状态。

    4.4 前台下载时只支持单文件下载，后台下载时支持选择多个文件下载。

### 工程目录

```

├──entry/src/main/ets/                              // 应用首页
│  ├──components             
│  │  ├──AddPictures.ets                            // 添加图片组件
│  │  ├──CustomDataSource.ets                       // 自定义数据源
│  │  └──SelectFolderDialog.ets                     // 选择文件夹组件
│  ├──entryability
│  │  └──EntryAbility.ets                           // 程序入口类
│  └──pages
│     ├──Download.ets                               // 下载页面            


---
## verification-code-scenario
> 本示例介绍了文本框显示光标、底部加横条、背景颜色改变、选择验证码、滑块验证码五种验证码实例。

源码: https://gitcode.com/HarmonyOS_Samples/verification-code-scenario

# 实现多种验证码场景的效果

### 介绍

本示例实现了5种验证码场景，基本涵盖了大部分应用的验证码场景。开发者可按需下载代码，实现自己应用的验证码场景。

### 效果预览
| 文本框显示光标                                | 底部加横条                                   | 背景颜色改变                                      | 选择验证码                                   |
|----------------------------------------|-----------------------------------------|---------------------------------------------|-----------------------------------------|
| ![image](screenshots/device/text.gif)  | ![image](screenshots/device/bottom.gif) | ![image](screenshots/device/background.gif) | ![image](screenshots/device/choose.gif) |
| 滑动验证码                                  |
| ![image](screenshots/device/slide.gif) |

### 使用说明：

加载完成后显示首页的5个验证码实例，点击对应按钮，进入相应的验证码页面：
1. 文本框显示光标：输入数字光标会移动到下一个文本框，同时下边框变色。
2. 底部加横条：在输入框内输入6位数字。
3. 背景颜色改变：输入数字后背景颜色改变。
4. 选择验证码：按照提示文字的顺序点击图片上的文字，然后点击提交。
5. 滑块验证码：点击滑块按钮向右滑动，直到将图片拼接完整时松手。

### 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  ├──Constants.ets                         // 公共常量类
│  │  └──GlobalBuilderContext.ets              // 全局页面信息
│  ├──entryability
│  │  └──EntryAbility.ets                      // 程序入口类
│  ├──pages                 
│  │  ├──BackgroundColorChange.ets             // 背景颜色改变
│  │  ├──BottomWithBar.ets                     // 底部加横条
│  │  ├──Index.ets                             // 首页
│  │  ├──SelectVerificationCode.ets            // 选择验证码
│  │  ├──SliderVerificationCode.ets            // 滑块验证码
│  │  └──TextBoxShowCursor.ets                 // 文本框显示光标
│


---
## video-cache
> 本案例实现了视频边缓存边播放的功能。

源码: https://gitcode.com/HarmonyOS_Samples/video-cache

# 实现视频边缓存边播放功能

### 简介

本示例基于三方库OhosVideoCache，实现了视频边缓存边播放的功能，将音视频的url传递给OhosVideoCache处理之后再设置给播放器， 即可一边下载音视频数据并保存在本地，一边读取本地缓存返回给播放器，适用于HTTP/HTTPS协议类型流媒体播放场景。

### 效果预览：

![image](screenshots/video.png)

使用说明：

1.本案例需要访问一个网络视频直链来实现边缓存边播放的功能，您可以修改VideoPlayerManager.ets中的ORIGIN_URL为想要播放的视频直链(HTTP/HTTPS协议类型典型链接: https://xxxx.mp4)，本案例也提供了一个本地视频和本地搭建服务器的方案，来模拟访问网络视频的情况，请参考搭建服务器章节。

2.安装应用后打开，应用会一边下载音视频数据并保存在本地，一边读取本地缓存返回给播放器进行播放。

### 搭建服务器

1.本案例提供了Python脚本快速搭建服务器，需要本地有Python环境，另外，您需要安装Flask框架，可以通过Python的包管理器pip来安装Flask，在终端输入以下命令：

```
pip install flask
```

2.修改video_server.py中的VIDEO_PATH，将其替换为想要播放的视频的实际路径。

3.使用终端运行脚本：
```
python video_server.py
```

4.脚本将启动一个Flask服务器，默认监听5000端口，您可以通过访问http://<您的电脑IP地址>:5000/video来播放视频。

### 工程目录

```
├──entry/src/main/ets
│  ├──common
│  │  └──CommonConstants.ets            // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──model
│  │  ├──GlobalProxyServer.ets          // 代理服务器
│  │  └──VideoPlayerManager.ets         // 播放器管理类
│  ├──pages                  
│  │  └──Index.ets                      // 首页
│  └──utils
│     └──utils.ets                      // 工具类
└──entry/src/main/resource              // 应用静态资源目录
```

### 相关权限

- ohos.permission.INTERNET
- ohos.permission.GET_NETWORK_INFO

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## video-play
> 视频播放的主要工作是将视频数据转码并输出到设备进行播放，同时管理播放任务。

源码: https://gitcode.com/HarmonyOS_Samples/video-play

# 实现AVPlayer视频播放功能

### 介绍
视频播放的主要工作是将视频数据转码并输出到设备进行播放，同时管理播放任务。本文将对视频播放全流程、视频切换、视频循环播放等场景开发进行介绍说明。
本示例主要展示了播放本地视频和网络视频相关功能,使用 @ohos.multimedia.media, @ohos.resourceManager,@ohos.wifiManager等接口,实现了视频播放、暂停、调节倍速、切换视频的功能;实现效果如下;

### 效果预览
| 播放                                         | 暂停                                       | 倍速弹窗                                               | 视频列表                                      |
|--------------------------------------------|------------------------------------------|----------------------------------------------------|-------------------------------------------|
| ![播放.png](screenshots/devices/playing.png) | ![暂停.png](screenshots/devices/pause.png) | ![img_2.png](screenshots/devices/speed_dialog.png) | ![视频列表.png](screenshots/devices/video_list.png) |


使用说明

1.点击视频界面，唤起视频操作面板，再次点击操作面板消失，如果不做任何操作操作界面会5s自动消失;

2.点击暂停/播放按钮，控制视频暂停播放;

3.滑动视频进度条，视频跳转到指定位置,在视频中间会出现时间进度方便用户查看视频进度;

4.点击倍速，可以选择1.0、1.25、1.75、2.0进行倍速调节;

5.点击下方视频名称，可以选择视频进行切换。注意：network是网络视频，没有连接网络无法切换到网络视频，有网络能在本地视频和网络视频进行切换;

6.点击左上角退出箭头，退出应用。

### 目录结构
```
├──entry/src/main/ets                             // 代码区
│  ├──components
│  │  ├──ExitVideo.ets                            // 退出应用组件
│  │  ├──SpeedDialog.ets                          // 播放倍速弹窗
│  │  └──VideoOperate.ets                         // 视频操作组件
│  ├──entryability
│  │  └──EntryAbility.ets                     
│  ├──pages
│  │  └──Index.ets                                // 首页视频界面
│  ├──utils
│  │  ├──GlobalContext


---
## video-player
> 本示例主要展示通过HarmonyOS提供的系统播放器AVPlayer和媒体会话等能力，实现视频类应用的开发。

源码: https://gitcode.com/HarmonyOS_Samples/video-player

# 实现视频流畅播放且支持后台与焦点打断功能

### 简介

本示例从用户交互和音频流状态变更两个维度，基于HarmonyOS提供的媒体（AVPlayer）和ArkUI等能力，实现长/短视频的流畅播放，视频支持前后台播放控制、播放形态切换、音频焦点切换、播放设备切换等场景，可以为视频播放应用提供灵活的交互体验和良好的观看效果。

### 效果预览

<img src="screenshots/videoPlayer.gif" width='320'>

### 使用说明

1. 启动应用后显示视频播放列表及首个视频自动播放。

2. 点击页面按钮可切换竖屏或横屏模式。

3. 上下滑动切换视频，并能看到历史播放记录。

4. 拖动进度条或全屏手势滑动可调节播放进度。

5. 应用切换到后台可以持续播放并且可以播控中心进行控制。

6. 全屏播放视频场景下，在屏幕左侧上下滑动可调节音量，在屏幕右侧上下滑动可调节亮度。


### 工程目录

```
├──entry/src/main/ets                              
│  ├──entryability  
│  │  └──EntryAbility.ets               // 程序入口
│  ├──model
│  │  ├──BasicDataSource.ets            // 懒加载DataSource
│  │  └──DataModel.ets                  // 数据类
│  ├──pages                                     
│  │  └──IndexPage.ets                  // 首页
│  ├──utils                                     
│  │  ├──WindowUtil.ets                 // 窗口工具类
│  │  └──BreakpointSystem.ets           // 断点工具类
│  └──view
│     ├──AVPlayer.ets                   // 视频组件
│     ├──VideoList.ets                  // 首页视频列表
│     ├──VideoSide.ets                  // 视频滑动组件
│     └──VideoDetails.ets               // 视频详情信息组件
├──entry/src/main/resources             // 应用资源目录
├──MediaService/src/main/ets
│  ├──common  
│  │  └──CommonConstants.ets            //常量类
│  ├──controller
│  │  ├──AvPlayerController.ets         //视频播放控制
│  │  └──AvSessionController.ets        //媒体会话控制
│  ├──model
│  │  └──VideoData.ets                  //视频数据类
│  └──utils
│      ├──BackgroundTaskManager.ets     // 后台播放功能
│ 


---
## video-render
> 该示例主要是用来指导如何通过视频解码进行画面渲染，包括基于XComponent渲染、基于OpenGL渲染、基于Vulkan渲染。

源码: https://gitcode.com/HarmonyOS_Samples/video-render

# 渲染视频数据

## 项目简介
本示例适用于视频解码后的视频画面渲染送显，渲染送显的方式包括基于XComponent渲染送显、基于OpenGL渲染送显、基于Vulkan渲染送显。本示例提供了视频渲染的多种方案，帮助开发者实现自定义播放器开发，了解视频解码到渲染的全流程。


## 效果预览
| 首页                                                  | 基于XComponent播放页                                     |
|-----------------------------------------------------|--------------------------------------------------------| 
| <img src='./screenshots/homePage.png' width="320">   | <img src='./screenshots/xcomponentPage.png' width='320'> | 
| 基于OpenGL播放页                                         | 基于Vulkan播放页                                     |
| <img src='./screenshots/openglPage.png' width='320'> | <img src='./screenshots/vulkanPage.png' width='320'> |

## 使用说明
点击进入基于XComponent渲染视频、基于OpenGL渲染视频、基于Vulkan渲染视频的子页面，点击播放即可渲染播放视频。

## 工程目录

```
├───entry/src/main/cpp
│   ├───capbilities
│   │   ├───include
│   │   │   ├───SampleInfo.h                // 视频样本
│   │   │   ├───SampleCallback.h            // 视频回调
│   │   │   ├───Demuxer.h                   // 媒体解析
│   │   │   └───VideoDecoder.h              // 视频解码
│   │   └───src
│   │       ├───SampleCallback.cpp          // 视频回调
│   │       ├───Demuxer.cpp                 // 媒体解析
│   │       └───VideoDecoder.cpp            // 视频解码
│   ├───player
│   │   ├───include
│   │   │   └───Player.h                    // 视频播放
│   │   ├───src
│   │   │   └───Player.cpp                  // 视频播放
│   └───render
│       ├───include
│       │   ├───OpenGLRender.h              // OpenGL渲染上下文
│       │   ├


---
## video-show
> 本示例使用Video组件展示了视频组件的基本功能，包括视频组件化，全屏化，窗口化，上下轮播视频等。

源码: https://gitcode.com/HarmonyOS_Samples/video-show

# 基于Video组件播放长视频

## 项目简介
本示例基于Video组件实现了播放长视频功能，指导开发者如何通过Video组件实现长视频播放，如：基础播控、视频首帧显示、自定义播放进度条、前台小窗播放、循环播放、视频全屏播放、视频音量设置、静音播放、长按倍速播放、点击选择倍速播放、接入播控中心等功能场景。

## 效果预览

| 首页                                                      | 小窗播放                                                      | 接入播控中心                                                   |
|---------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------|
| <img src='./screenshots/device/homePage.png' width=320> | <img src='./screenshots/device/smallVideo.png' width=320> | <img src='./screenshots/device/avSession.png' width=320> |

| 横屏-音量调节                                               | 
|-------------------------------------------------------|
| <img src='./screenshots/device/volume.png' width=320> |


## 使用说明
1. 安装进入应用。
2. 点击视频区域播放/暂停播放本地视频，并可通过点击视频列表内容切换视频。
3. 点击Slider实现视频跳转播放。
4. 点击右下角按钮，进入全屏播放。
5. 进入全屏后：
   1. 滑动视频左侧区域，实现音量调节。
   2. 点击播放速度按钮，选择视频播放倍速。
   3. 长按视频区域，实现视频倍速播放。
   4. 点击右下角静音按钮，实现静音播放。
6. 视频播放时，通过播控中心控制视频的播放、暂停、跳转播放、点击播放上一个/下一个视频。

## 工程目录
```
├──entry/src/main/ets
│  ├──constants
│  │  ├──CommonConstants.ets            // 常量
│  │  └──VideoStatus.ets                // Video状态
│  ├──controller
│  │  └──AVSessionController.ets        // AVSession控制类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets         // 备份恢复类
│  ├──mo


---
## video-subtitle
> 给视频添加字幕

源码: https://gitcode.com/HarmonyOS_Samples/video-subtitle

# 实现视频外挂字幕

## 项目简介

本示例分别使用AVPlayer实例和Video组件两种方式，实现了视频配置外挂字幕和设置字幕字体格式、字体大小、颜色。

## 效果预览

| 应用首页   | <img src="./screenshots/devices/home.jpg" height="320">         |
|:-------|-----------------------------------------------------------------|
| 应用效果展示 | <img src="./screenshots/devices/captionVideo.gif" height="320"> |


## 使用说明
1. 打开应用，点击按钮，进入AVPlayer/Video组件外挂字幕页面。
2. 点击下方字幕设置按钮，选择字幕格式，设置完成，点击确认，字幕格式修改生效。

## 工程目录

```
├──entry/src/main/ets/                              
│  ├──constants
│  │  └──Constants.ets                              // 常量文件
│  ├──entryability
│  │  └──EntryAbility.ets                           // 程序入口类
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                     // 备份入口类
│  ├──model  
│  │  └──ViewModel.ets                              // 视频播放参数类     
│  ├──pages  
│  │  ├──Index.ets                                  // 首页入口页面           
│  │  └──VideoPage.ets                              // 视频播放页
│  ├──utils                                         
│  │  ├──CommonUtil.ets                             // 公共工具类
│  │  └──Logger.ets                                 // 日志类
│  └──views             
│     ├──AvPlayerComponent.ets                      // AVPlayer视频播放组件
│     ├──CaptionFontComponent.ets                   // 字幕字体设置组件
│     └──VideoPlayerComponent.ets                   // Video视频播放组件
└──entry/src/main/resources                         // 应用静态资源目录
```

## 具体实现

1.AVPlayer实例注册on('subtitleUpdate')方法监听字幕信息，使用状态变量刷新Text组件内容，并通过改变Text属性修


---
## video-water-mark
> 指导开发者进行视频添加水印，场景包括：（1）本地视频文件添加水印；（2）相机录制添加水印。

源码: https://gitcode.com/HarmonyOS_Samples/video-water-mark

# 实现视频添加水印功能

### 介绍

本示例基于系统相机、OpenGL、视频编解码等能力，实现了本地视频文件添加水印和相机预览录制实时添加水印。

### 效果图预览
| 首页                                               | 相机添加水印页                                               | 本地视频添加水印页                                     | 
|--------------------------------------------------| ------------------------------------------------------------ | ------------------------------------------------------ |
| <img src='./screenshots/homePage.png' width=320> | <img src='./screenshots/cameraWaterMark.png' width=320>      | <img src='./screenshots/videoWaterMark.png' width=320> |
| 1、选择添加水印场景                                       | 1、点击录制，实现实时水印添加<br>2、点击播放，播放最近一次录制视频 | 1、点击添加水印，给本地视频文件添加水印                | 

### 工程结构&模块类型

```
├───entry/src/main/cpp
│   ├───camera
│   │   ├───ndk_camera.cpp
│   │   └───ndk_camera.h                        // 相机管理
│   ├───capbilities
│   │   ├───include
│   │   │   ├───audio_capturer.h                // 音频录制
│   │   │   ├───audio_decoder.h                 // 音频解码
│   │   │   ├───audio_encoder.h                 // 音频编码
│   │   │   ├───demuxer.h                       // 媒体解析
│   │   │   ├───muxer.h                         // 媒体封装
│   │   │   ├───video_decoder.h                 // 视频解码
│   │   │   └───video_encoder.h                 // 视频编码
│   │   ├───audio_capturer.cpp
│   │   ├───audio_decoder.cpp
│   │   ├───audio_encoder.cpp
│   │   ├───demuxer.cpp
│   │   ├───muxer.cpp
│   │   ├───video_decoder.cpp
│   │   └───video_encoder.cpp
│   ├───


---
## visionkit-sample-code-arkts
> 本示例展示了人脸活体检测能力、卡证识别能力和文档扫描能力。

源码: https://gitcode.com/HarmonyOS_Samples/visionkit-sample-code-arkts

# 实现人脸活体检测控件

## 介绍

本示例展示了使用视觉类AI能力中的人脸活体检测能力。

本示例模拟了在应用里，跳转人脸活体检测控件，获取到检测结果并展示出来。

需要使用人脸活体检测接口@hms.ai.interactiveLiveness.d.ts。

## 效果预览

|         **主窗口**          |                 **开始检测**                  |           **检测成功**           |          **检测失败**           |         **检测结果成功**          |            **检测结果失败**             |
|:------------------------:|:-----------------------------------------:|:----------------------------:|:---------------------------:|:---------------------------:|:---------------------------------:|
| ![](screenshots/app.png) | ![](screenshots/interactionDetection.png) | ![](screenshots/success.png) | ![](screenshots/failed.png) | ![](screenshots/resultSuccess.png) | ![](screenshots/resultFailed.png) | 

使用说明：

1. 在手机的主屏幕，点击”faceDetectionDemo“，启动应用。
2. 点击“Start detection”按钮，进入人脸活体检测控件。
3. 检测结束后获取到检测结果并展示出来。


## 工程目录

```
├─entry/src/main/ets                         // 代码区  
│  ├─entryability
│  │  └─EntryAbility.ets                     // 入口Ability
│  └─pages
│     └─Index.ets                            // 主页界面
└─screenshots                                // 截图
```

## 具体实现

本示例展示的控件在@hms.ai.interactiveLiveness.d.ts定义了人脸活体检测API：
```ts
function startLivenessDetection(config: InteractiveLivenessConfig): Promise<boolean>;
function getInteractiveLivenessResult(): Promise<InteractiveLivenessResult>;
```

业务使用时，需要先进行import导入interactiveLiveness。
调用进入活体控件接口和检测结果接口，接收处理返回的结果。参考entry/src/main/ets/pages/Index.ets.

## 相关权限

ohos.permission.CAMERA。




---
## visionkit-sample-code-card-recognition-demo-ark-ts
源码: https://gitcode.com/HarmonyOS_Samples/visionkit-sample-code-card-recognition-demo-ark-ts

# 实现卡证识别控件

## 介绍

本示例展示了使用视觉类AI能力中的卡证识别能力。

本示例模拟了在应用里，跳转卡证识别控件，获取到验证结果并展示出来。

需要使用卡证识别验证接口@hms.ai.CardRecognition.d.ets。



## 效果预览

| 预览                         | 拍照                         |
| ---------------------------- | ---------------------------- |
| ![](screenshots/preview.png) | ![](screenshots/capture.png) |



使用说明：

1. 在手机的主屏幕，点击”CardRecognition“，启动应用。
2. 点击拍照按钮，识别卡证图片。
3. 拍摄完成后卡证信息显示在页面上。



## 工程目录

```
├─entry/src/main/ets                         // 代码区  
│  ├─entryability
│  │  └─EntryAbility.ets                     // 入口Ability
│  └─pages
│     ├─MainPage.ets                         // 主页界面
│     └─CardDemoPage.ets                     // 卡证控件调用界面
└─entry/src/main/resources                   // 应用资源目录
```



## 具体实现

本示例展示的控件在@hms.ai.CardRecognition.d.ets定义了卡证识别控件：
```ts
/**
 * This is a ui component used to identify card
 * @syscap SystemCapability.AI.Component.CardRecognition
 * @atomicservice
 * @since 5.0.0(12)
 */
@Component
declare struct CardRecognition {
    /**
     * Supported card identification types.
     * @type { CardType }
     * @syscap SystemCapability.AI.Component.CardRecognition
     * @atomicservice
     * @since 5.0.0(12)
     */
    supportType: CardType;
    /**
     * Card side to recognize.
     * @type { ?CardSide }
     * @default CardSide.DEFAULT
     * @syscap SystemCapability.AI.Component.CardRecognition
     * @atomicservice
     * @since 5.0.0(12)
     */
    cardSide?: CardSide;
    /**
     * Card recognition result callba


---
## visionkit-sample-code-document-scan-demo-ark-ts
源码: https://gitcode.com/HarmonyOS_Samples/visionkit-sample-code-document-scan-demo-ark-ts

# 实现文档扫描控件

## 介绍

本示例展示了使用视觉类AI能力中的文档扫描能力。

本示例模拟了在应用里，跳转文档扫描控件，获取到扫描结果并展示出来。

需要使用文档扫描验证接口@hms.ai.DocumentScanner.d.ets。



## 效果预览

| 预览                         | 拍照                         | 编辑                      |
| ---------------------------- | ---------------------------- | ------------------------- |
| ![](screenshots/preview.png) | ![](screenshots/capture.png) | ![](screenshots/edit.png) |



使用说明：

1. 在手机的主屏幕，点击”DocumentScanDemo“，启动应用。
2. 点击拍照按钮，识别文档图片。
3. 点击缩略图，进入编辑页面。
4. 可更换滤镜、手动裁剪等。



## 工程目录

```
├─entry/src/main/ets                         // 代码区  
│  ├─entryability
│  │  └─EntryAbility.ets                     // 入口Ability
│  └─pages
│     └─DocDemoPage.ets                      // 文档扫描主界面
└─entry/src/main/resources                   // 应用资源目录
```



## 具体实现

本示例展示的控件在@hms.ai.DocumentScanner.d.ets定义了文档扫描控件：
```ts
/**
 * This is a ui component used for generating document scans.
 * @struct { DocumentScanner }
 * @syscap SystemCapability.AI.Component.DocScan
 * @atomicservice
 * @since 5.0.0(12)
 */
@Component
declare struct DocumentScanner {
    /**
     * config for document scanner.
     *
     * @type { DocumentScannerConfig }
     * @syscap SystemCapability.AI.Component.DocScan
     * @atomicservice
     * @since 5.0.0(12)
     */
    scannerConfig: DocumentScannerConfig;
    /**
     * @type { DocumentScannerResultCallback }
     * callback of the listened event, called when the Component is terminated.
     * @syscap SystemCapability.AI.Component.DocSca


---
## visionkit-samplecode-sheet-extraction-demo-arkts
> 本示例通过提供拍摄表格并转换为表格文档的服务。

源码: https://gitcode.com/HarmonyOS_Samples/visionkit-samplecode-sheet-extraction-demo-arkts

# 实现表格提取功能

## 介绍

本示例展示了使用视觉类AI能力中的表格提取能力。

本示例模拟了在应用里，跳转表格提取功能，获取到表格提取结果并展示出来。

需要使用文档扫描控件@hms.ai.DocumentScanner.d.ets。



## 效果预览

| 预览                           | 拍照                           | 表格提取                   |
|------------------------------|------------------------------|------------------------|
| ![](screenshots/preview.png) | ![](screenshots/capture.png) | ![](screenshots/sheetExtraction.png) |



使用说明：

1. 在手机的主屏幕，点击”SheetDemo“，启动应用。
2. 点击“SheetExtraction”按钮，跳转到文档扫描控件。
3. 将镜头对准一张表格，跳出”表格提取“气泡（必须保证是表格，否则无法出现入口）。
4. 点击”表格提取“气泡，进入表格提取拍摄页面。
5. 点击拍摄识别表格。



## 工程目录

```
├─entry/src/main/ets                         // 代码区  
│  ├─entryability
│  │  └─EntryAbility.ets                     // 入口Ability
│  └─pages
│     └─Index.ets                            // 应用主界面
│     └─SheetExtractionPage.ets              // 文档扫描主界面
└─entry/src/main/resources                  // 应用资源目录
```



## 具体实现

本示例展示的功能由@hms.ai.DocumentScanner.d.ets中定义的文档扫描控件提供：
```ts
/**
 * This is a ui component used for generating document scans.
 * @struct { DocumentScanner }
 * @syscap SystemCapability.AI.Component.DocScan
 * @atomicservice
 * @since 5.0.0(12)
 */
@Component
declare struct DocumentScanner {
    /**
     * config for document scanner.
     *
     * @type { DocumentScannerConfig }
     * @syscap SystemCapability.AI.Component.DocScan
     * @atomicservice
     * @since 5.0.0(12)
     */
    scannerConfig: DocumentScannerConfig;
    /**
     * @type { DocumentScannerResultCallback }
    


---
## wallet-kit-for-harmony-os_demo
> 华为钱包服务客户端示例主要展示华为钱包的开通车钥匙能力入口。


源码: https://gitcode.com/HarmonyOS_Samples/wallet-kit-for-harmony-os_demo

# 基于钱包服务实现数字车钥匙开通及使用

## 介绍

基于Stage模型，提供钱包交通卡和Pass卡的开卡、预览卡、查询卡信息、更新卡片信息、删除卡片、初始化钱包环境等功能。

## 效果预览

| 1                          | 2                                | 3                         |
|----------------------------|----------------------------------|---------------------------|
| ![](screenshots/Index.png) | ![](screenshots/TransitCard.png) | ![](screenshots/Pass.png) |

## 工程目录

```
├─entry/src/main/ets
                   |─application/AbilityStage.ts   // stage
                   ├─common                         // 页面工具类
                   ├─components                     // 页面组件
                   ├─mainability/MainAbility.ts    // 本地启动ability   
                   │              
                   └─pages
                       ├─ Index.ets                 // 首页
                       ├─ wallet
                                ├─ ICCECallBack.ets // ICCE工具类
                                ├─ Pass.ets         // Pass卡页面
                                ├─ TransitCard.ets  // 交通卡页面
```

## 具体实现

### 交通卡

在@hms.core.payment.walletTransitCard中定义了钱包交通卡接口API，示例接口如下：

```
  /**
          * Obtains an array of CardMetadataInDevice objects, each of which contains the device information and the metadata of every card supported by the device.
          * An empty array will be returned in the device without eSE or if the specified device does not support any transit card. 
          *
          * @param { DeviceType } specifiedDeviceType - Type of the specified device.
     


---
## wallet-kit-sample-code-severdemo-java
> 华为钱包服务服务端示例主要展示华为钱包的开通车钥匙能力。

源码: https://gitcode.com/HarmonyOS_Samples/wallet-kit-sample-code-severdemo-java

# 华为钱包服务服务端示例代码
### 目录

* [简介](#简介)
* [环境要求](#环境要求)
* [申请华为钱包服务](#申请华为钱包服务)
* [配置参数](#配置参数)
* [卡券模板和实例](#卡券模板和实例)
* [编译Maven工程](#编译Maven工程)
* [示例方法](#示例方法)
   1. [卡券实例示例方法](#卡券实例示例方法)
   1. [生成JWE](#生成JWE)
* [技术支持](#技术支持)
* [授权许可](#授权许可)


## 简介
Wallet Kit（钱包服务）集成了终端“芯-端-云”全栈技术的开放能力，可实现车钥匙的凭证电子化。让用户能够轻松地将车钥匙保存在手机中，以便在适当的时间使用。

## 环境要求
示例代码的运行环境为Maven和Oracle Java（1.8.0.211及以上版本）。

## 申请华为钱包服务
参照[创建Wallet Kit服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-preparations) 申请华为钱包服务。<br>

请注意在申请钱包服务的过程中需要创建一个服务号，该服务号即为passTypeIdentifier的值，后续将在配置示例代码中用到。<br>

您在申请过程中还会创建一对RSA公私钥，请妥善保管。其中私钥用于后续对JWE进行签名 (详情请参阅 [生成JWE](#生成JWE). 公钥用于钱包服务器验签。<br>

在设置完一类卡券的服务号之后，你就可以运行这个卡券对应的示例代码了。如果你想测试其他卡券，则需申请其他卡券的服务号。

## 配置参数
运行示例代码前，在”src\test\resources\release.config.properties”文件中配置如下参数：”gw.appid”, “gw.appid.secret”, “gw.tokenUrl”, “walletServerBaseUrl”, “servicePrivateKey”和“walletWebsiteBaseUrl”。

#### 设置 "gw.appid" and "gw.appid.secret":
"gw.appid"和"gw.appid.secret"为应用的"APP ID"和"SecretKey"。登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“我的应用”，选择目标应用，即可找到该应用的APP ID和SecretKey。

#### 设置 "gw.tokenUrl"
获取REST接口认证token的地址，将gw.tokenUrl设置为https://oauth-login.cloud.huawei.com/oauth2/v3/token

#### 设置 "walletServerBaseUrl":
"walletServerBaseUrl" 为REST接口请求的公共部分，格式为https://{walletkit_server_url}/hmspass。其中{walletkit_server_url}需要根据您的账号所属国家/地区自行替换，目前仅涉及中国大陆：wallet-passentrust-drcn.cloud.huawei.com.cn

#### 设置 "servicePrivateKety"
将"serv


---
## wallet-kit-sample-code-severdemo-nfc-java
> 华为钱包服务服务端示例主要展示华为钱包的激活车钥匙能力。

源码: https://gitcode.com/HarmonyOS_Samples/wallet-kit-sample-code-severdemo-nfc-java

# 华为钱包服务NFC示例代码

## 目录

* [简介](#简介)
* [安装](#安装)
* [环境要求](#环境要求)
* [示例代码](#示例代码)
* [授权许可](#授权许可)

## 简介
本示例代码展示如何使用华为钱包服务（HUAWEI Wallet Kit）NFC刷卡能力。

## 安装
运行示例代码前，您需安装Java和Maven。

## 环境要求
建议您使用Oracle Java 1.8。

## 示例代码
PassesController为统一入口类，定义了需要实现的接口。

1. 注册接口
调用注册接口注册、获取三方鉴权及授权证书。
	
2. 申请个性化token
调用requestToken方法申请个性化token。
	
3. 获取个性化数据
调用getPersonalInfo接口获取个性化数据。
	
4. 取消注册
用户删除卡券时，华为钱包将调用取消注册接口通知您卡券已删除。

## 技术支持
如果您对HMS Core还处于评估阶段，可在[Reddit社区](https://www.reddit.com/r/HuaweiDevelopers/)获取关于HMS Core的最新讯息，并与其他开发者交流见解。

如果您对使用HMS示例代码有疑问，请尝试：
- 开发过程遇到问题上[Stack Overflow](https://stackoverflow.com/questions/tagged/huawei-mobile-services)，在`huawei-mobile-services`标签下提问，有华为研发专家在线一对一解决您的问题。
- 到[华为开发者论坛](https://developer.huawei.com/consumer/cn/forum/blockdisplay?fid=18) HMS Core板块与其他开发者进行交流。

如果您在尝试示例代码中遇到问题，请向仓库提交[issue](https://github.com/HMS-Core/hms-wallet-nfc/issues)，也欢迎您提交[Pull Request](https://github.com/HMS-Core/hms-wallet-nfc/pulls)。

## 授权许可
华为钱包服务NFC刷卡能力集成示例代码经过[Apache License, version 2.0](http://www.apache.org/licenses/LICENSE-2.0)授权许可。



---
## water-flow
> 基于WaterFlow容器，实现瀑布流布局，使用sections实现了混合排列，实现了Tab吸顶、下拉刷新、无限加载等功能。

源码: https://gitcode.com/HarmonyOS_Samples/water-flow

# 实现WaterFlow瀑布流布局功能

### 介绍

本示例为开发者展示使用WaterFlow瀑布流容器实现首页布局效果，包括使用sections实现分组混排布局、删除滑动错位、结合item实现滑动吸顶、停止滑动自动播放，等场景。

### 效果预览

| 场景一                                        | 场景二                                        | 
|--------------------------------------------|--------------------------------------------|
| ![image](screenshots/device/Scenario1.png) | ![image](screenshots/device/Scenario2.png) |

### 使用说明

- 首页点击场景一，进入页面，显示分组混排布局的瀑布流，可上下滑动瀑布流，支持下拉刷新，加载更多，长按item删除。
- 首页点击场景二，进入页面，显示瀑布流，其中有选项item在瀑布流滑动时能够实现吸顶，有视频item时自动播放。

### 工程目录
```
├──entry/src/main/ets                        // 代码区
│  ├──common
│  │  ├──constants                  
│  │  │   └──CommonConstants.ets             // 常量类  
│  │  └──utils
│  │      └──Logger.ets                      // 日志类  
│  ├──entryability
│  │  └──EntryAbility.ets 
│  ├──model
│  │  └──MediaItem.ets                       // 瀑布流item数据类
│  ├──viewmodel
│  │  ├──SectionsWaterFlowDataSource.ets     // sections瀑布流数据
│  │  └──StickyWaterFlowDataSource.ets       // 吸顶瀑布流数据
│  ├──pages
│  │  ├──Index.ets                           // 场景聚合首页
│  │  ├──SectionsHomePage.ets                // 场景一-首页
│  │  └──StickyHomePage.ets                  // 场景二-首页               
│  └──view
│     ├──SectionsWaterFlowComponent.ets      // sections瀑布流组件 
│     └──StickyWaterFlowComponent.ets        // sticky瀑布流组件
└──entry/src/main/resources                  // 应用资源目录
```

### 具体实现

+ 场景一：使用WaterFlow的sections实现了分组混排布局，实现下拉刷新，加载更多，删除滑动错位；
+ 场景二：结合某一item实现了滑动吸顶，图


---
## watermark
> 本示例为开发者展示常用的水印添加能力，包括两种方式给页面背景添加水印、保存图片添加水印、拍照图片添加水印。

源码: https://gitcode.com/HarmonyOS_Samples/watermark

# 实现添加水印功能

### 介绍

本示例为开发者展示常用的水印添加能力，包括给页面添加水印、保存图片添加水印、拍照图片添加水印和pdf文件添加水印。

### 效果预览

| 首页                                  | 页面水印                                | 图片水印                                 | pdf水印                              |
|-------------------------------------|-------------------------------------|--------------------------------------|------------------------------------|
| ![](./screenshots/devices/home.png) | ![](./screenshots/devices/page.png) | ![](./screenshots/devices/image.png) | ![](./screenshots/devices/pdf.png) |

### 使用说明
打开首页，点击不同选项进入具体页面：
1. 使用Stack组件添加水印：在UI页面上呈现水印，使用Stack层叠布局实现。
2. 使用overlay属性添加水印：在UI页面上呈现水印，使用overlay浮层属性实现。
3. 保存图片添加水印：点击下载，在系统图库中可以看到保存后的图片，添加了水印。
4. 拍照图片添加水印：点击拍照，在系统图库中可以看到保存后的图片，添加了水印。
5. PDF添加水印：点击下载，可以看到生成的PDF文件，添加了水印。

### 工程目录

```
├──entry/src/main/ets/
│  ├──component
│  │  ├──NavBar.ets                     // 顶部导航条
│  │  └──Watermark.ets                  // 页面水印组件
│  ├──constants
│  │  ├──Utils.ets                      // 工具类
│  │  └──Constants.ets                  // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  └──pages            
│     ├──CameraPage.ets                 // 拍照添加水印
│     ├──Index.ets                      // 首页
│     ├──SaveImagePage.ets              // 保存图片添加水印
│     ├──WatermarkPdfPage.ets           // pdf文件添加水印
│     ├──WatermarkStackPage.ets         // 使用Stack添加页面背景水印
│     └──WatermarkOverlay.ets           // 使用overlay添加页面背景水印
└──entry/src/main/resources       


---
## wear-engine-sample
源码: https://gitcode.com/HarmonyOS_Samples/wear-engine-sample

# 穿戴服务

## 介绍

本实例展示了使用穿戴服务获取已连接穿戴设备，与穿戴设备侧应用交互的能力。

需要使用穿戴服务接口 **@kit.WearEngine**

## 效果预览
| **主页面**                      | **授权页面**                        | **设备信息页面**                        | **状态查询与订阅页面**                      | **消息通知页面**                        | **端对端应用通信页面**                  | **传感器页面**                         | **连接页面**                        |
|------------------------------|---------------------------------|-----------------------------------|------------------------------------|-----------------------------------|--------------------------------|-----------------------------------|---------------------------------|
| ![](./screenshots/Index.PNG) | ![](./screenshots/AuthPage.PNG) | ![](./screenshots/DevicePage.PNG) | ![](./screenshots/MonitorPage.PNG) | ![](./screenshots/NotifyPage.PNG) | ![](./screenshots/P2pPage.PNG) | ![](./screenshots/SensorPage.PNG) | ![](./screenshots/ServicePage.PNG) | 
## Sample工程的配置与使用

#### 在DevEco中配置Sample工程的步骤如下

1. [创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-createproject-0000001100334664)及[应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-createapp-0000001146718717)。
2. [申请WearEngine服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wearengine_apply)。
3. 打开Sample应用，使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)配置的应用包名替换AppScope\app.json5文件中的bundleName属性值。
4. 使用[AppGallery Connect](https://developer.huawei.com/consumer/cn/servi


---
## weather-service-kit-sample-code-arkts
源码: https://gitcode.com/HarmonyOS_Samples/weather-service-kit-sample-code-arkts

## 天气服务

### 介绍
Weather Service Kit（天气服务）是鸿蒙生态下的一个数据提供服务， 
Weather Service Kit融合了多家气象行业TOPs供应商，提供专业、精准、稳定的超本地化天气数据服务，
开发者可以通过Weather Service Kit提供的开放能力获取天气数据。

### 工程目录
```
├──entry/src/main/ets/
│  ├──entryability
│  │  ├──EntryAbility.ts    // 本地启动ability
│  └──pages
│     └── Index.ets          // 获取天气界面
└──entry/src/main/resources            // 应用静态资源目录
```

### 具体实现
调用Weather Service Kit获取天气数据
```ts
// 导入天气服务模块
import { weatherService } from '@kit.WeatherServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 建天气请求
let weatherRequest: weatherService.WeatherRequest = {
  location: {
    latitude: 0,
    longitude: 0
  },
  limitedDatasets: [
    weatherService.Dataset.CURRENT, weatherService.Dataset.DAILY, weatherService.Dataset.HOURLY,
    weatherService.Dataset.MINUTE, weatherService.Dataset.ALERTS, weatherService.Dataset.INDICES,
    weatherService.Dataset.TIDES
  ]
};

// 调用getWeather方法执行查询请求，并处理返回结果
try {
  let weather: weatherService.Weather = await weatherService.getWeather(weatherRequest);
  hilog.info(0x0000, 'testTag', `Success to get weather: ${JSON.stringify(weather)}`);
} catch (err) {
  let businessError: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag',
    `Failed to get weather. Code: ${businessError.code}, message: ${businessError.message}`);
}
```

### 相关权限
需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)网站上开通天气服务权限 ，并


---
## web-application-jump
源码: https://gitcode.com/HarmonyOS_Samples/web-application-jump

# 基于应用拉起相关能力实现Web跳转功能

## 介绍

本示例基于应用拉起相关能力，实现了Web页面与ArkTS页面的相互拉起、从Web页面拉起各类应用、以及拉起应用市场详情页等场景。

## 效果预览
手机运行效果图如下：

![](./screenshots/device/phone.png)

## 使用说明
1. 点击“跳转到原生页面”可从 ArkTS 页面经由 Navigation 跳转到其他 ArkTS 页面
2. 点击“跳转到Web 页面”可从 ArkTS 页面跳转到 Web 页面
3. 点击“拉起三方应用”可拉起安装的 PulledUpApplication 应用
4. 点击“拉起系统应用”可拉起系统设置
5. 点击“跳转到市场详情页”可拉起应用市场对应应用的详情页
6. 点击“拉起其他设备的该应用”可在其他设备已安装应用的前提下，拉起互联设备的对应应用

## 工程目录结构

```
├──entry/src/main/ets                                   // 代码区
│  ├──common
│  |  ├──Logger.ets                                     // 日志工具类
│  |  └──Constants.ets                                  // 常量
│  ├──entryability
│  |  └──EntryAbility.ets
│  ├──entrybackupability
│  |  └──EntryBackupAbility.ets
│  └──pages
│     ├──Index.ets                                      // 入口界面
│     └──OriginPage.ets                                 // 原生页面
└──entry/src/main/resources                             // 应用资源目录
```

## 具体实现

从Web页面拉起原生页面需要在Web组件的onLoadIntercept拦截器拦截页面加载，并使用Navigation提供的组件路由能力跳转到原生的页面。

从Web页面拉起另外的Web页面，只需要在前端侧使用a标签配置href属性，即可实现从Web页面跳转到其他的Web页面。

从Web页面拉起三方应用，首先同样需要在Web组件的onLoadIntercept中进行拦截，然后执行自定义的拉起逻辑，在拉起之前，需要首先对三方应用进行配置，配置三方应用的module.json5文件中的exported属性为true，同时需要在skills属性中配置entities与actions。最后在拉起方应用内使用隐式拉起的方式，配置Want类型的配置参数，其中action配置为之前在被拉起方中的actions，同时配置entities属性也为被拉起方中的entities，最后使用startAbility进行拉起。即可在不指定bundleName的情况下拉起应用。在本项目中，您需要先安装配套的dependence目录下的PulledUpApplication应用，避免拉起三方应用时拉起失败，也可以在下载本项目后自行配置拉起参数，从而拉起其他的三方应用。

从Web页面拉起系统应用，同样的要在onLoadIntercept中进行拦


---
## web-get-camer-image
> 本示例介绍如何在HTML页面中拉起原生相机进行拍照，并获取返回的图片。

源码: https://gitcode.com/HarmonyOS_Samples/web-get-camer-image

# 基于Web组件拉起相机进行拍照

### 介绍

本示例主要介绍在HTML页面中如何实现把相机拉起并进行拍照，并可以获取返回的照片。

### 效果预览

![Index](screenshot/device/pic.png)

##### 使用说明

1. 点击HTML页面中的相机按钮，拉起原生相机进行拍照。
2. 完成拍照后，将图片在HTML的img标签中显示。

### 工程目录

```

├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets            // 程序入口类
│  └──pages
│     └──Index.ets                   // 应用首页
└──entry/src/main/resources          // 应用静态资源目录
```

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## web-interceptor
> ArkWeb提供了多种网络请求拦截相关能力，本示例基于onLoadIntercept()、onInterceptRequest()和WebSchemeHandler，实现了页面重定向、链接白名单配置、本地资源替换、自定义资源加载策略和配置公共请求头等典型开发场景。

源码: https://gitcode.com/HarmonyOS_Samples/web-interceptor

# 实现基于Web组件的请求拦截功能

## 项目简介

本实例基于onLoadIntercept()接口、onInterceptRequest()接口和WebSchemeHandler请求拦截器实现了Web组件的请求拦截功能，
并结合请求重定向、页面白名单配置、本地资源替换、自定义资源加载策略和配置公共请求头等典型实践场景给出实际应用案例，
帮助开发者更好地掌握Web组件请求拦截功能的选择和使用。

## 效果预览

|                | 请求重定向                                            | 页面白名单配置                                              | 本地资源替换                                               | 自定义资源加载策略                                            | 配置公共请求头                                       |
|----------------|--------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|-----------------------------------------------|
| 配置url          | ![image](screenshots/device/RedirectRequest.png) | ![image](screenshots/device/PageWhitelist.png)       | ![image](screenshots/device/LocalResource.png)       | ![image](screenshots/device/CustomLoading.png)       | ![image](screenshots/device/CommonHeader.png) |
| 加载Web页面        | ![image](screenshots/device/RedirectRequestResult.png) | ![image](screenshots/device/PageWhitelistResult.png) | ![image](screenshots/device/LocalResourceResult.png) | ![image](screenshots/device/CustomLoadingResult.png) | ![image](screenshots/device/CommonHeaderResult.png) |

## 安装说明

为清晰地展示配置公共请求头场景下的响应信息，本示例搭建了一个本地服务端。将原始请求添加公共请求头后，转发到本地服务端，本地服务端会将该请求的请求头信息作为响应，返回给客户端。开发者可参考如下步骤启动本地服务端。

1. 搭建Node.js环境：本示例的服务端是基于No


---
## web-pdfviewer
> 本示例通过Web组件实现预览本地PDF文件和预览网络PDF文件。

源码: https://gitcode.com/HarmonyOS_Samples/web-pdfviewer

# 基于Web组件实现预览PDF文件功能

### 介绍

本示例通过Web组件实现预览本地PDF文件和预览网络PDF文件，Tabs容器组件包含了两个独立的TabContent子组件，分别标示为预览本地PDF文件和预览网络PDF文件。每个子组件内部构建一个Web组件。第一个Web组件利用resource协议关联本地PDF文件路径以预览本地存储的PDF资源；第二个Web组件则通过配置网络链接属性，实现从互联网加载并预览远程PDF文件内容。

### 效果预览

![](screenshots/device/WebPDFViewer.gif)


##### 使用说明

- 运行代码前,需要把[CommonConstants.ets](entry/src/main/ets/constants/CommonConstants.ets)文件中的REMOTE_URL替换成网络PDF文件地址。
- 进入页面默认预览本地PDF文件，点击预览网络PDF文件按钮可以切换到预览网络PDF文件模块。

### 工程目录

```
├──entry/src/main/ets/
│  ├──constants
│  │  └──CommonConstants.ets         // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets            // 程序入口类
│  ├──pages
│  │  └──Index.ets                   // 应用首页
│  └──utils
│     └──Logger.ets                  // 日志类
└──entry/src/main/resources          // 应用静态资源目录
```

### 具体实现

1. 本地PDF加载:通过resource协议（需在工程resources/rawfile 目录下添加PDF文件,通过RESOURCE_URL获取的PDF文件）来实现本地PDF文件资源的装载与呈现，在无需网络连接的情况下，也能顺利加载并预览用户本地PDF资源。
2. 网络PDF加载:通过设置网络链接属性，能够对接互联网上的PDF文件资源。提供有效的远程PDF文件URL（REMOTE_URL），实现云端PDF资源的加载与预览。

### 相关权限

- 允许应用使用Internet网络权限：ohos.permission.INTERNET。

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## web-pre-render
> 本示例使用预渲染实现了Web页面的瞬开效果。

源码: https://gitcode.com/HarmonyOS_Samples/web-pre-render

# 基于预渲染技术实现Web页面瞬开效果

### 介绍

本示例基于预渲染技术，实现了点击后Web页面瞬间打开的效果，无需额外加载过程，减少用户等待时长，提高了用户体验。

### 效果预览
|                               web                               |
|:--------------------------------------------------------------:|
| <img src="./screenshots/device/phone.png" width="320"/> |

使用说明：
1. 点击标签打开弹窗，加载Web网页。

### 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  └──Constants.ets                  // 公共常量类
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  └──pages              
│     ├──Index.ets                      // 首页
│     └──WebPage.ets                    // Web预渲染页面
└──entry/src/main/resources             // 应用静态资源目录
```

### 具体实现

1. 创建Web组件。
2. 在EntryAbility中预渲染网页，首页打开弹窗实现瞬开效果。

### 相关权限
ohos.permission.INTERNET

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。 

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## web-scroller
> 本篇在Scroll滚动组件中嵌套了一个Web组件，通过nestedScroll进行滚动拦截，实现了一个文章详情展示案例。

源码: https://gitcode.com/HarmonyOS_Samples/web-scroller

# 实现Web组件嵌套滑动功能

## 简介
本示例基于组件通用的onScrollFrameBegin()滚动开始的注册回调以及设置滚动模式，实现了父组件滚动后Web组件再进行滚动、Web组件全量展开滑动、多容器嵌套滚动等功能，为用户滚动浏览网页内容提供了更加精确有效的操作逻辑支撑。

## 效果预览
手机运行效果图如下：

![image](screenshots/device/phone.gif)
## 工程目录

```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets               // 程序入口类
│  ├──pages                  
│  │  ├──NestedScrolling.ets            // 父组件滚动后Web组件再进行滚动
│  │  ├──FullExpansion.ets              // Web组件全量展开滑动
│  │  ├──WebNestedTabs.ets              // 多容器嵌套滚动
│  │  └──Index.ets                      // 首页
│  ├──view                  
│  │  └──StandardButtonList.ets         // 封装首页功能区
│  └──viewmodel                  
│     └──MenuViewModel.ets              // 菜单栏数据
└──entry/src/main/resource              // 应用静态资源目录

```
## 使用说明
- 点击第一个按钮进入页面后滑动屏幕，容器页面会先滚动并调整顶部原生Image组件的尺寸，当Image组件高度达到阈值后会固定在顶部，后续滚动表现为Web页面滚动。
- 点击第二个按钮进入页面后滑动屏幕，Web组件会以原始高度展开，实现跟随滑动。
- 点击第三个按钮进入页面后，若滑动顶部组件，只有顶部Web页面会滚动，若滑动底部组件，整个容器会跟随滚动至顶部组件不可见。

## 具体实现
- 父组件滚动后Web组件再进行滚动：依赖onScrollFrameBegin()控制元素尺寸与嵌套滚动效果。
- Web组件全量展开滑动：依靠renderMode为RenderMode.SYNC_RENDER，保持Web组件同步渲染，使得父容器尺寸大小适应Web组件。
- 多容器嵌套滚动：设置滚动模式，向下滚动时优先父组件滚动，向上滚动时优先自身滚动。

## 相关权限
- ohos.permission.INTERNET：网络请求权限用于访问网络页面

## 约束与限制
1. 本示例仅支持标准系统上运行，支持设备：华为手机。
2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。
3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## web-user-agent
> 本示例基于ArkTS和Web组件实现了User Agent的设置和获取功能。

源码: https://gitcode.com/HarmonyOS_Samples/web-user-agent

# 基于Web组件实现设置和获取用户代理的功能

### 介绍

本示例基于ArkTS和Web组件实现了User Agent（用户代理）的设置和获取功能。帮助开发者在Web开发中掌握获取默认用户默认代理信息，设置、获取自定义用户代理等功能的开发实现方案。

### 效果预览
![](screenshots/devices/webuseragent.png)

### 工程目录
```

├──entry/src/main/ets                              
│  ├──entryability  
│  │  └──EntryAbility.ets          // 程序入口
│  ├──pages                                     
│  │  └──Index.ets                 // 首页
│  └──utils
│     └──Logger.ets                // 日志        
└──entry/src/main/resources        // 应用资源目录
   └──rawfile                     
      └──Index.html                // html页面
```

### 使用说明
1. 点击设置用户代理按钮，可以进行设置代理操作。
2. 点击获取用户代理按钮，“自定义用户代理：”位置将会显示之前设置的信息。
3. 点击获取默认用户代理按钮，可以获取默认用户代理信息。
4. 点击刷新按钮，上部的web页面将会刷新重新展示最新的用户代理信息。

### 相关概念
- getUserAgent: 获取当前默认用户代理。
- setCustomUserAgent: 设置自定义用户代理，会覆盖系统的用户代理。。
- getCustomUserAgent: 获取自定义用户代理。

### 相关权限

网络使用权限：ohos.permission.INTERNET

### 依赖

不涉及

### 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## window-pip
> 本示例通过@kit.ArkUI、@kit.MediaKit等接口，实现了视频播放、手动和自动拉起画中画、画中画窗口控制视频播放和暂停等功能。

源码: https://gitcode.com/HarmonyOS_Samples/window-pip

# 实现画中画效果

## 介绍

本示例基于媒体服务和ArkUI的基本能力，实现视频播放、手动和自动拉起画中画、画中画窗口控制视频播放和暂停等功能。

## 效果预览
| 首页                                                        | 视频播放页                                                 | 画中画                                                           |
|--------------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------------------|
| <img src='screenshots/devices/home_cn.png' width=320> | <img src='screenshots/devices/pip1_cn.png' width=320> | <img src='screenshots/devices/pip2_cn.png' width=320> |

## 使用说明

1. 在主界面，可以**点击对应视频按钮**进入**视频播放页面**；
2. 视频播放页面**点击开启**，应用**拉起画中画**，点击**关闭**，**关闭画中画**；
3. 视频播放页面**点击自动开启画中画**，在返回桌面时会**自动拉起画中画**；
4. 视频播放页面会显示一些**回调信息**。

## 工程目录

```
├──entry/src/main/ets                        // 代码区
│  ├──constants
│  │  └──Constants.ets                       // 常量类
│  ├──entryability
│  │  └──EntryAbility.ets       
│  ├──pages
│  │  ├──AVPlayer.ets                        // 视频播放
│  │  ├──VideoPlay.ets                       // 视频播放页面
│  │  └──WindowPiP.ets                       // 首页
│  └──utils
│     └──Logger.ets                          // 日志工具类
└──entry/src/main/resources                  // 应用资源目录
```


## 具体实现

- 整个示例用**Navigation**构建页面，主页面放置五个可点击视频框，点击之后进入视频播放页面。
- 进入视频播放页面后，有三块区域，最上方的**XComponent**，中间的**画中画控制按钮**以及下方的**回调信息显示框**。
- 点击**开启**后，应用手动拉起画中画，视频在画中画播放，返回桌面视频依旧画中画播放；点击**关闭**后，画中画播放的视频返回**XComponent**播放，同时返回桌面不会拉起画中画。
- 


---
## wlan-info-query
> 本示例基于wifiManager接口，实现WLAN信息的查询。

源码: https://gitcode.com/HarmonyOS_Samples/wlan-info-query

# 基于短距通信服务实现WLAN信息查询功能

## 介绍

本示例基于短距通信服务，实现WLAN信息的查询功能。帮助开发者在WLAN无线网络相关场景开发中，掌握WLAN开关查询，WLAN状态查询、监听等功能的实现方案。

## 效果预览

|                  首页                  |                  详情页                  |
|:------------------------------------:|:-------------------------------------:|
| ![](./screenshots/device/index.png) | ![](./screenshots/device/detail.png) |

## 使用说明

1. 启动应用，若启动WLAN且已连接，显示已连接WLAN及附近可用WLAN（注：可用WLAN查询结果可能为空，设置定时10秒重复查询）。
2. 点击已连接WLAN右侧icon，显示WLAN详情页（注：非系统应用获取到的MAC地址为随机地址）。
3. 可用WLAN列表仅作展示查询能力，无交互动作。

## 工程目录
```
├──entry/src/main/ets               
│  ├──common
│  │  ├──constants.ets             // 常量类
│  │  └──utils                     // 工具函数               
│  ├──entryability  
│  │  └──EntryAbility.ets          // 程序入口
│  ├──pages                                     
│  │  └──Index.ets                 // 首页
│  └──view
│     ├──DetailInfoView.ets        // WLAN详情页
│     ├──InfoItemView.ets          // WLAN详情项
│     └──WlanItemView.ets          // WLAN列表项
└──entry/src/main/resources        // 应用资源目录
```

## 具体实现

1. 使用wifiManager.getLinkedInfo获取已连接的WLAN信息。
2. 使用wifiManager.getScanInfoList获取附近可用WLAN信息。
3. 使用wifiManager.getIpInfo获取子网掩码、网关等信息。

## 相关权限

ohos.permission.GET_WIFI_INFO：允许应用获取Wi-Fi信息

## 约束与限制

1. 本示例仅支持标准系统上运行，支持设备：华为手机。

2. HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3. DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4. HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。


---
## xcomponent-vsync
> XComponent提供了应用在native侧调用OpenGLES图形接口的能力，本文主要介绍如何配合Vsync事件，完成自定义动画。在这种实现方式下，自定义动画的绘制不在UI主线程中完成，即使主线程卡顿，动画效果也不会受影响。

源码: https://gitcode.com/HarmonyOS_Samples/xcomponent-vsync

# 基于XComponent技术实现自定义动画功能

### 介绍
XComponent提供了应用在native侧调用OpenGLES图形接口的能力，本文主要介绍如何配合Vsync事件，完成自定义动画。在这种实现方式下，自定义动画的绘制不在UI主线程中完成，即使主线程卡顿，动画效果也不会受影响。

### 效果演示

![](screenshots/device/XComponentVsync.gif)

### 实现思路
1. CMakeLists文件中增加lib依赖
2. 创建Vsync实例
3. 创建OH_NativeVSync_RequestFrame回调，并在回调中使用egl接口进行绘制

### 高性能知识点

- 一个 Vsync 实例对应一个EventRunner创建的新线程，在这个线程中执行渲染处理，理论上这个线程的运算耗时，只会影响动画帧率，不会影响应用主线程的帧率。
- 其余OpenGLES的绘制方法，与社区的OpenGLES的用法一致。
### 工程结构&模块类型

```
├──entry/src/main
│  ├──cpp                           // C++ 代码区
│  │  ├──common                     // 常量定义文件
│  │  │  ├──native_common.h
│  │  │  └──plugin_common.h         
│  │  ├──manager                    // 生命周期管理模块
│  │  │  ├──plugin_manager.cpp
│  │  │  └──plugin_manager.h
│  │  ├──render                     // 渲染模块
│  │  │  ├──egl_core_shader.cpp
│  │  │  ├──egl_core_shader.h
│  │  │  ├──plugin_render.cpp
│  │  │  └──plugin_render.h
│  │  ├──types
│  │  │  └──libentry                // C++接口导出
│  │  │     ├──index.d.ts                        
│  │  │     └──oh-package.josn5                 
│  │  ├──CMakeLists.txt             // CMake配置文件
│  │  └──napi_init.cpp              // Native模块注册
│  └──ets                           // ets 代码区
│     ├──constants
│     │  └──CommonConstants.ets     // 常量定义文件  
│     ├──entryability
│     │  └──EntryAbility.ets       
│     └──pages
│        └──Index.ets               // 主页界面
└──entry/src/main/resources         // 应用资源目录
```

### 模块依赖

**不涉及**

### 参考资料

1. XComponent。 
2. Vsync。


---
## xengine-samplecode-NNGI-demo-cpp
> 本示例利用基于神经网络的全局光照算法（NNGI），通过AI和光线追踪技术，实现少量光线即可实现全局光照效果。

源码: https://gitcode.com/HarmonyOS_Samples/xengine-samplecode-NNGI-demo-cpp

# xengine-samplecode-NNGI-demo-cpp

本示例利用基于神经网络的全局光照算法（NNGI），通过AI和光线追踪技术，实现少量光线即可实现全局光照效果。


---
## xengine-samplecode-RTDDGI-demo-cpp
> 本示例利用硬件光线追踪能力，基于动态漫反射全局光照算法，实时渲染全场景高质量动态全局光照。

源码: https://gitcode.com/HarmonyOS_Samples/xengine-samplecode-RTDDGI-demo-cpp

# xengine-samplecode-RTDDGI-demo-cpp

本示例利用硬件光线追踪能力，基于动态漫反射全局光照算法，实时渲染全场景高质量动态全局光照。


---
## xengine-samplecode-RTVisibleMask-Reflection-demo-cpp
> 本示例建立一个利用XEngine光线追踪API，实现实时渲染高质量反射（Reflection）效果的应用程序。

源码: https://gitcode.com/HarmonyOS_Samples/xengine-samplecode-RTVisibleMask-Reflection-demo-cpp

# xengine-samplecode-RTVisibleMask-Reflection-demo-cpp

本示例建立一个利用XEngine光线追踪API，实现实时渲染高质量反射（Reflection）效果的应用程序。


---
## xengine-samplecode-gles-demo-cpp
> 本示例基于XEngine加速引擎接口，实现图像超分和自适应VRS的功能。

源码: https://gitcode.com/HarmonyOS_Samples/xengine-samplecode-gles-demo-cpp

# 基于GPU加速引擎服务实现超分和自适应VRS(OpenGL ES)

## 简介

本篇Codelab主要介绍如何使用XEngine空域GPU超分API、空域AI超分API进行纹理的超分以及使用XEngine自适应可变速率着色API修改着色率。示例代码通过XComponent组件调用NAPI创建EGL/OpenGL ES环境，实现绘制SPONZA场景，并展示XEngine特性的使用。本篇CodeLab使用Native C++模板创建。

## 效果预览

如图所示，XComponent组件绘制SPONZA场景，点击超分下拉选择菜单，切换超分模式，点击勾选框选择是否开启自适应可变速率着色

![XEngine Spatial Upscale](screenshots/device/XEngine_GLES_Spatial_Upscale_Example.jpg)

## 相关概念

- [EGL(Embedded Graphic Library)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/egl)：EGL 是Khronos渲染API (如OpenGL ES 或 OpenVG) 与底层原生窗口系统之间的接口。
- [XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)：可用于EGL/OpenGL ES和媒体数据写入，并显示在XComponent组件。

## 使用说明

1. 运行示例代码。
2. 点击下拉选择菜单，在no upscale（不使用超分）、neural upscale（空域AI超分）、spatial upscale（空域GPU超分）、fsr upscale（FSR1.0超分）四种模式间进行切换。
3. 点击勾选框，可以开启/关闭自适应可变速率着色。

## 工程目录
```
├── entry/src/main	         // 代码区
│  ├── cpp
│  │  ├── types
│  │  │  ├── libnativerender
             └── index.d.ts      // native层接口注册文件
│  │  │── napi_init.cpp          // native api层接口的具体实现函数
│  │  │── CMakeLists.txt         // native层编译配置
│  │  │── 3rdParty               // 三方件
│  │  │── common                 // 通用接口
│  │  │── model                  // 模型
│  │  │── file                   // 文件管理
│  │  │── libs                   // 三方动态库
│  │  │── manager                // native&arkts交互
│  │  │── render                 // 渲染
│  │  │── shader                 // 渲染shader
│  ├── ets
│  │  ├── entryabil


---
## xengine-samplecode-subpass-shading-demo-cpp
> 本示例通过使用Subpass Shading特性，实现降低DDR带宽的功能

源码: https://gitcode.com/HarmonyOS_Samples/xengine-samplecode-subpass-shading-demo-cpp

# 基于Subpass Shading特性优化Forward+管线带宽

## 简介

本篇Codelab主要介绍如何使用Subpass Shading。示例代码通过XComponent组件调用NAPI创建Vulkan环境，实现绘制SPONZA场景，并展示Subpass Shading特性的使用。本篇CodeLab使用Native C++模板创建。

## 效果预览

如图所示，XComponent组件绘制SPONZA场景。

![Subpass_Shading_VULKAN_Example.jpg](screenshots/device/Subpass_Shading_VULKAN_Example.jpg)

## 相关概念

- [XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)：可用于EGL/OpenGLES和媒体数据写入，并显示在XComponent组件。

## 使用说明

1. 运行示例代码。

## 工程目录
```
├── entry/src/main	             // 代码区
│  ├── cpp
│  │  ├── types
│  │  │  ├── libnativerender
             └── index.d.ts      // native层接口注册文件 
│  │  │── napi_init.cpp          // native api层接口的具体实现函数
│  │  │── CMakeLists.txt         // native层编译配置
│  │  │── 3rdParty               // 三方件
│  │  │── common                 // 通用接口  
│  │  │── file                   // 文件管理
│  │  │── libs                   // 三方动态库
│  │  │── manager                // native&arkts交互
│  │  │── render                 // 渲染
│  ├── ets
│  │  ├── entryability 
             └── EntryAbility.ts // 程序入口类
│  │  ├── pages 
             └── index.ets       // 主界面展示类
│  ├── resources                 // 资源文件目录
│  │  ├── base
│  │  │  ├── media
             └── icon.png        // 图片资源
│  │  ├── rawfile
│  │  │  ├── forward_plus        // forward plus shader文件
│  │  │  ├── sponza_full         // 模型文件
│  │  │  ├── subpass_shading     // subpass shading shader文件
```

## 具体实现
本示例展示的功能使用了Vulkan扩展接口[VK_HUAWEI_subpass_


---
## xengine-samplecode-vulkan-demo-cpp
> 本示例基于XEngine加速引擎接口，实现图像超分和自适应VRS的功能。

源码: https://gitcode.com/HarmonyOS_Samples/xengine-samplecode-vulkan-demo-cpp

# 基于GPU加速引擎服务实现超分和自适应VRS(Vulkan)

## 简介

本篇Codelab主要介绍如何使用XEngine空域GPU超分API进行纹理的超分以及开启自适应可变速率着色，通过XComponent组件创建Vulkan环境，实现绘制SPONZA场景。本篇CodeLab使用Native C++模板创建。

## 效果预览

如图所示，XComponent组件绘制SPONZA场景，点击超分下拉选择菜单，切换超分模式，点击勾选框选择是否开启自适应可变速率着色

![XEngine Spatial Upscale](screenshots/device/XEngine_VULKAN_Spatial_Upscale_Example.jpg)

## 相关概念
- [XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)：可用于媒体数据写入，并显示在XComponent组件。

## 使用说明

1. 运行示例代码。
2. 点击下拉选择菜单，在no upscale（不使用超分）、spatial upscale（空域GPU超分）、fsr upscale（FSR1.0超分）三种模式间进行切换。
3. 点击勾选框，可以开启/关闭自适应可变速率着色。

## 工程目录
```
├──entry/src/main	         	// 代码区
│  ├──cpp
│  │  ├──types
│  │  │  └──libnativerender
│  │  │    	└──index.d.ts      	// native层接口注册文件
│  │  ├──napi_init.cpp          // native api层接口的具体实现函数
│  │  ├──CMakeLists.txt         // native层编译配置
│  │  ├──3rdParty               // 三方件
│  │  ├──common                 // 通用接口
│  │  ├──file                   // 文件管理
│  │  ├──libs                   // 三方动态库
│  │  ├──manager                // native&arkts交互
│  │  ├──render                 // 渲染
│  │  └──vulkanbase             // vulkan基础能力封装
│  ├──ets
│  │  ├──entryability
│  │  │  └──EntryAbility.ts 	// 程序入口类
│  │  ├──pages
│  │  │  └──index.ets       	// 主界面展示类
│  └──resources                 // 资源文件目录
│     ├──base
│     │  └──media
│     │     └──icon.png        	// 图片资源
│     └──rawfile
│        └──Sponza
│           └──sponza.obj     	// 模型资源
```

## 具体实现
本示例展示的功能使用


---
## xengine-samplecode-vulkan-temporal-upscale-demo-cpp
> 本示例基于XEngine加速引擎接口，实现图像超分的功能。

源码: https://gitcode.com/HarmonyOS_Samples/xengine-samplecode-vulkan-temporal-upscale-demo-cpp

# 基于时域AI超分(Vulkan)增强图像渲染质量

## 简介

本篇Codelab主要介绍如何使用XEngine空域GPU超分API、时域AI超分API进行纹理的超分以及开启自适应可变速率着色，通过XComponent组件创建Vulkan环境，实现绘制SPONZA场景。本篇CodeLab使用Native C++模板创建。

## 效果预览

如图所示，XComponent组件绘制SPONZA场景，点击超分下拉选择菜单，切换超分模式，点击勾选框选择是否开启自适应可变速率着色

![XEngine Temporal Upscale](screenshots/device/XEngine_VULKAN_Temporal_Upscale_Example.png)

## 相关概念
- [XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)：可用于媒体数据写入，并显示在XComponent组件。

## 使用说明

1. 运行示例代码。
2. 点击下拉选择菜单，在no upscale（不使用超分）、spatial upscale（空域GPU超分）、fsr upscale（FSR1.0超分）、temporal upscale（时域AI超分）四种模式间进行切换。
3. 点击勾选框，可以开启/关闭自适应可变速率着色。

## 工程目录
```
├──entry/src/main	         			// 代码区
│  ├──cpp
│  │  ├──types
│  │  │  └──libnativerender
│  │  │    	└──index.d.ts      			// native层接口注册文件
│  │  ├──napi_init.cpp                  // native api层接口的具体实现函数
│  │  ├──CMakeLists.txt                 // native层编译配置
│  │  ├──3rdParty                       // 三方件
│  │  ├──common                         // 通用接口
│  │  ├──file                           // 文件管理
│  │  ├──libs                           // 三方动态库
│  │  ├──manager                        // ArkTs与native接口绑定
│  │  ├──render                         // 渲染
│  │  └──vulkanbase                     // vulkan基础能力封装
│  ├──ets
│  │  ├──common
│  │  │  └──CommonConstants.ets         // 通用常量
│  │  ├──entryability
│  │  │  └──EntryAbility.ts  	        // 程序入口类
│  │  ├──pages
│  │  │  └──index.ets       	        // 主界面展示类
│  └──resources       


---
## zip-lib
> 本示例通过@ohos.zlib和@ohos.fileio接口，实现添加文件、解压和压缩文件场景。

源码: https://gitcode.com/HarmonyOS_Samples/zip-lib

# 实现解压和压缩功能

### 介绍

本示例通过@ohos.zlib和@ohos.fileio接口，实现添加文件、解压和压缩文件功能，便于用户进行常见的文件解压操作。

### 效果预览

| 主页                               | 新建弹窗                               |
|----------------------------------|------------------------------------|
| ![](screenshots/device/main.png) | ![](screenshots/device/create.png) |

使用说明

1.点击屏幕右上角 **+** 按钮，弹出创建文件窗口；

2.输入文件名称、文件内容，并点击 **确定** 按钮来创建文件；

3.文件创建成功后，文件名称自动追加.txt后缀并在主页面列表会显示，同时文件的物理地址为/data/app/el2/100/base/ohos.samples.ziplib/haps/entry/files/，点击 **压缩** 按钮，提示“文件压缩成功”，并会在文件列表创建一个相同名称的.zip文件；

4.点击压缩文件后的 **解压** 按钮，提示“文件解压成功”，并会再次在文件列表创建一个同名文件夹。

### 工程目录

```
├──entry/src/main/ets/
│  ├──common
│  │  └──AddDialog.ets                    // 弹窗组件
│  ├──entryability
│  │  └──EntryAbility.ets                 // 程序入口文件
│  ├──model
│  │  ├──DataSource.ets                   // 懒加载文件
│  │  └──Logger.ets                       // 日志文件
│  └──pages
│     └──Index.ets                        // 首页，接口都在这里调用
└──entry/src/main/resources               // 应用静态资源目录
``` 

### 具体实现

* 添加文件、解压和压缩文件的接口都在首页调用，源码参考[Index.ets](entry/src/main/ets/pages/Index.ets)
  * 添加文件：通过调用fileio.openSync()创建文件并调用fileio.writeSync()向文件中写入内容；
  * 压缩文件：通过调用zlib.zipFile()压缩文件；
  * 解压文件：通过zlib.unzipFile解压文件。

### 相关权限

不涉及。

### 依赖

不涉及。

### 约束与限制

1.本示例仅支持标准系统上运行，支持设备：华为手机。

2.HarmonyOS系统：HarmonyOS 5.0.5 Release及以上。

3.DevEco Studio版本：DevEco Studio 5.0.5 Release及以上。

4.HarmonyOS SDK版本：HarmonyOS 5.0.5 Release SDK及以上。



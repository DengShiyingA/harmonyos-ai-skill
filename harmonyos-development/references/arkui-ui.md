# ArkUI Components, Layout, and Interaction Patterns

## Contents
- ArkUI — declarative UI
- Custom component basics
- Component lifecycle callbacks
- Layout containers
- Performance-critical patterns
- Animation
- Tabs — bottom/top navigation
- Swiper — carousel / banner
- WaterFlow — Pinterest-style layout
- Grid — fixed grid layout
- TextInput / TextArea
- AlertDialog / Toast
- Common form components — quick reference
- HarmonyOS 6.0 visual effects (沉浸光感视效 / 液态玻璃)
- Builders, styles, extends
- sys.symbol — icon glyph system
- Multi-device / foldable screen adaptation (API 21)
- Breakpoint detection
- Container breakpoints with `ContainerReader` (API 26 Release)
- Foldable screen — listen for fold/unfold events
- Responsive layout switching (if/else, not .visibility)
- `GridRow`/`GridCol` does not support `LazyForEach`
- Share breakpoint via `@Provide`/`@Consume`
- Global `@Reusable` / `@ReusableV2` pools (API 26 Release)
- UIDesignKit — icon processing & HdsNavigation
- `hdsDrawable` — icon adaptive processing
- `HdsNavigation` — system-style navigation component
- Custom dialog — openCustomDialog & openBindSheet
- openCustomDialog (general-purpose modal/non-modal)
- openBindSheet (bottom half-modal sheet)
- bindContentCover (full-screen modal overlay)
- Keyboard layout adaptation (软键盘适配)
- Set keyboard avoidance mode (in UIAbility)
- Prevent a component from moving with keyboard
- Monitor keyboard height
- Focus control
- Dark mode adaptation (深色模式适配)
- Resource qualifier approach (recommended)
- Detect & react to color mode changes
- Programmatic mode switching
- Custom font (自定义字体)
- Screen orientation (横竖屏切换)
- Clipboard — pasteboard read/write
- Gesture conflict resolution (手势冲突处理)
- hitTestBehavior — control touch event response
- Gesture binding priority
- GestureGroup modes
- Immersive window (沉浸式/全屏/避让区)
- Extend component into status bar & navigation bar
- Get safe area dimensions for manual padding
- Hide/show system bars
- Status bar text color (light/dark content)
- Common list operations (列表常用操作)
- Swipe-to-delete (left swipe action)
- Drag reorder
- Pull-down refresh
- Scroll to bottom (chat-style)
- Keep scroll position on data insert (LazyForEach)
- ListItemGroup + sticky header (grouped list)
- onReachEnd — load more data

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `ArkUI component, layout, animation, Navigation UI, Tabs, Swiper, Grid, List, dialog, keyboard, dark mode, gesture, immersive window`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

## ArkUI — declarative UI


### Custom component basics

```ts
@Entry                      // marks route/page entry
@Component
struct Index {
  @State count: number = 0;

  build() {
    Column({ space: 12 }) {
      Text(`Count: ${this.count}`)
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
      Button('Increment')
        .onClick(() => { this.count++; })
    }
    .width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```


### Component lifecycle callbacks

**All `@Component`:**

| Callback | When | Notes |
|---|---|---|
| `aboutToAppear()` | After created, BEFORE `build()` | Can change state here; changes apply in first `build()` |
| `onDidBuild()` | After `build()` completes | Do NOT change state or call `animateTo()`. API 12+ |
| `aboutToDisappear()` | Before destruction | Do NOT change state (especially `@Link`). No async/await |
| `aboutToReuse(params)` | Reusable component re-added from cache | Update state with new params. API 10+ |
| `aboutToRecycle()` | Component moving to reuse cache | Release heavy resources. API 10+ |

**Only `@Entry`:**

| Callback | When |
|---|---|
| `onPageShow()` | Each time page is displayed |
| `onPageHide()` | Each time page is hidden |
| `onBackPress(): boolean` | User taps Back. Return `true` to override default |

**Execution order (cold start):**
`Parent aboutToAppear → Parent build → Parent onDidBuild → Child aboutToAppear → Child build → Child onDidBuild → onPageShow`


### Layout containers

| Container | When to use | Performance |
|---|---|---|
| `Column` / `Row` | Linear arrangement | **Best** — single-pass layout |
| `Stack` | Overlapping / stacking | Good |
| `Flex` | Items need stretch/shrink | **Slower** — extra pass for flexGrow/flexShrink |
| `RelativeContainer` | Complex layouts, avoid deep nesting | Good — flat structure |
| `GridRow` / `GridCol` | Responsive multi-device grids | Good |
| `List` | Scrollable list with recycling | Best for long lists (with `LazyForEach`) |

**Column/Row alignment:**
- Main axis: `justifyContent(FlexAlign.Start | .Center | .End | .SpaceBetween | .SpaceAround | .SpaceEvenly)`
- Cross axis: Column → `alignItems(HorizontalAlign.Start | .Center | .End)`, Row → `alignItems(VerticalAlign.Top | .Center | .Bottom)`

**Stack:** `alignContent` takes 9 positions (TopStart, Top, TopEnd, Start, Center, End, BottomStart, Bottom, BottomEnd). `zIndex` controls layer order.

**Flex vs Column/Row:** Flex requires re-layout for `flexShrink`/`flexGrow`. Always prefer `Column`/`Row` when you don't need flex behavior.

**RelativeContainer:** Use `__container__` as anchor ID for the container itself. Each child needs `.id()`. Set `.alignRules({ top: { anchor: 'id', align: VerticalAlign.Bottom } })`.

**Blank():** Fills remaining space in Row/Column — use for "label ... value" layouts: `Row() { Text('Name'); Blank(); Text('Value') }`.

**displayPriority:** Lower-priority children auto-hide when container shrinks. `Row() { A().displayPriority(1); B().displayPriority(3); C().displayPriority(1) }` — A and C hide first.

**layoutWeight:** Proportional sizing — `Row() { Column().layoutWeight(1); Column().layoutWeight(2) }` gives 1:2 ratio.

**AttributeModifier** — reusable style object:
```ts
class PrimaryButtonModifier implements AttributeModifier<ButtonAttribute> {
  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.width('100%').height(48).fontSize(16).fontColor(Color.White).backgroundColor('#007DFF');
  }
  applyPressedAttribute(instance: ButtonAttribute): void {
    instance.backgroundColor('#0056B3');
  }
}
// Usage:
Button('Submit').attributeModifier(new PrimaryButtonModifier())
```


### Performance-critical patterns

**`LazyForEach` for large lists** (only renders visible items):
```ts
class MyDataSource implements IDataSource {
  private data: string[] = []
  totalCount(): number { return this.data.length }
  getData(index: number): string { return this.data[index] }
  registerDataChangeListener(listener: DataChangeListener): void { /* ... */ }
  unregisterDataChangeListener(listener: DataChangeListener): void { /* ... */ }
}

List() {
  LazyForEach(this.dataSource, (item: string, index: number) => {
    ListItem() { Text(item) }
  }, (item: string) => item)  // key generator — MUST produce unique keys
}
.cachedCount(5)  // preload 5 items off-screen
```

**`@Reusable` components** (69% faster component creation):
```ts
@Reusable
@Component
struct MyListItem {
  @State message: Message = new Message('default')

  aboutToReuse(params: Record<string, ESObject>) {
    this.message = params.message as Message
  }
  aboutToRecycle() { /* release heavy resources */ }
  build() { Text(this.message.value) }
}
```
Rules: only works within same parent; don't nest `@Reusable` inside `@Reusable`; combine with `LazyForEach`.

**Global reuse pools (API 26 Release):** `@ComponentV2({ reusePool, poolAccepts })` can let compatible child trees share `@ReusableV2` components across different parents. Release heavy resources in `aboutToRecycle()`, reset transient state before reused content is shown, keep reuse identifiers stable, and profile before accepting the added lifecycle complexity.

Official guide: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-reuse-pool

**Layout performance rules:**
- Max 3 levels of nesting — each level adds layout cost
- Use `if/else` over `.visibility()` — hidden components still participate in layout
- Use `RelativeContainer` to flatten deep Row/Column/Flex hierarchies (documented 26% improvement)
- Set explicit dimensions on `List` inside `Scroll` — without them ALL children load at once
- Avoid `@StorageLink` for frequently-changing data — propagates to all subscribers

**onVisibleAreaChange** — trigger logic when component enters/leaves viewport:
```ts
Image(item.url)
  .onVisibleAreaChange([0.0, 1.0], (isVisible: boolean, currentRatio: number) => {
    if (isVisible && currentRatio >= 1.0) { this.loadHighRes(); }    // fully visible
    if (!isVisible) { this.releaseImage(); }                          // off screen
  })
```
Use cases: lazy image loading, video auto-play/pause on scroll, exposure analytics.


### Animation

**Explicit animation (`animateTo`)** — state changes in closure animate:
```ts
this.getUIContext()?.animateTo({
  duration: 300,
  curve: Curve.EaseOut,
  onFinish: () => { console.info('done') }
}, () => {
  this.width = 200  // this change animates
})
```

**Property animation (`.animation()`)** — implicit, applied to preceding attributes:
```ts
Text('Hello')
  .width(this.myWidth)
  .animation({ duration: 500, curve: Curve.EaseIn })
```

**Curve values:** `Curve.Linear | .Ease | .EaseIn | .EaseOut | .EaseInOut | .FastOutSlowIn | .Friction | .Sharp | .Smooth`

**Spring curves (string):** `'spring(velocity,mass,stiffness,damping)'`, `'springMotion(response,dampingFraction)'`, `'responsiveSpringMotion(response,dampingFraction)'`

**Shared element transition:**
```ts
// Bind same geometryTransition ID on source and target
Image($r('app.media.photo')).geometryTransition('picture')
// Wrap state change in animateTo
this.getUIContext()?.animateTo({ duration: 300 }, () => { this.isExpanded = !this.isExpanded })
```

**Keyframe animation (`keyframeAnimateTo`)** — multi-step sequences:
```ts
this.getUIContext()?.keyframeAnimateTo({ iterations: 2 }, [
  { duration: 100, event: () => { this.translateX = 10; } },
  { duration: 100, event: () => { this.translateX = -10; } },
  { duration: 100, event: () => { this.translateX = 0; } },
]);
```

**Animation performance tips:** Prefer transform properties (`scale`/`translate`/`rotate`/`opacity`) over layout properties (`width`/`height`/`margin`) — transforms skip re-layout.


### Tabs — bottom/top navigation

```ts
@Entry @Component
struct MainPage {
  @State currentIndex: number = 0;

  @Builder tabBuilder(index: number, title: string, icon: Resource) {
    Column() {
      SymbolGlyph(icon).fontSize(24)
        .fontColor([this.currentIndex === index ? '#007DFF' : '#99000000'])
      Text(title).fontSize(10).margin({ top: 4 })
        .fontColor(this.currentIndex === index ? '#007DFF' : '#99000000')
    }.justifyContent(FlexAlign.Center).height('100%').width('100%')
  }

  build() {
    Tabs({ barPosition: BarPosition.End }) {        // BarPosition.Start for top
      TabContent() { HomePage() }
        .tabBar(this.tabBuilder(0, 'Home', $r('sys.symbol.house')))
      TabContent() { MinePage() }
        .tabBar(this.tabBuilder(1, 'Me', $r('sys.symbol.person')))
    }
    .barHeight(56)
    .onChange((index) => { this.currentIndex = index; })
    .scrollable(false)                               // disable swipe between tabs
  }
}
```

Glass-blur tab bar: `.barOverlap(true).barBackgroundBlurStyle(BlurStyle.Thin)`.


### Swiper — carousel / banner

```ts
Swiper() {
  ForEach(this.banners, (item: BannerItem) => {
    Image(item.url).width('100%').height(180).borderRadius(12)
  })
}
.loop(true)
.autoPlay(true)
.interval(3000)
.indicator(new DotIndicator()
  .color('#33000000').selectedColor('#007DFF')
  .itemWidth(8).selectedItemWidth(16))
```


### WaterFlow — Pinterest-style layout

```ts
WaterFlow({ scroller: this.scroller }) {
  LazyForEach(this.dataSource, (item: CardItem) => {
    FlowItem() {
      Column() {
        Image(item.image).width('100%').borderRadius(8)
        Text(item.title).fontSize(14).padding(8)
      }
    }
  }, (item: CardItem) => item.id)
}
.columnsTemplate('1fr 1fr')       // 2 columns
.columnsGap(8)
.rowsGap(8)
.cachedCount(10)
```


### Grid — fixed grid layout

```ts
Grid() {
  ForEach(this.items, (item: GridItemData) => {
    GridItem() {
      Column() {
        Image(item.icon).width(40).height(40)
        Text(item.name).fontSize(12).margin({ top: 4 })
      }
    }
  })
}
.columnsTemplate('1fr 1fr 1fr 1fr')   // 4 columns
.rowsGap(12)
.columnsGap(12)
.height(200)
```


### TextInput / TextArea

```ts
TextInput({ placeholder: 'Enter username' })
  .type(InputType.Normal)                          // .Email, .Number, .Password, .PhoneNumber
  .maxLength(20)
  .onChange((value: string) => { this.username = value; })
  .onSubmit((enterKey: EnterKeyType) => { /* handle submit */ })

TextArea({ placeholder: 'Enter description', text: $$this.desc })
  .maxLength(200)
  .showCounter(true)                                // character count indicator
```

Two-way binding with `$$`: `TextInput({ text: $$this.value })` — no `onChange` needed.


### AlertDialog / Toast

```ts
// Alert dialog
AlertDialog.show({
  title: 'Confirm',
  message: 'Delete this item?',
  primaryButton: { value: 'Cancel', action: () => {} },
  secondaryButton: { value: 'Delete', fontColor: Color.Red,
    action: () => { this.deleteItem(); }
  },
});

// Toast
this.getUIContext().getPromptAction().showToast({
  message: 'Operation successful',
  duration: 2000,
});
```


### Common form components — quick reference

| Component | Key Props | Example |
|---|---|---|
| `Checkbox` | `select`, `onChange((val: boolean) => {})` | `Checkbox({ name: 'agree' }).select(this.agreed)` |
| `Toggle` | `type(ToggleType.Switch)`, `isOn`, `onChange` | `Toggle({ type: ToggleType.Switch, isOn: $$this.on })` |
| `Radio` | `value`, `group`, `checked`, `onChange` | `Radio({ value: 'male', group: 'gender' }).checked(true)` |
| `Select` | `options: SelectOption[]`, `selected`, `value`, `onSelect` | `Select([{value:'A'},{value:'B'}]).selected(0)` |
| `Slider` | `value`, `min`, `max`, `step`, `onChange` | `Slider({ value: $$this.val, min: 0, max: 100 })` |
| `DatePicker` | `start`, `end`, `selected`, `onChange` | `DatePicker({ selected: this.date }).onChange((v) => {})` |
| `TimePicker` | `selected`, `useMilitaryTime`, `onChange` | `TimePicker({ selected: this.time })` |
| `Search` | `value`, `placeholder`, `onSubmit`, `onChange` | `Search({ value: $$this.keyword, placeholder: 'Search' })` |
| `Progress` | `value`, `total`, `type(ProgressType.Linear)` | `Progress({ value: 60, total: 100 })` |
| `LoadingProgress` | — | `LoadingProgress().width(48).color('#007DFF')` |


### HarmonyOS 6.0 visual effects (沉浸光感视效 / 液态玻璃)

HarmonyOS 6.0 (API 23) introduces system-level "Immersive Light Perception" visual effects. Users enable via Settings → Desktop & Personalization → Immersive Light Effect (强/均衡/弱). Developers achieve similar effects through these ArkUI attributes:

**BlurStyle enum (API 9–11):**

| Name | Since | Level |
|---|---|---|
| `Thin` / `Regular` / `Thick` | API 9 | Material blur |
| `BACKGROUND_THIN` / `BACKGROUND_REGULAR` / `BACKGROUND_THICK` / `BACKGROUND_ULTRA_THICK` | API 10 | Depth-of-field (min→max) |
| `COMPONENT_ULTRA_THIN` / `COMPONENT_THIN` / `COMPONENT_REGULAR` / `COMPONENT_THICK` / `COMPONENT_ULTRA_THICK` | API 11 | Component-level material |
| `NONE` | API 10 | No blur |

**backgroundBlurStyle (API 9+):**
```ts
Column() { /* content */ }
  .backgroundBlurStyle(BlurStyle.Thin, {
    colorMode: ThemeColorMode.LIGHT,     // SYSTEM | LIGHT | DARK
    adaptiveColor: AdaptiveColor.DEFAULT, // DEFAULT | AVERAGE
    scale: 1.0                            // 0.0–1.0 (blur intensity)
  })
```

**foregroundBlurStyle (API 10+):**
```ts
Image($r('app.media.photo'))
  .foregroundBlurStyle(BlurStyle.Regular)
```

**backgroundEffect (API 11+) — fine-grained control:**
```ts
Column() { /* content */ }
  .backgroundEffect({
    radius: 20,          // blur radius
    saturation: 15,      // [0, 50] recommended
    brightness: 0.6,     // [0, 2] recommended
    color: '#80FFFFFF'   // mask color
  })
```

**blur / backdropBlur (API 7+) — numeric radius:**
```ts
Column() { /* content */ }
  .backdropBlur(20, { grayscale: [30, 50] })  // background blur
  .blur(10)                                    // foreground blur
```

**backgroundBrightness (API 12+):**
```ts
Column() { /* content */ }
  .backgroundBrightness({ rate: 0.5, lightUpDegree: 0.2 })
```

**Visual effect filters (API 12+):**
```ts
import { uiEffect } from '@kit.ArkGraphics2D';

const blurFilter = uiEffect.createFilter().blur(10);
Column() { /* content */ }
  .backgroundFilter(blurFilter)    // background filter
  .foregroundFilter(blurFilter)    // content filter
```

**pointLight (API 11+, System API only — NOT available for third-party apps):**
```ts
// System apps only! Supports: Image, Column, Flex, Row, Stack, Button, Toggle
Flex()
  .pointLight({
    lightSource: { positionX: '50%', positionY: '50%', positionZ: 80, intensity: 2, color: Color.White },
    illuminated: IlluminatedType.BORDER,  // NONE | BORDER | CONTENT | BORDER_CONTENT
    bloom: 0.5                            // luminous intensity 0–1
  })
```
Up to 12 light sources can illuminate a single component. HarmonyOS 6.0 adds dual-edge flow light and UV background flow light effects.

**systemMaterialEffect (HDS layer, API 23+, HarmonyOS-only SDK):**
```ts
import { hdsMaterial } from '@kit.ArkUI';

Column() { /* content */ }
  .systemMaterialEffect({
    materialType: hdsMaterial.MaterialType.ADAPTIVE,
    materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
  })
```
Note: `hdsMaterial` is part of the closed-source HarmonyOS Design System (HDS), not OpenHarmony. Requires HarmonyOS 6.0 SDK (API 23+).


### Builders, styles, extends

```ts
@Builder function Label(text: string) { Text(text).fontSize(16) }

@Styles function Card() { .padding(12).borderRadius(12).backgroundColor('#FFF') }

@Extend(Text) function title() { .fontSize(22).fontWeight(FontWeight.Bold) }

// Usage:
Text('Hello').title()
Column() { Label('x') } .Card()
```


## sys.symbol — icon glyph system

HarmonyOS Symbol is a 1500+ vector icon font with multi-layer color and 7 animation types.

```ts
SymbolGlyph($r('sys.symbol.bell_fill'))
  .fontSize(24)
  .fontColor([Color.Blue, Color.Green])
  .symbolEffect(new BounceSymbolEffect(EffectScope.WHOLE), true)
```

**Confirmed working names** (SDK 6.0.1): `xmark` · `plus` · `minus` · `checkmark` · `chevron_right` · `chevron_left` · `star` · `star_fill` · `bell` · `bell_fill` · `doc` · `video` · `mic` · `mic_fill` · `clock` · `trash` · `pencil` · `camera` · `person`

**Names that do NOT exist** (common mistakes): `photo` · `doc_richtext` · `sparkles` · `checklist` · `image` (use `doc` or `camera` instead) · `location_fill` (use text label instead)

Find valid names: https://developer.huawei.com/consumer/cn/design/harmonyos-symbol


## Multi-device / foldable screen adaptation (API 21)


### Breakpoint detection

```ts
import { display } from '@kit.ArkUI'

export const BP_SM = 'sm'   // < 600 vp  — phone portrait
export const BP_MD = 'md'   // < 840 vp  — phone landscape / small tablet
export const BP_LG = 'lg'   // >= 840 vp — large tablet / foldable unfolded

export function getBreakpoint(): string {
  try {
    const d = display.getDefaultDisplaySync()
    const widthVp = d.width / d.densityPixels
    if (widthVp < 600) return BP_SM
    if (widthVp < 840) return BP_MD
    return BP_LG
  } catch (e) {
    return BP_SM
  }
}
```

### Container breakpoints with `ContainerReader` (API 26 Release)

Use `ContainerReader` when a reusable component must adapt to its own container rather than the application window. This capability starts at API 26.0.0, so keep it out of API 24 compatibility examples unless the project gates it with an availability check or supplies an older-device fallback.

The official guide binds container size and breakpoint state to
`ContainerReader`, then derives layout properties such as `Grid` columns from
the returned breakpoint. Keep those decisions bound to the container so they
update when a split view, nested pane, or reusable card changes size.

Treat the guide's imports, bindings, and `breakpointConfig` signatures as
API-26-SDK-specific. Read the current guide and verify them against the
project's installed Release SDK before generating compile-ready code.

Official guide: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-container-reader


### Foldable screen — listen for fold/unfold events

```ts
// display.on callback receives (id: number) — NOT empty params
private displayListener: (id: number) => void = (_id: number) => {
  this.breakpoint = getBreakpoint()
}

aboutToAppear(): void {
  this.breakpoint = getBreakpoint()
  display.on('change', this.displayListener)
}

aboutToDisappear(): void {
  display.off('change', this.displayListener)
}
```


### Responsive layout switching (if/else, not .visibility)

Always use `if/else` to switch between phone and tablet layouts. `.visibility(Visibility.None)` hides but still lays out — wastes resources and can cause measurement bugs.

```ts
if (this.breakpoint === BP_SM) {
  // Phone: single-column List + LazyForEach
  List({ space: 8 }) { LazyForEach(...) }
} else {
  // Tablet/foldable: GridRow with responsive columns
  Scroll() {
    GridRow({
      columns: { sm: 1, md: 2, lg: 3 },
      gutter: { x: 12, y: 12 },
      breakpoints: { value: ['600vp', '840vp'] }
    }) {
      ForEach(this.gridItems, (item) => { GridCol() { MyCard({ record: item }) } })
    }
  }
}
```


### `GridRow`/`GridCol` does not support `LazyForEach`

`GridRow`/`GridCol` is a responsive layout container, not a lazy loader. Use `ForEach` inside it. To keep the grid reactive to data changes, maintain a `@State gridItems: T[]` that is updated via a `DataChangeListener`:

```ts
class GridRefreshListener implements DataChangeListener {
  private updateFn: () => void
  constructor(fn: () => void) { this.updateFn = fn }
  // Must implement ALL methods — see API 21 DataChangeListener note above
  onDataReloaded(): void { this.updateFn() }
  onDataAdd(_i: number): void { this.updateFn() }
  onDataAdded(_i: number): void { this.updateFn() }
  // ... all other methods
  onDataChange(_i: number): void { /* @ObjectLink handles per-item updates */ }
  onDataChanged(_i: number): void { }
}

// In @Entry @Component:
@State gridItems: MyRecord[] = []
private gridListener = new GridRefreshListener(() => {
  this.gridItems = [...this.dataSource.getAllData()]
})
aboutToAppear() { this.dataSource.registerDataChangeListener(this.gridListener) }
aboutToDisappear() { this.dataSource.unregisterDataChangeListener(this.gridListener) }
```


### Share breakpoint via `@Provide`/`@Consume`

Declare in the `@Entry` root, consume in any `NavDestination` child:
```ts
// Root
@Provide('breakpoint') breakpoint: string = BP_SM

// Detail page (NavDestination)
@Consume('breakpoint') breakpoint: string
```
`@Provide`/`@Consume` works across `Navigation`/`NavDestination` because they are in the same component subtree.


## UIDesignKit — icon processing & HdsNavigation

Available from HarmonyOS 5.0+ (API 12+). Provides Huawei Design System components.


### `hdsDrawable` — icon adaptive processing

```ts
import { hdsDrawable } from '@kit.UIDesignKit';

// Render app icon with system-consistent adaptive shape (squircle, circle, etc.)
const drawable = new hdsDrawable.HdsAdaptiveIconDrawable(
  context,            // UIAbilityContext or ApplicationContext
  iconResource,       // Resource ($r('app.media.icon'))
  { size: 48 }        // options: size in vp
);
const pixelMap = await drawable.getPixelMap();
```


### `HdsNavigation` — system-style navigation component

```ts
import { HdsNavigation, HdsNavigationItem } from '@kit.UIDesignKit';

@Entry
@Component
struct MainPage {
  @State currentIndex: number = 0;
  private tabs: HdsNavigationItem[] = [
    { icon: $r('app.media.home'), selectedIcon: $r('app.media.home_filled'), label: '首页' },
    { icon: $r('app.media.mine'), selectedIcon: $r('app.media.mine_filled'), label: '我的' },
  ];

  build() {
    Column() {
      // Page content
      Blank()
      HdsNavigation({
        items: this.tabs,
        selectedIndex: this.currentIndex,
        onItemClick: (index: number) => { this.currentIndex = index; }
      })
    }.height('100%')
  }
}
```

`HdsNavigation` supports: dynamic blur background, custom content areas (badges, dot indicators), message count badges on items.


## Custom dialog — openCustomDialog & openBindSheet


### openCustomDialog (general-purpose modal/non-modal)

```ts
import { ComponentContent } from '@kit.ArkUI';

// 1. Define dialog content via @Builder
@Builder
function dialogContentBuilder(params: { message: string; close: () => void }) {
  Column({ space: 16 }) {
    Text(params.message).fontSize(16)
    Button('OK').onClick(() => params.close())
  }
  .padding(24)
  .backgroundColor(Color.White)
  .borderRadius(16)
}

// 2. Open dialog
const uiContext = this.getUIContext();
const contentNode = new ComponentContent(uiContext, wrapBuilder(dialogContentBuilder), {
  message: 'Hello',
  close: () => uiContext.getPromptAction().closeCustomDialog(contentNode),
});
uiContext.getPromptAction().openCustomDialog(contentNode, {
  alignment: DialogAlignment.Center,
  isModal: true,
  autoCancel: true,       // tap outside to close
});
```


### openBindSheet (bottom half-modal sheet)

```ts
const uiContext = this.getUIContext();
const sheetNode = new ComponentContent(uiContext, wrapBuilder(sheetBuilder), params);
uiContext.openBindSheet(sheetNode, {
  title: { title: 'Select Option' },
  height: SheetSize.MEDIUM,
  preferType: SheetType.BOTTOM,
  detents: [SheetSize.MEDIUM, SheetSize.LARGE, 200],   // draggable heights
  backgroundColor: '#F1F3F5',
}, targetComponentId);
```


### bindContentCover (full-screen modal overlay)

```ts
@State isPresented: boolean = false;

@Builder
fullScreenContent() {
  Column() {
    Text('Full Screen Modal').fontSize(20)
    Button('Close').onClick(() => { this.isPresented = false; })
  }.width('100%').height('100%').backgroundColor(Color.White)
}

// Trigger:
Button('Show').onClick(() => { this.isPresented = true; })
  .bindContentCover($$this.isPresented, this.fullScreenContent(), {
    modalTransition: ModalTransition.DEFAULT,   // .NONE, .ALPHA
  })
```

> **Note**: Do NOT use the deprecated `CustomDialog` or `@ohos.promptAction` — use `UIContext.getPromptAction().openCustomDialog()`, `UIContext.openBindSheet()`, and `.bindContentCover()` instead.


## Keyboard layout adaptation (软键盘适配)


### Set keyboard avoidance mode (in UIAbility)

```ts
import { KeyboardAvoidMode } from '@kit.ArkUI';

// OFFSET = page lifts up (default); RESIZE = page compresses; NONE = keyboard overlaps
windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
```


### Prevent a component from moving with keyboard

```ts
Row() { /* title bar — should stay fixed */ }
  .expandSafeArea([SafeAreaType.KEYBOARD])
  .zIndex(1)
```


### Monitor keyboard height

```ts
import { window } from '@kit.ArkUI';

window.getLastWindow(this.getUIContext().getHostContext()).then(win => {
  win.on('keyboardHeightChange', (height: number) => {
    this.keyboardHeight = this.getUIContext().px2vp(height);
  });
});
```


### Focus control

```ts
TextInput().defaultFocus(true)                                    // auto-focus on page load
this.getUIContext().getFocusController().requestFocus('inputId');  // programmatic focus
this.getUIContext().getFocusController().clearFocus();             // dismiss keyboard
```


## Dark mode adaptation (深色模式适配)


### Resource qualifier approach (recommended)

Place light-mode colors/images in `resources/base/`, dark-mode variants (same filenames) in `resources/dark/`:

```
resources/base/element/color.json    → { "color": [{ "name": "bg_color", "value": "#FFFFFF" }] }
resources/dark/element/color.json    → { "color": [{ "name": "bg_color", "value": "#1A1A1A" }] }
resources/base/media/icon.png        → light icon
resources/dark/media/icon.png        → dark icon
```

Usage: `$r('app.color.bg_color')` / `$r('app.media.icon')` — auto-switches with system theme.


### Detect & react to color mode changes

```ts
// In EntryAbility — store current mode
onCreate(): void {
  AppStorage.setOrCreate('currentColorMode', this.context.config.colorMode);
}
onConfigurationUpdate(newConfig: Configuration): void {
  AppStorage.setOrCreate('currentColorMode', newConfig.colorMode);
}

// In component — watch for changes
@StorageProp('currentColorMode') @Watch('onColorModeChange')
currentColorMode: number = ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET;

onColorModeChange(): void {
  const isDark = this.currentColorMode === ConfigurationConstant.ColorMode.COLOR_MODE_DARK;
  // update status bar, custom logic, etc.
}
```


### Programmatic mode switching

```ts
this.getUIContext().getHostContext()?.getApplicationContext()
  .setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);   // or COLOR_MODE_LIGHT / COLOR_MODE_NOT_SET
```


## Custom font (自定义字体)

```ts
// 1. Register font (in EntryAbility onWindowStageCreate or component aboutToAppear)
const uiContext = windowStage.getMainWindowSync().getUIContext();
uiContext.getFont().registerFont({
  familyName: 'MyCustomFont',
  familySrc: $rawfile('MyCustomFont.ttf'),
});

// 2. Use in component
Text('Hello').fontFamily('MyCustomFont')
```

Font size follow/ignore system setting — configure in `profile/configuration.json`:

```json
{ "configuration": { "fontSizeScale": "followSystem", "fontSizeMaxScale": "2" } }
```

Reference in `app.json5`: `"configuration": "$profile:configuration"`.


## Screen orientation (横竖屏切换)

```ts
import { window } from '@kit.ArkUI';

// Get window instance
const win = await window.getLastWindow(this.context);

// Set orientation
win.setPreferredOrientation(window.Orientation.USER_ROTATION_LANDSCAPE);   // enter landscape
win.setPreferredOrientation(window.Orientation.USER_ROTATION_PORTRAIT);    // back to portrait
win.setPreferredOrientation(window.Orientation.AUTO_ROTATION);             // follow sensor

// Monitor window size for layout adaptation
win.on('windowSizeChange', (size) => {
  const orientation = display.getDefaultDisplaySync().orientation;
  this.isLandscape = (orientation === display.Orientation.LANDSCAPE ||
                      orientation === display.Orientation.LANDSCAPE_INVERTED);
});
```

Also configurable in `module.json5`: `"abilities": [{ "orientation": "portrait" }]`.
Options: `portrait`, `landscape`, `auto_rotation`, `auto_rotation_landscape`, `follow_desktop`.


## Clipboard — pasteboard read/write

```ts
import { pasteboard } from '@kit.BasicServicesKit';

// Write text to clipboard
const pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'Hello World');
const board = pasteboard.getSystemPasteboard();
await board.setData(pasteData);

// Read from clipboard
const data = await board.getData();
if (data.hasType(pasteboard.MIMETYPE_TEXT_PLAIN)) {
  const text = data.getPrimaryText();
}
```

Supported MIME types: `MIMETYPE_TEXT_PLAIN`, `MIMETYPE_TEXT_HTML`, `MIMETYPE_TEXT_URI`, `MIMETYPE_PIXELMAP`.


## Gesture conflict resolution (手势冲突处理)


### hitTestBehavior — control touch event response

```ts
Stack() {
  BottomComponent().hitTestBehavior(HitTestMode.None)       // skip self, pass to sibling
  TopComponent().hitTestBehavior(HitTestMode.Transparent)   // self responds AND passes to sibling
}
```

| Mode | Behavior |
|---|---|
| `Default` | Self responds, blocks siblings |
| `Transparent` | Self responds, does NOT block siblings |
| `None` | Skips self, passes to siblings |
| `Block` | Only self responds, stops all propagation |


### Gesture binding priority

```ts
// Parent takes priority over child for same gesture type
ParentComponent()
  .priorityGesture(TapGesture().onAction(() => { /* parent handles */ }))

// Both parent and child respond simultaneously
ParentComponent()
  .parallelGesture(PanGesture().onAction(() => { /* parent also handles */ }))

// Block child gestures entirely
ParentComponent()
  .gesture(TapGesture(), GestureMask.IgnoreInternal)
```


### GestureGroup modes

```ts
// Sequential: all must succeed in order
GestureGroup(GestureMode.Sequence, LongPressGesture(), PanGesture())

// Parallel: all run simultaneously
GestureGroup(GestureMode.Parallel, PinchGesture(), RotationGesture())

// Exclusive: first to succeed wins
GestureGroup(GestureMode.Exclusive, TapGesture(), SwipeGesture())
```

> **Note**: System gestures (onClick, onTouch, drag, bindMenu) always win over custom gestures of the same type.


## Immersive window (沉浸式/全屏/避让区)


### Extend component into status bar & navigation bar

```ts
// Method 1 — expandSafeArea (simplest, component-level)
Column() { /* content */ }
  .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])

// Method 2 — window-level fullscreen (affects all pages)
const win = windowStage.getMainWindowSync();
win.setWindowLayoutFullScreen(true);
```


### Get safe area dimensions for manual padding

```ts
import { window } from '@kit.ArkUI';

const win = await window.getLastWindow(context);
const systemAvoid = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
const topHeight = px2vp(systemAvoid.topRect.height);       // status bar height
const bottomHeight = px2vp(systemAvoid.bottomRect.height);  // navigation bar height

// Listen for changes (e.g. split screen, fold/unfold)
win.on('avoidAreaChange', (options: window.AvoidAreaOptions) => {
  if (options.type === window.AvoidAreaType.TYPE_SYSTEM) {
    // update top/bottom padding
  }
});
```


### Hide/show system bars

```ts
win.setSpecificSystemBarEnabled('status', false);             // hide status bar
win.setSpecificSystemBarEnabled('navigationIndicator', false); // hide nav indicator
```


### Status bar text color (light/dark content)

```ts
win.setWindowSystemBarProperties({
  statusBarContentColor: '#FFFFFF',   // white text for dark backgrounds
});
```


## Common list operations (列表常用操作)


### Swipe-to-delete (left swipe action)

```ts
ListItem() { /* content */ }
  .swipeAction({
    end: {
      builder: () => {
        Button('Delete').backgroundColor(Color.Red)
          .onClick(() => {
            animateTo({ duration: 300 }, () => {
              this.dataList.splice(index, 1);
            });
          })
      },
      actionAreaDistance: 56,
    },
    edgeEffect: SwipeEdgeEffect.Spring,
  })
```


### Drag reorder

```ts
List() {
  ForEach(this.dataList, (item: string, index: number) => {
    ListItem() { Text(item) }
  })
}
.onItemDragStart((event: ItemDragInfo, itemIndex: number) => {
  this.dragIndex = itemIndex;
})
.onItemDragMove((event: ItemDragInfo, itemIndex: number, insertIndex: number) => {
  animateTo({ duration: 200 }, () => {
    const tmp = this.dataList.splice(this.dragIndex, 1);
    this.dataList.splice(insertIndex, 0, tmp[0]);
    this.dragIndex = insertIndex;
  });
})
```


### Pull-down refresh

```ts
Refresh({ refreshing: $$this.isRefreshing }) {
  List() { /* items */ }
}
.onRefreshing(() => {
  // fetch new data...
  this.isRefreshing = false;
})
```


### Scroll to bottom (chat-style)

```ts
const scroller = new Scroller();
List({ scroller }) { /* items */ }

// After new message:
scroller.scrollEdge(Edge.Bottom);
// Or scroll to specific index:
scroller.scrollToIndex(this.messages.length - 1);
```


### Keep scroll position on data insert (LazyForEach)

```ts
List() { LazyForEach(this.dataSource, ...) }
  .maintainVisibleContentPosition(true)   // new items at top don't shift visible content
```


### ListItemGroup + sticky header (grouped list)

```ts
@Builder sectionHeader(title: string) {
  Text(title).fontSize(14).fontColor('#99000000')
    .width('100%').padding({ left: 16, top: 8, bottom: 8 })
    .backgroundColor('#F1F3F5')
}

List() {
  ForEach(this.groups, (group: GroupData) => {
    ListItemGroup({ header: this.sectionHeader(group.title) }) {
      ForEach(group.items, (item: ItemData) => {
        ListItem() { Text(item.name) }
      })
    }
  })
}
.sticky(StickyStyle.Header)         // header sticks to top when scrolling
```


### onReachEnd — load more data

```ts
List() { LazyForEach(this.dataSource, ...) }
  .onReachEnd(() => {
    if (!this.isLoading) {
      this.isLoading = true;
      this.loadNextPage().then(() => { this.isLoading = false; });
    }
  })
```

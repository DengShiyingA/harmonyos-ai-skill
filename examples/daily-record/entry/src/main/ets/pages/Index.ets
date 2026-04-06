import { DailyRecord, RecordDataSource } from '../model/RecordModel'
import { RecordCard } from '../components/RecordCard'

@Entry
@Component
struct Index {
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack()
  @State dataSource: RecordDataSource = new RecordDataSource()
  @State isRefreshing: boolean = false

  aboutToAppear(): void {
    // 加载示例数据（后续替换为数据库查询）
    this.loadSampleData()
  }

  build() {
    Navigation(this.pathStack) {
      Stack({ alignContent: Alignment.BottomEnd }) {
        // 主列表
        if (this.dataSource.totalCount() === 0) {
          this.EmptyView()
        } else {
          this.RecordList()
        }

        // 悬浮发布按钮
        Button() {
          SymbolGlyph($r('sys.symbol.plus'))
            .fontSize(24)
            .fontColor(['#FFFFFF'])
        }
        .width(56)
        .height(56)
        .borderRadius(28)
        .backgroundColor('#D97757')
        .shadow({ radius: 8, color: 'rgba(217,119,87,0.3)', offsetY: 4 })
        .margin({ right: 20, bottom: 20 })
        .onClick(() => {
          this.pathStack.pushPath({ name: 'PublishPage' })
        })
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#FAF5EE')
    }
    .title(this.NavigationTitle())
    .titleMode(NavigationTitleMode.Full)
    .navDestination(this.PageRouter)
  }

  @Builder
  NavigationTitle() {
    Row({ space: 8 }) {
      Text('每日记录')
        .fontSize(28)
        .fontWeight(FontWeight.Bold)
        .fontColor('#2d2520')
      Text(`${this.dataSource.totalCount()} 条`)
        .fontSize(14)
        .fontColor('#a8967e')
        .margin({ bottom: 2 })
    }
    .alignItems(VerticalAlign.Bottom)
  }

  @Builder
  PageRouter(name: string) {
    if (name === 'PublishPage') {
      PublishPage()
    } else if (name === 'DetailPage') {
      DetailPage()
    }
  }

  @Builder
  RecordList() {
    List({ space: 12 }) {
      LazyForEach(this.dataSource, (record: DailyRecord, index: number) => {
        ListItem() {
          RecordCard({
            record: record,
            onCardClick: () => {
              this.pathStack.pushPath({
                name: 'DetailPage',
                param: record
              })
            },
            onFavoriteClick: () => {
              this.dataSource.toggleFavorite(index)
            }
          })
        }
      }, (record: DailyRecord) => record.id)
    }
    .width('100%')
    .height('100%')
    .padding({ left: 16, right: 16, top: 8 })
    .cachedCount(5)
    .edgeEffect(EdgeEffect.Spring)
  }

  @Builder
  EmptyView() {
    Column({ space: 16 }) {
      SymbolGlyph($r('sys.symbol.doc'))
        .fontSize(64)
        .fontColor(['#d4c4b0'])
      Text('还没有记录')
        .fontSize(18)
        .fontColor('#a8967e')
      Text('点击右下角 + 开始你的第一条记录')
        .fontSize(14)
        .fontColor('#c4b5a4')
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private loadSampleData(): void {
    const r1 = new DailyRecord(
      '今天在公园散步',
      '阳光很好，看到了樱花开了。走了 8000 步，感觉很放松。',
      '',
      '城市公园'
    )
    const r2 = new DailyRecord(
      '学鸿蒙开发第一天',
      '用 Claude Code 配合 HarmonyOS AI Skills 写了第一个 ArkUI 组件，比想象中顺利。@State 和 @Observed 的区别搞清楚了。',
      '',
      ''
    )
    r2.isFavorite = true
    this.dataSource.addRecord(r1)
    this.dataSource.addRecord(r2)
  }
}

// 发布页面（占位，后续扩展）
@Component
struct PublishPage {
  @Consume('pathStack') pathStack: NavPathStack
  @State title: string = ''
  @State content: string = ''

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        TextInput({ placeholder: '标题' })
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .backgroundColor('transparent')
          .onChange((value: string) => { this.title = value })

        TextArea({ placeholder: '写点什么...' })
          .fontSize(16)
          .height(200)
          .backgroundColor('#FFFFFF')
          .borderRadius(12)
          .onChange((value: string) => { this.content = value })

        // 功能按钮栏（后续接入相机、定位）
        Row({ space: 20 }) {
          this.ActionButton('sys.symbol.camera', '拍照')
          this.ActionButton('sys.symbol.image', '相册')
          this.ActionButton('sys.symbol.location_fill', '定位')
        }
        .padding({ top: 8 })

        Blank()

        Button('发布')
          .width('100%')
          .height(48)
          .borderRadius(24)
          .backgroundColor('#D97757')
          .fontColor('#FFFFFF')
          .fontSize(16)
          .fontWeight(FontWeight.Medium)
          .onClick(() => {
            if (this.title.length > 0) {
              // TODO: 保存到数据库 + 通知列表刷新
              this.pathStack.pop()
            }
          })
      }
      .padding(20)
      .width('100%')
      .height('100%')
      .backgroundColor('#FAF5EE')
    }
    .title('新记录')
  }

  @Builder
  ActionButton(icon: string, label: string) {
    Column({ space: 4 }) {
      SymbolGlyph($r(icon))
        .fontSize(24)
        .fontColor(['#D97757'])
      Text(label)
        .fontSize(12)
        .fontColor('#8a7b6b')
    }
    .onClick(() => {
      // TODO: 接入对应 Kit
    })
  }
}

// 详情页面（占位，后续扩展动画）
@Component
struct DetailPage {
  @Consume('pathStack') pathStack: NavPathStack
  @State record: DailyRecord = new DailyRecord('', '')

  build() {
    NavDestination() {
      Scroll() {
        Column({ space: 16 }) {
          if (this.record.imageUri) {
            Image(this.record.imageUri)
              .width('100%')
              .height(240)
              .borderRadius(16)
              .objectFit(ImageFit.Cover)
          }

          Text(this.record.title)
            .fontSize(24)
            .fontWeight(FontWeight.Bold)
            .fontColor('#2d2520')

          if (this.record.location) {
            Row({ space: 4 }) {
              SymbolGlyph($r('sys.symbol.location_fill'))
                .fontSize(14)
                .fontColor(['#D97757'])
              Text(this.record.location)
                .fontSize(14)
                .fontColor('#a8967e')
            }
          }

          Text(this.record.content)
            .fontSize(16)
            .fontColor('#4a3f35')
            .lineHeight(26)
        }
        .padding(20)
        .alignItems(HorizontalAlign.Start)
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#FAF5EE')
    }
    .title('详情')
    .onReady((context: NavDestinationContext) => {
      const param = context.pathInfo?.param
      if (param) {
        this.record = param as DailyRecord
      }
    })
  }
}

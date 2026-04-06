import { DailyRecord } from '../model/RecordModel'

// 使用 @Reusable 实现组件复用（列表性能提升 69%）
@Reusable
@Component
export struct RecordCard {
  @ObjectLink record: DailyRecord
  onCardClick: () => void = () => {}
  onFavoriteClick: () => void = () => {}

  aboutToReuse(params: Record<string, ESObject>): void {
    // @ObjectLink 自动更新，无需手动处理
  }

  build() {
    Column({ space: 8 }) {
      // 图片区域
      if (this.record.imageUri) {
        Image(this.record.imageUri)
          .width('100%')
          .height(180)
          .borderRadius(12)
          .objectFit(ImageFit.Cover)
      }

      // 标题
      Text(this.record.title)
        .fontSize(18)
        .fontWeight(FontWeight.Bold)
        .fontColor('#2d2520')
        .maxLines(1)
        .textOverflow({ overflow: TextOverflow.Ellipsis })

      // 内容预览
      Text(this.record.content)
        .fontSize(14)
        .fontColor('#8a7b6b')
        .maxLines(2)
        .textOverflow({ overflow: TextOverflow.Ellipsis })

      // 底部信息栏
      Row() {
        // 位置
        if (this.record.location) {
          Row({ space: 4 }) {
            SymbolGlyph($r('sys.symbol.location_fill'))
              .fontSize(14)
              .fontColor(['#D97757'])
            Text(this.record.location)
              .fontSize(12)
              .fontColor('#a8967e')
          }
        }

        Blank()

        // 时间
        Text(this.formatTime(this.record.timestamp))
          .fontSize(12)
          .fontColor('#a8967e')

        // 收藏按钮
        SymbolGlyph($r(this.record.isFavorite ? 'sys.symbol.star_fill' : 'sys.symbol.star'))
          .fontSize(20)
          .fontColor([this.record.isFavorite ? '#E8C872' : '#c4b5a4'])
          .onClick(() => this.onFavoriteClick())
          .margin({ left: 12 })
      }
      .width('100%')
    }
    .padding(16)
    .backgroundColor('#FFFFFF')
    .borderRadius(16)
    .shadow({ radius: 4, color: 'rgba(0,0,0,0.06)', offsetY: 2 })
    .onClick(() => this.onCardClick())
  }

  private formatTime(timestamp: number): string {
    const date = new Date(timestamp)
    const month = date.getMonth() + 1
    const day = date.getDate()
    const hour = date.getHours().toString().padStart(2, '0')
    const minute = date.getMinutes().toString().padStart(2, '0')
    return `${month}/${day} ${hour}:${minute}`
  }
}

// 数据模型 — 使用 @Observed 实现嵌套对象观察
@Observed
export class DailyRecord {
  id: string
  title: string
  content: string
  imageUri: string
  location: string
  timestamp: number
  isFavorite: boolean

  constructor(title: string, content: string, imageUri: string = '', location: string = '') {
    this.id = `${Date.now()}_${Math.floor(Math.random() * 1000)}`
    this.title = title
    this.content = content
    this.imageUri = imageUri
    this.location = location
    this.timestamp = Date.now()
    this.isFavorite = false
  }
}

// LazyForEach 数据源 — 必须实现 IDataSource 接口
export class RecordDataSource implements IDataSource {
  private records: DailyRecord[] = []
  private listeners: DataChangeListener[] = []

  totalCount(): number {
    return this.records.length
  }

  getData(index: number): DailyRecord {
    return this.records[index]
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener)
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const idx = this.listeners.indexOf(listener)
    if (idx >= 0) {
      this.listeners.splice(idx, 1)
    }
  }

  addRecord(record: DailyRecord): void {
    this.records.unshift(record)
    this.notifyDataReload()
  }

  deleteRecord(index: number): void {
    this.records.splice(index, 1)
    this.notifyDataReload()
  }

  toggleFavorite(index: number): void {
    this.records[index].isFavorite = !this.records[index].isFavorite
    this.notifyDataChange(index)
  }

  getAllRecords(): DailyRecord[] {
    return this.records
  }

  private notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded()
    })
  }

  private notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index)
    })
  }
}

@Observed
export class TodoItem {
  id: string;
  title: string;
  done: boolean;

  constructor(id: string, title: string, done: boolean = false) {
    this.id = id;
    this.title = title;
    this.done = done;
  }
}

@Component
struct TodoRow {
  @ObjectLink item: TodoItem;

  build() {
    Row() {
      Checkbox()
        .select(this.item.done)
        .onChange((checked: boolean) => {
          this.item.done = checked;
        })
      Text(this.item.title)
        .fontSize(16)
        .margin({ left: 8 })
    }
    .width('100%')
    .padding(12)
  }
}

@Entry
@Component
struct TodoListPage {
  @State items: TodoItem[] = [
    new TodoItem('1', 'Review ArkTS strict typing'),
    new TodoItem('2', 'Use stable keys in LazyForEach')
  ];

  build() {
    List() {
      LazyForEach(this.items, (item: TodoItem) => {
        ListItem() {
          TodoRow({ item })
        }
      }, (item: TodoItem) => item.id)
    }
    .width('100%')
    .height('100%')
  }
}

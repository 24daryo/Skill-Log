
class Node:
    def __init__(self, item):
        self.value = item
        self.prev = None
        self.next = None


class Mylist:
    def __init__(self, item):
        self.start = Node(item)

    # 配列のように指定が可能となる
    def __getitem__(self, key):
        node = self.start
        for _ in range(key):
            if node is not None:
                node = node.next
            else:
                break
        if node:
            return node.value
        else:
            print("要素が見つかりませんでした")
        return -1

    # 要素を追加する
    def append(self, item):
        new_node = Node(item)
        new_node.next = self.start
        self.start.prev = new_node
        self.start = new_node

    # 要素を削除する
    def delete(self, item):
        node = self.start
        while node is not None:
            if node.value == item:
                node.prev.next = node.next
                node.next.prev = node.prev
                print(f"要素{item}を削除しました")
                return
            node = node.next
        print(f"要素{item}が見つかりませんでした")

    # 要素を表示する
    def print(self):
        node = self.start
        text = f"[ {node.value}"
        node = node.next

        while node is not None:
            text += f", {node.value}"
            node = node.next

        text += "]"
        print(text)


mylist = Mylist(5)
mylist.append(4)
mylist.append(3)
mylist.append(7)
mylist.append(8)
# print(mylist[0])
# print(mylist[5])
mylist.delete(3)

mylist.print()

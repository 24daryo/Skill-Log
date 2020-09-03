
class Node:
    def __init__(self, item):
        self.value = item
        self.prev = None
        self.next = None


# LIFO(Last In First Out)
class MyStack:
    def __init__(self):
        self.count = 0
        self.now = None

    # 要素を追加する
    def insert(self, item):
        new_node = Node(item)
        # ノードを追加する
        if self.count > 0:
            self.now.next = new_node
            new_node.prev = self.now
            self.now = new_node
        else:
            self.now = new_node
        # カウントを+1する
        self.count += 1
        print(f"要素{new_node.value}を追加しました")

    # 要素を取り出す
    def pop(self):
        old_node = self.now
        if self.count > 0:
            # 最新ノードを更新
            self.now = old_node.prev
            self.now.next = None
            # カウントを-1する
            self.count -= 1
            print(f"要素{old_node.value}を取り出しました")
            return old_node.value
        else:
            print("取り出せる要素が存在しません")

    # 要素を表示する
    def print(self):
        node = self.now
        text = "]"
        if node:
            text = f"{node.value}" + text
            node = node.prev

        while node is not None:
            text = f"{node.value}, " + text
            node = node.prev

        text = "[" + text
        print(text)


# 挙動を確認する
mystack = MyStack()
mystack.print()
mystack.pop()
mystack.insert(3)
mystack.print()
mystack.insert(7)
mystack.print()
mystack.insert(5)
mystack.print()
mystack.pop()
mystack.print()

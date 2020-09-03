from collections import deque
from enum import Enum


# 木構造の中のノードを定義（ノードは値・左に子ノード、右に子ノードを持つ）
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class SerchType(Enum):
    BFS = 1
    DFS = 2


# 二分木クラスを定義
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def serch(self, node, item):
        if node:
            print(node.value)
            if item == node.value:
                print("アイテムが見つかりました")
                return
            elif item < node.value:
                self.serch(node.left, item)
            elif item > node.value:
                self.serch(node.right, item)
        else:
            print("見つかりませんでした")

    def traverse(self, start, serch_type: SerchType):
        if serch_type == SerchType.BFS:
            array = self.bfs(start, list())
        elif serch_type == SerchType.DFS:
            array = self.preorder(start, list())

        text = ""
        for element in array:
            text += str(element) + "->"
        print(text[:-2])

    # 幅優先探索
    def bfs(self, node, traversal) -> list:
        queue = deque()
        queue.append(node)
        while queue:
            now = queue.popleft()
            traversal.append(now.value)
            if now.left:
                queue.append(now.left)
            if now.right:
                queue.append(now.right)
        return traversal

    # 行きがけ順（preorder）を二分木クラスのメソッドとして生成
    # 深さ優先探索の一種
    def preorder(self, node, traversal) -> list:
        # ノードが存在する場合実行する
        if node:
            now = [node.value]
            left = self.preorder(node.left, traversal)
            right = self.preorder(node.right, traversal)
            traversal = now + left + right
        return traversal


# 二分木を作る
tree = BinaryTree(9)
tree.root.left = Node(3)
tree.root.right = Node(14)
tree.root.left.left = Node(1)
tree.root.left.right = Node(5)
tree.root.right.left = Node(12)
tree.root.right.right = Node(17)
tree.root.left.right.left = Node(4)
tree.root.left.right.right = Node(7)

# 定義した二分木をトラバースする
tree.traverse(tree.root, SerchType.DFS)
tree.traverse(tree.root, SerchType.BFS)

# バイナリーサーチする
tree.serch(tree.root, 16)

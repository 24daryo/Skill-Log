import Utility as U


# マージソート
def Merge(array) -> list:
    size = len(array)

    if size <= 1:
        return array
    else:
        # 半分の位置を求める
        mid = int(size / 2)

        # リストを左右に分割する(再帰処理)
        left = Merge(array[:mid])
        right = Merge(array[mid:])

        # 出力用の配列を作成
        output = []

        # 左右のリストから小さい順に取り出す
        while len(left) != 0 and len(right) != 0:
            if left[0] < right[0]:
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))

        # 残った左右どちらかのリストを出力に結合する
        if len(left) != 0:  # 左が残った
            output += left
        elif len(right) != 0:  # 右が残った
            output += right

        return output


array = U.SetArray(10)
print("配列を初期化")
print(array)

array = U.Shuffle(array)
print("シャッフル後")
print(array)

array = Merge(array)
print("ソート後")
print(array)

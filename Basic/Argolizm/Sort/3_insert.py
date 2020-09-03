import Utility as U


# 挿入ソート(イメージ)
def InsertionSortImage(array) -> list:
    size = len(array)
    for i in range(size):
        for blank in range(i):
            if array[blank] > array[i]:
                # 対象を取り出し
                target = array.pop(i)
                # 正しい位置に挿入
                array.insert(blank, target)
                break

    return array


# 挿入ソート
def InsertionSort(array):
    size = len(array)

    for i in range(1, size):
        target = array[i]
        blank = i

        # 対象より大きいものは右方向にシフトする。同時に空欄位置も取得する
        while blank >= 1 and target < array[blank-1]:
            array[blank] = array[blank-1]
            blank -= 1

        # シフト後の空スペースに挿入
        array[blank] = target
    return array


array = U.SetArray(10)
print("配列を初期化")
print(array)

array = U.Shuffle(array)
print("シャッフル後")
print(array)

array = InsertionSort(array)
print("ソート後")
print(array)

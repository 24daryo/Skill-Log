import Utility as U


# 選択ソート
# バブルソートより交換回数が少ないのが利点
def Sort(array):
    size = len(array)
    for i in range(size):
        # 最小要素の場所を取得する
        min_id = i
        for j in range(i, size):
            if array[j] < array[min_id]:
                min_id = j
        # 要素を交換する
        array[i], array[min_id] = array[min_id], array[i]
    return array


array = U.SetArray(100)

array = U.Shuffle(array)
print("シャッフル")
print(array)

array = Sort(array)
print("ソート後")
print(array)

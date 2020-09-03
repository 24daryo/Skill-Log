import Utility as U


# バブルソート
def bubble_sort(array: list) -> list:
    size = len(array)
    for i in range(size):
        for j in range(i, size):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


array = U.SetArray(100)

array = U.Shuffle(array)
print("シャッフル")
print(array)

array = bubble_sort(array)
print("ソート後")
print(array)

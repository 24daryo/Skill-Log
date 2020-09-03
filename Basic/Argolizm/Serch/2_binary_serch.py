import Utility as U


# ソート済みを前提とする
def binary_serch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            print("{0}番目に{1}が存在します".format(mid, target))
            return
        elif target < array[mid]:
            high = mid - 1
        elif target > array[mid]:
            low = mid + 1

    print("{0}が見つかりませんでした".format(target))
    return


#array = U.SetArray(100)
array = [1, 3, 5, 7, 9, 12, 15, 18, 21, 24, 26, 29]
print(array)
binary_serch(array, 7)

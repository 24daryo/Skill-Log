import Utility as U


# シェルソート
def Sort(array):
    h = len(array) // 2

    while h > 0:
        # h間隔の挿入ソート
        size = len(array)
        for i in range(h, size):
            target = array[i]
            left = i
            while left >= h and target < array[left - h]:
                array[left] = array[left - h]
                left -= h
            array[left] = target
        h //= 2
    return array


array = U.SetArray(100)
print("配列を初期化")
print(array)

array = U.Shuffle(array)
print("シャッフル後")
print(array)

array = Sort(array)
print("ソート後")
print(array)

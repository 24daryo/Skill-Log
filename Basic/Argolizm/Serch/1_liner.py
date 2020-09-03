import Utility as U


def liner_serch(array, target):
    for i, element in enumerate(array):
        if element == target:
            print("{0}番目に{1}が存在します".format(i+1, target))
            return
    print("{0}が見つかりませんでした".format(target))
    return


array = U.SetArray(100)
array = U.Shuffle(array)
print(array)
liner_serch(array, 8)

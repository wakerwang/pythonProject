# coding:utf-8


"""
{1,8, 10, 89, 1000, 1000，1234} 当一个有序数组中，有多个相同的数值时，如何将所有的数值都查找到，比如这里的 1000.
//分析
1. 返回的结果是一个可变数组 ArrayBuffer
2. 在找到结果时，向左边扫描，向右边扫描 [条件]
3. 找到结果后，就加入到ArrayBuffer
"""


def binary_search(list, left, right, finalVal):
    if right < left:
        return []

    mid = (left + right) // 2
    mid_val = list[mid]
    if mid_val > finalVal:
        binary_search(list, left, mid - 1, finalVal)
    elif mid_val < finalVal:
        binary_search(list, mid + 1, right, finalVal)
    else:
        res = []
        # 向左查找
        tmp = mid - 1
        while True:
            if tmp < 0 or list[tmp] != finalVal:
                break
            res.append(tmp)
            tmp -= 1
        # 向右查找
        print("向右查找")
        tmp = mid
        while True:
            print(tmp)
            if tmp > len(list) - 1 or list[tmp] != finalVal:
                break
            res.append(tmp)
            tmp += 1
        return res
    return []


ll = [1, 8, 10, 89, 1000, 1000, 1234]
res = binary_search(ll, 0, 6, 1000)
for num in res:
    print(num)

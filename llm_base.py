def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 提前退出标志，如果某一轮没有发生交换，则数组已经有序，无需继续排序
        swapped = False
        for j in range(n - i - 1):
            # 逐对比较相邻元素，将较大的元素交换到后面
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
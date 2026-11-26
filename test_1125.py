# 11-25 写一个小程序 对一组数字 分成两份和相等的组合
# 例如 [1,2,3,4,5,7] -> [1,2,5] [3,4,6] 这里1，2，5的和是8，3，4，6的和不是8啊
# 这里总和是22，所以两份各自是11，那么1+7+3就组成一份，另一份是[2,4,5],这是一种组合，需要找出全部的组合并返回


def split_array(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        print("数组元素之和为奇数，无法分成和相等的两份")
        return None
    target = total_sum // 2
    # 先找出所有和为 target 的子集，每个子集与它的补集是同一种分割的两个面
    subsets = find_combinations(arr, target)
    # 配对去重：子集和补集只算一种分割
    pairs = []
    seen = set()
    for subset in subsets:
        if frozenset(subset) in seen:
            continue
        complement = [x for x in arr if x not in subset]
        pairs.append([subset, complement])
        seen.add(frozenset(subset))
        seen.add(frozenset(complement))
    return pairs


def find_combinations(arr, target):
    results = []   # 收集所有方案
    path = []      # 当前正在拼的组合

    def backtrack(start, current_sum):
        if current_sum == target:
            # 空格1：为什么用 path[:] 而不是直接 append(path)？想想再填
            results.append(path[:])
            return
        if current_sum > target:
            return                     # 空格2：这行的作用是什么？
        for i in range(start, len(arr)):
            path.append(arr[i])        # 做"选 arr[i]"的决定
            backtrack(i + 1, current_sum + arr[i])   # 空格3：递归下一层
            path.pop()                 # 空格4：这行删掉会怎样？
    backtrack(0, 0)
    return results


def can_split(arr):
    total = sum(arr)
    if total % 2:
        return False
    target = total // 2
    can = [False] * (target + 1)
    can[0] = True                       # 和为 0：什么都不选就能做到
    for num in arr:
        # for s in range(target, num - 1, -1):   # 倒序！
        for s in range(num, target+1):  # 正序，有bug，会让数字重复使用
            if can[s - num]:
                can[s] = True
    return can[target]


def main():
    arr = [1, 3]
    result = split_array(arr)
    print(result)
    print(can_split(arr))


if __name__ == "__main__":
    main()

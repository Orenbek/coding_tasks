# coding=utf-8
def add(num_a, num_b):
    # type: (list[int], list[int]) -> list[int]
    result = []
    a = num_a[::-1]
    b = num_b[::-1]
    for i in range(max(len(a), len(b))):
        out_of_range = i >= len(result)
        sum = b[i] if i >= len(a) else a[i] if i >= len(b) else a[i] + b[i]
        if out_of_range:
            result.insert(i, sum % 10)
        else:
            result[i] += sum % 10
        result.insert(i + 1, int(sum / 10))
    return result[::-1][1:]


def multi(num_a, num_b):
    # type: (list[int], list[int]) -> list[int]
    result = []
    a = num_a[::-1]
    b = num_b[::-1]
    for i, val1 in enumerate(a):
        for j, val2 in enumerate(b):
            if i + j < len(result):
                result[i + j] += val1 * val2
            else:
                result.insert(i + j, val1 * val2)
    index = 0
    while index < len(result):
        if index == len(result) - 1 and result[index] == 0:
            break
        if index + 1 < len(result):
            result[index + 1] += int(result[index] / 10)
        else:
            result.insert(index + 1, int(result[index] / 10))
        result[index] = result[index] % 10
        index += 1
    return result[::-1][1:]


def main(num):
    if num == 0:
        return 0
    result = [1]
    pre_sum = [1]
    for index in range(1, num):
        pre_sum = multi(pre_sum, [index + 1])
        result = add(result, pre_sum)
    return ''.join(map(str, result))


print(main(int(input())))

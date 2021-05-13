#

def solution(a, b):
    answer = 1234567890
    if len(a) != len(b):
        raise Exception(f"The size of lists are different")
    else:
        result = 0
        for i in range(len(a)):
            result += a[i] * b[i]
        answer = result
    return answer


if __name__ == '__main__':
    listA01 = [1, 2, 3, 4]
    listB01 = [-3, -1, 0, 2]
    listA02 = [-1, 0, 1]
    listB02 = [1, 0, -1]


    # print(f"listA : {print(solution(listA01, listB01))}, ListB : {print(solution(listB02, listB02))}")


    print(solution(listA01, listB01))
    print(solution(listA02, listB02))
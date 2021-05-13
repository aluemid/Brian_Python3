from itertools import combinations as cb
# combinations(iterable, r) ==>
# Return r length subsequences of elements from the input iterable.


def check(total):
    for i in range(2, total):
        if total % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    if len(nums) == 0:
        raise Exception('nums is empty')
    else:
        for c in cb(nums, 3):
            if check(sum(c)):
                answer += 1



        # for i in range(0, len(nums) -2):
        #     for j in range(i+1, len(nums) -1):
        #         for k in range(j+1, len(nums)):
        #             if check(nums[i], nums[2], nums[k]):
        #                 answer += 1


    return answer

def prime_number(x):
    answer = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            answer += 1
    return 1 if answer == 1 else 0

def solution2(nums):
    return sum([prime_number(sum(c)) for c in cb(nums, 3)])







if __name__ == '__main__':
    test01 = [1,2,3,4]
    test02 = [1,2,7,6,4]

    print(solution(test01))
    print(solution(test02))
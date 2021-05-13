def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count1 = 0
    count2 = 0
    count3 = 0


    for i in range(len(answers)):
        if(answers[i] == person1[i % len(person1)]): # Point!! 반복되는 패턴을 이해하고 i값을 각 답 리스르의 값으로 나눈값을 인덱스로하여 비교한다.
            count1 += 1
        if(answers[i] == person2[i % len(person2)]):
            count2 += 1
        if(answers[i] == person3[i % len(person3)]):
            count3 += 1

    # print(f"{count1} / {count2} / {count3}")

    maxScore = max(count1, count2, count3)
    if count1 == maxScore:
        answer.append(1)
    if count2 == maxScore:
        answer.append(2)
    if count3 == maxScore:
        answer.append(3)
    return answer


def solution2(answers):
    people = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    count = [0] * len(people)


    # enumerate(iterable, start=0)
    # Return an enumerate object.
    # iterable must be a sequence, an iterator, or some other object which supports iteration.
    # The __next__() method of the iterator returned by enumerate() returns a tuple containing a count(from start which defaults to 0) and the values obtained from iterating over iterable.


    for IndexOfAnswer, AnswerValueOfIndex in enumerate(answers):
        for IndexOfPeople, ListOfPeople in enumerate(people):
            if AnswerValueOfIndex == ListOfPeople[IndexOfAnswer % len(ListOfPeople)]:
                count[IndexOfPeople] += 1

    return [IndexOfCount + 1 for IndexOfCount, valueOfCount in enumerate(count) if valueOfCount == max(count)]

if __name__ == '__main__':
    testAnswer01 = [1, 2, 3, 4, 5]
    testAnswer02 = [1, 3, 2, 4, 2]
    print(solution2(testAnswer01))
    print(solution2(testAnswer02))

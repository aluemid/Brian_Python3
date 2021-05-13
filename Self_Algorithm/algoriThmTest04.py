import collections


def solution(participant, completion):


    # collecitons.Counter(iterable or mapping)
    # A Counter is a dict subclass for counting hashable objects.
    # It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
    # Counts are allowed to be any integer value including zero or negative counts.
    # The Counter class is similar to bags or multisets in other languages.
    # As a dict subclass, Counter Inherited the capability to remember insertion order.
    # Math operations on Counter objects also preserve order.
    # Results are ordered according to when an element is first encountered in the left operand and then by the order encountered in the right operand.


    restOfParticipant = collections.Counter(participant) - collections.Counter(completion)
    print(restOfParticipant)
    answer = list(restOfParticipant.keys())[0]
    print(answer)

    return answer


def solution2(participant, completion):
    answer = ''

    for runner in enumerate(participant):
        for finisher in enumerate(completion):
            print(f"{runner} : {finisher}")
            if runner != finisher:
                break



if __name__ == "__main__":
    participant = ['leo', 'kiki', 'eden']
    completion = ['eden', 'kiki']

    print(solution(participant, completion))
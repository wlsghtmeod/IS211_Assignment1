def listDivide(numbers, divide = 2):
    count = 0
    for x in numbers:
        if x % divide == 0:
            count = count + 1
    return count


def testListDivide():
    assert listDivide([1,2,3,4,5], 2) == 2
    assert listDivide([2, 4, 6, 8, 10],2) == 5
    assert listDivide([30, 54, 63, 98, 100], divide = 10) == 2
    assert listDivide([]) == 0
    assert listDivide([1, 2, 3, 4, 5], 1) == 5


if __name__ == "__main__":
    testListDivide()




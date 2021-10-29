
def getScore(msg):    # Get score from user and validate it
    score = float(input(msg))
    while score < 0:
        print('Score cannot be less than zero')
        score = float(input(msg))
    return score


def display(scoreTest, scoreAssignment):   # Display score for test/assignmnet
    print('{:<8}{:>8}{:>8}{:>8}{:>8}{:>8}'.format('Type', '#', 'min', 'max', 'avg', 'std'))
    for i in range(48):
        print('=', end='')
    print()
    if len(scoreTest) == 0:
        print('{:<8}{:>8}{:>8}{:>8}{:>8}{:>8}'.format('Tests', 0, 'n/a', 'n/a', 'n/a', 'std'))
    else:
        num = len(scoreTest)
        minVal = min(scoreTest)
        maxVal = max(scoreTest)
        mean = calcMean(scoreTest)
        std = calcStd(scoreTest, mean)
        std = round(std, 2)
        mean = round(mean, 2)
        print('{:<8}{:>8}{:>8}{:>8}{:>8}{:>8}'.format('Tests', num, minVal, maxVal, mean, std))

    if len(scoreAssignment) == 0:
        print('{:<8}{:>8}{:>8}{:>8}{:>8}{:>8}'.format('Tests', 0, 'n/a', 'n/a', 'n/a', 'std'))
    else:
        num = len(scoreAssignment)
        minVal = min(scoreAssignment)
        maxVal = max(scoreAssignment)
        mean = calcMean(scoreAssignment)
        std = calcStd(scoreAssignment, mean)
        std = round(std,2)
        mean = round(mean,2)
        print('{:<8}{:>8}{:>8}{:>8}{:>8}{:>8}'.format('Programs', num, minVal, maxVal, mean, std))
    print()
    weight = 0
    weight = calcMean(scoreTest) * 0.6 + calcMean(scoreAssignment) * 0.4
    print('The weighted scores is: {:6.2f}'.format(weight))

def calcMean(lst):
    if (len(lst) == 0):
        return 0
    else:
        return sum(lst) / len(lst)

def calcStd(lst, mean):
    sqrt_sum = 0
    for num in lst:
        sqrt_sum += (num - mean) **2
    return (sqrt_sum/len(lst))**0.5

lst_test = []
lst_assignment = []
while True:
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')
    print()
    option = input('==> ')
    if option == '1':
        score = getScore('Enter the new Test score 0-100 ==> ')
        lst_test.append(score)
    elif option == '2':
        score = getScore('Enter the Test to remove 0-100 ==> ')
        if not score in lst_test:
            print('Could not find that score to remove')
        else:
            lst_test.remove(score)
    elif option == '3':
        lst_test.clear()
    if option == '4':
        score = getScore('Enter the new Assignment score 0-100 ==> ')
        lst_assignment.append(score)
    elif option == '5':
        score = getScore('Enter the Assignment to remove 0-100 ==> ')
        if not score in lst_assignment:
            print('Could not find that score to remove')
        else:
            lst_assignment.remove(score)
    elif option == '6':
        lst_assignment.clear()
    elif option == 'D' or option == 'd':
        display(lst_test, lst_assignment)
    elif option == 'Q' or option == 'q':
        break
    else:
        print('Invalid option!')

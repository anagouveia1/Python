#User Login Access

import random
def getUser(answerNumber):
        if answerNumber == 1:
            return "Welcome: Ana"
        elif answerNumber == 2:
            return "Welcome: Wake"
print ('Enter User Code:')

#EQT print(getAnswer(random.randint(1,2)))
r = input()
fortune = getUser(r)
print(fortune)

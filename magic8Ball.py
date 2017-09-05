import random

def getAnswer(answerNumber):
        if answerNumber == 1:
            return 'It is certain'
        elif answerNumber == 2:
            return 'It is decidedly so'
        
#EQT print(getAnswer(random.randint(1,2)))
r = random.randint(1,2)
fortune = getAnswer(r)
print(fortune)

print("")
print("Else as:")
print("Function_1(indexvalue by random variable as BELOW:") 
print(getAnswer(random.randint(1,2)))

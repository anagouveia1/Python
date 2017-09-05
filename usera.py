import random

def getAnswer(answerNumber):
        if answerNumber == 1:
            return 'Ana'
        elif answerNumber == 2:
            return 'Wake'
        
#EQT print(getAnswer(random.randint(1,2)))
print("Enter user code:")
r = input()
fortune = getAnswer(r)
print(fortune)
print("")
print("Else as:")
print("Function_1(indexvalue by random variable as BELOW:") 
print(getAnswer(random.randint(1,2)))

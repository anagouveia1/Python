#function being called from another function:
def spam():
    eggs = 99
    #bacon function is called upon this meal (this creates another local scope)
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    print(eggs)

spam()

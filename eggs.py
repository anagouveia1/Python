#How To Read Global Variables From Local
def spam():
    print(eggs)

eggs = 42
spam()
print(eggs)
print("eggs needed:")
eggs = input()

spam()

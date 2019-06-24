
class pair:

    constant = 5

    def __init__(self , fn , sn):
        self.firstNumber  = fn
        self.secondNumber = sn

    def plus(self , anotherPair):
        self.firstNumber  += anotherPair.firstNumber
        self.secondNumber += anotherPair.secondNumber

    def minus(self , anotherPair):
        self.firstNumber  -= anotherPair.firstNumber
        self.secondNumber -= anotherPair.secondNumber

    def constantPlusPlus(self):
        self.constant += 1


tmp = input("Enter 4 Numbers For Two Pairs\n")

inp = tmp.split(" ")

p1 = pair(int(inp[0]),int(inp[1]))
p2 = pair(int(inp[2]),int(inp[3]))

p1.plus(p2)

p2.minus(p1)

p2.constantPlusPlus()


print(type(int(inp[0])))
#print(p1.firstNumber , p1.secondNumber , p1.constant , "p1 .")
#print(p2.firstNumber , p2.secondNumber , p2.constant , "p2 .")

#l1 = [p1,p2]

#for i in l1:
#    print(i.firstNumber)

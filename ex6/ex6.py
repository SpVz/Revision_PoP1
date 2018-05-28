import random
from collections import defaultdict
Number = random.randint(1000,9999)
#Number=1234
#print(Number)
Number=[int(x) for x in str(Number)]
#SetNumber=set(Number)
DictNumber=defaultdict(list)
for i in range (len(Number)):
    DictNumber[i].append(Number[i])
#print(DictNumber)
cow=0
#bull=0
while cow!=4:
    cow=0
    bull=0
    Guess_Number=int(input("Please enter a number: "))

    while Guess_Number<1000 or Guess_Number>9999:
        Guess_Number=int(input("Please enter a 4 digit number"))

    Guess_Number=[int(x) for x in str(Guess_Number)]
    #SetGuessNumber=set(Guess_Number)
    DictGuessNumber=defaultdict(list)
    for i in range (len(Number)):
        DictGuessNumber[i].append(Guess_Number[i])
    '''for i in range(4):
        if Guess_Number[i]==Number[i]:
            cow+=1'''
    #bull=len(SetNumber&SetGuessNumber)-cow
    #counts={}
    for key in DictNumber:
        if DictNumber[key]==DictGuessNumber[key]:
            cow+=1
    
    for key in DictNumber:
        for key2 in DictGuessNumber:
            if key!=key2 and DictNumber[key]==DictGuessNumber[key2] and DictNumber[key]!=DictGuessNumber[key]:
                bull+=1
    '''if bull>0 and bull<=4:
        #bull-=1
    if bull>4:
        bull-=2'''
    if cow+bull>4 and cow==0:
        bull-=2
    elif cow+bull<=4 and cow==0:
        bull-=1
    else:
        if cow+bull>4 and cow>0:
            bull-=(cow+bull-4)
        elif cow+bull>=4 and bull>0:
            bull-=1
            
    print(cow,"cows",bull,"bulls")




import random

def rolldice():
    roll=random.randint(2,12)
    return roll

#Now,just to test our dice,let's roll the dice 100 times.

x=0
wallet = 100
while x < 1000:
    result = rolldice()
    print (result)
    if result < 8:
        print ("You lose.")
        wallet -=1
        print (wallet)
    else:
        print("You win.")
        wallet +=1
        print (wallet)
        x+=1




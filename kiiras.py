import random
def gambleing():
    gambleing = random.randint(1, 5)
szam = int(input("Melyik számot választod[1-5]:"))
if szam == gambleing:
        print("You won")

elif szam != gambleing:
    print("You lose")
    
lehetoseg = str(input("Wanna play again? Y/N:"))
if lehetoseg == "Y":
    gambleing()

gambleing()
while 




from random import randint

class card:
    #num = input("Enter number of players :")
    #values = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
    #faces = [ '2', '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'J' , 'Q' , 'K' , 'A']
    #suits = ["Diamonds" , "Clubs" , "Hearts" , "Spades"]
    global faces
    global suits
    global values
    game = False
    total = 0
    global handP
    global handH
    global sumPlayer
    global sumDealer
    global j
    global notLoss

    #j = 0
    #lengthF = len(faces)
    #lengthS = len(suits)

    def __init__(self , value , face , suit):
        self.value = value
        self.face = face
        self.suit = suit

    def rand(self):
        faces = [ '2', '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'J' , 'Q' , 'K' , 'A']
        suits = ["Diamonds" , "Clubs" , "Hearts" , "Spades"]
        values = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
        lengthF = len(faces)
        lengthS = len(suits)

        randomFace = randint(0 , lengthF - 1)
        randomSuit = randint(0 , lengthS - 1 )
        if randomFace > 8:
            if randomFace == len(faces) - 1:
                self.value = 11
            else:
                self.value = 10
        else:
            self.value = values[randomFace]

        self.face = faces[randomFace]
        self.suit = suits[randomSuit]

    def getFace(self):
        return self.face

    def hasAce(self):
        if self.face == 'A':
            return True
        else:
            return False

    #def __str__(self):
        #taco = str(self.face)
        #bell = str(self.suit)
        #print(taco + " of " + bell)

#gameNotOver = True
j = 0
while j == 0:
    indexPlayer = 2
    indexHouse = 2

    ans = input("Type deal to deal cards\n")
    if ans == "no":
        break


    handP = []
    handH = []

    card1 = card(0 , '0' , "0") #Creates the decks handP ()
    card1.rand()
    handP.append(card1)
    card2 = card(0 , '0' , "0")
    card2.rand()
    handP.append(card2)
    card3 = card(0 , '0' , "0")
    card3.rand()
    handH.append(card3)
    card4 = card(0 , '0' , "0")
    card4.rand()
    handH.append(card4)
    notLoss = True


    sumPlayer = handP[0].value + handP[1].value
    strsum = str(sumPlayer)
    print("Your cards are " + handP[0].face + " of " + handP[0].suit + " and " + handP[1].face + " of " + handP[1].suit + "   " + strsum)

    print("The dealer is showing a " + handH[1].face + " of " + handH[1].suit)
    sumDealer = handH[0].value + handH[1].value


    while (notLoss):
        ans = input("What would you like to do?\n")

        if ans == "stay":
            print("Dealer has a " + handH[0].face + " of " + handH[0].suit   + " and " + handH[1].face + " of " + handH[1].suit)
            while sumDealer < 17:
                i = 0
                cardTemp = card(0 , '0' , "0") #
                cardTemp.rand()                # Adds a new card
                handH.append(cardTemp)         #
                sumDealer += handH[indexHouse].value
                print("the Dealer hits and adds a " + handH[indexHouse].face + " of " + handH[indexHouse].suit)
                while i < len(handH) and sumDealer > 21:
                    if handH[i].value == 11:
                        sumDealer = sumDealer - 10
                        handH[i].value = 1
                        break
                    i = i + 1

                indexHouse = indexHouse + 1
            strsum = str(sumDealer)
            if sumDealer == sumPlayer:
                print(strsum + " Tie: both numbers are the same" )
            elif sumDealer > sumPlayer:
                    print("Dealers total = " + strsum)
                    print("Dealer busted, You win" if sumDealer > 21 else "You lose")
            else:
                print("Dealers total = " + strsum)
                print("You win!")


            notLoss = False
        elif ans == "hit":
            i = 0
            card5 = card(0 , '0' , "0")
            card5.rand()
            handP.append(card5)
            print("You added a " + handP[indexPlayer].face + " of " + handP[indexPlayer].suit)
            sumPlayer += handP[indexPlayer].value
            indexPlayer = indexPlayer + 1
            while i < len(handP) and sumPlayer > 21:
                if handP[i].value == 11:
                    sumPlayer = sumPlayer - 10
                    handP[i].value = 1
                    break
                i = i + 1
            strsum = str(sumPlayer)
            print("The combined value of your cards is " + strsum)

            if sumPlayer > 21:
                print("busted")
                notLoss = False
















#handP.append(card1)
#handP.append(card2)
#print(handP[0].face + " of " + handP[0].suit)
#print(card1.face + " of " + card1.suit)

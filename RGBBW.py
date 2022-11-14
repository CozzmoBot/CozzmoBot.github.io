import random
import time

global typ, i, c, computer_slap
typ = random.randint(0, 4)
i = 0
c = random.randrange(0, 3)


def Card(typ):
    typ = random.randint(0, 4)
    cardlist = ["Red", "Green", "Blue", "Black", "White"]
    cardchosen = cardlist[typ]
    return cardchosen


def player():
    s = str(input("Slap? y/n"))
    if s == "y":
        slap = True

    else:
        slap = False

    return slap


def computer():
    slap = True
    return slap


def gameloop():
    computercards = 0
    playercards = 0
    cardnum = 52
    cardsout = 0
    i = 0
    while True:

        i += 1
        cardnum -= 1
        cardsout += 1
        if i == 0:
            cardsaid = "Red"

        elif i == 1:
            cardsaid = "Green"

        elif i == 2:
            cardsaid = "Blue"

        elif i == 3:
            cardsaid = "Black"

        elif i == 4:
            cardsaid = "White"

        elif i > 4:
            i = 0

        else:
            print("Terminal Malfunction in code")

        card = Card(typ)
        print("The card said was", cardsaid, "The card laid down was", card)
        time.sleep(0.5)

        playerslap = player()
        if card == cardsaid:
            c = random.randint(0, 2)

            if c >= 1:
                computerslap = computer()

            else:
                computerslap = False

            if computerslap == True and card == cardsaid:
                print("The Computer slapped")
                print("Slapcheck")
                print("The computer gained", cardsout, "cards")
                computercards += cardsout
                cardsout = 0
                time.sleep(3)

            elif playerslap == True and card == cardsaid:
                print("You slapped")
                print("Slapcheck")

                print("you got the cards")
                playercards += cardsout
                print(playercards)
                cardsout = 0
                time.sleep(3)

            elif computerslap == False and playerslap == True:
                print("Missed opportunity")
                time.sleep(3)

            else:
                pass

            c = random.randint(0, 2)

        elif card != cardsaid:
            c = random.randint(0, 22)

            if c <= 1:
                computerslap = computer()

            else:
                computerslap = False

            if computerslap == True and card != cardsaid:
                print("The Computer slapped")
                print("Slapcheck")
                computercards -= 2
                print("The computer lost two cards")
                cardnum += cardsout
                time.sleep(3)

            elif playerslap == True and card != cardsaid:
                print("You slapped")
                print("Slapcheck")

                print("you lost two cards")
                playercards -= 2
                cardnum += cardsout
                time.sleep(3)

            else:
                pass

            c = random.randint(0, 2)

        else:
            continue

        if cardnum == 0 and computercards >= playercards:
            print("The computer won!")
            time.sleep(3)
            print("Computer: 'Play again! :D'")
            break

        elif cardnum == 0 and playercards >= computercards:
            print("Yay you won!")
            print("Computer: 'I want a rematch >:('")
            break

        else:
            continue


#########################
##         end        ###
#########################


if __name__ == "__main__":
    gameloop()

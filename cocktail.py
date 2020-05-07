import random
import webbrowser
def baseChoice():
    base = int(input("Alright let's see what you have. "
                     "Enter the number corresponding to the base alcohol you'd like to work with.\n"
                     "Then I'll give you random cocktails from my library!\n\n"
                     "1. Vodka\n"
                     "2. Rum\n"
                     "3. Gin\n"
                     "4. Tequila\n"))
    if base == 1:
        vodka()
    elif base == 2:
        rum()
    elif base == 3:
        gin()
    elif base == 4:
        tequila()
    else:
        print("OOPS! Looks like that response wasn't valid, please try again")
        baseChoice()


def vodka():
    print("\nSomeone's looking to party tonight!")
    drinklist = ["Kamikaze", "Moscow Mule", "White Russian"]
    chosen = random.choice(drinklist)
    print("\nRandom cocktail: ", chosen)
    print("If you want to learn how to make a ", chosen, " enter Y. For another random choice, enter N")
    redo = str(input("")).upper()
    if redo == "N":
        vodka()
    elif redo == "Y":
        pass
    if chosen == "Kamikaze":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail is equal parts\n"
              "1. Vodka\n"
              "2. TripleSec\n"
              "3. Lime Juice\n"
              "Usually served in a martini glass with a lime wedge, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=EgvCOe2kIC0"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()
    elif chosen == "Moscow Mule":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail contains\n"
              "1. 4oz Ginger beer\n"
              "2. 1.5oz Vodka\n"
              "3. 1/6oz of lime juice\n"
              "Usually served in a copper cup with a lime wedge, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=J7X-AeGHPcE"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()
    elif chosen == "White Russian":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail contains\n"
              "1. 2 parts coffee liqueur\n"
              "2. 5 parts Vodka\n"
              "3. 3 parts Fresh Cream\n"
              "Usually served on the rocks, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=yG7F6q5-vi4"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()
def rum():
    print("\nLooks like you'd like to be in the sand right now, let's make that happen!")
    drinklist = ["Pina Colada", "Mai Tai", "Hurricane"]
    chosen = random.choice(drinklist)
    print("\nRandom cocktail: ", chosen)
    print("If you want to learn how to make a ", chosen, " enter Y. For another random choice, enter N")
    redo = str(input("")).upper()
    if redo == "N":
        rum()
    elif redo == "Y":
        pass
    if chosen == "Pina Colada":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail contains\n"
              "1. 3 parts Pineapple Juice\n"
              "2. 1 part Rum\n"
              "3. 1 part Coconut Cream\n"
              "Served with crushed ice, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=bac9aINop_0"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()
    elif chosen == "Mai Tai":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail contains\n"
              "1. 1.5oz of White Rum\n"
              "2. .5oz of Lime Juice\n"
              "3. .5oz of orange curacao\n"
              "4. .5oz of Orgeat Syrup\n"
              "5. .75oz of Dark Rum\n"
              "Served over ice, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=gb_NvXSYQ_E"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()
    elif chosen == "Hurricane":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail contains\n"
              "1. 1 part Light Rum\n"
              "2. 1 part Lemon Juice\n"
              "3. 1/2 part Over-proofed Rum\n"
              "4. 1/2 part Passion Fruit Syrup\n"
              "5. 1 part Dark Rum\n"
              "Shaken together and served over ice, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=HnSAw14WmLo"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()

def gin():
    print("\nAh, a man of class and refinement")
    drinklist = ["Gin Fizz", "Gimlet", "French 75"]
    chosen = random.choice(drinklist)
    print("\nRandom cocktail: ", chosen)
    print("If you want to learn how to make a ", chosen, " enter Y. For another random choice, enter N")
    redo = str(input("")).upper()
    if redo == "N":
        rum()
    elif redo == "Y":
        pass
    if chosen == "Gin Fizz":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail contains\n"
              "1. 2oz of Gin\n"
              "2. .75oz of Lemon Juice\n"
              "3. .5oz of Maple Syrup\n"
              "4. 1 Egg White\n"
              "5. Soda Water\n"
              "Served over ice with a lemon twist garnish, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=obGhGNUKx30"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()
    if chosen == "Gimlet":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail contains\n"
              "1. 50ml of Lime Syrup\n"
              "2. 50ml of Gin\n"
              "3. Slice of Lime\n"
              "Served in a chilled glass with ice and a lime garnish, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=nCS8hqH9MnE"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()
    if chosen == "French 75":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail contains\n"
              "1. 1tbsp of Lemon Juice\n"
              "2. 1 tsp of Sugar Syrup\n"
              "3. S50ml of Gin\n"
              "4. Champagne\n"
              "Shaken and served in a champagne flute, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=Y7cdLTKs0bg"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()


def tequila():
    print("\nLet's get tropical with some tequila!")
    drinklist = ["Margarita", "Tequila Sunrise", "Paloma"]
    chosen = random.choice(drinklist)
    print("\nRandom cocktail: ", chosen)
    print("If you want to learn how to make a ", chosen, " enter Y. For another random choice, enter N")
    redo = str(input("")).upper()
    if redo == "N":
        rum()
    elif redo == "Y":
        pass
    if chosen == "Margarita":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail contains\n"
              "1. 1.5oz of Tequila\n"
              "2. .5oz of Triple Sec\n"
              "3. 1oz of Lime Juice\n"
              "Served over ice with a lime wedge and salt garnish, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=q-gYcvipozY"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()
    if chosen == "Tequila Sunrise":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail contains\n"
              "1. .5oz of Genadine\n"
              "2. 1.5oz of Tequila\n"
              "3. .5oz of Triple Sec\n"
              "4. 1oz of Orange Juice\n"
              "5. .5oz of Sour Mix\n"
              "Served over ice with a lime wedge and salt garnish, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=NVeTGvwk8y0"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()
    if chosen == "Paloma":
        print("\nLet's make a ", chosen, "!")
        print("This cocktail contains\n"
              "1. 2oz of Tequila\n"
              "2. .5oz of Lime Juice\n"
              "3. 4oz of Grapefruit Soda (To fill the glass)\n"
              "Served over ice with a salt rim garnish, enjoy!\n")
        vid = "https://www.youtube.com/watch?v=9_3h0OWYUtA"
        print("Would you like to see a video on how to properly make a", chosen, "? (Enter Y or N)")
        vidChoice = str(input("")).upper()
        if vidChoice == "Y":
            webbrowser.open_new(vid)
            print("I hope you enjoyed, the video. Now go make one for yourself!")
            exit()
        else:
            print("\n\nThank you, and enjoy your drinking!")
            exit()

def main():
    print("Hello and welcome to the cocktail bar!\n"
          "Here, we'll look at the ingredients you have, "
          "and see which cocktails you can make at home during this quarantine!")
    yn = str(input("\nFirst thing's first, do you drink alcohol? (type y or n + ENTER)").upper())
    if yn == "Y":
        print("\nMy kind of friend!")
        baseChoice()
    elif yn == "N":
        print("Sorry, this doesn't seem to be a safe program for you.")
        exit()
    else:
        print("Sorry, that response isn't valid, try again!\n\n\n\n")
        main()
main()
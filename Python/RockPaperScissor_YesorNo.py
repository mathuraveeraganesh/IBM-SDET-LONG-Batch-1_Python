"""
    
    Enhance the previously written Rock-Paper-Scissors code so that it asks the user if they want to play another round.
    If they say 'Yes', the game should begin again.
    If they say 'No', the game should exit.

"""
while True:

    splayer1=input("Player1-Enter the PlayerName(Rock-Paper-Scissors)")
    splayer2=input("Player2-Enter the PlayerName(Rock-Paper-Scissors)")
    if splayer1==splayer2:
        print("It is tie")
    elif splayer1=="Rock":
        if splayer2=="Scissors":
            print("Rock win")
        else:
            print("Paper Win")
    elif  splayer1=="Scissors":
            if splayer2=="Paper":
                print("Scissors Win")
            else:
                print("Rock Win")
    elif   splayer1=="paper":
            if splayer2=="rock":
                print("Paper Win")
            else:
                print("Scissors Win")
    else:
        print("Please enter the correct Options")

    repeat=input("Please Enter Yes To Repeat or No to Exit Game")
    if repeat=="Yes":
        print("Game Started Again")
    elif repeat=="No":
        raise SystemExit
    else:
        raise SystemExit
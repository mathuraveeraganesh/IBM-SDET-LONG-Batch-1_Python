"""
    Make a two-player Rock-Paper-Scissors game.
    Remember the rules:
        Rock beats scissors
        Scissors beats paper
        Paper beats rock
"""
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
score=0
def tally_score():
    global score
    if input("what color is the sky ") == "blue":
        score=score+1
        print("correct")
    else:
        print("incorrect")
    if input("what color is the grass ") == "green":
        score=score+1
        print("correct")
    else:
        print("incorrect")
    if input("whats red mixed with blue ") == "purple":
        score=score+1
        print("correct")
    else:
        print("incorrect")
    if input("what color is a trees trunk ") == "brown":
        score=score+1
        print("correct")
    else:
        print("incorrect")
    if input("what color are the clouds") == "white":
        score=score+1
        print("correct")
    else:
        print("incorrect")
tally_score()
print("you scored " + score + "/5")
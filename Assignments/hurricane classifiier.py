
speed = float(input("whats the speed of the hurricane"))
if speed < 74:
    print("tropical storm")
elif speed < 96:
    print("catagory 1")
elif speed < 111:
    print("catagory 2")
elif speed < 130:
    print("catagory 3")
elif speed < 157:
    print("catagory 4")
elif speed >= 157:
    print("catagory 5")
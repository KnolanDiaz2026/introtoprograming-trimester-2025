
import random

def mystic_fortune_teller():
    
    
    if True:
        try:
            lucky_number = int(input("Lucky number (int): "))
            years_future = float(input("Years into the future (float): "))
            magical_multiplier = float(input("Magical multiplier (float): "))
            
        except ValueError:
            print(" Wrong ")
    
    mystical_number = (lucky_number * magical_multiplier) + years_future + random.randint(1, 10)
    
    if mystical_number < 20:
        fortune = "Calm period ahead."
    elif mystical_number < 40:
        fortune = "Good news soon."
    elif mystical_number < 60:
        fortune = "A challenge arises, but you'll prevail."
    elif mystical_number < 80:
        fortune = "Love and friendship surround you."
    else:
        fortune = "Great fortune is coming!"
    
    print(" Mystical number:", mystical_number)
    print(" Fortune:", fortune)

mystic_fortune_teller()
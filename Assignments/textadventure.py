def start_adventure():
    print("You meet a wizard on a mountain, Do you:")
    print("1. take his quest")
    print("2. Turn back and go home")

    choice = input("> ")

    if choice == "1":
            take_quest()
    elif choice == "2":
            go_home()
    else:
        print("Invalid choice. Try again.")
        start_adventure()

def go_home():
    print("You decide it's safer at home, you have a family.THE END")

def take_quest():
    print("the wizard tells you to make your journey to slay the evil dragon, what direction do you take to the dragons layer, do you:")
    print("1.go towads the river")    
    print("2.go towards the swamp")
    choice = input("> ")

    if choice == "1":
            the_river()
    elif choice == "2":
            the_swamp()
    else:
        print("Invalid choice. Try again.")
        take_quest()

def the_river():
  print("you arive at the river with no way across what do you do:")
  print("1.wait there")
  print("2.try to swim across")
  print("3.try and walk around")
  choice = input("> ")
  if choice == "1":
            wait_there()
  elif choice == "2":
            swim_across()
  elif choice == "3":
            walk_around()
  else:
        print("Invalid choice. Try again.")
        the_river()



def swim_across():
        print("you try and swim across but realize the current is too strong and get swept away and see a waterfall in the distance do you:")
        print("1.grab onto a overhaning branch")
        print("2.dive under and hope to grab onto a rock")
        choice = input("> ")

        if choice == "1":
            grab_branch()
        elif choice == "2":
            dive_under()
        else:
         print("Invalid choice. Try again.")
        the_river()
def grab_branch():
      print("it breaks instantly as you touch it and fly off the cliff")

def dive_under():
      print("you manage to grab a rock and eventualy run out of breath and drown")

def walk_around():
      print("you try and walk around and run into some bandits, do you:")
      print("1.fight them off")
      print("2.give them everything")
      choice = input("> ")

      if choice == "1":
            fight()
      elif choice == "2":
            give()
            the_river()
      else:
        print("Invalid choice. Try again.")
        the_river()
def fight():
      print("you are out numbered and made into a slave")
      the_river()
def give():
      print("you give them all your belonging and are never seen again")



def the_swamp():
   print("you deside to test your luck in the swamp and run into the biggest snake you have ever seen do you:")
   print("1.RUN")
   print("2.fight")
   choice = input("> ")

   if choice == "1":
            run()
   elif choice == "2":
            fight_snake()
   else:
        print("Invalid choice. Try again.")
        the_river()
def run():
      print("you run as fast as you can and fall into the water and get eaten by the crocodiles")
def fight_snake():
      print("you are over powerd by the snake but some how kill the beast but loose your legs in the battle and live out your days as the SNAKE SLAYER")

def wait_there():
  print("you deside to stand and wait after a day a goblin apears do you:")
  print("1.hear him out")
  print("2.fight him")
  choice = input("> ")

  if choice == "1":
            hear_him()
  elif choice == "2":
            fight_him()
  else:
        print("Invalid choice. Try again.")
        wait_there()
def hear_him():
      print("he offers to get you across the river, and give you bit of info for your journy, for a fee do you:")
      print("1.pay fee")
      print("2.dont pay fee")
     
      choice = input("> ")

      if choice == "1":
            pay_fee()
      elif choice == "2":
            dont_pay()
      else:
        print("Invalid choice. Try again.")
        wait_there()


def fight_him():
      print("you kill him easily but cant get across the river")
      hear_him()


def pay_fee():
      print(" he sends you across the river he tells you to remember the word ,macaroon, where do you go next")
      print("1.through the dark forest")
      print("2.through the village")
      choice = input("> ")

      if choice == "1":
            dark_forest()
      elif choice == "2":
            go_villa()
      else:
        print("Invalid choice. Try again.")
        hear_him()


def dont_pay():
      print("you tell him you will not pay he begins to walk away do you:")
      print("1.force him to get you across")
      print("2.let him leave and set up camp")
      choice = input("> ")

      if choice == "1":
            force_him()
      elif choice == "2":
            set_up()
      else:
        print("Invalid choice. Try again.")
        hear_him()

def force_him():
      print(" he sends you across the river where do you go next")
      print("1.through the dark forest")
      print("2.through the village")
      choice = input("> ")

      if choice == "1":
            dark_forest()
      elif choice == "2":
            go_villa()
      else:
        print("Invalid choice. Try again.")
        hear_him()

def set_up():
      print("you fall asleep in your camp and get stung by a scorpion")
      hear_him()




def dark_forest():
      print("you enter the forest and see it has killer bats that chase you out. if only you had somthing to reatch them, see if thers somthing in the village")
      hear_him()




def go_villa():
      print("you are walking through the village and are hungry but may need a bow do you:")
      print("1.buy food")
      print("2.buy a bow")
      print("3.buy a cool hat")







start_adventure()
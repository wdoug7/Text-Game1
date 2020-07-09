#imports
import random
import sys



#text walls
intro = "Before the journey begins, your soul must reincarnate into the husk of a Bounded Knight, Assassin, or Forbidden Traveler"

def exit_fun(): 
     sys.exit("You have lost this life, but your soul is hungry for resurrection.")


#Class for Character Selection, defines attack, defense, magic
class character_class:
    def __init__(self,atk,df,fate):
        self.atk = atk
        self.df = df
        self.fate = fate
        
#Class Choices
Bounded_Knight = character_class(50,40,10) 
Assassin = character_class(60,25,15)
Forbidden_Traveler = character_class(20,20,60)
    
#Difficulty Modifiers
easy = 0.8
normal = 1
hard = 1.2

#Starting Vars
gold = 50
inventory = []



#difficulty selection
while True:
        #choose from easy, normal, hard
        diff = input("Choose Your Difficult: ")
        if diff == "easy":
            current_diff = easy
            break
        elif diff == "normal":
            current_diff = normal
            break
        elif diff == "hard":
            current_diff = hard
            break
        else:
            print("Not a valid input, please try again")



print (intro)

#Class Selection
while True:
        diff = input("Choose Your Class: ")
        if diff == "Bounded Knight":
            current_class = Bounded_Knight
            break
        elif diff == "Assassin":
            current_class = Assassin
            break
        elif diff == "Forbidden Traveler":
            current_class = Forbidden_Traveler
            break
        else:
            print("Not a valid input, please try again")


print("A man approaches you with a rock in his right hand. He seems hungry.")

#choose ""attack" or "offer gold"
choice_1 = input("Do you attack him, or offer him a few gold? ") 

#First attack encounter; class descriptions, no reliance on attack or defense stats or difficulty modifiers
if choice_1 == "attack":
    if current_class == Bounded_Knight:
        print("You unsheathe your large sword and swing horizontally in a large swooping motion. The length of the blade cuts the man in two before he even had a chance to enter arms length of you") 
    elif current_class == Assassin:
        print("You sprint up to the man, pull out the knife hidden in your sleeve, and cut his jugular before he even has a chance to react")
    elif current_class == Forbidden_Traveler:
        if Forbidden_Traveler.fate > random.randint(40,70):
            print("You begin to whisper the unholy cantations of your lost tribe. Suddenly, the man is struck down by lightning.")
        else:
            print("You mutter to the Lost Gods, but the man begins to pummel your head in with a rock. It seems the Gods have forsaken you for today.")
            exit_fun()

if choice_1 == "offer gold":
    gold -= 5
    print(f"You throw five gold pieces near his feet. The man eagerly kneels to gather them as you walk away. You have {gold} remaining gold left. ")




        


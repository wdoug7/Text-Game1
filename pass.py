#imports
import random



#text walls
intro = "Before the journey begins, your soul must reincarnate into the husk of a Bounded Knight, Assassin, or Forbidden Traveler"



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


#Starting Vars
gold = 50

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
        elif diff == "Forbidden_Traveler":
            current_class = Forbidden_Traveler
            break
        else:
            print("Not a valid input, please try again")


print("A man approaches you with a rock in his right hand. He seems hungry.")

#choose ""attack" or "offer gold"
choice_1 = input("Do you attack him, or offer him a few gold?") 

if choice_1 == "attack":
    if current_class == Bounded_Knight:
        print("You unsheathe your large sword and swing horizontally in a large swooping motion. The length of the blade cuts the man in two before he even had a chance to enter arms length of you") 
    elif current_class == Assassin:
        print("You sprint up to the man, pull out the knife hidden in your sleeve, and cut his jugular before he even has a chance to react")
    elif current_class == Forbidden_Traveler:





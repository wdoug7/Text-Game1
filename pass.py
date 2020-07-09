



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


while True:
        diff = input("Choose Your Class: ")
        if diff == "Bounded_Knight":
            current_class = easy
            break
        elif diff == "Assassin":
            current_class = normal
            break
        elif diff == "Forbidden_Traveler":
            current_class = hard
            break
        else:
            print("Not a valid input, please try again")


import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        self.number_of_people = 100
        self.bushels_of_grain = 2800
        self.acres_of_land = 1000
        self.land_value = 19
        self.year = 1
        self.people_starved = self.number_of_people - (self.bushels_of_grain // 20)
        #self.people_entering = 
        
    
    def print_summary(self):
        print(f"\nO great Hammurab!")
        print(f"You are in year {self.year} of your 10 year rule over the reat kingdom of Sumer")
        print(f"In the previos year {self.people_starved} people starved to death.")
        #print(f"In the previous year {self.people_entering} people entered the kingdom.")
        print(f"The population is now {self.number_of_people}.")
        print(f"We harvested 3000 bushels at 3 bushels per acre.")
        #print(f"Rats destroyed 200 bushels, leaving {self.bushels_of_grain} in stroage.")
        print(f"The city owns {self.acres_of_land} acres of land.")
        print(f"Land is currently worth {self.land_value} bushels per acre.")

    def ask_how_many_acres_to_buy(self):
        while True:    
            acres = int(input("How many acres of land would you like to buy?")) 
            if acres > 0 and acres <= self.bushels_of_grain * self.land_value: #user enters positive # and user has enough grain to purchase land
                 self.acres_of_land += acres  #add acres purchased to acres of land owned
                 self.bushels_of_grain -= acres * self.land_value  #decrease bushels by the amount of land purchased
                 return acres
            elif acres > 0 and acres > self.bushels_of_grain * self.land_value:  # user enters a positive # number but does not have enough grain
                 print(f"O wise King Hammurabi, thy granaries only have {self.bushels_of_grain} and lack the bushels required to purchase the desired land; reconsider thy request.")
            else:
                    if acres < 0:
                        print("O mighty King Hammurabi, if thou dost wish to purchase negative acres of land, let it be known that such a request is a jest unworthy of thy grandeur.")
                        print("Instead, wise ruler, thou shouldst select the sell option, for only thus shall thy royal accounts be made right.")
                    else:
                        print("O Great Hammurabi, thou must enter a positive number to buy land.")

    def ask_how_many_acres_to_sell(self):
        while True:    
            acres = int(input("How many acres of land would you like to sell?"))
            if acres > 0 and acres <= self.acres_of_land: #user enters positive # and user has enough land to sell 
                 self.acres_of_land -= acres  #decrease acres sold from acres of land owned
                 self.bushels_of_grain += acres * self.land_value  #increase bushels by the amount of land sold
                 return acres
            elif acres > 0 and acres > self.acres_of_land:  # user enters a positive # number but does not have enough land
                 print(f"O great King Hammurabi, thou canst not sell more land than thou dost possess; thy request exceeds thy holdings of {self.acres_of_land}.")
            else:
                    if acres < 0:
                        print("O esteemed King Hammurabi, having declined to buy land, thou canst not sell a negative amount.")
                        print("Thou must wait until next year to amend thy request.")
                    else:
                        print("O Great Hammurabi, thou must enter a positive number to sell land if thy wishes to sell at all.")


    def ask_how_much_grain_to_feed_people(self):
        while True:    
            bushels = int(input("How much grain would you like to feed the great people of Sumer?"))
            if bushels > 0 and bushels <= self.bushels_of_grain: #user enters positive # and user has enough grain to feed
                self.bushels_of_grain -= bushels  #decrease bushels from total bushels
                return bushels
            elif bushels > 0 and bushels > self.bushels_of_grain:  # user enters a positive # number but does not have enough grain
                 print(f"O Great Hammurabi, we have only {self.bushels_of_grain} bushels of grain!")
            else:
                    if bushels < 0:
                        print("O noble King Hammurabi, thou canst not feed thy people with a negative amount of grain.")
                        print("Such a request is contrary to thy wisdom; adjust thy offering to sustain thy subjects.")
                    else:
                        print("O Great Hammurabi, thou must enter a positive number of bushels to feed the people.")


    def ask_how_many_acres_to_plant(self):
        while True:       
            acres_planted = int(input("How many acres of would you like to plant?"))
            if acres_planted < 0: #negative number error
                print("O mighty one, thou cannot plant negative acres of land.")
            elif acres_planted > self.acres_of_land:  #can't plant more land than you own
                print(f"Great Hammurabi, we only have {self.acres_of_land} in our kingdom.")
            elif acres_planted > self.bushels_of_grain/2:  #takes 2 bushels of grain to farm an acre of land
                 print(f"Thou knows it takes two bushels of grain to plant one acre of land!")
                 print(f"We only have {self.bushels_of_grain} bushels in storage!")
            elif acres_planted > self.number_of_people * 10:  #one person can farm 10 acres fof land
                 print(f"We only have {self.number_of_people} available to help plant.")
            else:
                 self.bushels_of_grain -= acres_planted * 2  #Decrease bushels
                 #self.acres_of_land -= acres_planted  #Decrease acres of land??
                 return acres_planted
    

            
            
            



    def new_cost_of_land(self):
        return random.randint(17,23)




        
        # statements go after the declarations

    # other methods go here

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
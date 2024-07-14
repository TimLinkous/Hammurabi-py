import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()
        self.total_starved = 0
        self.total_death_from_plagues = 0
        self.total_bushels_eaten_by_rats = 0
        self.total_immigrants = 0

    def main(self):
        self.playGame()

    def playGame(self):
        print("\n*********************************")
        print("*                               *")
        print("*     WELCOME TO HAMMURABI      *")
        print("*                               *")
        print("*********************************")

        self.population = 100
        self.bushels_of_grain = 2800
        self.acres_of_land = 1000
        self.land_value = 19
        self.year = 1
        self.people_starved = 0
        self.people_entering = 0
        self.harvest_per_acre = 3
        self.deaths_from_plagues = 0
        self.bushels_ate_by_rats = 0
        self.immigrants_entered = 0
        self.acres_planted = 0

        for self.year in range(1, 11):
            self.print_summary()

            self.ask_how_many_acres_to_buy()
            self.ask_how_many_acres_to_sell()

            grain_to_feed = self.ask_how_much_grain_to_feed_people()
            acres_planted = self.ask_how_many_acres_to_plant()

            initial_population = self.population #uprising wasnt working. needed a variable to store the initial pop

            # plague deaths
            self.deaths_from_plagues = self.plague_deaths(self.population)
            if self.deaths_from_plagues > 0:
                print("\n********************************************************************")
                print(f"A HORRIBLE PLAGUE HAS STRUCK YOUR KINGDOM! {self.deaths_from_plagues} PEOPLE HAVE PERISHED.")
                print("********************************************************************")
                self.total_death_from_plagues += 1
            self.population -= self.deaths_from_plagues

            #Starved people
            self.people_starved = self.starvation_deaths(self.population, grain_to_feed)
            self.total_starved =+ self.people_starved
        
            #uprising
            if self.uprising(initial_population + self.people_starved, self.people_starved):
                print("\nO Fallen Hammurabi, the great famine has ravaged our land and your reign is no more. The people have risen in despair.")
                print("*********")
                print("GAME OVER")
                print("*********")
                self.final_summary()
                return
            
            self.population -= self.people_starved
            
            #Immigrants
            if self.people_starved == 0:
                self.people_entering = self.immigrants(self.population, self.acres_of_land, self.bushels_of_grain)
                self.population += self.people_entering
                self.total_immigrants += self.people_entering
            else:
                self.people_entering = 0

            #Harvest
            total_harvest = self.harvest(acres_planted)
            self.harvest_per_acre = total_harvest // acres_planted if acres_planted > 0 else 0
            self.bushels_of_grain += total_harvest
            self.acres_planted = acres_planted

            #Rats
            self.bushels_ate_by_rats = self.grain_eaten_by_rats(self.bushels_of_grain)
            self.total_bushels_eaten_by_rats =+ self.bushels_ate_by_rats
            self.bushels_of_grain -= self.bushels_ate_by_rats
            

            self.land_value = self.new_cost_of_land()
        
        self.final_summary()
    
    def print_summary(self):
        print(f"\nO great Hammurab!")
        #if self.year == 1:
            #print(f"\nO great Hammurab!")
        #elif self.year > 1 and self.year <= 6:
            #if self.people_starved == 0:
                #print()
        print(f"You are in year {self.year} of your 10 year rule over the great Kingdom of Sumer.")
        print(f"In the previous year {self.people_starved} people starved to death.")
        print(f"In the previous year {self.people_entering} people entered the kingdom.")
        print(f"The population is now {self.population}.")
        print(f"We harvested {self.harvest_per_acre * self.acres_planted} bushels at {self.harvest_per_acre} bushels per acre.")
        print(f"Rats destroyed 200 bushels, leaving {self.bushels_of_grain} in stroage.")
        print(f"The city owns {self.acres_of_land} acres of land.")
        print(f"Land is currently worth {self.land_value} bushels per acre.")

    def final_summary(self):
        print("Final game summary: ")
        print(f"Population: {self.population}")
        print(f"Bushels of Grain: {self.bushels_of_grain}")
        print(f"Acres of Land: {self.acres_of_land}")
        print(f"Deaths from plagues: {self.deaths_from_plagues}")
        print(f'Bushels eaten by rats: {self.bushels_ate_by_rats}')
        print(f"Total starved to death: {self.people_starved}")
        print(f"Total Immigrants: {self.people_entering}")

        if self.people_starved == 0:
            print("O most benevolent King Hammurabi, thy unmatched wisdom and care have ensured that none in thy kingdom went hungry. Thy reign was masterful")
        elif self.people_starved > 0 and self.people_starved <= 10:
            print("O revered King Hammurabi, though thy leadership is commendable, a few of thy subjects have felt the pangs of hunger; let us strive for greater bounty.")
        elif self.people_starved > 5 and self.people_starved <= 25:
            print("O King Hammurabi, while thy reign is just, the hunger of some in thy kingdom reflects a need for better provision.")
        else:
            print("O King Hammurabi, thy people suffered greatly from hunger; such a plight calls for urgent and improved stewardship.")

    #ask questions methods
    def ask_how_many_acres_to_buy(self):
        while True:    
            acres = int(input("How many acres of land would you like to buy?\n")) 
            if acres >= 0 and acres * self.land_value <= self.bushels_of_grain: #user enters positive # and user has enough grain to purchase land
                 self.acres_of_land += acres  #add acres purchased to acres of land owned
                 self.bushels_of_grain -= acres * self.land_value  #decrease bushels by the amount of land purchased
                 return acres
            elif acres > 0:  # user enters a positive # number but does not have enough grain
                 print(f"O wise King Hammurabi, thy granaries only have {self.bushels_of_grain} bushels and lack the bushels required to purchase the desired land; reconsider thy request.")
            else:
                    if acres < 0:
                        print("O mighty King Hammurabi, if thou dost wish to purchase negative acres of land, let it be known that such a request is a jest unworthy of thy grandeur.")
                        print("Instead, wise ruler, thou shouldst select the sell option, for only thus shall thy royal accounts be made right.")
                    else:
                        print("O Great Hammurabi, thou must enter a positive number to buy land.")

    def ask_how_many_acres_to_sell(self):
        while True:    
            acres = int(input("How many acres of land would you like to sell?\n"))
            if acres >= 0 and acres <= self.acres_of_land: #user enters positive # and user has enough land to sell 
                 self.acres_of_land -= acres  #decrease acres sold from acres of land owned
                 self.bushels_of_grain += acres * self.land_value  #increase bushels by the amount of land sold
                 return acres
            elif acres > 0:  # user enters a positive # number but does not have enough land
                 print(f"O great King Hammurabi, thou canst not sell more land than thou dost possess; thy request exceeds thy holdings of {self.acres_of_land}.")
            else:
                if acres < 0: #user enters a negative number
                    print("O esteemed King Hammurabi, having declined to buy land, thou canst not sell a negative amount.")
                    print("Thou must wait until next year to amend thy request.")
                else:
                    print("O Great Hammurabi, thou must enter a positive number to sell land if thy wishes to sell at all.")

    def ask_how_much_grain_to_feed_people(self):
        while True:    
            bushels = int(input("How much grain would you like to feed the great people of Sumer?\n"))
            if bushels >= 0 and bushels <= self.bushels_of_grain: #user enters positive # and user has enough grain to feed
                self.bushels_of_grain -= bushels  #decrease bushels from total bushels
                return bushels
            elif bushels > 0:  # user enters a positive # number but does not have enough grain
                 print(f"O Great Hammurabi, we do not have enough grain. We have only {self.bushels_of_grain} bushels of grain!")
            else:
                    if bushels < 0:
                        print("O noble King Hammurabi, thou canst not feed thy people with a negative amount of grain.")
                        print("Such a request is contrary to thy wisdom; adjust thy offering to sustain thy subjects.")
                    else:
                        print("O Great Hammurabi, thou must enter a positive number of bushels to feed the people.")


    def ask_how_many_acres_to_plant(self):
        while True:       
            acres_planted = int(input("How many acres of would you like to plant?\n"))
            if acres_planted < 0: #negative number error
                print("O mighty one, thou cannot plant negative acres of land.")
            elif acres_planted > self.acres_of_land:  #can't plant more land than you own
                print(f"Great Hammurabi, we only have {self.acres_of_land} in our kingdom.")
            elif acres_planted > self.bushels_of_grain / 2:  #takes 2 bushels of grain to farm an acre of land
                 print(f"Thou knows it takes two bushels of grain to plant one acre of land!")
                 print(f"We only have {self.bushels_of_grain} bushels in storage!")
            elif acres_planted > self.population * 10:  #one person can farm 10 acres of land
                 print(f"We only have {self.population} available to help plant.")
            else:
                 self.bushels_of_grain -= acres_planted * 2  #Decrease bushels
                 return acres_planted
    

    #calculation methods
    def plague_deaths(self, population):
        if self.rand.randint(0, 99) < 15:
             return population // 2
        return 0
        
    def starvation_deaths(self, population, bushels_to_feed):
        people_fed = bushels_to_feed // 20
        return max(0, population - people_fed)
    
    def uprising(self, initial_population, people_starved) -> bool:
        return people_starved > round(initial_population * .45)
    
    def immigrants(self, population, acres_owned, grain_in_stroage):
        if self.people_starved == 0:
            return ((20 * acres_owned + grain_in_stroage) // (100 * population)) + 1
    
    def harvest(self, acres):
         return acres * self.rand.randint(1,6)
        
    def grain_eaten_by_rats(self, bushels):
        if self.rand.randint(0, 99) < 40:
            return bushels * self.rand.randint(10, 30) // 100
        return 0
         
    def new_cost_of_land(self):
        return random.randint(17,23)

    # other methods go here

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
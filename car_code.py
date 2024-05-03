from person import Person

class Car:
    """Class for car that can hold up to 5 people"""

    def __init__(self, make, model, year, lp_number) -> None:
        """"Constructs make, model, year, license plate number and occupants"""
        self.make = make
        self.model = model
        self.year = year
        self.lp_number = lp_number
        self.driver = None
        self.front_passenger = None
        self.back_passenger1 = None
        self.back_passenger2 = None
        self.back_passenger3 = None

    def __str__(self) -> str:
        """returns a string containing the information about the car’s make, model, year, and license plate number"""
        car_info = f"Make: {self.make}. Model: {self.model}. Year: {self.year}. License Plate Number: {self.lp_number}."
        return car_info
    
    def set_driver(self, Person):
        """Sets a driver of legal age"""
        if Person.allowed_to_drive():
            self.driver = Person
            return True
        else:
            return False
        
    def has_driver(self):
        """Checks if car has driver"""
        if self.driver != None:
            return True
        else:
            return False 
        
    def add_passenger(self, Person):
        """Adds occupants to car, with those age 10+ not in front seat"""
        if self.front_passenger is None and Person.allowed_to_drive() > 10:
            self.front_passenger = Person
        elif self.back_passenger1 == None:
            self.back_passenger1 = Person
        elif self.back_passenger2 == None:
            self.back_passenger2 == Person
        elif self.back_passenger3 == None:
            self.back_passenger3 == Person
            return True
        else:
            return False
    
        
    def has_passengers(self):
        if self.front_passenger != None or self.back_passenger1 != None or self.back_passenger2 != None or self.back_passenger3 != None:
            return True
        else:
            return False
        
    def get_num_occupants(self):
        """Counts the number of car occupants including the driver"""
        count = 0
        if self.has_driver():
            count += 1
        if self.front_passenger != None:
            count += 1
        if self.back_passenger1 != None:
            count += 1
        if self.back_passenger2 != None:
            count += 1
        if self.back_passenger2 != None:
            count += 1
        return count
    
    
    def get_num_passengers(self):
        """Counts the number of car occupants excluding the driver"""
        count = 0
        if self.front_passenger != None:
            count += 1
        if self.back_passenger1 != None:
            count += 1
        if self.back_passenger2 != None:
            count += 1
        if self.back_passenger2 != None:
            count += 1
        return count
    
    

    def is_empty(self):
        if self.has_driver() == False and self.has_passengers() == False:
            return "Is empty"
        else:
            return "Is not empty"
        
    def is_full(self):
        """returns whether or not the car is full (all spots for the driver and passenger are taken)"""
        if self.has_driver() and self.get_num_occupants() == 4:
            return "Is full"
        else:
            return "Is not full"

    def list_riders(self):
        """displays the name and age of the driver and 
        each of the passengers in the car, 
        as well as where they are sitting (front or back seat)"""
        occupants = [(self.driver, "front seat as driver"), (self.front_passenger, "front seat"),
                (self.back_passenger1, "back seat"), (self.back_passenger2, "back seat"),
                (self.back_passenger3, "back seat")]

        for occupant, position in occupants:
            if occupant:                    #if the occupant exists, i.e not None
                print("{} sitting in the {}".format(occupant, position))


if __name__ == "__main__":
    #Setting the attributes of car1
    car1 = Car("Tesla", "Model X", 2018, "ZIMGIRL1")  

    #Setting the attributes of car2
    car2 = Car("Nissan", "LEAF", 2010, "1234GH")    

    #executing the string method for car_info of car1     
    car1_information = str(car1)                                                    
    print(car1_information)

    #executing the string method for car_info of car2    
    car2_information = str(car2)                                                    
    print(car2_information)

    #Car Occupants
    person1 = Person("Faith", 23)                            
    person2 = Person("Jepkogei", 6)
    person3 = Person("Ruto", 22)
    person4 = Person("Tracy", 4)
    person5 = Person("Rovina", 19)

    #Setting car1 driver who is of legal age
    set_car1_driver = car1.set_driver(person1)                   
    print(set_car1_driver)

    #Setting car2 driver who is not of legal age
    set_car2_driver = car2.set_driver(person2)                   
    print(set_car2_driver)

    #Checks if car1 has a driver
    car1_driver_present = car1.has_driver()              
    print(car1_driver_present)

    #checks if car2 has a driver
    car2_driver_present = car2.has_driver()              
    print(car2_driver_present)

    #Adds passengers to car1
    added_person2 = car1.add_passenger(person2)
    print(added_person2) #tests the addition
    added_person3 = car1.add_passenger(person3)

    #checks if car1 has passengers
    car1_has_passengers = car1.has_passengers()   

    #checks if car2 has passengers
    car2_has_passengers = car2.has_passengers()  
    print(car2_has_passengers)   

    #Counts the number of car1 occupants including the driver
    num_car1_occupants = car1.get_num_occupants()               
    print(num_car1_occupants)

    #Counts the number of car1 occupants including the driver
    num_car2_occupants = car2.get_num_occupants()               
    print(num_car2_occupants)

    #Counts the number of car1 occupants excluding the driver
    num_car1_passengers = car1.get_num_passengers()               
    print(num_car1_passengers)

    #Counts the number of car1 occupants excluding the driver
    num_car2_passengers = car2.get_num_passengers()                
    print(num_car2_passengers)

    #checks if car1 is empty
    car1_is_empty = car1.is_empty()                         
    print(car1_is_empty)

    #checks if car2 is empty
    car2_is_empty = car2.is_empty()                         
    print(car2_is_empty)

    #checks if car1 is full
    car1_is_full = car1.is_full()                           
    print(car1_is_full)

    #checks if car2 is full
    car2_is_full = car2.is_full()   
    print(car2_is_full)

    #lists all occupants of car1 and their position
    car1.list_riders()

    #lists all occupants of car1 and their position - should be blank
    car2.list_riders()                                  
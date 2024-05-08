import random as random
import time as time
import sys as sys
import csv as csv


sys.stdout = open("Bank_Output.txt", "a", encoding='utf-8') #To log and redirect output 

class Bank_Details:

    list_of_names_used=[

    ]

    def __init__(self, branch_name: str, *services: str):
        
        #Running validations
        if not isinstance (branch_name, str): 
            raise TypeError (f"{branch_name} should be a string of characters!")

        
        for service in services:
            if not isinstance (service, str): 
                raise TypeError (f"{service} should have string representation!")

        if len(services) <= 1:
            print ("You need to input more than one service!")
        
        self.branch_name=branch_name
        self.services=services


    def __repr__ (self) -> str:
        new_services=', '.join(self.services)
        return f"The branch name is: {self.branch_name}. \nThe services offered are: {new_services}"


    def get_branch_name(self):
        print (self.branch_name)


    def change_branch_name (self, new_name: str):
        global list_of_names_used

        if new_name == self.branch_name or new_name in self.list_of_names_used:
            print ("This name is already being (or has been) used!")
        elif len(new_name) <= 0:
            print ("Please provide a valid name")
        elif not isinstance(new_name, str):
            raise TypeError ("Please provide string characters!")

        else:
            try:
                self.branch_name = new_name
                self.list_of_names_used.append(self.branch_name)
            except TypeError as e:
                print (f"An error has occured: {e}")
                
                new_input=str(input("Provide a new name: "))

                if new_input:
                    #Recursive function call
                    self.change_branch_name(new_input)
                else:
                    print ("You have provided an empty string!")
                    return None

        return self.branch_name
    

    def add_service(self, new_service: str):
        #Running validations
        if not isinstance(new_service, str):
            raise ValueError (f"The new service: {new_service}, should have string representation!")
        
        elif new_service in self.services:
            print (f"{new_service} is already a service in {self.branch_name}!")

            try:
                
                new_service_input=str(input("Provide a new service to be added: "))
            
                if new_service_input:
                    self.services+=(new_service_input, )
                else:
                    return None

                return self.services

            except TypeError as e:
                print (f"There was an issue with the opperation")
        
        else:
            self.services+=(new_service, )

        return self.services


    def remove_service(self, service_name: str):
        if not isinstance(service_name, str):
            raise TypeError ("The service you want to remove should have string representation!")
        
        elif service_name not in self.services:
            print(f"{service_name} is not part of the service collection")
            print(" ")
            for service in self.services:
                print(service)
        
        else: 
            service_list=list(self.services)
            service_list.remove(service_name)
            self.services=tuple(service_list)
        
        return self.services
            

class User:
    
    id_list=[

    ]

    customer_name_list=[

    ]

    def __init__ (self, name: str, age: int, date_joined, still_active: bool = True):
        
        global id_list, customer_name_list

        if not isinstance(name, str):
            raise TypeError (f"The name provided: {name}, should have string representation")
        
        elif not isinstance(age, int):
            raise TypeError (f"The age provided: {age}, should have number representation")
        
        if not isinstance(still_active, bool):
            raise TypeError (f"The state provided: {still_active}, should have boolean representation")


        id_characters=['qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890']
        generated_id=''

        #Generating IDs
        for _ in range(5):
            generated_id+=random.choice(id_characters)
            time.sleep(1)
        
        id=generated_id
        
        self.name=name
        self.age=age
        self.date_joined=date_joined
        self.id=id
        self.still_active=still_active
        
        id_list.append(id)
        customer_name_list.append(self.name)

    
    def __repr__(self) -> str:
        return f"Customer name: {self.name}. \nIdentification Number: {self.id}. \nDate Joined: {self.date_joined}. \nStatuse: {self.still_active}"
    

    def change_name(self, initial_name: str, new_name: str):

        global id_list, customer_name_list

        if not isinstance(new_name, str):
            raise TypeError (f"The name provided: {new_name}, should have string representation!")
        elif not isinstance(initial_name, str):
            raise TypeError (f"The name provided: {initial_name}, should have string representation!")

        elif initial_name not in customer_name_list:
            print(f"The name entered: {initial_name}, is not registered in the system")

        else:
            self.name=new_name

        return self.name


    def change_statuse(self):
        if self.still_active == True:
            print(f"{self.name} is still active... \nTo deactivate user, please press 0")
            answer=str(input())

            if answer != '0':
                print("Please select a valid option!")
            
            elif answer=='0':
                self.still_active = False
                print(f"{self.name} of ID {self.id} has been deactivated")

            return self.still_active
        
        elif self.still_active == False:
            print(f"{self.name} is currently inactive... \nTo activate the user, please press 1")
            answer=str(input())
            
            if answer != '1':
                print("Please select a valid option!")
            elif answer=='1':
                self.still_active = True
                print(f"{self.name} of ID {self.id} has been activated")
            
            return self.still_active
        

    def change_age(self, age: int):
        if not isinstance(age, int):
            raise TypeError (f"The value provided: {age}, should be a number!")
        else:
            self.age=age
            print(f"Your age has been changed to: {self.age}")
        
        return self.age

    
class Transactions (User):
    
    deposit_history=[

    ]

    withdraw_history=[

    ]

    def __init__(self, name: str, ammount: float = 0.0, still_active: bool = True):
        super().__init__(name, still_active)

        if not isinstance(ammount, float, int):
            raise TypeError (f"The ammount should be in numerical figures!")
        

        self.name=name
        self.ammount=ammount
        self.still_active=still_active

    def __repr__(self) -> str:
        return f"Name: {self.name}. \nStatuse: {self.still_active}. \nBallance: {self.ammount}"
    

    def deposit(self, deposit_ammount: int):
        global deposit_history

        if self.still_active != True:
            print ("This user is not active...")
        elif not isinstance (deposit_ammount, int, float):
            raise TypeError (f"Provide numerical values!")
        elif deposit_ammount <=0:
            print (f"You cannot deposit anything less or equals to zero! You entered: {deposit_ammount}")
        else:
            try:
                self.ammount+=deposit_ammount
                deposit_history.append(deposit_ammount)

            except TypeError as e:
                print ('There was an issue with the deposit function!')

        
        return self.ammount
    
    
    def withdraw(self, withdraw_ammount):
        global withdraw_history

        if self.still_active!= True:
            print ("This user is not active")
        elif not isinstance (withdraw_ammount, int):
            raise TypeError ("The value provided is not valid!")
        elif self.ammount <= withdraw_ammount:
            print (f"You do not have enough funds for this transaction. \nYour Ballance is {self.ammount}")
        
        else:
            try:
                self.ammount = int((self.ammount-withdraw_ammount))

                withdraw_history.append(withdraw_ammount)
            except TypeError as e:
                print ('There was an issue with the withdraw function')
        
        return self.ammount


    @staticmethod
    def csv_writer():
        global id_list, customer_name_list, deposit_history, withdraw_history

        collection = [

        ]

        try:

            for id, customer, deposit, withdraw in zip(id_list, customer_name_list, deposit_history, withdraw_history):
                collection.append([id, customer, deposit, withdraw])

            with open('bank_information.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)

                # Check if the file is empty
                csvfile.seek(0, 2)  # Move the file pointer to the end
                is_empty = csvfile.tell() == 0

                # Write header if file is empty
                if is_empty:
                    fieldnames = ['id_list', 'customer_name_list', 'deposit_history', 'withdraw_history']
                    writer.writerow(fieldnames)

                # Write data
                for data in collection:
                    writer.writerow(data)

            print("The data has been registered to a csv file. Name: bank_information.csv")
        
        
        except TabError as e:
            print(f"There was an issue with the CSV writer: {e}")


if __name__== 'main':
    print ("Code is running on main document...")
else:
    print ("Module has been exported...")

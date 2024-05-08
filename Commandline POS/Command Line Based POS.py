import csv
"""import sys

output_file= sys.stdout= ("output.txt", "w")
sys.stdout=output_file
"""
class Product:
    
    #Class atributes are accessed using the class name
    list_of_products = [ ]

    def __init__(self, product_name: str, product_id: int, price: float, quantity: int = 1):
        #Running Validations
        #"Raise" is used to provide more valuable information on the error

        if not isinstance (product_name, str):
            raise TypeError (f"{product_name} should be a string!")
        if not isinstance (product_id, int):
            raise TypeError (f"{product_id} should be an integer!")
        if not isinstance (price, float):
            raise TypeError (f"{price} should be a float!")
        if not isinstance (quantity, int):
            raise TypeError (f"{quantity} should be an integer")
        
        assert price >= 0, f"{price} is not a valid price!"


        #Initializing values
        self.product_name=product_name
        self.product_id=product_id
        self.__price = price #Price has been set to a private member; only accessible with relevant authority
        self.quantity=quantity


        Product.list_of_products.append(self) #Adds the attributes to thee list. This will Help write to the csv file


    def __str__(self):
        return f"This class has the following attributes: {self.product_name}, {self.product_id}, {self.__price}, and {self.quantity}."
        #How the object is represented as a string
        #The __repr__ is used to establish plain object representation 


    @property
    def price (self):
        return {self.__price}
        #This is a getter for reading the price

    @price.setter
    def price(self, value: float):
        assert isinstance(value, float), f"{value} should be a float!"

        if value <= 0:
            print(f"{value} should be greater than 0")
        else:
            self.__price = value
            print(f"The price of the item has been changed to {self.__price}")    
        
        #The price setter with relevant validation checks


class Customer:

    list_of_customers = [ ]

    def __init__(self, customer_id: int, email: str):
    
    
        #Running validations
        if not isinstance (customer_id, int):
            raise TypeError (f"The {customer_id} should be an integer!")

        if not isinstance (email, str):
            raise TypeError (f"The {email} should be a string")


        #Initializing values
        self.customer_id=customer_id
        self.email=email
        

        Customer.list_of_customers.append(self)
        #Customer id and email will be appended to the list. This will help for updating the csv file
    

    def __str__(self) -> str:
        return f"The attributes of the class are: {self.customer_id} and {self.email}"
        #Consider having print statement that retruns the methods associated to each class


class Sales (Product, Customer):
    #Class atribute for discount claculation
    discount_rate= 0.2
    #Will have to inherit from product and customer class
    def __init__(self, order_id, order_date, customer_id, price, quantity):

    
        Product.__init__(self, price, quantity)
        Customer.__init__(self, customer_id)

        self.order_id=order_id
        self.order_date=order_date


    def __str__(self):
        return "You can perform the following computations: Calculate Total Price and Calculate discount"


    def calculate_total_price (self):
        price_value=self._Product__price

        return  price_value * self.quantity
    

    def discount(self):
        price_value=self._Product__price
        discount_price= price_value * Sales.discount_rate
        
        return discount_price
    

class CsvWriter(Product, Customer):

    def __init__(self, product_name, quantity, customer_id):
        Product.__init__(self, product_name, quantity)
        Customer.__init__(self, customer_id)

    @staticmethod
    def csv_elements(customer_list, product_list, output_file):
        data_to_write = [ ]

        for customer_id in customer_list:
            for product_name in product_list:
                for quantity in product_list:
                    data_to_write.append({
                        "customer_id": Customer.customer_id,
                        "product_id": Product.product_name,
                        "quantity": Product.quantity
                    })

        
        with open(output_file, 'w', newline='') as csvfile:
            columns= ["customer_id", "product_id", "quantity"]                 

            # Create a CSV DictWriter object
            writer = csv.DictWriter(csvfile, fieldnames=columns)

            # Write the header row
            writer.writeheader()

            # Write the data rows
            for row in data_to_write:
                writer.writerow(row)

"""
if __name__=="__main__":
    print ("Running on main document", file= output_file)
else:
    pass"""


product1 = Product ("Laptop", 1, 1200.0, 2)
product2 = Product ("Phone", 2, 800.0, 3)

print(product1.__str__())

print(Product.list_of_products)
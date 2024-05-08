import tkinter as tk
from tkinter import ttk

class POSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SambaPOS")

        # Initialize data structures for orders, menu items, inventory, and tables
        self.orders = []
        self.menu_items = {
            "Burger": {"price": 10, "ingredient": {"Beef Patty": 1, "Bun": 1}},
            "Pizza": {"price": 15, "ingredient": {"Dough": 1, "Cheese": 1, "Tomato Sauce": 1}},
            "Salad": {"price": 20, "ingredient": {"Lettuce": 1, "Tomato": 1, "Cucumber": 1}}
        }
        self.inventory = {
            "Beef Patty": 50,
            "Bun": 100,
            "Dough": 75,
            "Cheese": 30,
            "Tomato Sauce": 40,
            "Lettuce": 20,
            "Tomato": 30,
            "Cucumber": 25
        }
        self.tables = {
            "Table 1": {"status": "Available", "capacity": 4},
            "Table 2": {"status": "Available", "capacity": 6},
            "Table 3": {"status": "Occupied", "capacity": 2},
            "Table 4": {"status": "Reserved", "capacity": 8}
        }

        # Create UI elements
        self.create_menu_screen()
        self.create_order_entry_screen()
        self.create_order_status_screen()
        self.create_checkout_screen()
        self.create_inventory_management_screen()
        self.create_table_management_screen()
        self.create_reporting_analytics_screen()
        self.create_customer_management_screen()
        self.create_navigation_buttons()

    def create_menu_screen(self):
        self.menu_screen = ttk.Frame(self.root)
        self.menu_screen.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Label(self.menu_screen, text="Menu").pack()
        for item, details in self.menu_items.items():
            ttk.Button(self.menu_screen, text=f"{item}: ${details['price']}", command=lambda i=item, p=details['price']: self.add_to_order(i, p)).pack()

    def create_order_entry_screen(self):
        self.order_entry_screen = ttk.Frame(self.root)
        self.order_entry_screen.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Label(self.order_entry_screen, text="Order Entry").grid(row=0, columnspan=2)
        ttk.Label(self.order_entry_screen, text="Item:").grid(row=1, column=0, padx=5, pady=5)
        self.item_entry = ttk.Entry(self.order_entry_screen)
        self.item_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.order_entry_screen, text="Quantity:").grid(row=2, column=0, padx=5, pady=5)
        self.quantity_entry = ttk.Entry(self.order_entry_screen)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(self.order_entry_screen, text="Add to Order", command=self.add_custom_to_order).grid(row=3, columnspan=2, padx=5, pady=5)

    def create_order_status_screen(self):
        self.order_status_screen = ttk.Frame(self.root)
        self.order_status_screen.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Label(self.order_status_screen, text="Order Status").grid(row=0, columnspan=2)
        self.order_status_text = tk.Text(self.order_status_screen, width=50, height=10)
        self.order_status_text.grid(row=1, column=0, columnspan=2)

    def create_checkout_screen(self):
        self.checkout_screen = ttk.Frame(self.root)
        self.checkout_screen.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Label(self.checkout_screen, text="Checkout / Payment").pack()
        self.total_label = ttk.Label(self.checkout_screen, text="Total Amount: $0.00")
        self.total_label.pack()
        ttk.Button(self.checkout_screen, text="Calculate Total", command=self.calculate_total).pack()

        ttk.Label(self.checkout_screen, text="Discount (%):").pack()
        self.discount_entry = ttk.Entry(self.checkout_screen)
        self.discount_entry.pack()

        ttk.Button(self.checkout_screen, text="Apply Discount", command=self.apply_discount).pack()

        self.final_price_label = ttk.Label(self.checkout_screen, text="Final Price: $0.00")
        self.final_price_label.pack()

        ttk.Button(self.checkout_screen, text="Checkout", command=self.checkout).pack()

    def create_inventory_management_screen(self):
        self.inventory_management_screen = ttk.Frame(self.root)
        self.inventory_management_screen.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Label(self.inventory_management_screen, text="Inventory Management").grid(row=0, columnspan=2)
        self.inventory_text = tk.Text(self.inventory_management_screen, width=50, height=10)
        self.inventory_text.grid(row=1, column=0, columnspan=2)
        ttk.Button(self.inventory_management_screen, text="Check Inventory", command=self.check_inventory).grid(row=2, column=0, columnspan=2, pady=5)

    def create_table_management_screen(self):
        self.table_management_screen = ttk.Frame(self.root)
        self.table_management_screen.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Label(self.table_management_screen, text="Table Management").grid(row=0, columnspan=2)
        ttk.Label(self.table_management_screen, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5)
        self.customer_name_entry = ttk.Entry(self.table_management_screen)
        self.customer_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.table_management_screen, text="Table Number:").grid(row=2, column=0, padx=5, pady=5)
        self.table_number_entry = ttk.Entry(self.table_management_screen)
        self.table_number_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(self.table_management_screen, text="Assign Table", command=self.assign_table).grid(row=3, columnspan=2, padx=5, pady=5)

    def create_reporting_analytics_screen(self):
        # Placeholder for reporting and analytics screen
        pass

    def create_customer_management_screen(self):
        # Placeholder for customer management screen
        pass

    def create_navigation_buttons(self):
        navigation_frame = ttk.Frame(self.root)
        navigation_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        ttk.Button(navigation_frame, text="Menu", command=self.show_menu_screen).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(navigation_frame, text="Order Entry", command=self.show_order_entry_screen).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(navigation_frame, text="Order Status", command=self.show_order_status_screen).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(navigation_frame, text="Checkout", command=self.show_checkout_screen).grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(navigation_frame, text="Inventory Management", command=self.show_inventory_management_screen).grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(navigation_frame, text="Table Management", command=self.show_table_management_screen).grid(row=0, column=5, padx=5, pady=5)

    def show_menu_screen(self):
        self.hide_all_screens()
        self.menu_screen.grid(row=1, column=0, columnspan=2)

    def show_order_entry_screen(self):
        self.hide_all_screens()
        self.order_entry_screen.grid(row=1, column=0, columnspan=2)

    def show_order_status_screen(self):
        self.hide_all_screens()
        self.order_status_screen.grid(row=1, column=0, columnspan=2)

    def show_checkout_screen(self):
        self.hide_all_screens()
        self.checkout_screen.grid(row=1, column=0, columnspan=2)

    def show_inventory_management_screen(self):
        self.hide_all_screens()
        self.inventory_management_screen.grid(row=1, column=0, columnspan=2)

    def show_table_management_screen(self):
        self.hide_all_screens()
        self.table_management_screen.grid(row=1, column=0, columnspan=2)

    def hide_all_screens(self):
        self.menu_screen.grid_remove()
        self.order_entry_screen.grid_remove()
        self.order_status_screen.grid_remove()
        self.checkout_screen.grid_remove()
        self.inventory_management_screen.grid_remove()
        self.table_management_screen.grid_remove()

    def add_to_order(self, item, price):
        self.orders.append({"item": item, "price": price, "status": "New"})
        self.update_order_status_display()
        print(f"Added {item} to the order.")

    def add_custom_to_order(self):
        item = self.item_entry.get()
        quantity = self.quantity_entry.get()

        if item and quantity:
            self.orders.append({"item": item, "quantity": int(quantity), "status": "New"})
            self.update_order_status_display()
            print(f"Added {quantity} {item}(s) to the order.")
        else:
            print("Invalid input.")

    def update_order_status_display(self):
        self.order_status_text.delete(1.0, tk.END)
        for i, order in enumerate(self.orders, start=1):
            self.order_status_text.insert(tk.END, f"Order {i}: {order['item']} ({order['status']})\n")

    def calculate_total(self):
        total = sum(order["price"] for order in self.orders)
        self.total_label.config(text=f"Total Amount: ${total:.2f}")

    def apply_discount(self):
        discount_percentage = float(self.discount_entry.get())
        total = sum(order["price"] for order in self.orders)
        discounted_amount = total * (discount_percentage / 100)
        final_price = total - discounted_amount
        self.final_price_label.config(text=f"Final Price: ${final_price:.2f}")

    def checkout(self):
        total = sum(order["price"] for order in self.orders)
        print(f"Total amount: ${total}")
        self.orders = []  # Clear the orders list
        self.update_order_status_display()

    def check_inventory(self):
        self.inventory_text.delete(1.0, tk.END)
        self.inventory_text.insert(tk.END, "Inventory Levels:\n")
        for item, quantity in self.inventory.items():
            self.inventory_text.insert(tk.END, f"{item}: {quantity}\n")

    def assign_table(self):
        customer_name = self.customer_name_entry.get()
        table_number = self.table_number_entry.get()

        if customer_name and table_number:
            if table_number in self.tables:
                self.tables[table_number]["status"] = "Occupied"
                print(f"Assigned table {table_number} to {customer_name}.")
            else:
                print(f"Table {table_number} does not exist.")
        else:
            print("Invalid input for customer name or table number.")

    def generate_sales_report(self):
        # Generate sales report based on orders
        sales_report = "Sales Report:\n"
        total_sales = sum(order['price'] for order in self.orders)
        sales_report += f"Total Sales: ${total_sales}\n"
        # Display the generated report
        self.display_report(sales_report)

    def generate_inventory_report(self):
        # Generate inventory report based on current inventory levels
        inventory_report = "Inventory Report:\n"
        for item, quantity in self.inventory.items():
            inventory_report += f"{item}: {quantity}\n"
        # Display the generated report
        self.display_report(inventory_report)

    def generate_employee_performance_report(self):
        # Placeholder: Generate employee performance report
        # This could involve analyzing order data and employee performance metrics
        employee_performance_report = "Employee Performance Report:\n"
        # Placeholder for employee performance analysis
        # Display the generated report
        self.display_report(employee_performance_report)

    def visualize_data(self):
        # Placeholder: Visualize data
        # This could involve using libraries like matplotlib or seaborn for data visualization
        pass

    def capture_customer_information(self):
        # Capture customer information such as name, email, and phone
        customer_name = input("Enter customer name: ")
        customer_email = input("Enter customer email: ")
        customer_phone = input("Enter customer phone: ")
        # Placeholder for storing customer information in a database or file
        self.store_customer_information(customer_name, customer_email, customer_phone)
        print("Customer information captured successfully.")

    def store_customer_information(self, name, email, phone):
        # Placeholder for storing customer information in a database or file
        pass

    def implement_loyalty_program(self):
        # Placeholder: Implement loyalty program
        # This could involve assigning loyalty points based on purchases
        pass

    def customer_communication_channels(self):
        # Placeholder: Customer communication channels
        # This could involve sending email or SMS notifications to customers
        pass

    def display_report(self, report):
        # Display the generated report in a new window
        report_window = tk.Toplevel(self.root)
        report_window.title("Generated Report")
        report_label = ttk.Label(report_window, text=report)
        report_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = POSApp(root)
    root.mainloop()

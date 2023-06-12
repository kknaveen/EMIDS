class User:
    def __init__(self, mob_num):
        self.mob_num = mob_num
        self.orders = {}
        
    def register(self):
        # Registration logic goes here
        print("User registered successfully.")
        
    def search_medicines(self,order_id,query):
        # Medicine search logic goes here        
        print("Searching for medicines with query:", query)
        self.orders[order_id] = query

    def place_order(self, prescript):
        order = Order(prescript)
        
        print("Order placed successfully.")

    def cancel_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            print("Order cancelled successfully.")
        else:
            print("Order not found.")

    def view_past_orders(self):
        print("Past order details:")
        for order_id, prescript in self.orders.items():
            print("Order ID:", order_id)
            print("Prescription:", prescript)
            print("")

class Order:
    def __init__(self, prescript):
        self.prescript = prescript
        self.shipping_charges = 0

    def calculate_shipping_charges(self, amount):
        if amount < 1000:
            self.shipping_charges = 50  # Assuming fixed shipping charges of Rs. 50 for orders below Rs. 1000

    def __str__(self):
        return "Order - Prescription: {}, Shipping Charges: Rs.{}".format(self.prescription, self.shipping_charges)


# Create a new user with a phone number
user = User("9876543210")

user.search_medicines(1,"Paracetomol1")
user.search_medicines(2,"Paracetomol2")
user.search_medicines(3,"Paracetomol3")
# Place some orders
user.place_order( "Prescription 1")
user.place_order( "Prescription 2")
user.place_order( "Prescription 3")


# View past order details
user.view_past_orders()

# Cancel an order
order_id_to_cancel = int(input("Enter the order ID to cancel: "))
user.cancel_order(order_id_to_cancel)

# View updated past order details
user.view_past_orders()

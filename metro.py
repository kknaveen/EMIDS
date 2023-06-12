class MetroSmartCard:
    def __init__(self, card_num, initial_bal):
        self.card_num = card_num
        self.bal = initial_bal
        

    def purchase_card(self):
        if self.bal == 0:
            self.bal = 100  # Assuming default amount of Rs. 100 for a new card
            print("Card purchased successfully.")
        else:
            print("You can purchase only one card.")

    def top_up(self, amount):   #top-up(recharging) the card
        self.bal += amount
        print(f"Rs. {amount} added to the card. Current balance: Rs. {self.bal}.")

    def calculate_fare(self, stations_travelled): #Calculating fare amount including discount
            fare = 15 + 5 * (max(stations_travelled - 3,0))#fare for 1st three stations is fixed at 15rs...then 5rs per station
            disc_count = stations_travelled // 5 #number of discounts to be included
            fare_discount = fare - (fare * 0.05 * disc_count) #fare amount including discount
            return fare_discount

    def deduct_fare(self, fare_discount):
        if self.bal >= fare_discount:
            self.bal -= fare_discount
            print(f"Fare deducted: Rs. {fare_discount}. Current balance: Rs. {self.bal}.")
        else:
            print("Insufficient balance. Please top up your card.")

    def enter_station(self):
        if self.bal >= 15:
            print("Entering the station...")
            # Perform necessary operations while entering the station
        else:
            print("Insufficient balance to enter the station. Please top up your card.")

    def exit_station(self):
        if self.bal >= 0:
            print("Exiting the station...")
            # Perform necessary operations while exiting the station
        else:
            print("Insufficient balance to exit the station. Please top up your card.")


# Usage example:

card = MetroSmartCard("123456", 0)  # Create a new card with zero balance
card.purchase_card()  # Purchase the card with default amount added
card.top_up(200)  # Top up the card with Rs. 200
card.enter_station()  # Try to enter the station
card.deduct_fare(card.calculate_fare(9))  # Calculate and deduct fare for 9 stations
card.exit_station()  # Try to exit the station

from movie import Movie

class Money:
    def __init__(self, current_money):
        self.current_money = current_money

    def get_money(self):
        return self.current_money
    
    def set_money(self, film):
        if int(self.current_money) >=film.price:
            self.current_money = int(self.current_money) -int(film.price)
            print("Ticket purchased.")
            print("Remaining balance:", self.current_money)
        else:
            print("You don't have enough money to purchase the ticket.")

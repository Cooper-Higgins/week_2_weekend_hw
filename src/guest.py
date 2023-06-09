class Guest:
    def __init__(self, name, wallet, fav_song, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song
        self.age = age
        self.drunkenness = drunkenness

    def buy_drink(self, drink):
        if self.sufficient_funds(drink):
            self.wallet -= drink.price
            self.drunkenness += drink.alcohol_level

    def buy_food(self, food):
        if self.sufficient_funds(food):
            self.wallet -= food.price
            self.drunkenness -= food.rejuvenation_level

    def sufficient_funds(self, item):
        return self.wallet >= item.price
class Bar:
    def __init__(self, name, rooms, guests, till):
        self.name = name
        self.rooms = rooms
        self.guests = guests
        self.till = till

    def guest_is_old_enough(self, guest):
        return guest.age >= 18

    def guest_can_afford_drink(self, guest, drink):
        return guest.sufficient_funds(drink)

    def guest_too_drunk(self, guest):
        return guest.drunkenness >= 50
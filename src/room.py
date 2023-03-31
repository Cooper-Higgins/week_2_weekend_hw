class Room:
    def __init__(self, name, entry_fee, capacity):
        self.name = name
        self.entry_fee = entry_fee
        self.capacity = capacity
        self.guests = []
        self.playlist = []

    def check_in_guests_to_room(self, guest):
        self.guests.append(guest)

    def check_out_guests_of_room(self):
        self.guests.clear()

    def add_song_to_room_playlist(self, song):
        self.playlist.append(song)

    def no_room_at_the_inn(self, guests, capacity):
        if len(guests) > capacity:
            return "No room at the inn"
        else:   
            return "Come on in!"
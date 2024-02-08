contact_counter = 0

class Contact:
    def __init__(self, array):
        self.id = array[0]
        self.name = array[1]
        self.email = array[2]
        self.phoneNumber = array[3]
        global contact_counter
        contact_counter += 1
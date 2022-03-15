class Chatbot:
    size_map = {
        "1": "Single",
        "2": "Double",
        "3": "Group size"
    }
    drink_map = {
        "1": "Mimosa",
        "2": "Mojito",
        "3": "Gin n Tonic"
    }

    def run(self):
        print("Welcome to the Cocktails Maniacs!")
        drink = self.get_drink_type()
        size = self.get_size()
        print("Alright, that\'s a {} {}!".format(size,drink))

    def print_message(self):
        print("I'm sorry, I did not understand your preference.\n"
              "Please enter the corresponding letter for your response.")

    
    def get_drink_type(self):
        res = input("What type of drink would you like? \n1- Mimosa \n2- Mojito \n3- Gin n Tonic \n> ")

        if res in self.drink_map:
            return self.drink_map.get(res)
        else:
            self.print_message()

    def get_size(self):
        res = input("What size drink can I get for you? \n1- Single \n2- Double \n3- Group size \n> ")
        if res in self.size_map:
            return self.size_map.get(res)
        else:
            self.print_message()
            return self.get_size()


maniacs = Chatbot()
maniacs.run()
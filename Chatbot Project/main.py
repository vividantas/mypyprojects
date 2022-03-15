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
        print("Welcome to the Cocktails Maniacs!\n")
        drink = self.get_drink_type()
        size = self.get_size()
        print("\nDelicious, great choice! Here is your {} {}!".format(size,drink))

    def print_message(self):
        print("\nI'm sorry, I did not understand your preference.\n"
              "Please enter the corresponding number for your response.\n")


    def get_drink_type(self):
        res = input("What type of drink would you like?\n \n1- Mimosa \n2- Mojito \n3- Gin n Tonic \n> ")

        if res in self.drink_map:
            return self.drink_map.get(res)
        else:
            self.print_message()
            return self.get_drink_type()

    def get_size(self):
        res = input("\nWhat size drink can I get for you?\n \n1- Single \n2- Double \n3- Group size \n> ")
        if res in self.size_map:
            return self.size_map.get(res)
        else:
            self.print_message()
            return self.get_size()


maniacs = Chatbot()
maniacs.run()
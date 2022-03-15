class Chatbot:
    size_map = {
        "a": "Small",
        "b": "Medium",
        "c": "Large"
    }
    drink_map = {
        "a": "Brewed Coffee",
        "b": "Mocha",
        "c": "Latte"
    }

    def run(self):
        print("Welcome to the Cafe Maniacs!")
        size = self.get_size()
        drink = self.get_drink_type()
        print("Alright, that\'s a {} {}!".format(size,drink))

    def print_message(self):
        print("I'm sorry, I did not understand your preference.\n"
              "Please enter the corresponding letter for your response.")

    def get_size(self):
        res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
        if res in self.size_map:
            return self.size_map.get(res)
        else:
            self.print_message()
            return self.get_size()

    def get_drink_type(self):
        res = input("What type of drink would you like? \n[a] Brewed Coffe \n[b] Mocha \n[c] Latte \n> ")

        if res in self.drink_map:
            return self.drink_map.get(res)
        else:
            self.print_message()


cafemaniacs = Chatbot()
cafemaniacs.run()




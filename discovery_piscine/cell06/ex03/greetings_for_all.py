#!/usr/bin/env python3


class Greeter: 
    def greetings(self, name='noble stranger'):
        if not isinstance(name, str):
            print("Error! It was not a name.")
        else:
            print(f"Hello, {name}.")

bot = Greeter()

bot.greetings('Alexandra')
bot.greetings('Wil')
bot.greetings()
bot.greetings(42)


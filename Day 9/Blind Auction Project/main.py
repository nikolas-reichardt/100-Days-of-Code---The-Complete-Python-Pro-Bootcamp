# TODO-1: Ask the user for input
game_over = False
dictionary = {}
key=0
while game_over == False:
    user = input("What's your name?")
    user_bid = int(input("How much do you bid?"))


# TODO-2: Save data into dictionary {name: price}
    dictionary[key]= {
        "name" : user,
        "bid" : user_bid
    }
    key += 1
    print("\n" * 20)

# TODO-3: Whether if new bids need to be added
    # TODO-4: Compare bids in dictionary
    if input("Does anyone else wants to bid? yes OR no").lower() == "no":
        game_over = True
        highest_bid = 0
        for number in range(key):
            #print(number)
            #print((dictionary[number]["bid"]))
            if dictionary[number]["bid"] > highest_bid:
                highest_bid = dictionary[number]["bid"]
                winner = dictionary[number]["name"]
    else:
        continue

print(f"the winner is {winner} with a staggering bid of {highest_bid}")

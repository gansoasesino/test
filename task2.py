p1_col = {}
p2_col = {}

diff = 0

differenceslist = []


def checkdifference(card, coll, existingcards, operation):
    cardcopies = coll.get(card)  # returns diff change

    if operation == 1:  # True is for checking after card add, False for checking after card remove

        if cardcopies is None:
            return 1
        elif existingcards > cardcopies:
            return 1
        else:
            return -1
    else:
        if cardcopies is None:
            return -1
        if existingcards < cardcopies:
            return 1
        else:
            return -1


def add_card(card, coll):
    cardcopies = coll.get(card)

    if cardcopies is None:
        coll[card] = 1
        cardcopies = 1
    else:
        cardcopies += 1
        coll[card] = cardcopies

    return cardcopies


def remove_card(card, coll):
    cardcopies = coll.get(card)

    # no exception handling here

    cardcopies -= 1

    if cardcopies == 0:
        coll.pop(card)
    else:
        coll[card] = cardcopies

    return cardcopies


p1_coll_size, p2_coll_size, changes = map(int, input("Enter collection sizes and number of changes: ").split())

p1_starting_coll = input("Enter the first player's card pool: ").split()

for i in range(p1_coll_size):
    add_card(int(p1_starting_coll[i]), p1_col)
    diff += 1

p2_starting_coll = input("Enter the second player's card pool: ").split()

for i in range(p2_coll_size):
    card = int(p2_starting_coll[i])
    copies = add_card(card, p2_col)
    diff += checkdifference(card, p1_col, copies, 1)

print(diff)

for i in range(changes):
    operation, targetplayer, card = input("Enter parameters: ").split()

    operation = int(operation)
    card = int(card)
    if targetplayer == 'A':
        if operation == 1:
            copies = add_card(card, p1_col)
            diff += checkdifference(card, p2_col, copies, operation)
        else:
            copies = remove_card(card, p1_col)
            diff += checkdifference(card, p2_col, copies, operation)
    else:
        if operation == 1:
            copies = add_card(card, p2_col)
            diff += checkdifference(card, p1_col, copies, operation)
        else:
            copies = remove_card(card, p2_col)
            diff += checkdifference(card, p1_col, copies, operation)

    differenceslist.append(diff)

print(differenceslist)






































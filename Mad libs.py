#turns out not a lot of Brits know mad libs! Plug it in to your code editors, hit run and have a laugh.

def the_adventure():
  adjective = input("Please pick an adjective: ")
  name = input("Please pick a name: ")
  noun = input("Please pick a noun: ")
  place = input("Please pick a place: ")
  animal = input("Please pick an animal: ")
  print("Once upon a time, there was a brave " + adjective + " knight named Sir " + name + ". He set off on a quest to find the " + noun + " of " + place + ". Along the way, he encountered a " + adjective + " " + animal + " who offered to be his guide. Together, they faced many " + adjective + " challenges and finally reached the " + place + ". Inside, they discovered a " + adjective + " treasure and celebrated their victory!")

def the_spooky_house():
  adjective = input("Please pick an adjective: ")
  plural_noun = input("Please input a plural noun: ")
  noun = input("Please pick a noun: ")
  sound = input("Please pick a sound: ")
  room = input("Please pick a room: ")
  creature = input("Please pick a creature: ")
  verb = input("Please pick a verb: ")
  print("On a dark and " + adjective + " night, a group of " + plural_noun + " decided to explore the " + adjective + " old house on the hill. They were armed with only a " + noun + " and a " + adjective + " sense of curiosity. As they entered, they heard " + sound + " coming from the " + room + ". Suddenly, a " + adjective + " " + creature + " appeared! They all screamed and " + verb + " back outside as fast as they could.")

def the_pizza_party():
  time = input("Please pick a time: ")
  noun = input("Please pick a noun: ")
  food = input("Please pick a food: ")
  adjective = input("Please pick an adjective: ")
  name = input("Please pick a name: ")
  verb_ing = input("Please pick a verb ending in ing: ")
  plural_noun = input("Please input a plural noun: ")
  print("It was " + time + " for the annual neighborhood " + noun + " party. Everyone brought their favorite " + food + " to share. There were " + adjective + " pizzas, " + plural_noun + " of soda, and a mountain of " + adjective + " desserts. The highlight of the evening was when " + name + " tried to breakdance and ended up " + verb_ing + " into the " + noun + ". It was a night to remember!")

print("Let's do a Madlib!")
print("Firstly, what's your name?")
name = input()
print("Very lovely to meet you " + name)
print("Which Madlib would you like to do? We have 3 to choose from:  The Adventure, The Spooky House and The Pizza Party")
madlib = input().lower()
while madlib != 'the adventure' and madlib != 'the spooky house' and madlib != 'the pizza party':
  print("Please enter one of the following to choose Madlib")
  madlib = input("The Adventure, The Spooky House and The Pizza Party: ").lower()
if madlib == 'the adventure':
  the_adventure()
elif madlib == 'the spooky house':
  the_spooky_house()
elif madlib == 'the pizza party':
  the_pizza_party()

#When the zombie apocalypse began, [person's name] was feeling very [adjective] about the whole situation.
#Instead of panicking, they grabbed a [object] and headed straight to the [place].
#on the way, they saw a [adjective] zombie trying to eat a [food] while wearing a [clothing item].
#It waved and said, "Do you happen to have any [plural noun]?"
# Confused but determined, [person's name] decided to [verb] as loudly as possible to scare the zombies away. 
#Unfortunately, this only attracted a giant group of zombies who all began to [verb] in slow motion.
#Thinking quickly (or not), they threw a [object] into the air, causing a very [adjective] distraction.
#Somehow, this terrible plan worked, and no one really knows why.

persons_name = input("Give me a person's name\n->")
adjective_one = input("Give me an adjective\n->")
object_one = input("Give me an object\n->")
place_one = input("Give me a place\n->")
adjective_two = input("Give me another adjective\n->")
food_one = input("Give me a food\n->")
clothing_item = input("Give me a clothing item\n->")
plural_noun = input("Give me a plural noun\n->")
verb_one = input("Give me a verb\n->")
verb_two = input("Give me another verb\n->")
object_two = input("Give me another object\n->")
adjective_three = input("Give me another adjective\n->")

print("When the zombie apocalypse began, " + persons_name + " was feeling very " + adjective_one + " about the whole situation. Instead of panicking, they grabbed a " + object_one + " and headed straight to the " + place_one + ". On the way, they saw a " + adjective_two + " zombie trying to eat a " + food_one + " while wearing a " + clothing_item + ". It waved and said, 'Do you happen to have any " + plural_noun + "?' Confused but determined, " + persons_name + " decided to " + verb_one + " as loudly as possible to scare the zombies away. Unfortunately, this only attracted a giant group of zombies who all began to " + verb_two + " in slow motion. Thinking quickly (or not), they threw a " + object_two + " into the air, causing a very " + adjective_three + " distraction. Somehow, this terrible plan worked, and no one really knows why.")
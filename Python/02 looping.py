name = input("What's your name? ")

understood = input("{}, do you understand Python while loops? ".format(name))

while understood.lower() != "yes":
    print("Ok, {}, while loops in Python repeat as long as a certain Boolean condition is met.".format(name))
    understood = input("{}, do you understand Python while loops now? ".format(name))
else:
    pass

print("That's great, {}. I'm pleased that you understand while loops now. That was getting repetitive.".format(name))

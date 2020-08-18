myPets = ['Oscar Wildescat', 'Cottonball', 'Snidely Whiplash']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print("I don't have a pet named " + name + '.')
else:
    print(name + ' is one of my pets.')
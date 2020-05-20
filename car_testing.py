from Car import Car

audi = Car("audi", 190)
for attr in dir(audi):
    if attr[0] == '_':
        print(attr)

for item in  audi.__dict__:
    print(item, audi.__dict__[item])


print(audi.__doc__)
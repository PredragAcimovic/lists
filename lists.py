#starting with lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#accessing elements in a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
#using individual values from a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
#3-1 
name = ['marko', 'marija', 'jelena', 'predrag']
print(name[0].title())
print(name[1].title())
print(name[2].title())
print(name[3].title())
#3-2
message = f"Hello my name is {name[0].title()}"
print(message)
#3-3
cars = ['audi', 'bmw', 'mercedes', 'porshe']
message = f"I would like to own {cars[2].title()}"
print(message)
#modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
#adding elements to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
#insering elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
#removing elements from a list
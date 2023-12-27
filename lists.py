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
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[2]
print(motorcycles)
#removing an item using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motrtcycles = motorcycles.pop()
print(motorcycles)
print(popped_motrtcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycles i owned was a {last_owned.title()}.")
#popping items from any position in a list
first_owned = motorcycles.pop(0)
print(f"The first motorcycles i owned was a {first_owned.title()}.")
#removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
#3-4
guests = ['marko teovanovic', 'marija acimovic', 'jelena vujic']
print(guests)
message = f"Hello, will you, {guests[2].title()} come too dinner, tonight at my place?"
print(message)
#3-5
is_unable = guests.pop(1)
print(f"{is_unable.title()}, is not able to come to dinner.")

guests.insert(1, 'petar petrovic')
message = f"Hello, will you, {guests[0].title(), guests[1].title(), guests[2].title()} come too dinner, tonight at my place?"
print(message)
guests.insert(0, 'dragan acimovic')
guests.insert(1, 'dragana acimovic')
guests.append('nikola vujic')
message = f"Hello, will you, {guests[0].title()}, come to dinner, tonight at my place?"
print(message)
message = f"Hello, will you, {guests[1].title()}, come to dinner, tonight at my place?"
print(message)
message = f"Hello, will you, {guests[2].title()}, come to dinner, tonight at my place?"
print(message)
message = f"Hello, will you, {guests[3].title()}, come to dinner, tonight at my place?"
print(message)
message = f"Hello, will you {guests[4].title()}, come to dinner, tonight at my place?"
print(message)
message = f"Hello, will you {guests[5].title()}, come to dinner, tonight at my place?"
print(message)
message = f"Hello my guests, im sorry, but i have only two empty space for dinner, i can invite only two of you."
print(message)
message = f"Hello, {guests[2].title()}, im sorry but i cant invite you."
print(message)
message = f"Hello, {guests[3].title()}, im sorry but i cant invite you."
print(message)
message = f"Hello, {guests[4].title()}, im sorry but i cant invite you."
print(message)
message = f"Hello, {guests[5].title()}, im sorry but i cant invite you."
print(message)
message = f"Hello, {guests[0].title()}, you are still invited!"
print(message)
message = f"Hello, {guests[1].title()}, you are still invited!"
print(message)
#organizing a list
#sorting a list permanently with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
#sorting a list temporaily with the sorted() function 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
#printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print(len(cars))
#3-8
place = ['france', 'italy', 'egypt', 'russia', 'india']
print(place)
place.reverse()
print(place)
print(sorted(place))
len(place)
print(len(place))
#avoiding index errors when working with lists
motorcycles= ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])
#working with list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
#doing more work within a for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to specialized your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

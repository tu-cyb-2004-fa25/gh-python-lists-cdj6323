# in-class exercise for Lecture 03 List



# 1. Fill in the missing code to produce the output: ['honda', 'yamaha', 'suzuki', 'kawasaki']

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

#<<insert your missing code here>>
motorcycles[3] = 'kawasaki'

print(motorcycles)

motorcycles.append('ducati')            #adds to end
motorcycles.insert(0,'kawasaki')        #inserts into stated index, everything else moves
del motorcycles[0]                      #deletes the element
motorcycle_brand = motorcycles.pop(0)   #deletes element from list and returns it
print(motorcycles)
motorcycles.remove('suzuki')            #searches for that string and removes it without needing to know the index, if there are multiple, removes the first one it finds
myindex = motorcycles.index('yamaha')   #finds the index of the item
print(motorcycles)


# 2. Please double each element in the list 

my_list = [1, [4, 6, 12], 7, 8]

#<<insert your missing code here>>

for num in range(len(my_list)):
    if isinstance(my_list[num], list):
        for i in range(len(my_list[num])):
            my_list[num][i] *= 2
    else:
        my_list[num] *= 2
        
print(my_list)


# 3. Fill in the code to produce the following output: [3, 6, 99, 45, 29, 34] 

#  You can insert multiple lines of code, obtain target_list based on list1 and list2

list1 = [3,6,99,12]

list2 = [64,45,29,34]

#<<Insert your code here>>

target_list = list1 + list2 
target_list.remove(12)
target_list.remove(64)
print(target_list)

#Sorting a list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

#permanently sorts the list
motorcycles.sort() 
#temporarily sort list
sorted_list = sorted(motorcycles)
#permanently reverse order
motorcycles.reverse()

print(list(range(1,7))) #makes a list of numbers
print(list(range(1,7,2))) #'2' skips every other

#Loop
squares = []
for value in range(1,11):
    square = value ** 2  #** repersents exponent
    squares.append(square)
print(squares)

#List slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #extract first 3 elements

# Try it yourself exercise

# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit

# (1) Store the locations in a list

places_to_visit = ['Switzerland', 'Australia', 'Figi', 'Iceland', 'St.Lucia']


# (2) Print your list in its original order

print(places_to_visit)

# (3) Print your list in alphabetical order without modifying the actual list

print(sorted(places_to_visit))

# (4) Show that your list is still in its original order by printing it

print(places_to_visit)

# (5) Change the order of your list in reverse order and print it

places_to_visit.reverse()
print(places_to_visit)

# (6) Change your list so it’s stored in reverse-alphabetical order, and print it 

places_to_visit.sort()
print(places_to_visit)



# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive. 

for count in range(1,21):
    print(count)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list. 

mylist = []
for number in range(1,31):
    if number % 3 == 0:
        mylist.append(number)
print(mylist)


# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube. 

third_powers = []
for number in range(1,11):
    third_powers.append(number ** 3)
for element in third_powers:
    print(element)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

list_of_cubes = []
for i in range(1,11):
    list_of_cubes.append(i ** 3)
print(list_of_cubes)
# in-class code

import copy



list1 = [1, 2, 3, 4, ["a", "b"]]

list2 = list1

list3 = list1[:]

list4 = list1.copy()

list5 = copy.copy(list1)

list6 = copy.deepcopy(list1)



list2.append(5)

list3[4].append("c")

list4[0] = 100

list5[4][-1] = "w"

list6[-1].append("c")



'''

# discuss the answers befor runing the following code

print(f"list1: {list1}")

print(f"list2: {list2}")

print(f"list3: {list3}")

print(f"list4: {list4}")

print(f"list5: {list5}")

print(f"list6: {list6}")

'''
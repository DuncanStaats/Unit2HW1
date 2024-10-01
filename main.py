'''
Name: Duncan Staats
Date: 9/30/24
Description: Unit 2 Homework 1
'''


print('Problem 1'.center(20,'-'))


print("Idea 1: Going through a dungeon to amass treasure.")
print("Idea 2: A priate sailing a ship, rocks as obstacles")
print("Idea 3: A person cooking somethings")


print('Problem 2'.center(20,'-'))


cat =r"""
   ,-. __ .-,
 --;`. '   `.'
  / (  ^__^  )
 ;   `(_`'_)' \
 '  ` .`--'_,  ;
~~`-..._)))(((.'
"""
print(cat)


print('Problem 3'.center(20,'-'))


distance = 173.8
m_p_g = int(input("How many miles per gallon does your car get(Whole Numbers Please): "))
gas_price = float(input("How much does a gallon of gas costs near your house: "))
gas_tank = int(input("How many gallons of gas does your car holds(Whole Numbers Please): "))


gallons_needed = distance / m_p_g
cost = round(gallons_needed * gas_price,2)


print(f"The cost to drive from Portland to Seattle is: ${cost} ")
# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(api_url)
# print(response.json())
import json
from json import JSONEncoder

class Car:
    def __init__(self, name, maxspeed, mileage, color = "trắng") -> None:
        self.maxspeed = maxspeed
        self.mileage = mileage
        self.name = name
        self.color = color
        
    def seating_capacity(self, capacity):
        return f"{capacity} chỗ ngồi"
    
class Bus(Car):
    priceBase = 15000
    
    def priceTicket(self, price):
        return f"{price + (self.priceBase * 0.1)} VND"
    
    def seating_capacity(self, capacity):
        return super().seating_capacity(capacity)
    
class BusEncoder(JSONEncoder):
    def defautl(self, o):
        return o.__dict__

bus = Bus("Xe Bus", 100, 3500, "xanh")
seating = bus.seating_capacity(50)
# busDict = dict(bus)
# print("Encode Vehicle Object into JSON")
# busJson = json.dumps(bus)
print(bus)

# print(f"{bus.name} có tốc độ tối đa {bus.maxspeed} km/h, đã đi {bus.mileage} km")
# print(f"{bus.name} có tốc độ tối đa {bus.maxspeed} km/h, đã đi {bus.mileage} km và có {seating}, màu {bus.color}")
# print(bus.priceTicket(20000))
# print(f"{bus.name} màu {bus.color}, có tốc độ tối đa {bus.maxspeed} km/h, đã đi {bus.mileage} km và có {seating}, giá vé là {bus.priceTicket(20000)} ")


# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number "))

# res = num1 * num2
# print("Multiplication is", res)


# print('My', 'Name', 'Is', 'James', sep='**')

# Read file
# fp = open(r'./text.txt', 'r')
# read file
# print(type(fp.read()))
# Closing the file after reading
# fp.close()

# Write file
# text = "This is new content"
# writing new content to the file
# fp = open('./text.txt', 'w')
# fp.write(text)
# fp.close()


# Write 
# file = open("employees.txt", "w")

# for i in range(3):
#     name = input("Enter the name of the employee: ")
#     file.writelines(name)
#     file.write("\n")
	
# file.close()

# print("Data is written into the file.")

# Writeline
# file1 = open("employees.txt", "w")
# lst = []
# for i in range(3):
# 	name = input("Enter the name of the employee: ")
# 	lst.append(name + '\n')
	
# file1.writelines(lst)
# file1.close()
# print(lst)
# print("Data is written into the file.")

# convert num to word 
# from cmath import inf
# from turtle import write
# import inflect

# file2 = open("read_demo.txt", "w")
# p = inflect.engine()
# listnum = []
# for i in range(21):
#     num = p.number_to_words(i)
#     listnum.append(num + ' line' + '\n')
#     print(num)
    
# file2.writelines(listnum)
# file2.close()
# print("Data is written into the file.")

# count line in file txt
# with open(r'./read_demo.txt') as fp1:
#     lines = len(fp1.readlines())
#     print(f"Total line: {lines}")
    
# count line no blank
# count = 0
# with open('read_demo.txt') as fp:
#     for line in fp:
#         if line.strip():
#             count += 1

# print('number of non-blank lines', count)



# testJson = """{"key1": "value1", "key2": "value2"}"""

# data = json.loads(testJson)
# print(data['key2'])

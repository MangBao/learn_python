import day_02_08
import json

def outer_func(who):
    def inner_func():
        print(f"Hello, {who}")
    inner_func()
    
outer_func("World")

name = day_02_08.person1["name"]
print(name)

print(json.dumps(day_02_08.thislist[0]))
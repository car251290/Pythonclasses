
## use of class and example.
class MyClass:
    def __init__(self, name, age, date,hour,minites) -> None:
        try:
            self.name = name
            self.age = age
            self.date = date
            self.hour = hour
            self.minites = minites
            
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
      
    def get_data( self):
        return self.date
      
    def get_hour( self):
        return self.hour + self.minites
      
    def get_minites( self):
        return self.minites
      
# enum example 
from enum import Enum

class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

def check_light(light):
    if light == TrafficLight.RED:
        print("The light is RED")
    elif light == TrafficLight.YELLOW:
        print("The light is YELLOW")
    elif light == TrafficLight.GREEN:
        print("The light is GREEN")
    else:
        print("The light is not working properly")

from enum import Enum
import time

class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

def check_light(light):
    if light == TrafficLight.RED:
        print("The light is RED")
    elif light == TrafficLight.YELLOW:
        print("The light is YELLOW")
    elif light == TrafficLight.GREEN:
        print("The light is GREEN")
    else:
        print("The light is not working properly")

check_light(TrafficLight.RED)
check_light(TrafficLight.YELLOW)
check_light(TrafficLight.GREEN)

### example asynchronous concurrency and parallelism 
def cpu_bound(number):
    return sum(i * i for i in range(number))

def find_sum(number):
    return sum(i for i in range(number))

if __name__ == "__main__":
    number = [5_000_000 + x for x in range(20)]
    
    start_time = time.time()
    for i in number:
        print(find_sum(i))
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
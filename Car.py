# Programmer: Javan Graber
# Date: 4/9/2026
# Program # 2: Car Class

# Define the class with the accelerate, brake, and get_speed methods
class Car:
    # Begin with an initializer method
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    # Create the accelerate method
    def accelerate(self, __speed):
        self.__speed = int(self.__speed + 5)
    # Create the brake method
    def brake(self, __speed):
        self.__speed = int(self.__speed - 5)
    # Create the get_speed method
    def get_speed(self):
        return int(self.__speed)

# Create the main function that gets the user input and displays the
# changing speeds through the several calls of the Car class
def main():
    year_model = input("Please enter your year model: ")
    make = input("Please enter your make: ")

    print(f"We will now test your {year_model} {make} car by changing some speeds")

    # Call for the Car class
    car_call = Car(year_model, make)
    # Accelerate five times and display the speeds
    for count in range (5):
        car_call.accelerate(count)
        print(f"The current speed is {car_call.get_speed()}")

    print("We will now start slowing down.")

    # Brake five times and display the speeds
    for count in range (5):
        car_call.brake(count)
        print(f"The current speed is {car_call.get_speed()}")

if __name__ == "__main__":
    main()

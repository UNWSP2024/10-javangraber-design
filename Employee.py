# Programmer: Javan Graber 
# Date: 4/9/2026
# Program #4 Employee Class:

# Create the Employee class that will save the given employee information and
# then give them
class Employee:
    # Begin with the initializer method
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__ID_number = id_number
        self.__department = department
        self.__job_title = job_title
    # Create the functions for returning the employee information
    def get_name(self):
        return self.__name
    def get_id_number(self):
        return self.__ID_number
    def get_department(self):
        return self.__department
    def get_job_title(self):
        return self.__job_title

# Define the main function that gets the user input, calls for the Employee Class, and
# Displays the information
def main():
        # Enter the first employee information
        name1 = "Susan Meyers"
        id_number1 = 47899
        department1 = "Accounting"
        job_title1 = "Vice President"
        # Do the first call for the Employee class
        employee1 = Employee(name1, id_number1, department1, job_title1)

        # Print the information
        print("Here is the information for the first employee:")
        print(f"Name: {employee1.get_name()}")
        print(f"ID_number: {employee1.get_id_number()}")
        print(f"Department: {employee1.get_department()}")
        print(f"Job title: {employee1.get_job_title()}")
        print("")

        # Enter the second employee information
        name2 = "Mark Jones"
        id_number2 = 39119
        department2 = "IT"
        job_title2 = "Programmer"
        # Do the second call for the Employee class
        employee2 = Employee(name2, id_number2, department2, job_title2)

        print("Here is the information for the second employee:")
        print(f"Name: {employee2.get_name()}")
        print(f"ID_number: {employee2.get_id_number()}")
        print(f"Department: {employee2.get_department()}")
        print(f"Job title: {employee2.get_job_title()}")
        print("")

        # Enter the third employee information
        name3 = "Joy Rogers"
        id_number3 = 81774
        department3 = "Manufacturing"
        job_title3 = "Engineer"
        # Do the third call for the Employee Class
        employee3 = Employee(name3, id_number3, department3, job_title3)

        print("Here is the information for the third employee:")
        print(f"Name: {employee3.get_name()}")
        print(f"ID_number: {employee3.get_id_number()}")
        print(f"Department: {employee3.get_department()}")
        print(f"Job title: {employee3.get_job_title()}")
        print("")


if __name__ == "__main__":
    main()

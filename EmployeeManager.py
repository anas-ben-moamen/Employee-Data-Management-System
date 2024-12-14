import csv

from Employee import Employee


class EmployeeManager:
    def __init__(self, filename="employees.csv"):
        self.filename = filename
        self.employees = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    emp = Employee(row["ID"], row["Name"], row["Position"], row["Salary"], row["Email"])
                    self.employees[emp.emp_id] = emp
        except:
            print("Could not load the file, starting fresh.")  

    def save_data(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Position", "Salary", "Email"])
            writer.writeheader()
            for emp_id in self.employees:  
                writer.writerow(self.employees[emp_id].to_dict())

    def add_employee(self, emp_id, name, position, salary, email):
        if emp_id in self.employees:
            print("Error: Employee ID already exists")
            return False
        new_emp = Employee(emp_id, name, position, salary, email)  
        self.employees[emp_id] = new_emp
        self.save_data()
        return True

    def update_employee(self, emp_id, name=None, position=None, salary=None, email=None):
        if emp_id not in self.employees:
            print("Error: Employee ID not found")
            return False
        emp = self.employees[emp_id]
        if name is not None: emp.name = name 
        if position is not None: emp.position = position
        if salary is not None: emp.salary = salary
        if email is not None: emp.email = email
        self.save_data()
        return True

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            self.employees.pop(emp_id) 
            self.save_data()
            return True
        else:
            print("Error: Employee ID not found")
            return False

    def search_employee(self, emp_id):
        return self.employees.get(emp_id)  # May return None, no default value set

    def list_employees(self):
        return [emp.to_dict() for emp in self.employees.values()]  

def main_menu():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. List Employees")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            email = input("Enter Email: ")
            success = manager.add_employee(emp_id, name, position, salary, email)
            if success:
                print("Employee added successfully!")
            else:
                print("Failed to add employee.")

        elif choice == "2":
            emp_id = input("Enter Employee ID to update: ")
            name = input("New Name (leave blank to skip): ")
            position = input("New Position (leave blank to skip): ")
            salary = input("New Salary (leave blank to skip): ")
            email = input("New Email (leave blank to skip): ")
            updated = manager.update_employee(emp_id, name=name, position=position, salary=salary, email=email)
            if updated:
                print("Employee updated!")
            else:
                print("Could not update employee.")

        elif choice == "3":
            emp_id = input("Enter Employee ID to delete: ")
            deleted = manager.delete_employee(emp_id)
            if deleted:
                print("Employee deleted.")
            else:
                print("Employee ID not found.")

        elif choice == "4":
            emp_id = input("Enter Employee ID to search: ")
            emp = manager.search_employee(emp_id)
            if emp:
                print("Employee Details:", emp.to_dict())
            else:
                print("Employee not found.")

        elif choice == "5":
            employees = manager.list_employees()
            if employees:
                print("Employees:")
                for emp in employees:
                    print(emp)
            else:
                print("No employees in the system.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1-6.")

main_menu()
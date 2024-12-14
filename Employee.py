class Employee:
    def __init__(self, emp_id, name, position, salary, email):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email

    def update_details(self, name=None, position=None, salary=None, email=None):
        if name:
            self.name = name
        if position:
            self.position = position
        if salary:
            self.salary = salary
        if email:
            self.email = email

    def to_dict(self):
        return {
            "ID": self.emp_id,
            "Name": self.name,
            "Position": self.position,
            "Salary": self.salary,
            "Email": self.email
        }
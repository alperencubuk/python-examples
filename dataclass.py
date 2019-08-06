# Dataclass from dict

from dataclasses import dataclass, fields


@dataclass
class Employee:
    name: str
    lastname: str
    mail: str
    phone: int
    age: int
    company: str
    department: str
    team: str
    job_title: str
    salary: int = 0


    def __post_init__(self):
        if self.age<18:
            print('Age must be 18 or higher')
        else:
            print(self.name, self.lastname, self.age)

    
    @classmethod
    def from_dict(cls, env):
        class_fields = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in env.items() if k in class_fields})


employee_info = {
    'name': 'Alperen',
    'lastname': 'Cubuk',
    'mail': 'info@alperencubuk.com',
    'phone': 5551231212,
    'age': 23,
    'company': 'Met',
    'department': 'IT',
    'team': 'Compass',
    'job_title': 'Developer',
    'salary': '5000',
    'EXTRA':'FIELD'
}

employee1 = Employee.from_dict(employee_info)

# Alperen Cubuk
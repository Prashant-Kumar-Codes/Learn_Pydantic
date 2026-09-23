from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, computed_field
from typing import List, Dict, Optional, Annotated

# using model data validator


class Student(BaseModel):
    
    name: Annotated[str, Field(max_length=50, title='Name of the Student', description='Give the name of the student in less than 50 characters', examples=['Prashant', 'Alpha'])]
    age: int = Field(gt=0, lt=45, strict=True)  # custom range using Feild
    standard: int
    email: EmailStr
    portfolio_link: Annotated[Optional[AnyUrl], Field(default=None, description='Added your portfolio link if you have.')]
    contact_detials: Dict[str, int]
    cgpa: float
    skills: List[str]
    
# adding field validation on the email for validation
    @field_validator('email')
    @classmethod
    def email_validator(cls, email_value):
        valid_domain = ['uni.ac.in', 'college.com']
        # e.g. alpha@uvi.ac.in, beta@college.com
        domain_name = email_value.split('@')[-1]
        
        if domain_name not in email_value:
            raise ValueError(f'{email_value} is not a valid email')
        return email_value


# there are two types of modes - 1. after(default) first type validation and then give input for data validaiton to field_validator

# adding field validator on the name to modify it
    @field_validator('name', mode='after')
    @classmethod
    def name_modifier(cls, name_value):
        return name_value.upper()
    
# adding field validator for age
    @field_validator('age', mode='after')
    @classmethod
    def age_validator(cls, age_value):
        if age_value<3:
            raise ValueError('Student\'s age cannot be less than 3')

def create_student():
    student_info = {'name': 'Prashant Kumar',
                    'age': 18,
                    'standard': 14,
                    'email': 'prashant@xx.com',
                    'portfolio_link': 'https://youtu.be/lRArylZCeOs',
                    'contact_detials': {'personal':9837987373, 'parents':'39983872'},
                    'cgpa': 8.12,
                    'skills': ['Python','Machine Learning', 'Deep Learning', 'Web Development']}
    
    valid_student = Student(**student_info)
    
    
    print(f'''Student Detials:
              Name: {valid_student.name}
              Age: {valid_student.age}
              Standard: {valid_student.standard}
              Email: {valid_student.email}
              Portfolio: {valid_student.portfolio_link}
              Contact_Details: {valid_student.contact_detials}
              CGPA: {valid_student.cgpa}
              Skiils: {valid_student.skills}
          ''')

    
    print('Student created successfullly with valid_student')

create_student()
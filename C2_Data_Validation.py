from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# usage of Field:
'''
1. Custom data validation like length, range and other constraints
2. Adding metadata for better API documentation and readility by using Annotated from typing

we use Field from Pydantic and Annotated from typing for more and better options
'''

class Student(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the Student', description='Give the name of the student in less than 50 characters', examples=['Prashant', 'Alpha'])]
    age: int = Field(gt=0, lt=120, strict=True)  # custom range using Feild
    standard: int
    email: EmailStr
    portfolio_link: Annotated[Optional[AnyUrl], Field(default=None, description='Added your portfolio link if you have.')]
    contact_detials: Dict[str, int]
    cgpa: float
    skills: List[str]


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
    
    print(f'''Nmae: {valid_student.name}
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
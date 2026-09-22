from pydantic import BaseModel
from typing import List, Dict, Optional

class Student(BaseModel):
    name: str
    age: int
    standard: int
    contact_detials: Dict[str, int]
    cgpa: float
    skills: List[str]

# ------ Adding optionals -------
# giving a default value for optional is mandatory
class Student_With_Optinal_Info(BaseModel):
    name: str
    age: int
    standard: Optional[int] = None
    contact_detials: Dict[str, int]
    cgpa: Optional[float] = None
    skills: List[str]


def create_student():
    student_info = {'name': 'Prashant Kumar',
                    'age': 18,
                    'standard': 14,
                    'contact_detials': {'personal':9837987373, 'parents':'39983872'},
                    'cgpa': 8.12,
                    'skills': ['Python','Machine Learning', 'Deep Learning', 'Web Development']}
    
    student_info2 = {'name': 'Prashant Kumar',
                'age': 18,
                'contact_detials': {'personal':9837987373, 'parents':'39983872'},
                'skills': ['Python','Machine Learning', 'Deep Learning', 'Web Development']}
    
    valid_student = Student(**student_info)
    valid_student_with_optional_info = Student_With_Optinal_Info(**student_info2)
    
    
    print(f'''Nmae: {valid_student.name}
              Age: {valid_student.age}
              Stadard: {valid_student.standard}
              Contact_Details: {valid_student.contact_detials}
              CGPA: {valid_student.cgpa}
              Skiils: {valid_student.skills}
          ''')
    
    print('Student created successfullly with valid_student')
    
    
    print(f'''Nmae: {valid_student_with_optional_info.name}
              Age: {valid_student_with_optional_info.age}
              Stadard: {valid_student_with_optional_info.standard}
              Contact_Details: {valid_student.contact_detials}
              CGPA: {valid_student_with_optional_info.cgpa}
              Skiils: {valid_student_with_optional_info.skills}
          ''')

create_student()
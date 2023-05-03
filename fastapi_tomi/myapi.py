# python -m pip install fastapi
# pip install uvicorn

# uvicorn 파일명:app --reload
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# GET - GET AN INFORMATION
# POST - CREATE SOMETHING NEW
# PUT - UPDATE
# DELETE - DELETE SOMETHING

students = {
    1:{
        "name":"john",
        "age":17,
        "year":"year 12"
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None

# localhost:8000/docs 주소창에 입력하면 메시지를 볼 수 있음

# localhost:8000/
@app.get("/")
def index():
    return {"name":"First Data"}

# localhost:8000/get-student/1
@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    # = Path(None, description="The ID of the student you want to view", gt=0, lt=3)
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id:int, name: Optional[str]=None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id:int, student:Student):
    if student_id in students:
        return {"Error":"Student exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student : UpdateStudent):
    if student_id not in students:
        return {"Error":"Student odes not exist"}
    
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error":"Student does not exist"}

    del students[student_id]
    return {"Message": "Student deleted successfully"}

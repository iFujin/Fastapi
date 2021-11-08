from fastapi import FastAPI,Path
from typing import  Optional
from pydantic import BaseModel
app=FastAPI()

#already existing 
students={
    1:{"name":'raj',
    "age":'21',
    "year":9999}
    
    ,2:{
        "name":'victor',
        "age":'21',
        "year":99}
    }
#new class
class students_id(BaseModel):
    name:str
    age:int
    year:int

#update class
class update_class(BaseModel):
    name:Optional[str]
    age:Optional[int]
    year:Optional[int]


@app.get("/about")
def index():
    return ("hai i am fujin")

@app.get("/student/{login}")
def student(login:int=Path(None,description='enter login should be 1 or 2')):
    return students[login]

@app.get("/username")
def student(name:Optional[str]=None):
    for student_id in students:
        if students[student_id]['name']==name:
            return students[student_id] 
    return {'data':'is invalid '}

@app.post("/student_id{studid}")
def student_id(studid:int,student:students_id):
    if studid in students:
        return {"error: student already exits"}
    students[studid]=student
    return students[studid]

@app.put("/update_class/{student_id}")
def update_class(student_id:int,student:update_class):
    if student_id not in students:
        return{'error':'student does not exit for updating '}
    if student.name != None:
        students[student_id]['name'] = student.name
    if student.age != None:
        students[student_id]['age']=student.age
    if student.year != None:
        students[student_id]['year']=student.year
    return students[student_id]



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

App = FastAPI()
Studentdb = {}

class Student(BaseModel):
    id : int
    name : str
    email : str
    year : int
    branch : str

@App.get("/api/getstd")
def getstd():
    return {"message" : "To get the Student Data."}

@App.get("/api/getStudents")
response_model = List(Student)
def getStudents():
    return list(Studentdb.values())

@App.get("/api/gatbyidstudent")
response_model = List(Student)
def getbyidstudent(student_id : int):
    student = Studentdb.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail = "student not found")
    return student

@App.post("/api/addstudents", response_model="")
def addstudents(student : Student):
    if student.id in Studentdb:
        raise HTTPException(status_code=404, detail = "student found")
    Studentdb[student.id]=student
    return student

@App.delete("/api/delete/{student.id}")
def deleteStudent(student_id : int):
    if student_id not in Studentdb:
        raise HTTPException(status_code=404, detail = "student found")
    del Studentdb[student_id]
    return {"message" : "Student data deleted Successfully"}




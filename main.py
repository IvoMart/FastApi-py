from os import error
from typing import Optional
from fastapi import FastAPI
from fastapi.param_functions import Path

from models.students import Student, UpdateStudent

app = FastAPI()
'''
/**
End Points
*/

ej.: awesome.com/delete-user

GET - Obtener información
POST - Publicar información
PUT - Editar información (id)
DELETE - Eliminar información (id)

'''


'''
Lanzar con unicorn:
uvicorn main:app --reload

Swagger UI: http://127.0.0.1:8000/docs

'''



# End point Get - main
@app.get("/")
def index():
    # return {"name": "First Info"}
    return students


'''
Definir variable para consulta por parametro (id)
'''


students = {
    1: {
        "name": "Juan",
        "lastname": "Argüello",
        "age": 15,
        "b-day": "26/12/2021"
    }
}



# End point Get - (id) Parametro num. positivo
@app.get("/get-student/{_id}")
def get_students(_id: int = Path(None, gt=0, description="El identificador n° del estudiante al cual está interesado en obtener la información.")):
    try:
      return students[_id]
    except:
      print('Student doesnot exist!!')



# Query parameter Get - (name) ? Parametro string
# Accept null parameter = None (optional)
# test type - int
# Request URL http://127.0.0.1:8000/get-name?name=Juan
@app.get("/get-name")
def get_by_name(name: Optional[str] = None, test : Optional[int] = None):
    try:
        for student_id in students:
            if students[student_id]["name"] == name:
                return students[student_id]
        return {"Data": "Not Found"}
    except Exception:
        print("Error de procesamiento:" + Exception)



# End point Post
@app.post("/create-student")
def create_student(student : Student, student_id : int):
    if student_id in students:
        return {"Error" : "Student already Exists!!"}
    # Add to Students list
    students[student_id] = student
    return students[student_id]


# End point Put
@app.put("/edit-student/{student_id}")
def modif_student(student: UpdateStudent, student_id: int):
    if student_id not in students:
        return {"Error" : "Cannot find student!!"}
    
    try:
        if student.name != None:
            students[student_id].name = student.name
        if student.lastname != None:
            students[student_id].lastname = student.lastname
        if student.age != None:
            students[student_id].age = student.age
        if student.year != None:
            students[student_id].year = student.year
        
        # Edit all  register (id)
        # students[student_id] = student
        return students[student_id]
    except print(error):
        print("An Error occure while editting." + error)

        
        
# End point Delete
@app.delete("/delete-student/{student_id}")
def del_student(student_id: int):
    if student_id not in students:
        return {"Error" : "Cannot find student!!"}
    
    try:
        del students[student_id]
        return { "Message": f"Student deleted succesfully!!  {student_id}" }
    except error:
        print("An Error occure while deleting." + error)
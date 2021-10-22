from typing import Optional
from fastapi import FastAPI
from fastapi.param_functions import Path

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
    return students[_id]



# Query parameter Get - (name) ? Parametro string
# Accept null parameter = None (optional)
# test type - int
# Request URL http://127.0.0.1:8000/get-name?name=Juan
@app.get("/get-name")
def get_by_name(*, name: Optional[str] = None, test : Optional[int] = None):
    try:
        for student_id in students:
            if students[student_id]["name"] == name:
                return students[student_id]
        return {"Data": "Not Found"}
    except Exception:
        print("Error de procesamiento:" + Exception)

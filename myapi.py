# Stopped at 27:11
# https://www.youtube.com/watch?v=tLKKmouUams
from fastapi import FastAPI, Path

app = FastAPI()
# Example data 
students = {
    1: {
        "name":"john",
        "age" : 22,
        "class" : "year 2"
    }
}

#home
@app.get("/")
def index():
    return {"name" : "First Data"}

#Searching student
@app.get("/get-student/{student_id}")
# Path adds a discription on the Fastapi frontend
# Greater than, less than ,greater than/equal ...
# gt, lt ,ge, le

def get_student(student_id: int = Path(None, description="The id of the student",gt=0,lt=3)):
    return students[student_id]


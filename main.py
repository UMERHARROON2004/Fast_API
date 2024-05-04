from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI()
class Animal(BaseModel):
    name: str
    age: int
    address: str
animals_db = [
    Animal(name="Lion", age=5, address="African Forest"),
    Animal(name="Elephant", age=10, address="Jungle"),
    Animal(name="Giraffe", age=7, address="Forest")
]
@app.post("/animals/")
def create_animal(animal: Animal):
    animals_db.append(animal)
    return {"message": "Animal created successfully"}
@app.get("/animals/", response_model=List[Animal])
def get_animals():
    return animals_db
@app.get("/animals/{name}", response_model=Animal)
def get_animal_by_name(name: str):
    for animal in animals_db:
        if animal.name == name:
            return animal
    raise HTTPException(status_code=404, detail="Animal not found")
@app.put("/animals/{name}")
def update_animal_name(name: str, new_name: str):
    for animal in animals_db:
        if animal.name == name:
            animal.name = new_name
            return {"message": "Animal name updated successfully"}
    raise HTTPException(status_code=404, detail="Animal not found")
@app.delete("/animals/{name}")
def delete_animal(name: str):
    for i, animal in enumerate(animals_db):
        if animal.name == name:
            del animals_db[i]
            return {"message": "Animal deleted successfully"}
    raise HTTPException(status_code=404, detail="Animal not found")

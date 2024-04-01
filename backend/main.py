from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import uuid

class Recipe(BaseModel):
    recipe_id: Union[str, None] = None
    title: str
    description: str
    preparation_time: int
    estimated_cost: Union[float, None] = None



#CORS CONFIG
    
# Configure CORS
origins = [
    "*",  # Replace with your React app's origin
    
]



app = FastAPI(title="Recipe Sharing API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

example_recipes = [
        {
            "id": 0,
            "title": "Super Cake",
            "ingredients": [
                {"id": 1, "description": "Add sugar"},
                {"id": 2, "description": "Add butter"},
                {"id": 3, "description": "Add waterRRRRRRRRRaaaa"},
            ],
            "steps": [
                {"id": 1, "description": "Stir"},
                {"id": 2, "description": "Mix"},
                {"id": 3, "description": "Serve"},
            ],
        },
        {
            "id": 1,
            "title": "Recipe 2",
            "ingredients": [{"id": 1, "description": "Add salt"}],
            "steps": [{"id": 1, "description": "Mix"}],
        },
        {
            "id": 2,
            "title": "Recipe 3",
            "ingredients": [{"id": 1, "description": "Add flour"}],
            "steps": [{"id": 1, "description": "Bake"}],
        },
    ]
# read recipes
@app.get("/recipes")
async def get_all_recipes():
    #example_recipes = ["recipe_1","recipe_2","recipe_3","recipe_4"]  

    return example_recipes


@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: str):
    return {"recipe_id": f"{recipe_id}"}



#create recipe
@app.post("/recipes/")
async def create_recipe(recipe: Recipe):
    recipe.recipe_id = uuid.uuid4()
    return recipe


#change recipe
@app.put("/recipes/{recipe_id}")
async def update_recipe(recipe_id: str, recipe: Recipe):
    print(recipe)
    new_title="changed title"
    recipe.title = new_title
    #return {"changed recipe_id": f"{recipe_id}"}
    return recipe


#delete recipe

@app.delete("/recipes/{recipe_id}")
async def delete_recipe(recipe_id: str):
    #return {"deleted recipe with recipe_id": f"{recipe_id}"}
    global example_recipes  # Declare that you're using the global variable
    for idx, recipe in enumerate(example_recipes):
        if recipe.get("id") == int(recipe_id):
            deleted_recipe = example_recipes.pop(idx)
            print(example_recipes)
            return {"message": "Recipe deleted", "recipe": deleted_recipe}
    print(example_recipes)
    return {"message": "Recipe not found"}



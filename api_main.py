from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, field_validator
import tasks 

app = FastAPI()
accepted_langs = ["English", "French", "German", "Romanian"]

# data validation
class Translation(BaseModel):
    text : str
    initial_lang : str
    final_lang : str

    @field_validator('initial_lang', 'final_lang')
    def validate_input(cls, lang):
        if lang not in accepted_langs:
            raise ValueError("Invalid Language")
        return lang

# route1: index route
@app.get("/")

def get_root():
    return {"message" : "Deep Learning Translator"}

# route2: /translate : POST route
@app.post("/translate")
def post_translation(t : Translation, background_tasks : BackgroundTasks): 
    translation_id = tasks.store_translation(t) # stores translation request sent to the server onto db and returns the saved id
    background_tasks.add_task(tasks.run_translation, translation_id) # runs translation in the background
    return {"task id" : translation_id} # long translations take time, can cause server to timeout, so immediately return to the user while  translation is running in the background

# route3: /retrieve translaiton
@app.get("/results")
def get_translation(translation_id:int):
    return {"translation" : tasks.find_translation(translation_id)}



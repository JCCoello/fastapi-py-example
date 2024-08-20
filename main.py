from typing import Union
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

fruitbowl = {}

@app.get("/fruit")
def read_root():
    return fruitbowl


@app.post("/fruit")
def new_fruit(fruit: str, quantity: int):
    print("new fruit:", fruit, quantity)
    if fruit not in fruitbowl:
        fruitbowl[fruit] = quantity
    else:
        fruitbowl[fruit] += quantity
    return fruitbowl

@app.delete("/fruit")
def fruit(fruit: str):
    try:
        del fruitbowl[fruit]
    except:
      return {
            "status": f"{fruit} was not in the fruit bowl.",
           "fruitbowl":  fruitbowl
       }


    return {
        "status": f"{fruit} removed from the fruit bowl.",
        "fruitbowl":  fruitbowl
    }

@app.delete("/fruit/reduce")
def fruit(fruit: str):
    try:
        print(fruitbowl[fruit] )
        if fruit in fruitbowl and fruitbowl[fruit] > 1:
            fruitbowl[fruit] -= 1
        else:
            del fruitbowl[fruit]

    except:
      return {
            "status": f"{fruit} was not in the fruit bowl.",
           "fruitbowl":  fruitbowl
       }


    return {
        "status": f"removed one {fruit} from the fruit bowl.",
        "fruitbowl":  fruitbowl
    }


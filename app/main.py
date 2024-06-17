from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.post("/example")
async def example(parameter):


    return "hello"


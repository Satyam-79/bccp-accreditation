"Metallic Bellows India Private Limited"
from fastapi import FastAPI, HTTPException

from scrapper_asme import asme_active
from scrapper_si import si_active

app = FastAPI()


@app.get("/asme/{s}")
def asme(s: str):
    value = asme_active(s)
    return {"value": value}
    raise HTTPException(status_code=404)


@app.get("/si/{s}")
def si(s: str):
    value = si_active(s)
    return {"value": value}
    raise HTTPException(status_code=404)

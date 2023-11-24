from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def index():
   return { "data" : "Bem vindo!!!" }


@app.get("/quadrado")
def listaQuadrados(max : Optional[int] = 10):
   quadrados = []
   for i in range(1, max+1):
       quadrados.append(i**2)
  
   return {
       "max" : max,
       "quadrados" : quadrados
   }



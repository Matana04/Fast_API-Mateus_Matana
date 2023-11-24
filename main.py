from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def index():
   return { "data" : "Bem vindo!!!" }


#Parte 1 - Quadrados


@app.get("/quadrado")
def listaQuadrados(max : Optional[int] = 10):
   quadrados = []
   for i in range(1, max+1):
       quadrados.append(i**2)
  
   return {
       "max" : max,
       "quadrados" : quadrados
   }


#Parte 2 - 


@app.get("/tabuada/{n}")
def listaTabuada(n : int, start : Optional[int] = 1 , end : Optional[int] = 10):
   tabuada = []
   for i in range(start, end+1):
       tabuada.append(n*i)
  
   return {
       "número" : n,
       "tabuada" : tabuada
   }
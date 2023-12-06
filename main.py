from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


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


#Parte 2 - Tabuada


@app.get("/tabuada/{n}")
def listaTabuada(n : int, start : Optional[int] = 1 , end : Optional[int] = 10):
   tabuada = []
   for i in range(start, end+1):
       tabuada.append(n*i)
  
   return {
       "número" : n,
       "tabuada" : tabuada
    }


#Parte 3 - Bhaskara


class num(BaseModel):
   a : float
   b : float
   c : float

@app.post("/bhaskara")
def Bhaskara(conta : num):
    d = conta.b**2 -4*conta.a*conta.c
    x1 = ((-conta.b) + d ** 0.5) / (2*conta.a)
    x2 = ((-conta.b) - d ** 0.5) / (2*conta.a)
    return {
       "eq" : str(conta.a) + "x²" + str(conta.b) + "x" + str(conta.c),
       "x1" : x1,
       "x2" : x2
    }


#Parte 3 - Bhaskara

class letra(BaseModel):
   frase : str

@app.post("/conta")
def ContaLetra(contal : letra):
    v = 0
    c = 0
    o = 0
    for i in range(0, len(contal.frase)):
        caractere = contal.frase[i]
        if caractere.lower() in 'aeiou':
            v = v+1
        elif caractere.lower() in ' ':
            c = c+1
        else:
            o = o+1
            
    return {
        "frase" : contal.frase,
        "vogais": v,
        "espacos": c,
        "outros": o
    }

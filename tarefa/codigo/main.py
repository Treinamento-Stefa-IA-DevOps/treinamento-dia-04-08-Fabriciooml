import pickle
from fastapi import FastAPI

app = FastAPI()
@app.post('/model')
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age:float, Lifeboat:int, Pclass:int):
    with open('./codigo/model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)

    prediction = titanic.predict([[Sex, Age, Lifeboat, Pclass]])
    
    prediction = bool(prediction)
    
    return {"survived": prediction, 
            "status": 200,
            "message": "SUCCESS"}

@app.get('/model')
def get():
    return {'hello':'test'}

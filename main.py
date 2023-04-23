from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

origins = [
    "http://localhost:3000",
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SigninModel(BaseModel):
    ID: str
    password: str

class SignupModel(BaseModel):
    name: str
    ID: str
    password: str


@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.post("/api/signin")
async def signin(signinModel: SigninModel):
    with open("/root/database/database.csv", encoding="utf-8") as f:
        for l in f:
            data = l.strip().split()
            if data[1] == signinModel.ID and data[2] == signinModel.password:
                return {
                    "status": True,
                    "message": "Success"
                }
    return {"status": False, "message": "Fail"}

@app.post("/api/signup")
async def signin(signupModel: SignupModel):
    with open("/root/database/database.csv", encoding="utf-8") as f:
        for l in f:
            data = l.strip().split()
            if data[1] == signupModel.ID:
                return {"status": False, "message": "Fail"}
    f.close()
    inputData = f"\n{signupModel.name}\t{signupModel.ID}\t{signupModel.password}"
    with open("/root/database/database.csv", "a", encoding="utf-8") as ff:
        ff.write(inputData)
    ff.close()
    return {"status": True, "message": "Success"}
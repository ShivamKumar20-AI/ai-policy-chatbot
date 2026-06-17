from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import ask_chatbot

app = FastAPI(title="AI Policy Explainer Chatbot")

class Question(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "AI Policy Explainer Chatbot is running. POST to /ask with a question."}

@app.post("/ask")
def ask(payload: Question):
    return ask_chatbot(payload.question)
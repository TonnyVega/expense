import json
from typing import List
from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
from schemes import Expense
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    
    allow_methods=["*"],
    allow_headers=["*"],
)





db: List[Expense] = [
        Expense (
                id = "8a64875b-43fd-461e-ab52-3b3632d9006f",
                name= "asus monitor",
                category = "electronic",
                amount = 12,
                date = "today"
                ),
         Expense (
                id = "8a65875b-43fd-461e-ab52-3b3632d9006f",
                name= "asu5 monitor",
                category = "electronic",
                amount = 13,
                date = "today"
                ),
          Expense (
                id = "8164875b-43fd-461e-ab52-3b3632d9006f",
                name= "asus monitor",
                category = "lectronic",
                amount = 115,
                date = "today"
                ),
           Expense (
                id = "8164875b-43fd-461e-ab52-3b3632d9006f",
                name= "monitor",
                category = "ionic",
                amount = 11,
                date = "today"
                )
            ]

@app.get('/')
def home():
    return [{'expenses':'Api'}]


@app.get('/expenses')
async def expenses():
    return db

@app.post('/expenses')
async def expenses(expenses :Expense):
    db.append(expenses)
    pid =  expenses.id
    raise HTTPException(
        status_code= 200,
        detail =f"expense with id: {pid} added successfully"
    )

@app.delete('/expenses/{expense_id}')
async def delete_expense(expense_id:UUID):
    for expense  in db:
        if expense.id == expense_id:
            db.remove(expense)
            return f"expense with id: {expense_id} has been removed."
    raise HTTPException(
        status_code= 404,
        detail =f"Expense with id: {expense_id} does not exist."
    )


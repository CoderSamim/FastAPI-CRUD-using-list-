from fastapi import FastAPI
from schemas import Book

app=FastAPI()


data=[]         #take a list to store data without database




@app.post('/book')
def add_book(book:Book):
    data.append(book.dict())
    return data


@app.get('/book')
def get_books():
    return data

@app.get('/book/{id}')
def get_book(id:int):
    id=id-1
    return data[id]

@app.put('/book/{id}')
def rename_book(id:int, book:Book):
    data[id-1]=book
    return data

@app.delete('/book/{id}')
def rename_book(id:int):
    data.pop(id-1)
    return data


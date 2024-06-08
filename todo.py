from fastapi import APIRouter, HTTPException
from model import Todo
from typing import List
from datetime import datetime

todo_router = APIRouter()

todos = []

@todo_router.post("/todo", response_model=Todo)
async def create_todo(todo: Todo):
    todo.id = len(todos) + 1
    todo.timestamp = datetime.now()
    todos.append(todo)
    return todo

@todo_router.get("/todo", response_model=List[Todo])
async def get_todos():
    return todos

@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

from fastapi import FastAPI

from .routes.todos import TodoRoutes

app = FastAPI()

todo = TodoRoutes()
app.include_router(todo.router, tags=['Todo'])

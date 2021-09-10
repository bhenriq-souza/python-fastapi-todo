from fastapi import APIRouter


class TodoRoutes:
    router = APIRouter(prefix="/todos")

    @router.get("/", tags=['Todos'])
    def get_todos():
        pass

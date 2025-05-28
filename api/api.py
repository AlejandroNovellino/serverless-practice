# api/index.py
from fastapi import FastAPI

# start FastAPI application
app = FastAPI()


@app.get("/")
@app.get("/{path:path}")  # Captura cualquier ruta bajo /api/
async def read_root(path: str | None = None, name: str | None = "World"):
    """
    Return a greeting message.

    Args:
        path (str | None): Any other path.
        name (str | None): Name to greet, defaults to "Mundo".
    """

    greeting_name: str = name if name else "World"
    
    # return the greeting message
    return {"message": f"Hello {greeting_name} from Vercel with FastAPI!"}

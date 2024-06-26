import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/clicked", response_class=HTMLResponse)
def clicked(request: Request):
    return templates.TemplateResponse(request=request, name="clicked.html")


@app.get("/settings", response_class=HTMLResponse)
def settings(request: Request, name: str = None):
    if name is None:
        name = "Matt"
    return templates.TemplateResponse(request=request, name="settings.html", context={"name": name})

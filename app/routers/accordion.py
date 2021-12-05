from fastapi import Request, APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/accordion", response_class=HTMLResponse)
async def unsplash_home(request: Request):
    tag = "flower"
    result = "Type a number"
    return templates.TemplateResponse(
        "accordion.html",
        {"request": request, "result": result, "tag": tag}
    )

@router.post("/accordion", response_class=HTMLResponse)
def post_accordion(request: Request, tag: str = Form(...)):
    return templates.TemplateResponse(
        "accordion.html",
        {"request": request, "tag": tag}
    )
from fastapi import Request, APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/twoforms", response_class=HTMLResponse)
async def unsplash_home(request: Request):
    result = "Type a number"
    return templates.TemplateResponse(
        "twoforms.html",
        {"request": request, "result": result}
    )

@router.post("/form1", response_class=HTMLResponse)
def form_post1(request: Request, number: int = Form(...)):
    result = number + 2
    return templates.TemplateResponse(
        "twoforms.html",
        {"request": request, "result": result, "yournum": number}
    )

@router.post("/form2", response_class=HTMLResponse)
def form_post1(request: Request, number: int = Form(...)):
    result = number + 100
    return templates.TemplateResponse(
        "twoforms.html",
        {"request": request, "result": result, "yournum": number}
    )
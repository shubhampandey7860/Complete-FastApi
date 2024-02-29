from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory='templates')
app = FastAPI()


# Endpoint for displaying the form
@app.get("/form", response_class=HTMLResponse)
async def display_form(request: Request):
    return templates.TemplateResponse('form.html', {
        'request': request,
        'id': id,
        'price': 'product.price',
        'description': 'product.description',
        'title': 'product.title'
    })


# Endpoint for receiving form data
@app.post("/submit")
async def submit_form(name: str = Form(...), email: str = Form(...)):
    # Process the form data here (in this example, just printing)
    print("Received form data:")
    print("Name:", name)
    print("Email:", email)
    return {"message": "Form submitted successfully", "name": name, 'email': email}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=5000)

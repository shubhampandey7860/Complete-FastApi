from fastapi import APIRouter, Header, Cookie, Form
from typing import Optional, List
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(prefix='/products', tags=['products'])

products = ['watch', 'camera', 'phone']


@router.post("/new")
def create_product(name: str = Form(...)):
    products.append(name)
    return products


@router.get("/all")
def get_all_products():
    data = " ".join(products)
    response = Response(content=data, media_type="type/plain")
    response.set_cookie(key="test_cookie", value='test_cookie_value')
    return response


@router.get("/{id}", responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>product</div>"
            }
        },
        "description": "Returns html for an object"

    },
    404: {
        "content": {
            "text/plain": {
                "example": "<div>Product not available</div>"
            }
        },
        "description": " A clear text error message"

    }
})
def get_product(id: int):
    if id > len(products):
        out = "product not available"
        return PlainTextResponse(status_code=404, content=out, media_type="text/plain")
    else:
        product = products[id]
        out = f"""
        <head>
            <style>
                .product{{
                width:500px;
                height:200px;
                border:2px inset green;
                background-color:lightblue;
                text-align:center;
                }}
            </style>
        </head>
        <body>
            <div class="product">
            {product}
            </div>
        </body>
    """
        return HTMLResponse(out, media_type="text/html")


@router.get("/with_header")
def get_products(
        response: Response,
        custom_header: Optional[List[str]] = Header(None),
        test_cookie: Optional[str] = Cookie(None)

):
    if custom_header:
        response.headers['custom_response_header'] = " and ".join(products)
    return {
        'data': products,
        'custom_header': custom_header,
        'my_cookie': test_cookie
    }

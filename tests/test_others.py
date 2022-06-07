
from application.models import Product



def test_post_products(app, client):
    response = client.post("/product", json= {
    "name": "Test Pro 2",
    "description": "Test description, basics.",
    "price": "35.00",
    "qty": "10"
})
    print(response.status_code)
    assert response.status_code == 200

    
def test_get_products(app, client):
    response = client.get("/product")
    assert response.status_code == 200
    # assert len(response.json) == 1

    
def test_add_db(app, db):
    result = db.session.query(Product).all()
    print("Other results", result)
    pass

from application.models import Product



def test_post_products(app, client):
    response = client.post("/product", json= {
        "name": "Test Pro",
        "description": "ananinki ve de ebeninki",
        "price": "35.00",
        "qty": "10"
    })
    assert response.status_code == 200

    
def test_get_products(app, client):
    response = client.get("/product")
    assert response.status_code == 200
    assert len(response.json) == 1

    
def test_add_db(app, db):
    result = db.session.query(Product).all()
    print("Views", result)
    pass
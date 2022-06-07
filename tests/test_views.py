
from application.models import Product



def test_post_products(app, client):
    response = client.post("/product", json= {
        "name": "Test Pro",
        "description": "Test decription",
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

def test_data_repo(app, db, repo):
    print(repo)
    pass
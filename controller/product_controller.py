from app import app
@app.route('/product/show')
def showProduct():
    return "product page"

@app.route('/product/addProduct')
def addProduct():
    return "Show all products"
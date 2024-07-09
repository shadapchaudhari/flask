from app import app 

@app.route('/payment/users')
def makePayment():
    return "payment"
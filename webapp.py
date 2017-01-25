from flask import Flask
from database import *
from flask import Flask, url_for, flash, redirect, request , render_template
from flask import session as login_session
from flask import g 

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.bind = engine 
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()
'''
def verify_password(email, password):
	customer = session.query(Customer).filter_by(email=email).first()
	if not customer or not customer.verify_password(password):
		return False
	return True

@app.route('/')
@app.route('/inventory')
def inventory():
	items = session.query(Product).all()
	return render_template ("inventory.html", items = items)

	htmlString=""
	for item in productInventory:
		htmlString += "<p>" + item.name + "</p> <p>" + item.description + "</p> <p>" + item.price + "</p> <br> <br>"
	return htmlString

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		if email is None or password is None:
			flash('Missing Arguments')
			return redirect(url_for('url'))
		if verify_password(email,password):
			customer = session.query(Customer).filter_by(email=email).one()
			flash('Login Successful, welcome %s' % customer.name)
			login_session['name'] = customer.name
			login_session['email'] = customer.email
			login_session['id'] = customer.id
			return redirect(url_for('inventory'))
		else:
			flash('Incorrect username/email combination')
			return redirect(url_for('login'))

'''

@app.route('/newUser', methods = ['GET','POST'])
def newUser():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        gender= request.form['gender']
        date_of_birth= request.form['date_of_birth']
        #add photo

        if name == "" or email == "" or password == "":
            flash("Your form is missing arguments")
            return redirect(url_for('newUser'))
        if session.query(User).filter_by(email = email).first() is not None:
            flash("A user with this email address already exists")
            return redirect(url_for('newUser'))
        user = User(name = name, email=email, gender=gender, date_of_birth=date_of_birth)
        user.hash_password(password)
        session.add(user)
        
        session.commit()
        flash("User Created Successfully!")
        return redirect(url_for('newUser'))
    else:
        return render_template('newUser.html')

@app.route("/product/<int:product_id>")
def product(product_id):
	return "To be implemented"

@app.route("/product/<int:product_id>/addToCart", methods = ['POST'])
def addToCart(product_id):
	return "To be implemented"

@app.route("/shoppingCart")
def shoppingCart():
	return "To be implemented"

@app.route("/removeFromCart/<int:product_id>", methods = ['POST'])
def removeFromCart(product_id):
	return "To be implmented"

@app.route("/updateQuantity/<int:product_id>", methods = ['POST'])
def updateQuantity(product_id):
	return "To be implemented"

@app.route("/checkout", methods = ['GET', 'POST'])
def checkout():
	return "To be implmented"

@app.route("/confirmation/<confirmation>")
def confirmation(confirmation):
	return "To be implemented"

@app.route('/logout', methods = ['POST'])
def logout():
	return "To be implmented"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from database import *
from flask import Flask, url_for, flash, redirect, request , render_template
from flask import session as login_session
from flask import g 
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])



app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.bind = engine 
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

def verify_password(email, password):
	customer = session.query(User).filter_by(email=email).first()
	if not customer or not customer.verify_password(password):
		return False
	return True
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/create', methods = ['GET','POST'])
def newOutfit():
    if request.method == 'POST':
        
        description = request.form['description']
        category = request.form['category']
        gender = request.form['gender']
        name = request.form['name']
       
        if category is None or 'file' not in request.files:
            flash("Your form is missing arguments")
            return redirect(url_for('newOutfit'))
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('newOutfit'))
        
        if file and allowed_file(file.filename):
            outfit = Outfit(name=name, description=description, category = category, gender=gender)
       
            session.add(outfit)
            session.commit()
            filename = str(outfit.id) + "_" + secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            outfit.set_photo(filename)
            session.add(outfit)
            
            session.commit()
            
            return redirect(url_for('explore'))
        else:
        	flash("Please upload either a .jpg, .jpeg, .png, or .gif file.")
        	return redirect(url_for('newOutfit'))
    else:
        return render_template('create.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
'''
@app.route('/inventory')
def inventory():
	items = session.query(Product).all()
	return render_template ("inventory.html", items = items)

	htmlString=""
	for item in productInventory:
		htmlString += "<p>" + item.name + "</p> <p>" + item.description + "</p> <p>" + item.price + "</p> <br> <br>"
	return htmlString
'''
@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
        outfits=session.query(Outfit).all()
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		if email is None or password is None:
			flash('Missing Arguments')
			return redirect(url_for('url'))
		if verify_password(email,password):
			user = session.query(User).filter_by(email=email).one()
			flash('Login Successful, welcome %s' % user.name)
			login_session['name'] = user.name
			login_session['email'] = user.email
			login_session['id'] = user.id
			return redirect(url_for('firstt')) #take me to main page
		else:
			flash('Incorrect username/email combination')
    		return redirect(url_for('login'))
        login_session['id']=user.id ##other than that the input matches the details
        return render_template('first.html',user=user,outfits=outfits)

@app.route('/aboutUs')
def aboutUs():
	return render_template('aboutUs.html')
#@app.route('/user/<string:name>')
#def profile():
#	return render_template('profile.html')
@app.route('/Lookette/Welcome')
def firstt():
	return render_template('first.html')
@app.route('/Lookette/Create')
def create():
	return render_template('create.html')
@app.route('/Lookette/Explore')
def explore():
	outfits = session.query(Outfit).all()
	return render_template('explore.html', outfits=outfits )
def winter_outfits():
    return render_template('winter_outfits.html')

def categories():
    winter_outfits=session.query.filter_by(category=Winter).all
    summer_outfits=session.query.filter_by(category=Summer).all
    spring_outfits=session.query.filter_by(category=Spring).all
    fall_outfits=session.query.filter_by(category=Fall).all
    casual_outfits=session.query.filter_by(category=Casual).all
    formal_outfits=session.query.filter_by(category=Formal).all
    party_outfits=session.query.filter_by(category=Party).all
    sporty_outfits=session.query.filter_by(category=Sporty).all
    return render_template('first.html' 'winter_outfits.html', winter_outfits=winter_outfits, summer_outfits=summer_outfits, fall_outfits=fall_outfits,spring_outfits=spring_outfits, casual_outfits=casual_outfits, formal_outfits=formal_outfits, party_outfits=party_outfits, sporty_outfits=sporty_outfits)
	
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
        user = User(name = name, email=email, gender=gender, date_of_birth=date_of_birth)
        user.hash_password(password)
        session.add(user)
        
        session.commit()
        flash("User Created Successfully!")
        return redirect(url_for('firstt')) #take me to main page
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
    del(login_session['id'])
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)

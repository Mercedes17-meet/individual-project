from flask import Flask
from database import *
from flask import Flask, url_for, flash, redirect, request , render_template
from flask import session as login_session
from flask import g 
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.bind = engine 
Base.metadata.create_all(engine)
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

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['fileToUpload']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
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
	elif request.method == 'POST':
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
	return render_template('explore.html')
	
	
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
	return "To be implmented"

if __name__ == '__main__':
    app.run(debug=True)

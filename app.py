from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'online_cake_shop'

mysql = MySQL(app)
@app.route('/test_db')
def test_db():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT DATABASE();")  
        db_name = cur.fetchone()
        return f"Connected to database: {db_name[0]}"
    except Exception as e:
        return f"Error connecting to database: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password)

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                       (username, email, hashed_password))
        mysql.connection.commit()
        cursor.close()

        flash('Signup successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user[3], password):  # Assuming password is in the 4th column
            session['user_id'] = user[0]  # Assuming first column is user ID
            session['email'] = user[1]     # Assuming second column is email
            
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials, try again!", "danger")

    return render_template('login.html')

@app.route('/menu')
def dashboard():
    return "Welcome to the Dashboard!"



@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        cake_name = request.form.get('cake_name')
        quantity = request.form.get('quantity')
        address = request.form.get('address')

        print("Cake Name:", cake_name)  # Debugging
        print("Quantity:", quantity)
        print("Address:", address)

        if not cake_name or not quantity or not address:
            flash("All fields are required!", "danger")
            return redirect(url_for('order'))

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO orders (cake_name, quantity, address) VALUES (%s, %s, %s)", (cake_name, quantity, address))
        mysql.connection.commit()
        cursor.close()
        flash('Order placed successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('order.html')


if __name__ == '__main__':
    app.run(debug=True)

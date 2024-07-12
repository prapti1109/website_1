from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='C:/Users/Administrator/teamplates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    hobbies = db.Column(db.String(200))
    address = db.Column(db.String(200))
    city = db.Column(db.String(50))

# Route to display the registration form
@app.route('/', methods=['GET'])
def registration_form():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    first_name = request.form['txtFirstName']
    middle_name = request.form['txtMiddleName']
    last_name = request.form['txtLastName']
    gender = request.form['Gender']
    hobbies = ', '.join(request.form.getlist('chkHobby'))  # Convert list to comma-separated string
    address = request.form['txtAddress']
    city = request.form['cmbCity']

    # Save the form data in the database
    new_user = User(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        gender=gender,
        hobbies=hobbies,
        address=address,
        city=city
    )
    db.session.add(new_user)
    db.session.commit()

    print("First Name:", first_name)
    print("Middle Name:", middle_name)
    print("Last Name:", last_name)
    print("Gender:", gender)
    print("Hobbies:", hobbies)
    print("Address:", address)
    print("City:", city)

    return "Form submitted successfully."


if __name__ == '__main__':
    app.run(debug=True)

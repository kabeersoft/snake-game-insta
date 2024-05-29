from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Function to load users from the JSON file
def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            return json.load(file)
    return []

# Function to save users to the JSON file
def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

# Load users at the start
users = load_users()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users.append({'email': email, 'password': password})
        save_users(users)  # Save the updated user list to the file
        return redirect(url_for('success'))
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/user')
def user():
    return render_template('user.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)

<<<<<<< HEAD
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

# print(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# @app.route("/about.html")
# def About():
#     return render_template('/about.html')

# @app.route("/work.html")
# def testing():
#     return render_template('/work.html')

# @app.route("/contact.html")
# def contactus():
#     return render_template('/contact.html')

# @app.route("/<username>")
# def usern(username=Nonee):
#     return render_template(username)

def write_to_file(data):
    with open('database.txt', newline='', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}::{subject}::{message}')

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return 'form submitted'
            return redirect('/thankyou.html')
        except:
            return 'The data was not saved to the database'
    else:
        return 'Oops, Please try again.'

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
=======
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

# print(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# @app.route("/about.html")
# def About():
#     return render_template('/about.html')

# @app.route("/work.html")
# def testing():
#     return render_template('/work.html')

# @app.route("/contact.html")
# def contactus():
#     return render_template('/contact.html')

# @app.route("/<username>")
# def usern(username=Nonee):
#     return render_template(username)

def write_to_file(data):
    with open('database.txt', newline='', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}::{subject}::{message}')

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return 'form submitted'
            return redirect('/thankyou.html')
        except:
            return 'The data was not saved to the database'
    else:
        return 'Oops, Please try again.'

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
>>>>>>> 8ff8c151af66b4df0068b6b04c323948dd6eb42e
        csv_writer.writerow([email,subject,message])
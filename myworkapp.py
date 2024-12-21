# main application: myworkapp.py

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

# @app.route("/index.html")
# def index():
#     return render_template("index.html")
#
# @app.route("/works.html")
# def works():
#     return render_template("works.html")
#
# @app.route("/work.html")
# def work():
#     return render_template("work.html")
#
# @app.route("/about.html")
# def about():
#     return render_template("about.html")
#
# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")


# 279. Building a Portfolio 3
# making the URLs more dynamic

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# 280. Building a Portfolio 4
# Submitting a form

# @app.route("/submit_form", methods=["POST", "GET"])
# def submit():
#     #return render_template(page_name)
#     return "Form submitted. Thanks!"

# 282. Building a Portfolio 5
# Submitting form data

# @app.route("/submit_form", methods=["POST", "GET"])
# def submit():
#     #return render_template(page_name)
#     if request.method == "POST":
#         data = request.form.to_dict()
#         print(f"data : {data}")
#         # return "Form submitted. Thanks!"
#         return redirect("./thankyou.html")
#     else:
#         return "Something went wrong. Try again!"

# 283. Building a Portfolio 6
# Submitting form data and saving to a file

# def write_to_file(data):
#     with open("database.txt", mode="a") as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f"\n{email},{subject},{message}")
#
# @app.route("/submit_form", methods=["POST", "GET"])
# def submit():
#     #return render_template(page_name)
#     if request.method == "POST":
#         data = request.form.to_dict()
#         # print(f"data : {data}")
#         write_to_file(data)
#         return redirect("./thankyou.html")
#     else:
#         return "Something went wrong. Try again!"

# 284. Building a Portfolio 7
# Submitting form data and saving to a CSV file

import csv

def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # csv_writer = database.write(f"\n{email},{subject},{message}")
        csv_writer = csv.writer(database, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route("/submit_form", methods=["POST", "GET"])
def submit():
    #return render_template(page_name)
    if request.method == "POST":
        data = request.form.to_dict()
        # print(f"data : {data}")
        write_to_csv(data)
        return redirect("./thankyou.html")
    else:
        return "Something went wrong. Try again!"

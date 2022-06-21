from flask import Flask, render_template

app = Flask(__name__)


# Creating the first page
# Route -> rhsm.com/users, rhsm.com/contacts
# Functions -> what do you sow on the page.
# Templates -> create path template

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route(f"/user/<name_user>")
def users(name_user):
    return render_template("users.html", name_user=name_user)


# Website online
if __name__ == '__main__':
    app.run(debug=True)

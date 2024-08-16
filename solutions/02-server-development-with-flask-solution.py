from flask import Flask  # import the Flask class to create an app


app = Flask(__name__)  # invoke the Flask clas


@app.route('/')  # define the first route, the home route
def index():  # define the function that responds to the above route
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()  # Start the server listening for requests


# A. index
# B. create
@app.route("/reviews", methods=["GET", "POST"])
def index_review():
    if request.method == "GET":
        return "This route would be the home page for the reviews resource"
    elif request.method == "POST":
        return "This route would be for creating a new review"


# C. show
# D. update
# E. delete
@app.route("/reviews/<id>", methods=["GET", "PUT", "DELETE"])
def individual_review(id):
    if request.method == "GET":
        return "This route would be to show the details page of an individual review"
    elif request.method == "PUT":
        return "This route would be for updating the specific review"
    elif request.method == "DELETE":
        return "This route would delete the specific review"

# F. new

@app.route("/reviews/new", methods=["GET"])
def new_review():
    return "This route would be to serve the user the form to create a new review"

# G. edit

@app.route("/reviews/<id>/edit", methods=["GET"])
def edit_review():
    return "This route would show the form to edit the particular review"

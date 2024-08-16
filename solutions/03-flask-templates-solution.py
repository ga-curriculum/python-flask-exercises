# import what we need to use from the flask library
from flask import Flask, render_template, request

# To fake a database until we learn to use a real one, the collection below will be our application's "data"
reviews = [
    {"book_title": "The Handmaid's Tale",
        "review_text": "A harrowing documentary of modern America", "score": 5, "id": "1"},
    {"book_title": "To Serve Man",
        "review_text": "Delicious recipes", "score": 3, "id": "2"},
    {"book_title": "Pride and Prejudice",
        "review_text": "The pride is ok but the prejudice not so much", "score": 4, "id": "3"},
]


app = Flask(__name__)  # invoke the Flask class

# Example Template Route


@app.route("/example")
def example_route():
    return render_template("example.html", adjective="fun")


# Show Route

# Create a route with the url reviews/ID, where ID is a route variable
# Render the show.html template, providing the review with the matching id
# In the show.html template, display the book_title and review_text information.
# The book_title should be an h2 element, while the review_text should be a paragraph element
# Hint: You will have to loop through the list to find the right review to provide
@app.route("/reviews/<id>", methods=["GET"])
def show_review(id):
    for review in reviews:
        if review["id"] == id:
            return render_template("show.html", review=review)


# Index Route

# Create a route with the url "reviews"
# Render the index.html template, providing the entire list of reviews as a keyword argument
@app.route("/reviews", methods=["GET"])
def index_review():
    return render_template("index.html", reviews=reviews)


# Create Route

# Create a route that accepts a POST request to "/reviews"
# The route should create a new_review dictionary that contains the attached request's data
# Add the new_review dictionary to the reviews list
# Return a dictionary as follows: { "status": 201, "data": reviews } as the response from this route
@app.route("/reviews", methods=["POST"])
def create_review():
    new_review = {}
    new_review["book_title"] = request.form["book_title"]
    new_review["review_text"] = request.form["review_text"]
    new_review["score"] = request.form["score"]
    new_review["id"] = str(len(reviews))
    reviews.append(new_review)
    return {
        "status": 201,
        "data": reviews
    }

# Enter the command below into your terminal to test your create route:

# curl - X POST http: // localhost: 5000/reviews \
#    - d "book_title=War and Peace 2: Andrei Rises Again" \
#    - d "review_text=Tolstoy should have stopped with the first one." \
#    - d "score=2"

# This command sends a POST request to the specified URL with the data provided

if __name__ == '__main__':
    app.run()  # Start the server listening for requests

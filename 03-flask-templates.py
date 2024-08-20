# import what we need to use from the flask library
from flask import Flask, render_template, request

app = Flask(__name__)  # invoke the Flask class

# Example 1: Rendering HTML Route


@app.route("/hello")
def example_route():
    return "<h1>Hello, World!</h1>"


# Example 2: Rendering a Template Route


@app.route("/example")
def example_route():
    return render_template("example.html", adjective="fun")


# Mock Data

# Instead of a database, the collection below will be our application's "data"
reviews = [
    {"book_title": "The Little Prince",
        "review_text": "A profound and poetic tale about life, love, and human nature.", "score": 5, "id": "1"},
    {"book_title": "The Alchemist",
        "review_text": "A magical story about following your dreams and listening to your heart.", "score": 5, "id": "2"},
    {"book_title": "The Kite Runner",
        "review_text": "A powerful story of friendship, betrayal, and redemption.", "score": 4, "id": "3"},
]

# Show Route

# Create a route with the url reviews/ID, where ID is a route variable
# Render the provided show.html template, providing the review with the matching id
# In the show.html template, display the book_title and review_text information.
# The book_title should be an h2 element, while the review_text should be a paragraph element
# Hint: You will have to loop through the list to find the right review to provide


# Index Route

# Create a route with the url "reviews"
# Render the index.html template, providing the entire list of reviews as a keyword argument


# Create Route

# Create a route that accepts a POST request to "/reviews"
# The route should create a new_review dictionary that contains the attached request's data
# Add the new_review dictionary to the reviews list
# Return a dictionary as follows: { "status": 201, "data": reviews } as the response from this route

# Enter the command below into your terminal to test your create route:

# curl - X POST http: // localhost: 5000/reviews \
#    - d "book_title=The Midnight Library" \
#    - d "review_text=A thought-provoking journey through the choices that make up our lives." \
#    - d "score=4"


if __name__ == '__main__':
    app.run()  # Start the server listening for requests

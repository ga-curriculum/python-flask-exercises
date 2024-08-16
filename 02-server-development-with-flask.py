#2.1. Running a Flask Server

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


# 2.2. API Routes
# Create each of the seven RESTful routes for "/reviews", responding with a string describing what the route's purpose is.
# Note that, in order for these routes to be part of the app, you will have to move the app.run() conditional statement to be the very last piece of code in the app.


# A. index

# B. create

# C. show

# D. update

# E. delete

# F. new

# G. edit

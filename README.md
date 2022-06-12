Import the package you would like to use then follow the tutorial relating to each
python-firebase
from firebase_compsci import firebase

pyrebase
from firebase_compsci import pyrebase


Python-Firebase
Getting Started
You can fetch any of your data in JSON format by appending ‘.json’ to the end of the URL in which your data resides and, then send an HTTPS request through your browser. Like all other REST specific APIs, Firebase offers a client to update(PATCH, PUT), create(POST), or remove(DELETE) his stored data along with just to fetch it.

The library provides all the correspoding methods for those actions in both synchoronous and asynchronous manner. You can just start an asynchronous GET request with your callback function, and the method

To fetch all the users in your storage simply do the following:

from firebase import firebase
firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
result = firebase.get('/users', None)
print result
{'1': 'John Doe', '2': 'Jane Doe'}
The second argument of get method is the name of the snapshot. Thus, if you leave it NULL, you get the data in the URL /users.json. Besides, if you set it to 1, you get the data in the url /users/1.json. In other words, you get the user whose ID equals to 1.

from firebase import firebase
firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
result = firebase.get('/users', '1')
print result
{'1': 'John Doe'}
You can also provide extra query parameters that will be appended to the url or extra key-value pairs sent in the HTTP header.

from firebase import firebase
firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
result = firebase.get('/users/2', None, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print result
{'2': 'Jane Doe'}
Creating new data requires a POST or PUT request. Assuming you don’t append print=silent to the url, if you use POST the returning value becomes the name of the snapshot, if PUT you get the data you just sent. If print=silent is provided, you get just NULL because the backend never sends an output.

from firebase import firebase
firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
new_user = 'Ozgur Vatansever'

result = firebase.post('/users', new_user, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print result
{u'name': u'-Io26123nDHkfybDIGl7'}

result = firebase.post('/users', new_user, {'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print result == None
True
Deleting data is relatively easy compared to other actions. You just set the url and that’s all. Backend sends no output as a result of a delete operation.

from firebase import firebase
firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
firebase.delete('/users', '1')
# John Doe goes away.
Authentication
Authentication in Firebase is nothing but to simply creating a token that conforms to the JWT standarts and, putting it into the querystring with the name auth. The library creates that token for you so you never end up struggling with constructing a valid token on your own. If the data has been protected against write/read operations with some security rules, the backend sends an appropriate error message back to the client with the status code 403 Forbidden.

from firebase import firebase
firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', authentication=None)
result = firebase.get('/users', None, {'print': 'pretty'})
print result
{'error': 'Permission denied.'}

authentication = firebase.Authentication('THIS_IS_MY_SECRET', 'ozgurvt@gmail.com', extra={'id': 123})
firebase.authentication = authentication
print authentication.extra
{'admin': False, 'debug': False, 'email': 'ozgurvt@gmail.com', 'id': 123, 'provider': 'password'}

user = authentication.get_user()
print user.firebase_auth_token
"eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJhZG1pbiI6IGZhbHNlLCAiZGVidWciOiBmYWxzZSwgIml
hdCI6IDEzNjE5NTAxNzQsICJkIjogeyJkZWJ1ZyI6IGZhbHNlLCAiYWRtaW4iOiBmYWxzZSwgInByb3ZpZGVyIjog
InBhc3N3b3JkIiwgImlkIjogNSwgImVtYWlsIjogIm96Z3VydnRAZ21haWwuY29tIn0sICJ2IjogMH0.lq4IRVfvE
GQklslOlS4uIBLSSJj88YNrloWXvisRgfQ"

result = firebase.get('/users', None, {'print': 'pretty'})
print result
{'1': 'John Doe', '2': 'Jane Doe'}
Concurrency
The interface heavily depends on the standart multiprocessing library when concurrency comes in. While creating an asynchronous call, an on-demand process pool is created and, the async method is executed by one of the idle process inside the pool. The pool remains alive until the main process dies. So every time you trigger an async call, you always use the same pool. When the method returns, the pool process ships the returning value back to the main process within the callback function provided.

 import json
 from firebase import firebase
 from firebase import jsonutil

firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', authentication=None)

def log_user(response):
    with open('/tmp/users/%s.json' % response.keys()[0], 'w') as users_file:
        users_file.write(json.dumps(response, cls=jsonutil.JSONEncoder))

firebase.get_async('/users', None, {'print': 'pretty'}, callback=log_user)


Pyrebase
A simple python wrapper for the Firebase API.

Support
Does your business or project depend on Pyrebase? Reach out to pibals@protonmail.com

Installation
pip install pyrebase
Getting Started
Python Version
Pyrebase was written for python 3 and will not work correctly with python 2.

Add Pyrebase to your application
For use with only user based authentication we can create the following configuration:

import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
We can optionally add a service account credential to our configuration that will allow our server to authenticate with Firebase as an admin and disregard any security rules.

import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)
Adding a service account will authenticate as an admin by default for all database queries, check out the Authentication documentation for how to authenticate users.

Use Services
A Pyrebase app can use multiple Firebase services.

firebase.auth() - Authentication

firebase.database() - Database

firebase.storage() - Storage

Check out the documentation for each service for further details.

Authentication
The sign_in_with_email_and_password() method will return user data including a token you can use to adhere to security rules.

Each of the following methods accepts a user token: get(), push(), set(), update(), remove() and stream().

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": "Mortimer 'Morty' Smith"
}

# Pass the user's idToken to the push method
results = db.child("users").push(data, user['idToken'])
Token expiry
A user's idToken expires after 1 hour, so be sure to use the user's refreshToken to avoid stale tokens.

user = auth.sign_in_with_email_and_password(email, password)
# before the 1 hour expiry:
user = auth.refresh(user['refreshToken'])
# now we have a fresh token
user['idToken']
Custom tokens
You can also create users using custom tokens, for example:

token = auth.create_custom_token("your_custom_id")
You can also pass in additional claims.

token_with_additional_claims = auth.create_custom_token("your_custom_id", {"premium_account": True})
You can then send these tokens to the client to sign in, or sign in as the user on the server.

user = auth.sign_in_with_custom_token(token)
Manage Users
Creating users
auth.create_user_with_email_and_password(email, password)
Note: Make sure you have the Email/password provider enabled in your Firebase dashboard under Auth -> Sign In Method.

Verifying emails
auth.send_email_verification(user['idToken'])
Sending password reset emails
auth.send_password_reset_email("email")
Get account information
auth.get_account_info(user['idToken'])
Refreshing tokens
user = auth.refresh(user['refreshToken'])
Database
You can build paths to your data by using the child() method.

db = firebase.database()
db.child("users").child("Morty")
Save Data
push
To save data with a unique, auto-generated, timestamp-based key, use the push() method.

data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)
set
To create your own keys use the set() method. The key in the example below is "Morty".

data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").child("Morty").set(data)
update
To update data for an existing entry use the update() method.

db.child("users").child("Morty").update({"name": "Mortiest Morty"})
remove
To delete data for an existing entry use the remove() method.

db.child("users").child("Morty").remove()
multi-location updates
You can also perform multi-location updates with the update() method.

data = {
    "users/Morty/": {
        "name": "Mortimer 'Morty' Smith"
    },
    "users/Rick/": {
        "name": "Rick Sanchez"
    }
}

db.update(data)
To perform multi-location writes to new locations we can use the generate_key() method.

data = {
    "users/"+ref.generate_key(): {
        "name": "Mortimer 'Morty' Smith"
    },
    "users/"+ref.generate_key(): {
        "name": "Rick Sanchez"
    }
}

db.update(data)
Retrieve Data
val
Queries return a PyreResponse object. Calling val() on these objects returns the query data.

users = db.child("users").get()
print(users.val()) # {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}
key
Calling key() returns the key for the query data.

user = db.child("users").get()
print(user.key()) # users
each
Returns a list of objects on each of which you can call val() and key().

all_users = db.child("users").get()
for user in all_users.each():
    print(user.key()) # Morty
    print(user.val()) # {name": "Mortimer 'Morty' Smith"}
get
To return data from a path simply call the get() method.

all_users = db.child("users").get()
shallow
To return just the keys at a particular path use the shallow() method.

all_user_ids = db.child("users").shallow().get()
Note: shallow() can not be used in conjunction with any complex queries.

streaming
You can listen to live changes to your data with the stream() method.

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child("posts").stream(stream_handler)
You should at least handle put and patch events. Refer to "Streaming from the REST API" for details.

You can also add a stream_id to help you identify a stream if you have multiple running:

my_stream = db.child("posts").stream(stream_handler, stream_id="new_posts")
close the stream
my_stream.close()
Complex Queries
Queries can be built by chaining multiple query parameters together.

users_by_name = db.child("users").order_by_child("name").limit_to_first(3).get()
This query will return the first three users ordered by name.

order_by_child
We begin any complex query with order_by_child().

users_by_name = db.child("users").order_by_child("name").get()
This query will return users ordered by name.

equal_to
Return data with a specific value.

users_by_score = db.child("users").order_by_child("score").equal_to(10).get()
This query will return users with a score of 10.

start_at and end_at
Specify a range in your data.

users_by_score = db.child("users").order_by_child("score").start_at(3).end_at(10).get()
This query returns users ordered by score and with a score between 3 and 10.

limit_to_first and limit_to_last
Limits data returned.

users_by_score = db.child("users").order_by_child("score").limit_to_first(5).get()
This query returns the first five users ordered by score.

order_by_key
When using order_by_key() to sort your data, data is returned in ascending order by key.

users_by_key = db.child("users").order_by_key().get()
order_by_value
When using order_by_value(), children are ordered by their value.

users_by_value = db.child("users").order_by_value().get()
Storage
The storage service allows you to upload images to Firebase.

child
Just like with the Database service, you can build paths to your data with the Storage service.

storage.child("images/example.jpg")
put
The put method takes the path to the local file and an optional user token.

storage = firebase.storage()
# as admin
storage.child("images/example.jpg").put("example2.jpg")
# as user
storage.child("images/example.jpg").put("example2.jpg", user['idToken'])
download
The download method takes the path to the saved database file and the name you want the downloaded file to have.

storage.child("images/example.jpg").download("downloaded.jpg")
get_url
The get_url method takes the path to the saved database file and returns the storage url.

storage.child("images/example.jpg").get_url()
# https://firebasestorage.googleapis.com/v0/b/storage-url.appspot.com/o/images%2Fexample.jpg?alt=media
Helper Methods
generate_key
db.generate_key() is an implementation of Firebase's key generation algorithm.

See multi-location updates for a potential use case.

sort
Sometimes we might want to sort our data multiple times. For example, we might want to retrieve all articles written between a certain date then sort those articles based on the number of likes.

Currently the REST API only allows us to sort our data once, so the sort() method bridges this gap.

articles = db.child("articles").order_by_child("date").start_at(startDate).end_at(endDate).get()
articles_by_likes = db.sort(articles, "likes")
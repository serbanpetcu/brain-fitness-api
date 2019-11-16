#!flask/bin/python
from flask import Flask
from model.Teacher import Teacher
from model.Admin import Admin
from model.User import User

app = Flask(__name__)

#for testin
userObject={'userID':'-1','username':'test'}

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/testUser')
def createTestNewUser():
    return 'Created Test New Users'

@app.route('/createUser')
def createNewUser():
    output = User.createUser(userObject)
    return output

@app.route('/userCreateNewUser')
def userCreateNewUser():
    output = Admin.userCreateNewUser(userObject)
    return output

if __name__ == '__main__':
    app.run(debug=True)

class User:

    userObject={}
    new_user=True

    def __init__(self,UserObject):
        self.userObject = userObject
        if self.UserObject['user_id'] is None:
            self.new_user = False
        else:
            self.new_user = True
            self._createUser()

          #fetch all records from db about user_id
        self._populateUser()

    def createUser(self):
        #sql("",self.userType,self.username,self.name)
        output = 'succesfully created new user'
        return output

    def _populateUser():
        return -1

    def getLessonDate():
        self.UserObject['user_id']
        return -1

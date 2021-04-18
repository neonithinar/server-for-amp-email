from pyrebase import initialize_app
from time import time

firebaseConfig = {
    "apiKey": "AIzaSyADqDB65qggnbyxD0NV28vdwQ8KDwXSnLE",
    "authDomain": "amp-email-chatbot-6cedd.firebaseapp.com",
    "databaseURL": "https://amp-email-chatbot-6cedd-default-rtdb.firebaseio.com",
    "projectId": "amp-email-chatbot-6cedd",
    "storageBucket": "amp-email-chatbot-6cedd.appspot.com",
    "messagingSenderId": "837029626975",
    "appId": "1:837029626975:web:3e57fbb5cecd258aad47ea"
}
milliseconds = int(time() * 1000)


firebase_app = initialize_app(firebaseConfig)
db = firebase_app.database()
email = "test_email_new@testmail.com"
# pushing data with specific key => key to be changed to unique id email
sample_data = {"email": email,
               "message": "created fifth message for same email",
               "timestamp": milliseconds}


# db.push(data) # to push without a specific id to the child
# db.child("chats").push(sample_data) # to set data to a specific child

# read data
# chat_content = db.child("chats").get()

# print(chat_content.val()) # retuns whole child dataset attr
# print(chat_content.key()) # returns child name

# for item in chat_content.each():
#     # print(item.key())
#     # print(item.val()["email"])
#     if item.val()["email"] == email:
#         user_data = item.val()

    # else:
    #     print("email not found")


def get_data():
    """ returns all data from firebase realtime database under chats"""
    chat_content = db.child("chats").get()
    return chat_content.val()

def write_data():
    try:
        db.child("chats").push(sample_data)
        return "upload succesful"
    except Exception as e:
        return f"An Error Occured: {e}"

# write_data(sample_data)

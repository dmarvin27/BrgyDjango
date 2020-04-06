import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyBOds3vSHR7KktWocBo3jZoaFE55MlWc5A",
  'authDomain': "barangaysystem-5cccc.firebaseapp.com",
  'databaseURL': "https://barangaysystem-5cccc.firebaseio.com",
  'projectId': "barangaysystem-5cccc",
  'storageBucket': "barangaysystem-5cccc.appspot.com",
  'messagingSenderId': "974011598558",
  'appId': "1:974011598558:web:66a7088526c2bf5983644f",
  'measurementId': "G-BKX1J70FFH"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

auth = firebase.auth()

user = auth.sign_in_with_email_and_password(
    "marvin@gmail.com", "marvindeguzman")

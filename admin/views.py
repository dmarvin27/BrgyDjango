from django.shortcuts import *
from django.http import *
from .config import *
import random
import string
import json

def randomStringDigits(stringLength=20):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


def save_barangay(request):
    data = request.body.decode('utf8')
    data = json.loads(data)
    _barangayname = data["Name"]
    _announcement = data["Announcement"]
    data = {"Name":_barangayname,"Announcement":_announcement}
    result = db.child("Barangay").child(randomStringDigits()).set(data)
    return HttpResponse("<html><body>Successfuly Save %s.</body></html>" % result)


def get_barangay(request):
    all_barangay = db.child("Barangay").get().val()
    return JsonResponse(all_barangay)


def update_barangay(request, id):
    data = json.loads(request.body)
    _barangayname = data["Name"]
    _announcement = data["Announcement"]
    data = {"Name":_barangayname,"Announcement":_announcement}
    barangay = db.child("Barangay").child(id).update(data, user['idToken'])
    return HttpResponse("<html><body> Updated successfully for %s </body></html>" % barangay)

def delete_barangay(request, id):
    db.child("Barangay").child(id).remove(user['idToken'])
    return HttpResponse("<html><body>Deleted ID: %s.</body></html>" % id)
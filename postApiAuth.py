from flask import jsonify, request
from dbModel import *
import socket

def ipValidation(addr):
    try:
        socket.inet_aton(addr)
        return True
    except socket.error:
        return False

def postApiauth():
    if request.method == 'POST':
        jsonData = request.get_json()
        if jsonData is None:
            return jsonify({'Error': 'Invalid or missing JSON data'}), 400
        if not(3<= len(jsonData['USERNAME']) <=20):
            return jsonify({'USERNAME' : 'Length should be between 3 to 10'}), 400
        if not(5<= len(jsonData['PASSWORD']) <=30):
            return jsonify({'PASSWORD' : 'Length should be between 5 to 30'}), 400
        if not isinstance(jsonData['HOST_IP'], list):
            return jsonify({'HOST_IP': 'Given data is not a list'}), 400
        for hostIp in jsonData['HOST_IP']:
            check = ipValidation(hostIp)
            if check is False:
                return jsonify({'HOST_IP' : 'Given data is not a IPv4'}), 400
            
        postApiAuthDetails = AUTOMATION_API_AUTH(USERNAME=jsonData['USERNAME'], PASSWORD=jsonData['PASSWORD'])
        db.session.add(postApiAuthDetails)
        db.session.commit()

        for hostIp in jsonData['HOST_IP']:
            postHostIpDetails = AUTOMATION_HOST_DETAILS(API_ID = postApiAuthDetails.API_ID, HOST_IP=hostIp)
            db.session.add(postHostIpDetails)
            db.session.commit()

        return jsonify({'Message': 'The Auth Host Details were added Successfully'}), 201
from flask import jsonify, request
from dbModel import *
from postApiAuth import ipValidation

global PostHostIpDetails
PostHostIpDetails = None

def patchApiauth(userName):
    if request.method == 'PATCH':
        jsonData = request.get_json()
        postApiAuthDetails = AUTOMATION_API_AUTH.query.filter_by(USERNAME=userName).first()
        if jsonData is None or postApiAuthDetails is None:
            return jsonify({'Error': 'Invalid missing JSON data or Username does not exist'}), 400
        if 'HOST_IP' not in jsonData and 'PASSWORD' not in jsonData:
            return jsonify({'Message': 'Data is null'}), 400

        
        try:
            if jsonData['PASSWORD'] != '' or jsonData['PASSWORD'] is not None:
                postApiAuthDetails.PASSWORD = jsonData['PASSWORD']
                if not(5<= len(postApiAuthDetails.PASSWORD) <=30):
                    return jsonify({'PASSWORD' : 'Length should be between 5 to 30'}), 400
            db.session.add(postApiAuthDetails)
            db.session.commit()
        except KeyError:
            pass


        try:
            if 'HOST_IP' not in jsonData:
                pass
            elif jsonData['HOST_IP'] is not [] or jsonData['HOST_IP'] is not None:
                if not isinstance(jsonData['HOST_IP'], list):
                    return jsonify({'HOST_IP': 'Given data is not a list'}), 400
                for hostIp in jsonData['HOST_IP']:
                    check = ipValidation(hostIp)
                    if check is False:
                        return jsonify({'HOST_IP' : 'Given data is not a IPv4'}), 400
                    PostHostIpDetails = AUTOMATION_HOST_DETAILS(API_ID = postApiAuthDetails.API_ID, HOST_IP=hostIp)
                db.session.add(PostHostIpDetails)
                db.session.commit()
        except KeyError:
            pass

        return jsonify({'Message': 'The Auth Host Details were updated Successfully'}), 201
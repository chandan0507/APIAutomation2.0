from flask import jsonify, request
from dbModel import *

def getApiauth(userName):
    if request.method == 'GET':
        getApiAuthDetails = AUTOMATION_API_AUTH.query.filter_by(USERNAME=userName).first()
        if getApiAuthDetails is None:
            return jsonify({'USERNAME': 'Username does not exist'}), 400
        getApiHostDetails = AUTOMATION_HOST_DETAILS.query.filter_by(API_ID=getApiAuthDetails.API_ID).all()
        if not getApiHostDetails:
            return jsonify({'Error': 'Host IPs does not exist'}), 400
        #hostIps = [hostDetail.HOST_IP for hostDetail in getApiHostDetails]
        hostIps = []
        for hostIp in getApiHostDetails:
            hostIps.append(hostIp.HOST_IP)
        returnApiAuthDetails = {'USERNAME': getApiAuthDetails.USERNAME, 'PASSWORD': getApiAuthDetails.PASSWORD, 'API_ID': getApiAuthDetails.API_ID, 'HOST_IPs': hostIps}
        return jsonify(returnApiAuthDetails)
        
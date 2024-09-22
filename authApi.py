from functools import wraps
from flask import jsonify, request
from dbModel import AUTOMATION_API_AUTH, AUTOMATION_HOST_DETAILS


def fetchUsername(userName):
    getApiAuthDetails = AUTOMATION_API_AUTH.query.filter_by(USERNAME=userName).first()
    if getApiAuthDetails is None:
        return False
    getApiHostDetails = AUTOMATION_HOST_DETAILS.query.filter_by(API_ID=getApiAuthDetails.API_ID).all()
    if not getApiHostDetails:
        return False
        #hostIps = [hostDetail.HOST_IP for hostDetail in getApiHostDetails]
    hostIps = []
    for hostIp in getApiHostDetails:
        hostIps.append(hostIp.HOST_IP)
    if getApiAuthDetails.USERNAME == request.authorization.username and getApiAuthDetails.PASSWORD == request.authorization.password and request.remote_addr in hostIps:
        return True
    return False

def login_required(f):
    """ basic auth for api """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """(*args, **kwargs) in url what ever and how many arguments also if we get means,
        Same will be passed to the route function, the url value could be parameter as id,
        Or it could be a key value pair as role=admin"""
        if not request.authorization:
            return jsonify({'message': 'basic auth is required'})
        callMe = fetchUsername(request.authorization.username)
        if callMe == False:
            return jsonify({'message': 'Username or IP is not registered'}), 401  # Fall back to remote_addr if no proxy is used
        return f(*args, **kwargs)
    return decorated_function
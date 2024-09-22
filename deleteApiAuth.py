from flask import jsonify, request
from dbModel import *

def deleteApiauth(userName):
    if request.method == 'DELETE':
        getApiAuthDetails = AUTOMATION_API_AUTH.query.filter_by(USERNAME=userName).first()
        if getApiAuthDetails is None:
            return jsonify({'USERNAME': 'Username does not exist'}), 400
        getApiHostDetails = AUTOMATION_HOST_DETAILS.query.filter_by(API_ID=getApiAuthDetails.API_ID).all()

        if not getApiHostDetails:
            return jsonify({'Error': 'Host IPs does not exist'}), 400
        for hostDetail in getApiHostDetails:
            db.session.delete(hostDetail)
            db.session.commit()
        db.session.delete(getApiAuthDetails)
        db.session.commit()

        return jsonify({'Message': 'Deatils are deleted Successfully'})
        
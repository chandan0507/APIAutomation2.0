from flask import request, jsonify
from dbModel import *
from datetime import datetime

def post_test():
    if request.method == 'POST':
        json_data = request.get_json()

        if not(3<= len(str(json_data['TEST_RUN_ID'])) <=10):
            return jsonify({'TEST_RUN_ID' : 'Length should be between 3 to 10'}), 400
        if not(5<= len(json_data['TEST_CASE_NAME']) <=30):
            return jsonify({'TEST_CASE_NAME' : 'Length should be between 5 to 30'}), 400
        if not(4<= len(json_data['PRODUCT']) <=15):
            return jsonify({'PRODUCT' : 'Length should be between 4 to 15'}), 400
        if (json_data['RESULT'].upper() not in ['PASS', 'FAIL']):
            return jsonify({'RESULT' : 'Should be either pass or fail'}), 400
        post_test_case_details = AUTOMATION_TEST_CASE(
            TEST_RUN_ID=int(json_data['TEST_RUN_ID']),
            TEST_CASE_NAME=json_data['TEST_CASE_NAME'],
            PRODUCT=json_data['PRODUCT'],
            EXECUTION_TIME=datetime.strptime(json_data['EXECUTION_TIME'], "%d-%m-%Y %H:%M:%S"),
            RESULT=json_data['RESULT']
        )

        db.session.add(post_test_case_details)
        db.session.commit()

        return jsonify({'Message': 'The Test Details were added Successfully'}), 201
from flask import request, jsonify
from dbModel import *

def get_test(run_id):
    if request.method == 'GET':
        try:
            run_id = int(run_id)
        except ValueError:
            return jsonify({'message': 'Expected int got Char'}), 400
        # The details of filtered run_id row is stored into a variable
        get_test_case_details = AUTOMATION_TEST_CASE.query.filter_by(TEST_CASE_ID=run_id).first()
        # If there is no rows for the selected get_test_case_details
        if get_test_case_details is None:
            # Return a 404 error if no test case is found with the given run_id
            return jsonify({'TEST_CASE_ID': f'{run_id} Not Found'}), 404
        #return jsonify(get_test_case_details.returnGet())
        return jsonify({'TEST_CASE_ID': get_test_case_details.TEST_CASE_ID, 'TEST_RUN_ID': get_test_case_details.TEST_RUN_ID, 'TEST_CASE_NAME': get_test_case_details.TEST_CASE_NAME, 'PRODUCT': get_test_case_details.PRODUCT, 'EXECUTION_TIME': get_test_case_details.EXECUTION_TIME, 'RESULT': get_test_case_details.RESULT})
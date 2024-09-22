from flask import request, jsonify
from collections import OrderedDict
from dbModel import *

def get_run(run_id):
    if request.method == 'GET':
        try:
            run_id = int(run_id)
        except ValueError:
            return jsonify({'message': 'Expected int got Char'}), 404
        # select all the testc cases rows with the given run_id and store it into get_test_case_details variable
        get_test_case_details = AUTOMATION_TEST_CASE.query.filter_by(TEST_RUN_ID=run_id).all()
        # print(get_test_case_details)
        if get_test_case_details == []:
            # Return a 404 error if no test case is found with the given run_id
            return jsonify({'TEST_RUN_ID': f'{run_id} Not Found'}), 404
        
        get_test_case_list = []
        for case in get_test_case_details:
            get_test_case_list.append({
                'TEST_CASE_ID': case.TEST_CASE_ID,
                'TEST_CASE_NAME': case.TEST_CASE_NAME,
                'PRODUCT': case.PRODUCT,
                'EXECUTION_TIME': case.EXECUTION_TIME,
                'RESULT': case.RESULT
            })
        get_test_case_list_response = OrderedDict({
            'TEST_CASE_DETAILS': get_test_case_list
        })
            
        return jsonify(get_test_case_list_response)
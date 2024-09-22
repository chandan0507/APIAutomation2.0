from flask import request, jsonify
from dbModel import *


def delete_test(run_id):
    if request.method == 'DELETE':
        try:
            run_id = int(run_id)
        except ValueError:
            return jsonify({'message': 'Expected int got Char'}), 404
        # Delete the row by filtering for the run_id of first selected row
        delete_test_case_details = AUTOMATION_TEST_CASE.query.filter_by(TEST_CASE_ID=run_id).first()
        # Validating if delete is null or non null, if non null delete the selected first row
        if delete_test_case_details is not None:
            db.session.delete(delete_test_case_details)
            db.session.commit()
            return jsonify({"message": "Test case Details deleted successfully."}), 200
        else:
            return jsonify({"message": "Test case not found."}), 404
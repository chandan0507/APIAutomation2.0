from authApi import login_required
from deleteApiAuth import deleteApiauth
from getApiAuth import getApiauth
from getTestCase import get_test
from getTestRun import get_run
from deleteTestRun import delete_test
from patchApiAuth import patchApiauth
from postTestCase import post_test
from postApiAuth import postApiauth
from dbModel import *

@app.route('/get_test/<test_case_id>', methods=['GET'])
@login_required
def getTestCaseDeatils(test_case_id):
    return get_test(test_case_id)
    
@app.route('/get_run/<test_run_id>', methods=['GET'])
@login_required
def getTestRunDetails(test_run_id):
    return get_run(test_run_id)
    
@app.route('/delete_test/<test_case_id>', methods=['DELETE'])
@login_required
def deleteTestRunDetails(test_case_id):
    return delete_test(test_case_id)

@app.route('/post_test', methods=['POST'])
@login_required
def postTestCaseDeatils():
    return post_test()

@app.route('/post_auth', methods=['POST'])
def postAuthHostDetails():
    return postApiauth()

@app.route('/patch_auth/<userName>', methods=['PATCH'])
def patchAuthHostDetails(userName):
    return patchApiauth(userName)

@app.route('/get_auth/<userName>', methods=['GET'])
def getAuthHostDetails(userName):
    return getApiauth(userName)

@app.route('/delete_auth/<userName>', methods=['DELETE'])
def deleteAuthHostDetails(userName):
    return deleteApiauth(userName)

if __name__ == '__main__':
    app.run(debug=True, port=8081)
    
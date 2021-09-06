

import flask
from flask import request, jsonify

app = flask.Flask(__name__)

# Create some test data for our catalog in the form of a list of dictionaries.
input_sample = [{
"TransId": 247424,
"AmountUsed":100,
"MembershipId":"GYGJBSDGFDJBB", 
"MemberPhone":"9810294203", 
"Sequence" :1,
"BalanceType" : 0, 
"RecognitionId":5,
"MemberEmail":"", 
"SchemeId": 1,
"VoucherExpiry": "31 DEC 2020 23:59",
"BalancePoints":"45",
"IsEnrollment": "Y",
"MemberType":"Y", 
"TransactionDate":"21 NOV 2020 14:59",
"TransAmount" :"500", 
"ComplexName": "PVR"
},
    {
"TransId": 2474232,
"AmountUsed":400,
"MembershipId":"GYGJBSDGFDJBHG", 
"MemberPhone":"9500445796", 
"Sequence" :2,
"BalanceType" : 0, 
"RecognitionId":6,
"MemberEmail":"", 
"SchemeId": 1,
"VoucherExpiry": "16 JUN 2021 13:51",
"BalancePoints":"45",
"IsEnrollment": "Y",
"MemberType":"Y", 
"TransactionDate":"11 MAR 2021 11:15",
"TransAmount" :"100", 
"ComplexName": "PVR"
}]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Test API for Dynamic Vocher</h1>
<p>A smaple api application which gets response and gives back voucher details.</p>'''


@app.route('/WebVoucherRestAPI', methods=['GET'])
def api_all():
    return jsonify(input_sample)


@app.route('/WebVoucherRestAPI/CreateLoyaltyVoucher', methods=['GET'])
def api_id():

    if 'MemberPhone' in request.args:
        memberphone = int(request.args['MemberPhone'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = str('Voucher Code for posted trans : VOC123456789')

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

if __name__=='__main__':
    app.run(debug=False)
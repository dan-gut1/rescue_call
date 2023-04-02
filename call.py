from flask import Flask
from sonetel import api
from requests import exceptions

# Init flask object basicly its the frontend (webserver) itself.
app = Flask(__name__)
number_to_dial1 = "050000000"
number_to_dial2 = "050000000"

@app.route('/')     # make the app listining on this address for example: 'http://serveraddress:5000/'.
def make_call():

    call = api.Account(username='sonetel_user', password='sonetel_password')    # make sonetel api object in to varibal called 'call'
    try:
        call_status = call.callback(number_to_dial1, number_to_dial2)  # Now that we have sonetel object with its capabilites we can make calls between to pairs or any other.
        # print(f'call status is: {call_status} type: {type(call_status)}')
    except exceptions.HTTPError as e:   # In any case of error in the api response we catching the crash and returning error to the web page.
        return f'<p>Server error: {e} </p>'
    
    return "<p>Rescue call is on the way</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
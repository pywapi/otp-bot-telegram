from twilio.rest import Client
from config import Config

# Function to make a call
def make_call(to_number, voice=Config.DEFAULT_VOICE, script=Config.BANK_SERVICE_SCRIPT):
    client = Client(account_sid, auth_token)

    try:
        call = client.calls.create(
            twiml=f'<Response><Say voice="{voice}">{script}</Say></Response>',
            to=to_number,
            from_=twilio_phone_number
        )
        print(f"Calling {to_number}...")
        print(f"Call SID: {call.sid}")
    except Exception as e:
        print(f"Error making the call: {str(e)}")

if __name__ == "__main__":
    to_number = '+xxxxxxxxxxxx' 
    make_call(to_number)

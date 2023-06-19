from twilio.rest import Client
from env._secrete import twilio_account_sid, twilio_auth_token


def send_txt_message(from_, to, msg_body):
    # send text message via twilio

    # Your Account SID from twilio.com/console
    account_sid = twilio_account_sid
    # Your Auth Token from twilio.com/console
    auth_token = twilio_auth_token
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=to,
        from_=from_,
        body=msg_body)
    print(message.sid)


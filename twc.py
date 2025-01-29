import os
def t(msg,num):
    from twilio.rest import Client
    account_sid = os.getenv('TWILIO_ACCOUNT_SID') 
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=msg,  
        from_='whatsapp:+14155238886',  
        to=num  
    )
    print(f"Message sent! Message SID: {message.sid}")
#Send sms using python

from twilio.rest import Client 
 
account_sid = 'AC008f7ad4d71f2476371aac70dec81c04' 
auth_token = '[auth_token]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12055706562',   
                              body = ' it works '     
                              to='my_phone_number' 
                          ) 
 
print(message.sid)


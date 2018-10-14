#Day 27 & 28

import requests
from twilio.rest import TwilioRestClient

username = 'username' 
account_sid = username
password = 'password' 

number_to_text = '+5531845152' 
twilio_number = '+5531845152'
message_body = 'Another new one!!'
media_url = 'http://img2.10bestmedia.com/Images/Photos/96123/captiva-beach-captiva_54_990x660_201404211817.jpg'

"""
Create / Send  --- POST METHOD
"""

message = client.messages.create(
    to = number_to_text,
    from_ = twilio_number,
    body = message_body,
    media_url = media_url,
)

print(message.sid)
print(message.media_list.list())


message_data = client.messages.get(sid='MM84e7ab9fd6af47a6a7e4012703ba317c')

print(message_data)
print(dir(message_data))

image_list = [i.uri for i in message_data.media_list.list()]
print(image_list)


"""
the_new_list = []
for x in some_list:
    the_new_list.append(x.uri)


OPTIONAL
status_callback = "http://www.yourwebsite.com/some/way/to/handle/"

message = client.messages.create(
    to=number_to_text,
    from_=twilio_number,
    body=message_body,
    media_url=media_url,
    status_callback=status_callback,
)
"""





def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)






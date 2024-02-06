import boto3
pinpoint = boto3.client('pinpoint', region_name='us-east-1')  
application_id = '36208f9837714d56b830a7b66fdaf5ec'
to_address = 'emiroberti@icloud.com'
from_address = 'emiroberti@icloud.com'  

response = pinpoint.send_messages(
    ApplicationId=application_id,
    MessageRequest={
        'Addresses': {
            to_address: {
                'ChannelType': 'EMAIL'
            }
        },
        'MessageConfiguration': {
            'EmailMessage': {
                'FromAddress': from_address,
                'SimpleEmail': {
                    'Subject': {
                        'Charset': 'UTF-8',
                        'Data': 'Your email subject here'
                    },
                    'HtmlPart': {
                        'Charset': 'UTF-8',
                        'Data': '<html><head></head><body><p>Your email body in HTML format here</p></body></html>'
                    },
                    'TextPart': {
                        'Charset': 'UTF-8',
                        'Data': 'Your email body in text format here'
                    }
                }
            }
        }
    }
)

print(response)

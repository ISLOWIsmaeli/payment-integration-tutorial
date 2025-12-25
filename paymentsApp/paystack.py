import json
import requests
from django.conf import settings

def checkout(payload):
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        'https://api.paystack.co/transaction/initialize',
        headers=headers, 
        data=json.dumps(payload)
    )
    response_data = response.json() 
    print("I need to know how the response looks like:")
    print(response_data)
    print("/////////////////////End of knowing how response data looks like///////////////////////////////////")

    if response_data.get('status') == True:
        return True, response_data['data']['authorization_url']
    else:
        return False, "Failed to initiate payment, please try again later."
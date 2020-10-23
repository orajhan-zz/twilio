import io
import json
import logging
import os
from fdk import response
from twilio.rest import Client

def handler(ctx, data: io.BytesIO = None):
    message = os.environ.get("message")
    try:
        # get account sid and token from Twilio console
        account_sid = os.environ.get("my_account_sid")
        auth_token = os.environ.get("my_auth_token")
        client = Client(account_sid, auth_token)

        sms_from = os.environ.get("sms_from")
        send_to = os.environ.get("send_to")
        logging.getLogger().info(sms_from,send_to)
        sms = client.messages.create(body=message, from_=sms_from, to=send_to)

        logging.getLogger().info(sms.sid)

    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    logging.getLogger().info("Message hase been sent by Twilio")

    return response.Response(
        ctx, response_data=json.dumps(
            {"message": " {0}".format(message)}),
        headers={"Content-Type": "application/json"}
    )

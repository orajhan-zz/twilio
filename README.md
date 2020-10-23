# Send a SMS via Twilio using OCI Function
https://docs.cloud.oracle.com/en-us/iaas/Content/Notification/Tasks/managingtopicsandsubscriptions.htm#

PagerDuty has been integrated with OCI Notofication Service but PagerDuty is not the only option to send a SMS.
We are able to integrate with OCI Function that will be invoked by many other services. 
You can manage the contents of message as well as phone number in OCI console itself.  (please ensure your phone number is verified in Twilio)

# Twilio trial accounts cannot send messages to unverified numbers
verify  at twilio.com/user/account/phone-numbers/verified
To add another verified number, you need to upgrade account from Trial, hence my code sends a SMS to one verified phone number.

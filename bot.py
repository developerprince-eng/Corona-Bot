from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'bulawayo' in incoming_msg or 'welcome' in incoming_msg:
        msg.body('*Welcome* *to* *BPRA* , Empowering residents and promoting social accountability and good local governance!  Corona Virus/ COVID19 pandemic is upon us keep social distance and good hygiene practices . Please help us monitor service delivery in your ward by sending updates .\n\nSend \n*Services* for Service updates.\n*About*  COVID-19 / Corona virus\n*Help* for Bulawayo Service number\n\n*Menu* for full Menu option.')       
        responded = True

    if 'menu' in incoming_msg:
        msg.body('*Menu*: \n\n*Lockdown \U0001F512*\n*Symptoms \U0001F637*\n*Prevention* \U0001F3E5 \n*Help* \U0001F6C2\n*Stats* \U0001F4F0	\n\n')
        responded = True

    if  'services' in incoming_msg or 'lockdown' in incoming_msg:
        msg.body('\n\n*For* *Service* *Assistance*\nPlease send *Ward* followed by your *ward* *number*\nFollowed by service not available *water*, *refuse* \n\ne.g. Ward 12 water')
        responded = True

    if 'about' in incoming_msg: 
        msg.body('\n\n*What* *is* *COVID-19?*\n\nCoronaviruses are a large family of viruses which may cause illness in animals or humans.  In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS).\n\n*The* *most* *recently* *discovered* *coronavirus* *causes* *coronavirus* *disease* *COVID-19.*\n\n*What* *is* *COVID-19?*\n\nCOVID-19 is the infectious disease caused by the most recently discovered coronavirus.The first case of the virus has been identified in Wuhan, Hubei Province, China.United Nations, Public health officials and partners are working hard to identify the source of the virus.')
        responded = True

    if 'symptoms' in incoming_msg: 
        msg.body('\n\n*Coronavirus* *symptoms* *include*:\n1. Respiratory Symptoms \n2. Fever \n3. Cough \n4. Shortness of breath \n5. Breathing Difficulties')
        responded = True

    if 'prevent measures' in incoming_msg or 'measures' in incoming_msg: 
        msg.body('\n\n*Perform* *the* *Following* *as* *Preventative* *measures*: \n\n1. Wash you hands under running water with soap for 20 seconds. \n2. Use Hand sanitizer regularly\n3. Practice Social Distancing keeping a distance of 2 meters apart.')
        responded = True

    if 'help' in incoming_msg:
        msg.body('\n\n*For* *Assistance* *Please* *use* *the* *following* *Contacts*: \n\n1. *Police* - *0292* *995/* *72515* \n2. *Ambulance* - *0292* *68496* \n3. *Council* *faults* - *0292* *75011* ')
        responded = True

    if 'fatalities' in incoming_msg or 'stats' in incoming_msg:
        msg.media('https://oncocare.co.zw/wp-content/uploads/2014/05/MHC.jpg')
        msg.body('*Fatalities*: *1* \n*Cases*: *194* \n*Confirmed*: *7*\n*Negative*: *187*\n')
        responded = True

    if 'ward 1 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 1 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 1 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 1 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 2 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 2 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 2 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 2 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 3 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 3 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 3 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 3 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 4 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 4 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 4 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 4 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 5 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 5 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 5 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 5 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 6 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 6 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 6 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 6 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 7 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 7 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 7 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 7 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 8 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 8 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 8 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 8 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True 
    if 'ward 9 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 9 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 9 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 9 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 10 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 10 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 10 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 10 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 11 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 11 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 11 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 11 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 12 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 12 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 12 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 12 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 13 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 13 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 13 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 13 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 14 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 14 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 14 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 14 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 15 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 15 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 15 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 15 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 16 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 16 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 16 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 16 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True  
    if 'ward 17 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 17 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 17 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 17 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 18 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 18 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 18 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 18 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 19 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 19 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 19 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 19 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 20 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 20 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 20 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 20 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True 
    if 'ward 21 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 21 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 21 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 21 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 22 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 22 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 22 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 22 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 23 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 23 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 23 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 23 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True  
    if 'ward 24 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 24 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 24 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 24 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 25 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 25 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 25 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 25 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 26 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 26 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 26 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 26 your refuse complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'ward 27 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 27 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 27 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 27 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True  
    if 'ward 28 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 28 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 28 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 28 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 29 water' in incoming_msg:
        msg.body('Thank you complaint member of Ward 29 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True
    if 'ward 29 refuse' in incoming_msg:
        msg.body('Thank you complaint member of Ward 29 your water complaint has been noted, Relevent authorities shall be notified')
        responded = True   
    if 'made' in incoming_msg or 'developed' in incoming_msg :
        msg.media("https://developerprince.herokuapp.com/static/assets/images/logo.png")
        msg.body('This bot was made by \U0001F913	*DeveloperPrince* \U0001F31F')
        responded = True
    if not responded:
        resp = 'Please press for *Menu* for Menu '
        msg.body(resp)
    return str(resp)


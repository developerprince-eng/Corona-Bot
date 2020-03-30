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
    if 'corona' in incoming_msg or 'welcome' in incoming_msg:
        msg.body('*Welcome* *to* *BPRA* , Empowering residents and promoting social accountability and good local governance!  Corona Virus/ COVID19 pandemic is upon us keep social distance and good hygiene practices . Please help us monitor service delivery in your ward by sending updates .\n\nSend \n*Services* for Service updates.\n*About*  COVID-19 / Corona virus\n*Help* for Bulawayo Service number\n\n*Menu* for full Menu option.')       
        responded = True

    if 'menu' in incoming_msg:
        msg.body('*Menu*: \n\n*1*. *Services*\n*2*. *Symptoms*\n*3*. *Prevent Measures*\n*4*. *Help*\n*5*. *Stats*\n\n')
        responded = True

    if  'services' in incoming_msg:
        msg.body('\n\n*For* *Service* *Assistance*\nPlease send *Ward* followed by your *ward* *number*\nFollowed by service not available *water*, *refuse* \n\ne.g. Ward 12 water')
        responded = True

    if 'about' in incoming_msg: 
        msg.body('\n\nCOVID-19 is the infectious disease caused by the most recently discovered coronavirus. This new Virus and disease were unknown before the outbreak began in Wuhan, China in December 2019 (WHO 2020)')
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
        msg.body('*Fatalities*: *1* \n*Cases*: *6* \n*Confirmed*: 4\n')
        responded = True

    if 'ward 1 water' in incoming_msg:
        msg.body('Thank you complaint has been noted for Ward 1, Relevent authorities shall be notified')
        responded = True
    if 'ward 1 refuse' in incoming_msg:
        msg.body('Thank you complaint has been noted for Ward 1, Relevent authorities shall be notified')
        responded = True
    if 'ward 2 water' in incoming_msg:
        msg.body('Thank you complaint has been noted for Ward 1, Relevent authorities shall be notified')
        responded = True
    if 'ward 2 refuse' in incoming_msg:
        msg.body('Thank you complaint has been noted for Ward 1, Relevent authorities shall be notified')
        responded = True   
    if 'ward 3 water' in incoming_msg:
        msg.body('Thank you complaint has been noted for Ward 1, Relevent authorities shall be notified')
        responded = True
    if 'ward 3 refuse' in incoming_msg:
        msg.body('Thank you complaint has been noted for Ward 1, Relevent authorities shall be notified')
        responded = True   
    if 'ward 4 water' in incoming_msg:
        msg.body('Thank you complaint has been noted for Ward 1, Relevent authorities shall be notified')
        responded = True
    if 'ward 4 refuse' in incoming_msg:
        msg.body('Thank you complaint has been noted for Ward 1, Relevent authorities shall be notified')
        responded = True   
    if 'made' in incoming_msg or 'developed' in incoming_msg :
        msg.media("https://developerprince.herokuapp.com/static/assets/images/logo.png")
        msg.body('This bot was made by *DeveloperPrince*')
        responded = True
    if not responded:
        resp = 'Please press for *Menu* for Menu '
        msg.body(resp)
    return str(resp)
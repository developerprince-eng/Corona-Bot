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
    if 'Corona' in incoming_msg:
        msg.body('Welcome to WILD interactive chat\n This Platform will help you get information on Corona Virus and how to avoid contracting it while if you suspect you might have contracted it please press 5 so that you get tested or send 1 for Menu. ')       
        responded = True
    if '1' in incoming_msg:
        msg.body('2. What is COVID-19/ CORONA VIRUS \n3. Symptoms \n4. Preventative Measures \n5. How to Get Help \n6. Corona Staticstics in Bulawayo')
        responded = True
    if '2' in incoming_msg:
        msg.body('COVID-19 is the infectious disease caused by the most recently discovered coronavirus. This new Virus and disease were unknown before the outbreak began in Wuhan, China in December 2019 (WHO 2020)')
        responded = True
    if '3' in incoming_msg:
        msg.body('Coronavirus symptoms include: \n1. Respiratory Symptoms \n2. Fever \n 3. Cough \n4. Shortness of breath \n5. Breathing Difficulties')
        responded = True
    if '4' in incoming_msg:
        msg.body('Perform the Following as Preventative measures: \n 1. Wash you hands under running water with soap for 20 seconds. \n2. Use Hand sanitizer regularly\n3. Practice Social Distancing keeping a distance of 2 meters apart.')
        responded = True
    if '5' in incoming_msg:
        msg.body('Contact any Clinic Close to you')
        responded = True
    if '6' in incoming_msg:
        msg.body('Fatalities: 1 \n Cases: 6 \n Confirmed: 4\n')
        responded = True
    if 'made' in incoming_msg or 'developed' in incoming_msg :
        msg.body('This bot was made by *DeveloperPrince*')
        responded = True
    if not responded:
        resp = 'Please press for 1 for Menu'
        msg.body(resp)
    return str(resp)
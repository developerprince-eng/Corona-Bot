# CORONA BOT

![DeveloperPrince](https://developerprince.herokuapp.com/static/assets/images/logo.png)

This a python based bot build for aiding people during the Corona Crisis.

## Tools and frameworks

1. The bot has been built using python 3.7.4
2. Twilio 
3. Flask

## Setup

1. Create Virtual Environment

```bash 
python -m venv dev 
python3 -m venv dev
```

2. Activate Virtual Environment

```bash
dev\Scripts\activate
```

or 

```bash
source dev\bin\activate 
```

3. Install  packages

```bash
pip install -r requirements.txt
```

4. Set up environment and run

```bash 
set FLASK_ENV=development && set FLASK_APP=bot.py
flask run
```
or

```bash
export FLASK_ENV=development && export FLASK_APP=bot.py
flask run
```

5. Globally Port using ngrok

```bash
ngrok http 500
```

Then use the http or https which are created by ngrok for globally accessing your local host application and connect to channel of your choice in Twilio Console. 

Enjoy. 

Project is Developed by **DeveloperPrince**.
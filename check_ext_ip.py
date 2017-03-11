import smtplib
import os.path
from email.mime.text import MIMEText
from requests import get
import urllib.request
from urllib.request import urlopen


file_path = "/tmp/ip_ext.txt"
ip_act = get('https://api.ipify.org').text

def send_mail(ip):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your mail adress", "your password")
    body ="your new external ip: %s" %ip
    msg = MIMEText(body)
    msg['Subject'] = 'Subject'
    msg['From'] = 'sender'
    msg['To'] = 'receiver'
    server.sendmail("sender adress", "receiver adress", msg.as_string())
    server.quit()

def internet_on():  #Do whe have an internet connexion?
    try:
        urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as err:
        return False

if internet_on():
    if os.path.exists(file_path):
        with open(file_path,'r') as fch:
    	       ip_anc = fch.read()

        if ip_act != ip_anc:
    	       send_mail(ip_act)

    with open(file_path,'w') as fch:
        fch.write(ip_act)

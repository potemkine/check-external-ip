# check-external-ip
Check the external IP. Useful when you host a server at home and dont want to use an dyndns


I use it at home on a raspberry pi, with a cron launching it every 10 MN.


First the script test if we have an internet connexion, then if the external ip adress changed since the last time the script was launched, an e-mail is sent to the receiver of your choice to inform him of the new ip address.


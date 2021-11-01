import os
import random
import schedule
import time
import tweepy

from paramiko import AutoAddPolicy, SSHClient
from scp import SCPClient

from frames import FRAMES
from tokens import *



def twitter(): 
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)

def job(): 
    frame = random.choice(FRAMES)
    frame = f"/Volumes/SYMPHOGEAR/{frame}"
    os.system(f"cp {frame} frame.jpg")
    
    try: 
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(
            hostname= SERVER_IP,
            port = "22",
            username = "root", 
            password = SEVER_PASSWORD
            )
        
        with SCPClient(ssh.get_transport()) as scp: 
            scp.put('./frame.jpg', '/var/www/html')
    except Exception as e: 
        print(e)
        
    try: 
        twitter().update_status_with_media(status = "", filename = frame)
    except Exception as e: 
        print(e)


schedule.every().hour.at(":00").do(job)
schedule.every().hour.at(":05").do(job)
schedule.every().hour.at(":10").do(job)
schedule.every().hour.at(":15").do(job)
schedule.every().hour.at(":20").do(job)
schedule.every().hour.at(":25").do(job)
schedule.every().hour.at(":30").do(job)
schedule.every().hour.at(":35").do(job)
schedule.every().hour.at(":40").do(job)
schedule.every().hour.at(":45").do(job)
schedule.every().hour.at(":50").do(job)
schedule.every().hour.at(":55").do(job)

while True: 
    schedule.run_pending()
    time.sleep(1)










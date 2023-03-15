import pysftp
import datetime
from telethon import TelegramClient, events, Button
import os

# Coded by M.A.H
# ID Telegram : @DevSecIR

remote_path = '/etc/x-ui/x-ui.db'

# Information needed to send a message to Telegram
api_hash = '7a6c5903264' # your Api Hash
api_id = 12345 # your Api Id

client = TelegramClient("bot", api_id=api_id, api_hash=api_hash)
client.start()

chat_id = -10012345 # Channel id 

data = [
    {
        "host": 'example',
        "user" : 'root',
        "pass" : 'Password',
        'remote' : '/etc/x-ui/x-ui.db'
    } ,
    {
        "host": 'example',
        "user" : 'root',
        "pass" : 'Password',
        'remote' : '/etc/x-ui/x-ui.db'
    } ,
    {
        "host": 'example',
        "user" : 'root',
        "pass" : 'Password',
        'remote' : '/etc/x-ui/x-ui.db'
    }
    
]

# solar date
date_str = datetime.datetime.now().strftime('%Y/%m/%d')

# Work !!
async def main():
    async with client:
        for i in data :
            # Information required to connect to the SFTP server
            hostname = i["host"]
            username = i['user']
            password = i['pass']
            remote_path = i['remote']

            # Connect to the SFTP server
            with pysftp.Connection(host=hostname, username=username, password=password, port=22) as sftp:
                # file download
                with sftp.cd('/'):
                    sftp.get(remote_path)

            # Send file to Telegram
            with open('x-ui.db', 'rb') as f:
                await client.send_file(entity=chat_id, file=f, caption=f'Date : {date_str}\n\nIP : `{hostname}`')

            # Delete the file from the system
            os.remove('x-ui.db')
client.loop.run_until_complete(main())

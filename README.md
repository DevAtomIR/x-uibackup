<h1 align="center"><img src="https://cdn-icons-png.flaticon.com/512/2818/2818765.png" width="30" height="30" alt="backup"> x-ui Backup</h1>
Backup x-ui.db file on servers in <a href="https://github.com/FranzKafkaYu/x-ui">x-ui panel</a>
<em><h5 align="center"><img src="https://cdn-icons-png.flaticon.com/512/5968/5968350.png" width="15" height="15" alt="python"> (Programming Language - Python 3)</h5></em>



## Documentation
**Clone and Install Script**
```
git clone https://github.com/DevAtomIR/x-uibackup/
cd x-uibackup
pip install -r requirements.txt
python3 backup.py
```
 
## How to use the script
Install requirements.txt before running the script

Edit the backup.py file
replace the `api_id` and `api_hash` sections in the script
* [To get api id and hash](https://my.telegram.org/apps)

Enter the numeric ID of the Telegram channel in the `chat_id` field of the script
* [To get id channel](https://t.me/userinfobot)

In the data section, write your server information
```     
 {
   "host": 'example',
   "user": 'root',
   "pass": 'Password',
   'remote' : '/etc/x-ui/x-ui.db'
 }
```
📝Note :
Before running the script, please connect to the servers that you want to backup through SSH, so that your session is created in `~/.ssh/known_hosts.`\
Better to set up a cron job for the script to automatically backup
##

* [Telegram](https://t.me/DevAtom)
* [GitHub](https://github.com/DevAtomIR)


#### 💰 Donation Links

<b>BTC</b> : `bc1qucxu8r6xza0l38zqsxrq3c6sunx880cm2tj4dr`</br>
<b>TRON</b> : `TML3NtgE8J6iqR8UFq5JuCthwvbjH6KH7U`</br>
<b>USDT(TRC20)</b> : `TExYVr8ZPHf9FJcnimD9wnnUTwbBjGZFxk`</br>
<b>TON</b> : `EQBI-iR-BSVZDffrjlRuhVSIMN9BkAV9uHFWoy-TeIOV978t`</br></br>

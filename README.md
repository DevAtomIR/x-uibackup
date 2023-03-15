<h1 align="center">x-ui Backup</h1>
Backup x-ui.db file on servers in x-ui panel
<em><h5 align="center">(Programming Language - Python 3)</h5></em>



## Documentation
**Clone and Install Script**
```shell script
git clone https://github.com/AnonSecIR/x-uibackup/
cd x-uibackup
pip install -r requirements.txt
python3 backup.py
```

* [Developer](https://t.me/DevSecIR)
 
 ## How to use the script
 Install requirements.txt before running the script

Edit the backup.py file
Replace these in the script
api_hash = ''
api_id = 123456
* [To get api id and hash](https://my.telegram.org/apps)

In the data section, write your server information
```     
 {
   "host": 'example',
   "user": 'root',
   "pass": 'Password',
   'remote' : '/etc/x-ui/x-ui.db'
 }
```
 

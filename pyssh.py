

import paramiko
import datetime




def connect(host, user, psw):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=psw)
    return ssh

def executerecorrente():
    ssh = connect('IP-ADDRESS','admin','PASSWORD')
    ssh.exec_command('reboot')
    ssh.close()

executerecorrente()

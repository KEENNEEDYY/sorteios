
#from typing import Sized
#from pysnmp.hlapi import *
#from random import shuffle
#from pathlib import Path
#import pyodbc
#import time
import paramiko
import datetime
#import mysql.connector
#from scp import SCPClient
#from multiprocessing.pool import ThreadPool
#import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from email.mime.base import MIMEBase
#from email import encoders



def connect(host, user, psw):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=psw)
    return ssh

def executerecorrente():
    ssh = connect('10.0.25.67','admin','R0ck3t')
    ssh.exec_command('reboot')
    ssh.close()

executerecorrente()

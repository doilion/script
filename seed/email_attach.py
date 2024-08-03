"""
发现真不太行 163邮箱的imap服务器不支持ID命令
"""

import imaplib
import email
from email.header import decode_header
import os
import sys

# 配置你的邮箱信息
username = '20213002838@hainanu.edu.cn'
# password = 'sxDBfxrjNuYcAGw7'
password = 'doilion12!'
# password = 'zAWyf97ssxtCQxCB'
imap_url = 'imap.163.com'

import imaplib

# 添加缺失的命令
imaplib.Commands['ID'] = ('AUTH')

conn = imaplib.IMAP4_SSL(port = '993',host = 'imap.163.com')
conn.login('liwenjie@hainanu.edu.cn','sxDBfxrjNuYcAGw7')

# 上传客户端身份信息
args = ("name","XXXX","contact","20213002838@hainanu.edu.cn","version","1.0.0","vendor","myclient")
typ, dat = conn._simple_command('ID', '("' + '" "'.join(args) + '")')
print(conn._untagged_response(typ, dat, 'ID'))

status, msgs = conn.select()
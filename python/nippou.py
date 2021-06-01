# -*- coding:utf-8 -*-
import smtplib, ssl
from email.mime.text import MIMEText
from datetime import datetime

import sys
args = sys.argv
Place = args[1]
Time = args[2]


# アカウント情報
gmail_account  = r"送信元メールアドレス"
gmail_password = r"アカウントパスワード"

# context作成
context = ssl.create_default_context()

# Gmailにログイン
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
server.login(gmail_account, gmail_password)

body_str = "お疲れ様です。" + "<br>" + "<br>"
body_str += "本日は" + Place + "に直行後出勤します" + "<br>"
body_str += "そのため到着は" + Time + "後になる予定です" + "<br>" + "<br>"
body_str += "以上、よろしくお願いします"


# メールデータ(MIME)作成
msg = MIMEText(body_str, "html")
msg["Subject"] = "メールタイトル"     # メールタイトル
msg["To"]      = "送信先メールアドレス" # 送信先メールアドレス(適宜書き換える)
msg["From"]    = gmail_account       # 送信元メールアドレス

# メール送信
server.send_message(msg)
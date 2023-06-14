import os 
import smtplib 
from dotenv import load_dotenv
import json

load_dotenv()

#Работа с текстом письма
text=("""Привет, %friend_name%! %my_name% приглашает тебя на сервер по майнкрафт %server_name%!

%server_name% — это новая версия самого крутого сервера майнкрафт
Лучшие условия,новые знакомства, выживание и главное - самые отзывчивые админы!

%friend_name%, присоединяйся к %server_name%""")

server_name="MineSurvival"
player_name="SlackJaguar786"
my_name="PoPcOrN7407"

text=text.replace("%server_name%", server_name)
text=text.replace("%friend_name%", player_name)
text=text.replace("%my_name%", my_name)


email_from=os.getenv("EMAIL_FROM")
email_to="dariashmidkova@yandex.ru"


headers=f"""From: {email_from}
To: {email_to}
Subject: Ограниченное предложение! Приглашение!Креатив-for free!
Content-Type: text/plain; charset="UTF-8";

"""

letter=headers+text
print (letter)
letter=letter.encode("UTF-8")
with open("mails.json", "r") as my_file:
    file_contents = my_file.read()
    file_contents = json.loads(file_contents)

password=os.getenv("PASSWORD")
server = smtplib.SMTP_SSL('smtp.yandex.com:465')
server.login(email_from, password)
for pochta in file_contents:          
#Отправка письма ``~~~''''''
    server.sendmail(email_from,pochta,letter)
    print ("Сообщение отправлено успешно!")
server.quit() 

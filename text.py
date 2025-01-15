import smtplib

email_sender = "iljuhasirotenko@yandex.ru"
password = "cakhejxcxojszpxz"
email_getter = "ilyshasirotenko@yandex.ru"

server = smtplib.SMTP_SSL("smtp.yandex.ru:465")

server.login(email_sender, password)

sender = 'iljuhasirotenko@yandex.ru'
destination = 'ilyshasirotenko@yandex.ru'
name_text = 'Приглашение!'

letter = """From: {sender}
To: {destination}
Subject: {name_text}
Content-Type: text/plain; charset="UTF-8

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл""". format(sender = sender, destination = destination, name_text = name_text);
letter = letter. replace("%website%", "https://dvmn.org/profession-ref-program/ilya.sirotenko.01/eR7lL/")
letter = letter. replace("%friend_name%", "Влад") 
letter = letter. replace("%my_name%","Илья")
letter = letter.encode("UTF-8")

server.sendmail(email_sender, email_getter, letter)
server.quit()

print(letter)

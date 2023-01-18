import smtplib , ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "shobhitraj4757@gmail.com"  # Enter your address
receiver_email = "shobhitrajpatna@gmail.com"  # Enter receiver address
password = '****************'
message = """This is SHOBHIT RAJ message while learning python 19/1/2023"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

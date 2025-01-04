import smtplib, ssl




def send_email(message):

    #connecting the mail to the server
    username = "bear062005@gmail.com"
    password = "kmfu mpfn jgqe pees"

    #receiving mail
    receiver = "bear062005@gmail.com"

    #default
    host= "smtp.gmail.com"
    port = 465

    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)




import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_log_to_email(email_from, email_to, password, file_name, html_report):
    msg = MIMEMultipart('alternative')
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = "Autotests results"

    with open(file_name, "rb") as f:
        part = MIMEApplication(f.read(), Name=basename(file_name))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file_name)
        msg.attach(part)

    body = "Autotests results for GB stand https://test-stand.gb.ru"

    with open(html_report, 'r', encoding='utf-8') as f:
        html_report_text = f.read()

    body += html_report_text
    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(email_from, password)
    text = msg.as_string()
    server.sendmail(email_from, email_to, text)
    server.quit()

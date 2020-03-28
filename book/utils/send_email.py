from django.core.mail import send_mail
import base64
import uuid

from demo4.models import EmailVerifyRecord
from book.settings import EMAIL_FROM


def send_register_email(email):
    email_record = EmailVerifyRecord()
    code = base64.b64encode(uuid.uuid4().bytes)
    email_record.code = code
    email_record.email = email
    email_record.save()

    email_title = "【测试】注册激活链接"
    email_body = "请点击下面的连接激活你的账号：http://192.168.18.153:8000/active/{0}".format(code)

    send_mail(email_title, email_body, EMAIL_FROM, [email])


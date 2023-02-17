from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Py25 account project',
        f'http://localhost:8000/api/v1/account/activate/{code}/',
        'baitikovskij@gmail.com',
        [email]
    )
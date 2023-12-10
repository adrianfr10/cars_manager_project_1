from flask_mail import Mail, Message

class MailConfig:
    mail = None

    @classmethod
    def init(cls, app) -> None:
        cls.mail = Mail(app)

    @classmethod
    def send_register_token(cls,sender_mail: str, recipient_email: str, token: str) -> None:
        if not cls.mail:
            raise Exception('Mail not initialized. Call init() first.')

        msg = Message('Your register token', sender=sender_mail, recipients=[recipient_email])
        msg.body = f'Welcome! Your register token: {token}'
        try:
            cls.mail.send(msg)
        except Exception as e:
            raise Exception(f'Error during sending e-mail: {str(e)}')

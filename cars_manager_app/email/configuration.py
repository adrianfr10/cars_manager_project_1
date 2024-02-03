from flask_mail import Mail, Message

class MailConfig:
    """
    This class is used for email configuration with Flask
    """
    mail = None

    @classmethod
    def init(cls, app) -> None:
        """
        This method is used to initialize mail attribute of the class, that is set to None
        :param app:
        :return:
        """
        cls.mail = Mail(app)

    @classmethod
    def send_register_token(cls,sender_mail: str, recipient_email: str, token: str) -> None:
        """
        This method preforms sending an email that contains a register token, to specified recipients
        :param sender_mail:
        :param recipient_email:
        :param token:
        :return:
        """
        if not cls.mail:
            raise Exception('Mail not initialized. Call init() first.')

        msg = Message('Your register token', sender=sender_mail, recipients=[recipient_email])
        msg.body = f'Welcome! Your register token: {token}'
        try:
            cls.mail.send(msg)
        except Exception as e:
            raise Exception(f'Error during sending e-mail: {str(e)}')

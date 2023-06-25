import random
import string
import logging as logger


def generate_random_email_and_password(domain=None, email_prefix=None):
    if not domain:
        domain = 'test.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_string = ''.join(random.choices(string.ascii_letters, k=10))
    email = email_prefix + '_' + random_string + '@' + domain
    password = ''.join(random.choices(string.ascii_letters, k=20))

    logger.info(f"Generated random email: {email}")

    return {"email":email, "password":password}

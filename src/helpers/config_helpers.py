import os


def get_base_url():
    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'http://localhost:9999/testsite'

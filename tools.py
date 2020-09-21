import jsonpickle
import json
from fake_usrag_bor import FakeUserAgentBOR

ua = FakeUserAgentBOR()
rheader = ua.simple_header(ua.random_chrome_user_agent)
proxies = {
        "https": "http://185.25.206.192:3128",
}


def message_pp(message):
    return json.dumps(json.loads(jsonpickle.encode(message)), indent=4, sort_keys=True)


def write_log(message):
    with open('logs.txt', 'a') as log_file:
        log_file.write(message_pp(message) + 2 * '\n')
    print('Логи успешно записаны!')


def clear_logs():
    with open('logs.txt', 'w'):
        print('Логи были успешно очищены!')

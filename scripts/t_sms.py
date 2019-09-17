from libs.txm import send_sms, get_code

if __name__ == '__main__':
    code = get_code()
    print(code)
    result = send_sms('18352556410', code, '5')
    print(result)


from qcloudsms_py import SmsSingleSender
from .settings import *
from utils.logging import logger
import random

sender = SmsSingleSender(appid, appkey)

# 短信发送成功的标识：发送后没有异常，响应的大字典中result值为0
# {'result': 0, 'errmsg': 'OK', 'ext': '', 'sid': '2028:f826a20b647e9cfa4100', 'fee': 1}
def send_sms(mobile, code, exp):
    try:
        response = sender.send_with_param(86, mobile,
            template_id, (code, exp), sign=sms_sign, extend="", ext="")
    except Exception as e:
        logger.error('sms error: %s' % e)
        return False
    if response and response['result'] == 0:
        return True
    logger.error('sms error: %s' % response['errmsg'])
    return False


def get_code():
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    return code


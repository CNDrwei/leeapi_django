from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
from settings import constant
from .logging import logger
# mac
import ssl

ssl._create_unverified_context = ssl._create_default_https_context

_app_id = constant.APP_ID
_app_key = constant.APP_KEY
_template_id = 402722
_sms_sign = "Owen的技术栈"

# 需要发送短信的手机号码
phone_numbers = ["18516575654"]

_sender = SmsSingleSender(_app_id, _app_key)

import random

def get_code():
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    return code

def send_sms_params(mobile, code, ex):
    result = None
    try:
        result = _sender.send_with_param(86, mobile, _template_id, (code, ex),
                                         sign=_sms_sign, extend="", ext="")
    except HTTPError as e:
        logger.warning(e)
    except Exception as e:
        logger.warning(e)
    if result and result.get('result') == 0:
        return True
    return False


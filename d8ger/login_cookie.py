#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import ssl
import os

import requests

# 屏蔽HTTPS证书校验, 忽略安全警告
requests.packages.urllib3.disable_warnings()
context = ssl._create_unverified_context()

user_home = os.path.expanduser('~')


def auto_login() -> str:
    """
    自动登录, 获取登录Cookie
    :rtype: str
    """
    try:
        with open(user_home + "/ssoLogin.json", 'r') as sso_login_request_data:
            request_json = json.load(sso_login_request_data)
    except Exception as e:
        print("当前用户目录{}下不存在{}文件, 请先创建并按照JSON格式填写请求数据".format(user_home, "ssoLogin.json"))
        print("示例ssoLogin.json:")
        default_login = {
            "url": "https://sso.testa.huitong.com/api/v100/ssonew/login",
            "method": "POST",
            "headers": {
                "Content-Type": "application/json",
                "HT-app": 6
            },
            "body": {
                "phone": "18999999999",
                "smsAuthCode": "123456",
                "loginType": 0,
                "pwd": "ht123456."
            }
        }
        print(json.dumps(default_login, ensure_ascii=False, indent=4))
        exit(0)
    url = request_json['url']
    method = request_json['method']
    request_headers = handle_json_str_value(request_json['headers'])
    request_body = handle_json_str_value(request_json['body'])
    # request_headers = {"Content-Type": "application/json", "HT-app": "6"}
    response = requests.request(method, url, headers=request_headers, json=request_body, timeout=3, verify=False)
    response_headers = response.headers
    # 处理Cookie, 多个Cookie之间使用';'分隔, 否则校验cookie时出现"domain."在高版本中tomcat中报错
    # https://blog.csdn.net/w57685321/article/details/84943176
    cookie = response_headers.get("set-Cookie").replace(", _r", "; _r").replace(", _a", "; _a")
    # JSON标准格式
    response_body = json.dumps(response.json(), ensure_ascii=False, indent=4)
    print("登录响应Cookie结果: \n{}\n登录响应BODY结果: {}".format(cookie, response_body))
    return cookie


def example_httpie_cmd(cookie: str):
    httpie_cmd = "http --verify=no -v POST http://localhost:8119/account/sentinel HT-app:6 Content-Type:application/json 'Cookie:{}' subAccountId:=123456 phone=16620975912"
    print(("示例Httpie命令: \n" + httpie_cmd).format(cookie))
    print("\nhttpie使用参考: https://httpie.org/docs#non-string-json-fields\n")


def handle_json_str_value(json: json) -> json:
    """
    将json的值都变为字符串处理
    :param json:
    :rtype: json
    """
    for (k, v) in json.items():
        json[k] = str(v)
    return json


def main():
    cookie = auto_login()
    example_httpie_cmd(cookie)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import ssl
# import os

import requests
import argparse

# 屏蔽HTTPS证书校验, 忽略安全警告
requests.packages.urllib3.disable_warnings()
context = ssl._create_unverified_context()

# user_home = os.path.expanduser('~')


def init_login_file_name() -> str:
    """
    初始化参数, 读取shell命令参数, 自动登录
    依次返回httpie_view方式, 线程池, 登录cookie
    :rtype: str
    """
    parser = argparse.ArgumentParser(description="登录解析器")
    parser.add_argument("-f", "--filepath", type=str, help="登录JSON文件路径, 默认 ~/ssoLogin.json")
    args = parser.parse_args()
    sso_login_file_name = args.filepath
    if sso_login_file_name is None or len(sso_login_file_name) == 0 or str.isspace(sso_login_file_name):
        sso_login_file_name = "~/ssoLogin.json"
    print("设置登录文件: [{}]".format(sso_login_file_name))
    return sso_login_file_name


def auto_login() -> str:
    """
    自动登录, 获取登录Cookie
    :rtype: str
    """
    login_file_name = init_login_file_name()
    try:
        with open(login_file_name, 'r') as sso_login_request_data:
            request_json = json.load(sso_login_request_data)
    except Exception as e:
        print("不存在{}文件, 请先创建并按照JSON格式填写请求数据".format(login_file_name))
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
                "pwd": "123456"
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
    httpie_cmd = "http --verify=no -v POST https://127.0.0.1:8080/account/sentinel HT-app:6 Content-Type:application/json 'Cookie:{}' subAccountId:=123456 phone=16620975912"
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

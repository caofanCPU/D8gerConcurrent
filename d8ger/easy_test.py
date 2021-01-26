#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import datetime
import ssl
from concurrent.futures.thread import ThreadPoolExecutor

import numpy as np
import requests

# 屏蔽HTTPS证书校验, 忽略安全警告
requests.packages.urllib3.disable_warnings()
context = ssl._create_unverified_context()
# D8GER just for joke


def init_param() -> list:
    """
    初始化参数, 读取shell命令参数, 自动登录
    依次返回httpie_view方式, 线程池, 登录cookie
    :rtype: list
    """
    parser = argparse.ArgumentParser(description="并发执行接口")
    parser.add_argument("url", type=str, help="接口请求地址")
    parser.add_argument("-w", "--workers", type=int, choices=choice_nums(1, 65, 1), default=1, help="并发执行线程数, 取值范围[1, 64]")
    parser.add_argument("-l", "--loops", type=int, default=1, help="循环执行次数")
    args = parser.parse_args()
    loops = args.loops
    if loops < 1:
        loops = 1
    print("参数设置结果: 请求url=[{}], 执行次数=[{}], 并发线程数=[{}]".format(args.url, loops, args.workers))
    init_executor = ThreadPoolExecutor(max_workers=args.workers)
    return [loops, init_executor, args.url]


def choice_nums(start: int, end: int, delta: int) -> list:
    """
    返回指定的数组序列
    :rtype: list
    """
    return np.arange(start, end, delta).tolist()


def execute_http(i):
    """
    执行excuteUrl.json接口
    :param i 仅用于计数虚拟参数
    :return:
    """
    request_headers = {}
    request_body = {}
    response_text = "无响应文本"
    execute_start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    try:
        response = requests.request("POST", url, headers=request_headers, json=request_body, timeout=60, verify=False)
        # JSON标准格式
        response_text = response.text
    except Exception as e:
        print(e)
    execute_end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    return "execute_start_time=[{}], execute_end_time=[{}]\n响应结果:\n{}".format(execute_start_time, execute_end_time, response_text)


def handle_json_str_value(json):
    """
    将json的值都变为字符串处理
    :param json:
    :return:
    """
    for (k, v) in json.items():
        json[k] = str(v)
    return json


def main():
    # 全局变量
    global execute_num
    global url
    global executor
    # 初始化参数
    initial_param_list = init_param()
    execute_num = initial_param_list[0]
    executor = initial_param_list[1]
    url = initial_param_list[2]
    nums = list(range(0, execute_num))
    for result in executor.map(execute_http, nums):
        print(result)
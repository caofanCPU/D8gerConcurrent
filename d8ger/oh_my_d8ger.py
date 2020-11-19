#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import subprocess
import argparse
import os


def test_d8ger():
    """
    测试
    """
    print("0")


def search_port_occupy():
    parser = argparse.ArgumentParser(description="查找被占用的端口")
    parser.add_argument("port", type=int, help="端口号")
    args = parser.parse_args()
    port = args.port
    if port is None or port < 0:
        print("端口号非法, 请输入合法的端口号")
        return
    cmd = 'lsof -i :{}'.format(port)
    execute_block_shell(cmd)


def search_pid():
    parser = argparse.ArgumentParser(description="根据关键字查找进程ID")
    parser.add_argument("keyword", type=str, help="目标进程匹配关键字")
    args = parser.parse_args()
    keyword = args.keyword
    if keyword is None:
        print("进程ID非法, 请输入合法的进程ID")
        return
    cmd = "ps aux | grep {} | grep -v grep | awk '{}'".format(keyword, "{print $2}")
    execute_block_shell(cmd)


def kill_pid():
    parser = argparse.ArgumentParser(description="根据关键字KILL进程ID")
    parser.add_argument("keyword", type=str, help="目标进程匹配关键字")
    args = parser.parse_args()
    keyword = args.keyword
    if keyword is None:
        print("进程ID非法, 请输入合法的进程ID")
        return
    cmd = '''
    pid=`ps aux | grep {} | grep -v grep | awk '{}'`
    if [ -n "$pid" ]; then
        kill -9 $pid
        sleep 1
    fi
    '''.format(keyword, "{print $2}")
    execute_block_shell(cmd)


def cph():
    print('''
    ,------.   ,---.  ,----.   ,------.,------.
    |  .-.  \ |  o  |'  .-./   |  .---'|  .--. '
    |  |  \  :.'   '.|  | .---.|  `--, |  '--'.'
    |  '--'  /|  o  |'  '--'  ||  `---.|  |\  \\
    `-------'  `---'  `------' `------'`--' '--'\n
    ##### SCP命令 #####
    # -r 支持复制目录及其子文件
    - 本地文件传到远程服务器
    scp /Users/D8GER/Desktop/ssoLogin/LEARN-SH.sh  caofan@172.16.10.59:~/
    - 从远程服务器拉取文件
    scp caofan@172.16.10.59:~/HAHA.tmp /Users/D8GER/Desktop/ssoLogin/ZZ.xls
    - 无痕登录
    xD8scp || d8scp
    sshpass -f /Users/D8GER/Desktop/CAOFAN/sshpass/caofan-ssh-dev.txt scp /Users/D8GER/Desktop/ssoLogin/LEARN-SH.sh  caofan@172.16.10.59:~/
    sshpass -f /Users/D8GER/Desktop/CAOFAN/sshpass/caofan-ssh-dev.txt scp caofan@172.16.10.59:~/HAHA.tmp /Users/D8GER/Desktop/ssoLogin/ZZ.xls
    ##### cpv #####, zsh的一个插件cp, 文件复制时展示进度条
    ##### sudo cp #####, 普通复制
    ''')


def fk_grep():
    print('''
    ,------.,--. ,--. ,----.   ,------. ,------.,------.
    |  .---'|  .'   /'  .-./   |  .--. '|  .---'|  .--. '
    |  `--, |  .   ' |  | .---.|  '--'.'|  `--, |  '--' |
    |  |`   |  |\   \'  '--'  ||  |\  \ |  `---.|  | --'
    `--'    `--' '--' `------' `--' '--'`------'`--'
    grep -n '[a-zA-Z0-9]D8' X.txt
    grep -n '[^a-zA-Z0-9]D9' X.txt
    grep -n '^[a-z]' X.txt
    grep -n '^[^a-z]' X.txt
    grep -n '^$' X.txt
    grep -n '\.$' X.txt
    grep -n 'g.*d' X.txt
    grep -n 'go*d' X.txt
    grep -n 'o\{2,3\}' X.txt
    grep -En 'God|The'  X.txt     grep -n 'god\|The' X.txt
    grep -En 'o+' X.txt           grep -n 'o\+' X.txt
    grep -n '\.' X.txt            grep -En '\.' X.txt
    grep -En '(oo)+' X.txt        grep -n '\(oo\)\+' X.txt
    Search Today's log: ll -ah | grep \"[a-z_A-Z]\+\.log\"
    ''')


def arthas_help():
    print('''
      ,---.  ,------. ,--------.,--.  ,--.  ,---.   ,---.
     /  O  \ |  .--. ''--.  .--'|  '--'  | /  O  \ '   .-'
    |  .-.  ||  '--'.'   |  |   |  .--.  ||  .-.  |`.  `-.
    |  | |  ||  |\  \    |  |   |  |  |  ||  | |  |.-'    |
    `--' `--'`--' '--'   `--'   `--'  `--'`--' `--'`-----'\n
    # `和\ 为特殊字符, 必须使用\转义
    # 观察方法返回值
    watch com.xyz.caofancpu.trackingtime.controller.D8gerController queryD8gerMoPage \"{params,returnObj}\" -x 2
    watch com.xyz.caofancpu.trackingtime.controller.D8gerController queryD8gerMoPage \"{params,returnObj}\"
    # 观察方法入参, 对象层次限制2级
    watch com.xyz.caofancpu.trackingtime.controller.D8gerController queryD8gerMoPage \"{params,returnObj}\" -x 2 -b
    # 持续记录3次接口调用
    tt -t -n 3 com.xyz.caofancpu.trackingtime.controller.D8gerController queryD8gerMoPage
    # 展示记录接口调用的列表
    tt -l
    # 展示某个具体调用过程
    tt -i 1002
    # 重复某个具体调用, 重复3次, 重复间隔2秒
    tt -i 1002 -p --replay-times 3  --replay-interval 2000
    # 日志器
    logger
    # 类加载器列表
    classloader -t
    history
    help
    keymap
    dashboard
    # 清屏
    cls
    # 线程
    thread
    thread --state WAITING
    thread --state TIMED_WAITING
    thread --state RUNNABLE
    # 退出、关闭等命令, 禁止ctrl + C
    # 退出某个命令
    Q
    # 退出当前arthas-client
    quit
    # 关闭arthas-server
    shutdown
    ''')


def six_x():
    parser = argparse.ArgumentParser(description="关键词匹配目录搜索")
    parser.add_argument("keyword", type=str, help="关键词")
    args = parser.parse_args()
    keyword = args.keyword
    if keyword is None:
        print("请输入匹配关键词")
        return
    cmd = 'ls -ah | grep {}'.format(keyword)
    execute_block_shell(cmd)


def execute_block_shell(cmd: str):
    os.system(cmd)

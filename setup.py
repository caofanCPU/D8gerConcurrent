from setuptools import setup, find_packages

install_requires = ['requests', 'numpy', 'argparse']

setup(
    name="D8gerConcurrent",
    version="4.2.2",
    keywords=("pip", "concurrent", "d8ger", "test", "easy", "shell"),
    description="concurrent test and useful shell command",
    long_description="make efficient for concurrent test, login, shell commands ",
    license="Apache Licence",

    url="https://github.com/caofanCPU/D8gerConcurrent.git",
    author="D8ger",
    author_email="xyb5to0ZCY@Gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=install_requires,
    scripts=[],
    entry_points={
        'console_scripts': [
            'Dwelcome=d8ger.oh_my_d8ger:welcome',
            'DsearchPortOccupy=d8ger.oh_my_d8ger:search_port_occupy',
            'DsearchPid=d8ger.oh_my_d8ger:search_pid',
            'DkillPid=d8ger.oh_my_d8ger:kill_pid',
            'D6x=d8ger.oh_my_d8ger:six_x',
            'Dhcp=d8ger.oh_my_d8ger:hcp',
            'DfkGrep=d8ger.oh_my_d8ger:fk_grep',
            'Desa=d8ger.oh_my_d8ger:arthas_help',
            'DloginCookie=d8ger.login_cookie:main',
            'DeasyHttp=d8ger.easy_test:main',
        ]
    },
)

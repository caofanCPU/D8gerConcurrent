from setuptools import setup, find_packages

install_requires = ['requests', 'numpy', 'argparse']

setup(
    name="D8gerConcurrent",
    version="4.2.0",
    keywords=("pip", "concurrent", "d8ger", "test"),
    description="concurrent d8ger test",
    long_description="efficient concurrent test for you d8ger interface",
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
            'testD8ger=d8ger.oh_my_d8ger:test_d8ger',
            'easyHttp=d8ger.easy_test:main',
            'loginCookie=d8ger.login_cookie:main',
            'Psearch_port_occupy=d8ger.oh_my_d8ger:search_port_occupy',
            'Psearch_pid=d8ger.oh_my_d8ger:search_pid',
            'Pkill_pid=d8ger.oh_my_d8ger:kill_pid',
            'Pcph=d8ger.oh_my_d8ger:cph',
            'Pfk_grep=d8ger.oh_my_d8ger:fk_grep',
            'Parthas_help=d8ger.oh_my_d8ger:arthas_help',
            'Psix_x=d8ger.oh_my_d8ger:six_x',
        ]
    },
)

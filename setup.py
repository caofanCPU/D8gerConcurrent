from setuptools import setup, find_packages

install_requires = ['requests', 'numpy', 'argparse']

setup(
    name="D8gerConcurrent",
    version="4.0.1",
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
            'easy-http=d8ger.easy_test:main',
            'login-cookie=d8ger.login_cookie:main'
        ]
    },
)

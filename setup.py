from setuptools import setup, find_packages

install_requires = ['requests', 'numpy', 'argparse']

setup(
    name="D8gerConcurrent",
    version="1.0.0",
    keywords=("pip", "concurrent", "http", "test"),
    description="concurrent http test",
    long_description="efficient concurrent test for you http interface",
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
        'console_scripts': ['easy-http=easy_test:main']
    },
)

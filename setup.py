from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='simple_portfolio',
    version='0.1.7',
    description='Simple portfolio metrics for Robinhood',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Weston Platter',
    author_email='westonplatter@gmail.com',
    url='https://github.com/westonplatter/simple_portfolio/',
    packages=['simple_portfolio'],
    install_requires=[
        'click',
        'fast_arrow==0.0.5',
        "pandas",
        "numpy"
    ],
    entry_points='''
        [console_scripts]
        sp=simple_portfolio.cli:cli
    ''',
)

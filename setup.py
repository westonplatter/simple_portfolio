from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='simple_metrics',
    version='0.1.7',
    description='Simple portfolio metrics for Robinhood',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Weston Platter',
    author_email='westonplatter@gmail.com',
    url='https://github.com/westonplatter/simple_metrics/',
    packages=['simple_metrics'],
    install_requires=[
        'click',
        'fast_arrow==0.0.4',
    ],
    entry_points='''
        [console_scripts]
        sm=simple_metrics.cli:cli
    ''',
)

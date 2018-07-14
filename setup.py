from distutils.core import setup

setup(name='simple_metrics',
    version='0.0.1',
    description='Simple portfolio metrics for Robinhood',
    author='Weston Platter',
    author_email='westonplatter@gmail.com',
    url='https://www.python.org/sigs/simple_metrics/',
    packages=['simple_metrics'],
    install_requires=[
        'click'
    ],
    dependency_links=[
        'https://github.com/Jamonek/Robinhood/archive/1.0.1.zip',
    ],
    entry_points='''
        [console_scripts]
        sm=simple_metrics.cli:cli
    ''',
)

from distutils.core import setup

setup(name='simple_metrics',
    version='0.1.0',
    description='Simple portfolio metrics for Robinhood',
    author='Weston Platter',
    author_email='westonplatter@gmail.com',
    url='https://www.python.org/sigs/simple_metrics/',
    packages=['simple_metrics'],
    install_requires=[
        'click',
        'Robinhood==1.0.1',
    ],
    dependency_links=[
        # # this git commit hash is master as of July 14th. It's 64 commits ahead of release 1.0.1
        # 'https://github.com/Jamonek/Robinhood/archive/d21b1907dfa0ec9ba04177e597350b7d2a1ef31e.zip#egg=Robinhood-1.0.1',

        'https://github.com/westonplatter/Robinhood/archive/6294a5c3d53dd7553c05c272ebeb069df1c86aa2.zip#egg=Robinhood-1.0.1',
    ],
    entry_points='''
        [console_scripts]
        sm=simple_metrics.cli:cli
    ''',
)

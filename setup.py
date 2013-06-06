from distutils.core import setup

setup(
    name='dowser',
    version='0.1',
    packages=['dowser',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    package_dir={'dowser': 'dowser'},
    package_data=dict(dowser=['*.html', 'main.css'])
)

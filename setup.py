from setuptools import setup

readme = open('README.md')

setup(
    name='hashmaster',
    version='1.0.1',
    description='Fast Hash cracking Script.',
    url='https://github.com/ZSendokame/hashMaster',
    long_description_content_type='text/markdown',
    long_description=readme.read(),
    packages=[
        'hashUtil'
    ],
    scripts=[
        './hm.py'
    ]
)
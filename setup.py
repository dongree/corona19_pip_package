from setuptools import setup

setup(name='corona_lib',
      version='0.1',
      description='corona pip package',
      url='https://github.com/dongree/corona19_pip_package.git',
      author='dongree',
      author_email='dongwoo0307@naver.com',
      license='dongree',
      packages=['corona_lib'],
      zip_safe=False,
      install_requires=[
          "beautifulsoup == 4.9.3",
          "bs4 == 0.0.1",
          "requests == 2.25.1"
      ]
      )

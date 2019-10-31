from setuptools import setup, find_packages
 
setup(name='fnapi',
      version='0.2',
      url='https://fnapi.me/',
      license='MIT',
      author='Dima Suzmin',
      author_email='diman.suzmin@yandex.ru',
      description='Simple library for fortnite things',
      packages=find_packages(),
      long_description=open('README.md').read(),
      zip_safe=False)
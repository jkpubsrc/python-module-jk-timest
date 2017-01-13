from setuptools import setup


def readme():
	with open('README.rst') as f:
		return f.read()


setup(name='jk_timest',
	version='0.2017.1.12',
	description='This python module aids in estimating how long some long running process will require until it completes.',
	author='Jürgen Knauth',
	author_email='pubsrc@binary-overflow.de',
	license='Apache 2.0',
	url='https://github.com/jkpubsrc/python-module-jk-timest',
	download_url='https://github.com/jkpubsrc/python-module-jk-timest/tarball/0.2017.1.12',
	keywords=['time', 'estimation', 'eta'],
	packages=['jk_timest'],
	install_requires=[
	],
	include_package_data=True,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Programming Language :: Python :: 3.5',
		'License :: OSI Approved :: Apache Software License', 
	],
	long_description=readme(),
	zip_safe=False)


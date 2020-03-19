from setuptools import setup, find_packages



setup(
    name='Flask-Youtube',
    version='0.1',
    license='MIT',
    description='Flask extension to allow easy embedding of YouTube videos',
    author='Dash Altamirano',
    platforms='any',
    install_requires=['Flask'],
    packages=find_packages(),
    include_packege_data=True,
    package_data = { 'templates': ['*'] },
    zip_sage=False,
    classifiers=[
	'Development Status :: 5 - Production/Stable',
	'Enviroment :: Web Enviroment'
	'Intended Audience :: Developers',
	'Operating System :: OS Independient',
	'Programming Language :: Python',
	'Topic :: Software Development :: Libraries :: Python Modules'
	

      ]
  )	

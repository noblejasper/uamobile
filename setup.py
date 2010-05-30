from setuptools import setup, find_packages
import sys, os

version = '0.3.0'

setup(name='uamobile',
      version=version,
      description="WSGIUserAgentMobile - mobile user agent string parser for WSGI applications",
      long_description="""\
WSGIUserAgentMobile is HTTP mobile user agent string parser. It'll be useful in parsing HTTP_USER_AGENT strings of (mainly Japanese) mobile devices.

This library is ported from similar libraries in Perl and PHP and owes a lot to them.

HTTP-MobileAgent? http://search.cpan.org/~kurihara/HTTP-MobileAgent-0.26/lib/HTTP/MobileAgent.pm

PEAR::Net_UserAgent_Mobile? http://pear.php.net/package/Net_UserAgent_Mobile
""",
      classifiers=filter(None, map(str.strip, """\
Development Status :: 4 - Beta
License :: OSI Approved :: MIT License
Programming Language :: Python
Operating System :: OS Independent
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware
""".splitlines())),
      keywords='',
      author='Chihiro Sakatoku',
      author_email='csakatoku@gmail.com',
      url='http://github.com/csakatoku/uamobile',
      license='MIT License',
      platforms=["any"],
      packages=find_packages(exclude=['examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'IPy',
        'importlib',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      uamobile-scrape = uamobile.scrapers.command:main
      """,
      test_suite='nose.collector'
      )

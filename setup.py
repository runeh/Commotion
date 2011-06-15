try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

desc = "Let's write a blawg"
version = "0.1"

setup(name='commotion',
      version=version,
      description=desc,
      #long_description=open("README").read(),
      classifiers=[
	      ],
      keywords='blog',
	  install_requires=[
        'bottle',
      ],
      #author=author,
      #author_email=email,
      url='https://github.com/TheAtilla/Commotion',
      #license='BSD',
      #packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      platforms=["any"],
      #test_suite = 'nose.collector',
      #**extra
)
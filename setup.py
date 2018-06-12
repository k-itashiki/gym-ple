from setuptools import setup, find_packages
import sys, os.path

# Don't import gym module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gym_ple'))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='gym_ple',
      version=0.3,
      description='This package allows to use PLE as a gym environment.',
      url='https://github.com/lusob/gym-ple',
      author='lusob',
      author_email='luis@sobrecueva.com',
      packages=[package for package in find_packages()
                if package.startswith('gym')],
      keywords = ['AI', 'Reinforcement Learning', 'Games'],
      zip_safe=False,
      classifiers = [
              'Programming Language :: Python',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: MIT License',
              'Operating System :: OS Independent',
              'Topic :: Scientific/Engineering :: Artificial Intelligence',
              ],
      long_description = read('README.rst')
)

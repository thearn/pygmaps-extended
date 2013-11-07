from setuptools import setup, Extension
import numpy as np

SRC_DIR = "pygmaps"
PACKAGES = [SRC_DIR]

setup(name='pygmaps-enhanced',
      version='0.2.0',
      install_requires=['numpy', 'matplotlib'],
      description="Python wrapper for Google MAPs javascript API 3.0",
      author='Tristan Hearn',
      author_email='tristanhearn@gmail.com',
      url='https://github.com/thearn/pygmaps',
      license='Apache 2.0',
      packages=['pygmaps'],
      )

from setuptools import setup, find_packages


setup(name='greentea',
      version="0.0.1",
      description=(
          'A microframework for abstraction.'),
      python_requires='>=3.8.0',
      url='https://github.com/nryotaro/greentea',
      author='Nakamura, Ryotaro',
      author_email='nakamura.ryotaro.kzs@gmail.com',
      license='MIT License',
      classifiers=['Programming Language :: Python :: 3.8'],
      packages=find_packages(),
      install_requires=[
      ],
      extras_require={
          'test': [
              'pytest'
          ],
          'dev': [
              'ipython',
              'python-language-server[all]'
              ]})

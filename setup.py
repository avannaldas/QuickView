from setuptools import setup

setup(name='QuickView',
      version='0.1',
      description='QuickView gives you a quick glance at the dataset, just pass the pandas dataframe. It gives some useful summary and plots with just one line of code. All the summary that it outputs is made available through member variables. Its built using matplotlib.',
      url='http://github.com/avannaldas/QuickView',
      author='Abhijit Annaldas',
      author_email='avannaldas@hotmail.com',
      license='MIT',
      packages=['QuickView'],
      install_requires=[
          'pandas',
          'matplotlib'
      ],
      zip_safe=False)

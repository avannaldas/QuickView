from setuptools import setup

setup(name='QuickView',
      version='0.2',
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
      classifiers=[
          'Development Status :: 3 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities'
      ],
      zip_safe=False)

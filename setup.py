from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='bibtex_duplicate_remover',
      version='0.1',
      description='Removes duplicates in bibliography created by bibtex and biblatex',
      long_description='Removes duplicates in bibliography created by bibtex and biblatex and updates each cite key in tex files',
      url='http://github.com/rsokolewicz/bibtex_duplicate_remover',
      classifiers = [ 'Programming Language :: Python :: 3.8' ],
      author='rsokolewicz',
      author_email='rsokolewicz@gmail.com',
      packages=['bibtex_duplicate_remover'],
      install_requires = ['re', 'collections', 'numpy'],
      zip_safe=False)

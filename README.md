# briann

Credit: http://iamtrask.github.io/2015/07/12/basic-python-network/

https://en.wikipedia.org/wiki/Artificial_neural_network

http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html

https://wiki.python.org/moin/TestPyPI


## User guide

http://pythonhosted.org/briann


```
git clone https://github.com/leehart/briann.git
cd briann
pip install . --upgrade --user
Brian
```


## Developer guide

```
git clone git@github.com:leehart/briann.git
cd briann
pip install --editable . --upgrade --user
nano ~/.pypirc
python setup.py register -r https://testpypi.python.org/pypi
python setup.py sdist
twine upload dist/brian-0.0.2.tar.gz -r testpypi
pip install -i https://testpypi.python.org/pypi briann --upgrade --user
```

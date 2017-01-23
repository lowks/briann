# briann


https://en.wikipedia.org/wiki/Artificial_neural_network

http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html

https://wiki.python.org/moin/TestPyPI


## User guide

http://pythonhosted.org/briann


```
git clone https://github.com/leehart/briann.git
cd briann
pip install . --upgrade --user
```


## Developer guide

edit ~/.pypirc

```
git clone git@github.com:leehart/briann.git
cd briann
python setup.py register -r https://testpypi.python.org/pypi
twine upload dist/* -r testpypi
pip install -i https://testpypi.python.org/pypi briann --upgrade --user
```

#!/usr/bin/env python

from distutils.core import setup

setup(name='context2vector',
      version='1.0',
      description='Bidirectional-LSTM sentential context embeddings',
      author='Dezhou Shen',
      url='https://www.github.com/ShenDezhou/context2vec/',
      packages=['context2vec','context2vec.common','context2vec.eval','context2vec.eval.wsd','context2vec.train'],
      license='MIT'
     )
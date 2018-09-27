# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:34:49 2018

@author: afcarl
"""

from gensim import utils
from simserver import SessionServer

import gensim

#server = SessionServer('/tmp/my_server') # resume server (or create a new one)
server = SessionServer('./my_server') # resume server (or create a new one)

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

logger = logging.getLogger('gensim.similarities.simserver')

document = {'id': 'some_unique_string',
            'tokens': ['content', 'of', 'the', 'document', '...'],
            'other_fields_are_allowed_but_ignored': None}

from gensim import utils
texts = ["Human machine interface for lab abc computer applications",
         "A survey of user opinion of computer system response time",
         "The EPS user interface management system",
         "System and human system engineering testing of EPS",
         "Relation of user perceived response time to error measurement",
         "The generation of random binary unordered trees",
         "The intersection graph of paths in trees",
         "Graph minors IV Widths of trees and well quasi ordering",
         "Graph minors A survey"]

corpus = [{'id': 'doc_%i' % num, 'tokens': utils.simple_preprocess(text)} for num, text in enumerate(texts)]

utils.upload_chunked(server, corpus, chunksize=1000) # send 1k docs at a time

service = SessionServer('C:/0_afc_working/0_Doc2Vec/gensim-simserver-master/my_server/') # or wherever

logger.info("simberver_local_A: service.train(corpus, method='lsi')" )

service.train(corpus, method='lsi')

service.index(corpus) # index the same documents that we trained on...

service.delete(['doc_5', 'doc_8']) # supply a list of document ids to be removed from the index

service.index(corpus[:3]) # overall index size unchanged (just 3 docs overwritten)

print(service.find_similar('doc_0'))
#[('doc_0', 1.0000001192092896, None), ('doc_2', 0.11294259130954742, None), ('doc_1', 0.09881371259689331, None), ('doc_3', 0.08786647021770477, None)]

#print(service.find_similar('doc_5')) # we deleted doc_5 and doc_8, remember?
#ValueError: document 'doc_5' not in index

doc = {'tokens': gensim.utils.simple_preprocess('Graph and minors and humans and trees.')}
print(service.find_similar(doc, min_score=0.4, max_results=50))
#[('doc_7', 0.7615688443183899, None), ('doc_3', 0.5443614721298218, None)]


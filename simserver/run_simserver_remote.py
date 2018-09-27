#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 Radim Rehurek <radimrehurek@seznam.cz>
# Licensed under the GNU AGPL v3 - http://www.gnu.org/licenses/agpl.html

"""
USAGE: %(program)s DATA_DIRECTORY

    Start a sample similarity server, register it with Pyro and leave it running \
as a daemon.

Example:
    python -m simserver.run_simserver /tmp/server
"""

from __future__ import with_statement

import logging
import os
import sys

import gensim
import simserver
from gensim import utils

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(module)s:%(lineno)d : %(funcName)s(%(threadName)s) : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logging.info("running %s" % ' '.join(sys.argv))


    document = {'id': 'some_unique_string',
            'tokens': ['content', 'of', 'the', 'document', '...'],
            'other_fields_are_allowed_but_ignored': None}

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

    program = "run_simserver_remote"
    
    basename = "simserver"

    print()
    print("program = ", program)
    print("basename = ", basename)
    print("sys.argv = ", sys.argv)
    print()
    server = simserver.SessionServer(basename)
    
    server.train(corpus, method='lsi')

    server.index(corpus) # index the same documents that we trained on...

    utils.upload_chunked(server, corpus, chunksize=1000) # send 1k docs at a time

    server.delete(['doc_5', 'doc_8']) # supply a list of document ids to be removed from the index

    server.index(corpus[:3]) # overall index size unchanged (just 3 docs overwritten)

    print(server.find_similar('doc_0'))
    #[('doc_0', 1.0000001192092896, None), ('doc_2', 0.11294261366128922, None), ('doc_1', 0.09881372004747391, None), ('doc_3', 0.08786644041538239, None)]
    
    gensim.utils.pyro_daemon('gensim.testserver', server)

    logging.info("finished running %s" % program)

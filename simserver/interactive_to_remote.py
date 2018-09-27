# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:25:42 2018

@author: afcarl
"""

import Pyro4

service = Pyro4.Proxy(Pyro4.locateNS().lookup('gensim.testserver'))

print(service.status())

print(service.find_similar('doc_0'))
#[('doc_0', 1.0000001192092896, None), ('doc_2', 0.11294261366128922, None), ('doc_1', 0.09881372004747391, None), ('doc_3', 0.08786644041538239, None)]

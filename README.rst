=========================================================
(FIXED) simserver -- document similarity server in Python
=========================================================


Index plain text documents and query the index for semantically related documents.

Simserver uses transactions internally to provide a robust and scalable similarity server.


Installation
------------

Simserver builds on the gensim framework for topic modelling.

0a. Install updated "sqlitedict" version 1.5.0 from zipfile included herein ("python setup.py install").

0b. Install updated "cpython/threading.py" version 3.6.5 from zipfile included herein ("copy threading.py <python>/Lib/threading.py").

0c. Install updated "simserver" version 0.1.4 included herein ("python setup.py install").


REVISED INSTRUCTIONS FOR OPERATION:

This version has been tested under Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32

1. Run Locally:

    "python simserver_run_local.py"


2. Run Remotely:

2a. Run Pyro4 NameServer: "python -m Pyro4.naming": Output on Windows 7 Pro Anaconda Prompt:

"Not starting broadcast server for localhost.
NS running on localhost:9090 (127.0.0.1)
Warning: HMAC key not set. Anyone can connect to this server!
URI = PYRO:Pyro.NameServer@localhost:9090"


2b. Run Pyro4 NameServer Utility: "python -m Pyro4.nsc list": Output on Windows 7 Pro Anaconda Prompt:

'''--------START LIST

Pyro.NameServer --> PYRO:Pyro.NameServer@localhost:9090
    metadata: ['class:Pyro4.naming.NameServer']
    
--------END LIST'''


2c. Run simserver remote process: "python run_server_remote.py": Output on Windows 7 Spyder IDE IPython console:

'''runfile('xxx/gensim-simserver-WORKS/simserver/run_simserver_remote.py', wdir='xxx/gensim-simserver-WORKS/simserver')
2018-09-13 17:09:47,430 : INFO : running xxx/gensim-simserver-WORKS/simserver/run_simserver_remote.py
2018-09-13 17:09:47,432 : INFO : stable index pointer not found or invalid; starting from simserver\a
2018-09-13 17:09:47,433 : INFO : loading SaveLoad object from simserver\a\index_fresh
2018-09-13 17:09:47,433 : INFO : loading SaveLoad object from simserver\a\index_opt
2018-09-13 17:09:47,434 : INFO : loading SimModel object from simserver\a\model
2018-09-13 17:09:47,434 : INFO : opening Sqlite table 'unnamed' in simserver\a\payload
...
program =  run_simserver_remote
basename =  simserver
sys.argv =  ['xxx/gensim-simserver-WORKS/simserver/run_simserver_remote.py']
2018-09-13 17:09:47,605 : INFO : saved simserver\a\index_fresh.idx
2018-09-13 17:09:47,607 : INFO : updating 9 id mappings
...
2018-09-13 17:09:47,749 : INFO : deleting xxx\AppData\Local\Temp\sqldict799e26
2018-09-13 17:09:47,750 : INFO : deleting xxx\AppData\Local\Temp\sqldict799e26
[('doc_0', 1.0000001192092896, None), ('doc_2', 0.11294261366128922, None), ('doc_1', 0.09881372004747391, None), ('doc_3', 0.08786644041538239, None)]
2018-09-13 17:09:56,771 : INFO : gensim.testserver registered with nameserver (URI 'PYRO:gensim.testserver@127.0.0.1:56721')'''


2d. Run local process to access remote server: "python interactive_to_remote.py": Output on Windows 7 Pro Anaconda Prompt:

'''>>> import Pyro4
>>> service = Pyro4.Proxy(Pyro4.locateNS().lookup('gensim.testserver'))
>>> print(service.status())
SessionServer(
        stable=SimServer(loc='simserver\\a', fresh=SimIndex(7 docs, 12 real size
), opt=None, model=SimModel(method=lsi, dict=Dictionary(41 unique tokens: ['abc'
, 'applications', 'computer', 'for', 'human']...)), buffer=SqliteDict(xxx\AppData\Local\Temp\sqldict52159))
        session=None
)
>>> print(service.find_similar('doc_0'))
[('doc_0', 1.0000001192092896, None), ('doc_2', 0.11294261366128922, None), ('do
c_1', 0.09881372004747391, None), ('doc_3', 0.08786644041538239, None)]
>>>'''


#================================================================================
#================================================================================

ORIGINAL REPO INFORMATION BELOW (https://github.com/RaRe-Technologies/gensim-simserver):

#================================================================================
#================================================================================


[NO LONGER MAINTAINED AS OPEN SOURCE - USE SCALETEXT.COM INSTEAD]

Licensing
----------------

Simserver is released under the `GNU Affero GPL license v3 <http://www.gnu.org/licenses/agpl.html>`_.

This means you may use simserver freely in your application (even commercial application!),
but you **must then open-source your application as well**, under an AGPL-compatible license.

The AGPL license makes sure that this applies even when you make your application
available only remotely (such as through the web).

TL;DR: **simserver is open-source, but you have to contact me for any proprietary use.**

History
-------------

0.1.4:
  * performance improvements to sharding
  * change to threading model -- removed restriction on per-thread session access
  * bug fix in index optimize()

0.1.3: 
  * changed behaviour for very few training documents: instead of latent semantic analysis, use simpler log-entropy model
  * fixed bug with leaking SQLite file descriptors

-------------

Copyright (c) 2009-2012 Radim Rehurek

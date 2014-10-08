===========
Demo Agenda
===========

Using the generator:
====================

::

    docker run -it -v $(pwd):/target araport/adapter-generator create


Checking Adama status:
======================

::

    curl -k https://adama-dev.tacc.utexas.edu/community/v0.3/status


Registering a namespace:
========================

::

    curl -k https://adama-dev.tacc.utexas.edu/community/v0.3/namespaces \
         -X POST \
         -F name=demo \
         -H "Authorization: Bearer d160f94594a040ff810b7215a35fe792"


Expressologs by Locus
=====================

Test function:
--------------

::

    >>> main.search({'locus': 'AT1G10200'})

Register a service:
-------------------

::

    curl -k https://adama-dev.tacc.utexas.edu/community/v0.3/demo/services \
         -X POST \
         -F git_repository=https://github.com/waltermoreira/aip-demo.git \
         -F metadata=expressologsByLocus \
         -H "Authorization: Bearer d160f94594a040ff810b7215a35fe792"

Query:
------

::

    curl -k https://adama-dev.tacc.utexas.edu/community/v0.3/demo/expressologs_by_locus_v0.1/search\?locus\=AT1G10200

Delete:
-------

::

    curl -k https://adama-dev.tacc.utexas.edu/community/v0.3/demo/expressologs_by_locus_v0.1 \
         -X DELETE \
         -H "Authorization: Bearer d160f94594a040ff810b7215a35fe792"


Thalemine as Jbrowse
====================

Test function:
--------------

::

    >>> main.map_filter({
          "location": {
              "ref": "Chr1",
              "start": 658657,
              "objectName": "AT1G02920",
              "tracks": ["SequenceFeature","Gene"],
              "end": 659771
          },
          "name": "glutathione S-transferase 7"
       })

Register a service:
-------------------

::

    curl -k https://adama-dev.tacc.utexas.edu/community/v0.3/demo/services \
         -X POST \
         -F git_repository=https://github.com/waltermoreira/aip-demo.git \
         -F metadata=queryThalemineAsJbrowseIndex \
         -H "Authorization: Bearer d160f94594a040ff810b7215a35fe792"

Query:
------

::

    curl -k https://adama-dev.tacc.utexas.edu/community/v0.3/demo/query_thalemine_as_jbrowse_index_v0.1/search\?startswith\=FWA

Delete the service:
-------------------

::

    curl -k https://adama-dev.tacc.utexas.edu/community/v0.3/demo/query_thalemine_as_jbrowse_index_v0.1 \
         -X DELETE \
         -H "Authorization: Bearer d160f94594a040ff810b7215a35fe792"


A /list example
===============

::

    curl -k https://adama-dev.tacc.utexas.edu/community/v0.3/vaughn-dev/resolver_synonym_kinds_v0.1/list

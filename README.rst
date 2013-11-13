About
-------
This product defines templates for 
bda.plone.shop.interfaces.IBuyable
to be used with pp.plone-client.

How to
-------
- install Produce & Publish Server ( http://www.andreas-jung.com/contents/pdf-generation-with-plone-and-phantomjs )
- add the following to your buildout.cfg

environment-vars =
    
    PP_CONVERTER phantomjs
    
    PP_RESOURCE bda-default
    
- generate your pdf by going to http://yoursite/product/asPDF    


Problems?
---------
- on OS X I had to manually download phantomjs
- On Ubuntu I had a problem with gevent due to a bug in Ubuntu (reinstalling some libs did the trick... I think it was libevent)
Licence
-------
Published under the GNU Public Licence Version 2 (GPL 2)

Author
------
| Espen Moe-Nilssen
#!/usr/bin/env python
import urllib2
import os.path
import time
import xml.etree.ElementTree as ET

tmpfile = "/tmp/mta_service_status"
now = time.time()
filetime = datetime.fromtimestamp(path.getctime(tmpfile))

html = urllib2.urlopen('http://www.mta.info/status/serviceStatus.txt')

tree = ET.parse(html)
root = tree.getroot()
linebreak = "<br/>"
## root
#. <Element 'service' at 0xffe7d1ec>

for subway in root.findall('subway'):
   #print subway
   for line in subway.findall('line'):
       for name in line.findall('name'):
           print ("%s%s"%(name.text,linebreak))
       for text in line.findall('text'):
           try:
               print ("%s%s"%(text.text,linebreak))
           except UnicodeEncodeError, e:
               print 'Babelfish error!'


# ET.dump(root)
#. <Element 'subway' at 0xffe7d3cc>
#. 123
#. 
#.                     <span class="TitleDelay">Delays</span>
#.                     <span class="DateStyle">
#.                     &nbsp;Posted:&nbsp;09/20/2013&nbsp; 3:48PM
#.                     </span><br/><br/>
#.                   Following an earlier incident at <STRONG>14 St- Union Sq</STRONG>, [6] train service has resumed with residual delays.
#.                 <br/><br/>
#.               
#. 456
#. 
#.                     <span class="TitleDelay">Delays</span>
#.                     <span class="DateStyle">
#.                     &nbsp;Posted:&nbsp;09/20/2013&nbsp; 3:48PM
#.                     </span><br/><br/>
#.                   Following an earlier incident at <STRONG>14 St- Union Sq</STRONG>, [6] train service has resumed with residual delays.
#.                 <br/><br/>
#.               
#. 7
#. None
#. ACE
#. The Doctor has this information
#. BDFM
#. The Doctor has this information
#. G
#. None
#. JZ
#. None
#. L
#. None
#. NQR
#. The Doctor has this information
#. S
#. None
#. SIR
#. None
#. 

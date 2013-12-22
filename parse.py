#!/usr/bin/env python
import xml.etree.ElementTree as ET
tree = ET.parse('serviceStatus.txt')
root = tree.getroot()
## root
#. <Element 'service' at 0xffe7d1ec>

for subway in root.findall('subway'):
   print subway
   for line in subway.findall('line'):
       for name in line.findall('name'):
           print name.text
       for text in line.findall('text'):
           try:
               print text.text
           except UnicodeEncodeError, e:
               print 'fuck off python'


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
#. fuck off python
#. BDFM
#. fuck off python
#. G
#. None
#. JZ
#. None
#. L
#. None
#. NQR
#. fuck off python
#. S
#. None
#. SIR
#. None
#. 

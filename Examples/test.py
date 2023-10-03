from xml.dom import minidom

doc = minidom.parse('template.kml')

primaryCovElement = doc.getElementsByTagName('Primary Coverage')
placemarkElement = doc.createElement('Test')
extElement = doc.createElement('ExtendedData')
placemarkElement.appendChild(extElement)

kmlfile = open('test.kml', 'w')
kmlfile.write(doc.toxml())






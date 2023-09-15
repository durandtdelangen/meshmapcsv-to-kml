from xml.dom import minidom

doc = minidom.parse('template.kml')

name = doc.getElementsByTagName('name')[1]
print (name.childNodes)
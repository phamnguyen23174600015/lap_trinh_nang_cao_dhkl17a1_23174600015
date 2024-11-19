import xml.dom.minidom

doc = xml.dom.minidom.parse("bt3.xml")
all = doc.getElementsByTagName("*")

for pt in all:
    print(f"Phần tử: {pt.tagName}")
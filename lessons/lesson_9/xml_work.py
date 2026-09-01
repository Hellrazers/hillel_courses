# import xml.etree.ElementTree as ET
#
# tree = ET.parse('some_xml.xml')
# root = tree.getroot()
#
# for child in root:
#     print(child.tag, child.attrib)
#     for subchild in child:
#         print(subchild.tag, subchild.text)
#         if subchild.tag == 'timingExbytes':
#             for subsubchild in subchild:
#                 print(subsubchild.tag, subsubchild.text)
import xmltodict

with open('some_xml.xml') as f:
    file_content = f.read()

    print(file_content)

xml_to_dict = xmltodict.parse(file_content)
print(xml_to_dict)
print(xml_to_dict.get('groups').get('group').get('timingExbytes').get('bbo'))
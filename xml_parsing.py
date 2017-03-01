import sys
import xml.etree.ElementTree as ET

from pprint import pprint

# use triple " for multiline string
SAMPLE_XML = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""

def parseXML(xml_string : str) -> None :
   pprint(xml_string)

   xml_tree_root = ET.fromstring(xml_string)
   print('Root=', xml_tree_root.tag)

   for country in xml_tree_root.iter('country') :
       print('Country: ', country.attrib['name'])
       
       print('\tRank=', country.findtext('rank'))
       print('\tGDP Per Person=', country.find('gdppc').text)

       neighbors_iter = country.findall('neighbor')
       neighbor_list = []
       for neighbor in neighbors_iter :
           neighbor_list.append(neighbor.attrib['name'] + '->' + neighbor.attrib['direction'])
       print('\t', str(neighbor_list))

def main(cmd_args : list) -> None :
    if cmd_args :
        xml_file_path = cmd_args[0]

        print('Reading xml file : ', xml_file_path)

        with open(xml_file_path) as xml_file:
            xml_string = xml_file.read()
    else :
        xml_string = SAMPLE_XML
        print('Using inline xml...')

    parseXML(xml_string)

if __name__ == "__main__" :
    print('Usage : ')
    print('\t py -3 xml_parsing.py optional_xml_file_path')
    print('\t e.g. py -3 xml_parsing.py ./Data/country_with_GDP.xml')
    cmd_args = []
    if len(sys.argv) > 1 :
        cmd_args = sys.argv[1:]
    main(cmd_args)

#!/usr/bin/python

import util
import xml.etree.ElementTree as ET
import os
from xml.etree import ElementTree

### Removing excepted element from the list.
def filter_except(listdir):
    except_value = util.config.get("xml_parser", "except")
    except_list = except_value.split( )
    util.logger.debug(except_list)
    for e in except_list:
        if e in listdir:
            try:
                listdir.remove(e)
            except:
                pass
    util.logger.debug(listdir)
    return listdir

### Getting xml files. 
def get_xml_files(d):
    xmls = []
    filtered_list = filter_except(os.listdir(d))
    for file in filtered_list:
        if file.endswith(".xml"):
            xmls.append(os.path.join(d, file))
            util.logger.debug(os.path.join(d, file))
    return xmls

### Parse xmls and get min value
def get_min_element_from_xmls(xmls_list, name):
    numbers = []
    for path in xmls_list:
        util.logger.debug('path to xml %s', path)
        tree = ET.parse(path)
        root = tree.getroot()
        for human in root.findall(name):
            m = int(human.find('min').text)
            numbers.append(m)
    a = min(numbers, key=int)
    util.logger.debug('minimum from all xmls is %i', a)
    util.logger.debug('xml file %s name %s min value %s',path, human, m)
    return a

### Push result into the specified xml.
def push_result_into_xml(result_xml, minimum, name):
    util.logger.debug('push_result_into_xml function call')
    for path in result_xml:
        et = ET.parse(path)
        for human in et.findall(name):
            util.logger.debug('name %s ', human)
            util.logger.debug('min %s ', human.find('min').text)
            human.find('min').text = str(minimum)
            et.write(path)

### Main function.
def main():
    input_dir = util.config.get("xml_parser", "input_dir")
    #filter_except(os.listdir(input_dir))
    #return 0
    xmls_list = get_xml_files(input_dir)
    out_dir = util.config.get("xml_parser", "output_dir")
    result_xml = get_xml_files(out_dir)
    name = util.config.get("xml_parser", "name")
    minimum = get_min_element_from_xmls(xmls_list, name)
    push_result_into_xml(result_xml, minimum, name)

if __name__ == "__main__":
    main()

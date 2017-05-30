#!/usr/bin/python

import util
import xml.etree.ElementTree as ET
import os
from xml.etree import ElementTree

### Getting xml files. 
def get_xml_files(d):
    xmls = []
    for file in os.listdir(d):
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
def push_result_into_xml(m, name):
    util.logger.debug('push_result_into_xml function call')
    et = ET.parse('./output_xml_dir/result.xml')
    for human in et.findall(name):
        util.logger.debug('name %s ', human)
        util.logger.debug('min %s ', human.find('min').text)
        human.find('min').text = str(m)
    et.write('./output_xml_dir/result.xml')

### Main function.
def main():
    xmls_list = get_xml_files("./input_xml_dir")
    m = get_min_element_from_xmls(xmls_list, 'Lusine')
    push_result_into_xml(m, 'Lusine')

main()

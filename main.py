"""main.py

This module converts an autoinst.xml autoyast profile to a generic one that can be utilized by any openQA job run of
a test suite.
Usage: python3 main.py autoinst.xml
"""

import sys
from lxml import etree

if len(sys.argv) != 2:
    print("Please provide an autoyast profile as argument. \nUsage: python3 main.py autoinst.xml")
    exit(1)

tree = etree.parse(sys.argv[1])
root = tree.getroot()

# Define tags to replace list
tags_to_delete = ["add-on", "append"]

# Define tags_to_replace dictionary
# Key: element tag, value: replacement text
tags_to_replace = {"reg_code":   "{{SCC_REGCODE}}",
                   "reg_server": "{{SCC_URL}}",
                   "arch":       "{{ARCH}}",
                   "version":    "{{VERSION}}",
                   "ipaddr":     "{{HostIP}}"}

# Create a joined list that contains tags to delete and tags to replace
tags = tags_to_delete + list(tags_to_replace.keys())

# Append the XML namespace to all the tags
XMLNS = "{http://www.suse.com/1.0/yast2ns}"
tags_ns = [XMLNS + tag for tag in tags]

# Append the XML namespace to the tags that are keys of the tags_to_replace dictionary
tags_to_replace = {XMLNS+key: value for key, value in tags_to_replace.items()}

for element in root.iter(tags_ns):
    print("%s - %s" % (element.tag, element.text))
    if element.tag in tags_to_replace:
        element.text = tags_to_replace[element.tag]
    elif element.text is not None:
        element.getparent().remove(element)

tree.write('generated_autoinst.xml', encoding="utf-8", xml_declaration=True)

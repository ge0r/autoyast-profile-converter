"""main.py

This module converts an autoinst.xml autoyast profile to a generic one that can be utilized by any openQA job run of
a test suite.
Usage: python3 main.py name_of_autoinst.xml
"""

import sys
from lxml import etree

if len(sys.argv) != 2:
    print("Please provide an autoyast profile as argument. \nUsage: python3 main.py name_of_autoinst.xml")
    exit(1)

filename = sys.argv[1]
output_filename = "generated_" + filename

tree = etree.parse(filename)
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

# For "reg_code" sections, the replacement text depends on the name of the addon
addon_reg_code = {"sle-ha":     "{{SCC_REGCODE_HA}}",
                  "sle-ha-geo": "{{SCC_REGCODE_GEO}}",
                  "sle-we":     "{{SCC_REGCODE_WE}}",
                  "sle-rt":     "{{SCC_REGCODE_RT}}",
                  "sle-ltss":   "{{SCC_REGCODE_LTSS}}",
                  "sle-hpc":    "{{SCC_REGCODE_HPC}}"}

# Create a joined list that contains tags to delete and tags to replace
tags = tags_to_delete + list(tags_to_replace.keys())

# Append the XML namespace to all the tags
XMLNS = "{http://www.suse.com/1.0/yast2ns}"
tags_ns = [XMLNS + tag for tag in tags]
tags_to_replace = {XMLNS + key: value for key, value in tags_to_replace.items()}

for element in root.iter(tags_ns):
    if element.tag in tags_to_replace:
        if element.text:
            element.text = tags_to_replace[element.tag]

        # if the element you found is inside an "addon" section, it's tag is reg_code and it has registration code text
        if element.getparent().tag == XMLNS + "addon" and element.tag == XMLNS + "reg_code" and element.text:
            # Replace the registration code with the variable that corresponds to that product
            for child in element.getparent().iter(XMLNS + "name"):
                element.text = addon_reg_code[child.text]
    else:
        element.getparent().remove(element)

tree.write(output_filename, encoding="utf-8", xml_declaration=True)

# Append end of line at the end of file
with open(output_filename, 'a') as fd:
    fd.write('\n')

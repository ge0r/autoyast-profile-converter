"""main.py

This module converts an autoinst.xml autoyast profile to a generic one that can be utilized by any openQA job run of a
specific test suite.
Usage: python3 main.py autoinst.xml
"""

import sys
from lxml import etree

if len(sys.argv) != 2:
    print("Please provide an autoyast profile as argument. \nUsage: python3 main.py autoinst.xml")
    exit(1)

tree = etree.parse(sys.argv[1])
tree.write('generated_autoinst.xml', encoding="utf-8", xml_declaration=True)


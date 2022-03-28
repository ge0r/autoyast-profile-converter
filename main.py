"""main.py

This module converts an autoinst.xml autoyast profile to a generic one that can be utilized by any openQA job run of a
specific test suite.
Usage: python3 main.py autoinst.xml
"""

import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 2:
    print("Please provide an autoyast profile as argument. \nUsage: python3 main.py autoinst.xml")
    exit(1)

ET.register_namespace('y2', 'http://www.suse.com/1.0/yast2ns')
ET.register_namespace('config', 'http://www.suse.com/1.0/configns')
ET.register_namespace('', 'http://www.suse.com/1.0/yast2ns')
tree = ET.parse(sys.argv[1])
tree.write('generated_autoinst.xml')

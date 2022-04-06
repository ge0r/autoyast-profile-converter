# autoyast-profile-converter
A tool that converts an autoyast profile to a generic one that can be used by openQA jobs.

Usage : `python3 main.py name_of_your_autoinst.xml`

The output file will be prefixed with `generated_` and will have the following changes:

1. Sections with `<add-on>` and `<append>` tags will be removed.

2. Text in sections with specific tags will be replaced, as shown on the table below:
    
    | Tag | Replacement text|
    | --- | ----------- |
    | `<reg_code>` | `{{SCC_REGCODE}}` |
    | `<reg_server>` | `{{SCC_URL}}` |
    | `<arch>` | `{{ARCH}}` |
    | `<version>` | `{{VERSION}}` |
    | `<ipaddr>` | `{{HostIP}}` |

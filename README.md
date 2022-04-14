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

3. Registration code replacement inside `<addon>` (different from `<add-on>`) sections will depend on the name of the addon:
    | Addon name | Replacement text|
    | --- | ----------- |
    | `<sle-ha>` | `{{SCC_REGCODE_HA}}` |
    | `<sle-ha-geo>` | `{{SCC_REGCODE_GEO}}` |
    | `<sle-we>` | `{{SCC_REGCODE_WE}}` |
    | `<sle-rt>` | `{{SCC_REGCODE_RT}}` |
    | `<sle-ltss>` | `{{SCC_REGCODE_LTSS}}` |
    | `<sle-hpc>` | `{{SCC_REGCODE_HPC}}` |

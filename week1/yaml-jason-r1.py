#!/usr/bin/env python

import yaml
import json

def main():

    yamlfile = 'myyaml.yml'
    jsonfile = 'myjson.json'

    dict = {
        'ip_addy': '10.10.10.10',
        'subnet': '255.255.255.0',
        'gateway': '10.0.0.1',
        'type': 'ethernet'
    }

    list = [ 
        'blah1', 
        'blah2',
        dict 
    ]

    with open(yamlfile, "w") as f:
        f.write(yaml.dump(list, default_flow_style=False))

    with open(jsonfile, "w") as f:
        json.dump(list, f)

if __name__ == "__main__":
    main()

# ansible_parsers
Ansible filtering and parsing plays and scripts

This repository contains the following.

### Ansible playbooks
** lookup.yml **
this playbook will take input from a .csv file and convert into a json dictionary.
The input data currently contains IP address and hostname so we add that to inventory
in memory. 

** query_api **
This playbook will request data from an API producing json.
The json is created using the lookup.yml playbook.
The api application lives under the microservice directory.

To run the microservice application,
```
cd microservice
python run.py
curl http://localhost:5000/inventory
curl http://localhost:5000/inventory/keys
curl http://localhost:5000/inventory/<serial_number>/ip
```

the json format / data structure will be stored from .csv into this format below

```
    SGHY833WB": {
        "bay": "11\r", 
        "default_password": "defaultpw43", 
        "dns_primary": "147.204.72.67", 
        "dns_secondary": "147.204.72.68", 
        "fqdn": "info.au", 
        "gateway": "10.110.16.1", 
        "gen": "9", 
        "hostname": "bsa14686r", 
        "ip": "10.110.21.203", 
        "netmask": "255.255.240.0", 
        "sn": "SGHY833WB", 
        "system_location": "SY4", 
        "type": "Blade"
    }, 
    "SGH833SMQN": {
        "bay": "10\r", 
        "default_password": "defaultpw42", 
        "dns_primary": "147.204.72.67", 
        "dns_secondary": "147.204.72.68", 
        "fqdn": "info.au", 
        "gateway": "10.110.16.1", 
        "gen": "9", 
        "hostname": "bsa14685r", 
        "ip": "10.110.21.202", 
        "netmask": "255.255.240.0", 
        "sn": "SGH833SMQN", 
        "system_location": "SY4", 
        "type": "Blade"
    } 
```

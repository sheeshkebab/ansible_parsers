# ansible_parsers
Ansible filtering and parsing plays and scripts

This repository contains the following.

### Ansible playbooks
* * lookup.yml
this playbook will take input from a .csv file and convert into a json dictionary.
The input data currently contains IP address and hostname so we add that to inventory
in memory. 

* * query_api
This playbook will request data from an API producing json.
The json is created using the lookup.yml playbook.
The api application lives under the microservice directory.

To run the microservice application,
```

cd microservice
python run.py
curl http://localhost:5000/inventory
```

* * note : the microservice API needs the python flask libraries to run.


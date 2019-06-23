[![Build
Status](https://travis-ci.com/nkakouros-original/ansible-role-logstash.svg?branch=master)](https://travis-ci.com/nkakouros-original/ansible-role-logstash)
[![Galaxy](https://img.shields.io/badge/galaxy-nkakouros.logstash-blue.svg)](https://galaxy.ansible.com/nkakouros/logstash/)

ansible-role-logstash
=========

Installs and configures Logstash.

Description
-----------

This role will in a configurable manner:

- install Logstash
- configure Logstash
- configure Logstash pipelines
- support security features

Requirements
------------

None, other that working installations of the input/output feeders/consumers
you want to use. Also, Java should be installed on the target system. For
installing components of the ELK stack as well as the elastic beats, check my
other roles.

Role Variables
--------------

Look at the [defaults/main.yml](defaults/main.yml) file for this roles
variables
and their documentation.

Dependencies
------------

None

Example Playbook
----------------

This is a minimal playbook to have kibana installed as soon as possible, with
no
certificates, for development purposes.

```yaml
- hosts: logstash-server
  roles:
    - nkakouros.logstash
```

For a full example on how to configure and install a full ELK installation (from
where you can pick what is relevant for your use case) see the
[molecule/default/](molecule/default/) folder. In there, the
[prepare.yml](molecule/default/prepare.yml) file contains a playbook that will
install dependencies that this role will need. The
[playbook.yml](molecule/default/playbook.yml) file will contain a full and
complex example of how to use this role specifically.

License
-------

GPLv3

Author Information
------------------

Nikolaos Kakouros (nkak@kth.se)

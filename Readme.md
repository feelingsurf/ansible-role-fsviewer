[![tests](https://github.com/feelingsurf/ansible-role-fsviewer/workflows/Test%20ansible%20role/badge.svg)](https://github.com/feelingsurf/ansible-role-fsviewer/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-feelingsurf.fsviewer-blue.svg)](https://galaxy.ansible.com/feelingsurf/fsviewer)


ansible-role-fsviewer
=====================

This role installs [FeelingSurfViewer](https://github.com/feelingsurf/viewer).

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                    | Required | Default                     | Choices   | Comments                     |
|-----------------------------|----------|-----------------------------|-----------|------------------------------|
| fsviewer_dependencies       | yes      |                             | list      | See `defaults/main.yml`.     |
| fsviewer_version            | yes      | `2.3.1`                     | string    |                              |
| fsviewer_user               | yes      | `fsviewer`                  | string    | User to run the app as.      |
| fsviewer_group              | yes      | `fsviewer`                  | string    | Group to run the app as.     |
| fsviewer_extra_groups       | yes      | `[]`                        | list      |                              |
| fsviewer_home_dir           | yes      | `/home/{{ fsviewer_user }}` | string    |                              |
| fsviewer_env                | yes      | `[]`                        | list      | List of additional env vars. |
| fsviewer_options            | yes      | `[]`                        | list      | List of cli options.         |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-fsviewer
          fsviewer_env:
            - access_token=abcdef0123

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@FeelingSurf](https://github.com/feelingsurf)

[![CI](https://github.com/feelingsurf/ansible-role-fsviewer/actions/workflows/ci.yml/badge.svg)](https://github.com/feelingsurf/ansible-role-fsviewer/actions/workflows/ci.yml)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-feelingsurf.fsviewer-blue.svg)](https://galaxy.ansible.com/feelingsurf/fsviewer)


ansible-role-fsviewer
=====================

This role installs [FeelingSurfViewer](https://github.com/feelingsurf/viewer).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Debian - 13 (Trixie)](https://wiki.debian.org/DebianTrixie)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                    | Required | Default                     | Choices   | Comments                     |
|-----------------------------|----------|-----------------------------|-----------|------------------------------|
| fsviewer_dependencies       | yes      |                             | list      | See `defaults/main.yml`.     |
| fsviewer_version            | yes      | `2.6.0`                     | string    |                              |
| fsviewer_arch               | yes      | automatically selected      | string    |                              |
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

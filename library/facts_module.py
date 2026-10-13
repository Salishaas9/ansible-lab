#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: facts_module
short_description: Модуль фактов
description:
    - Собирает кастомные факты об управляемом узле
options: {}
author:
    - "Кошелева А.А."
'''

EXAMPLES = '''
- name: Собрать факты
  facts_module:
'''

RETURN = '''
ansible_facts:
    description: Кастомные факты об узле
    type: dict
    returned: always
    sample: {
        "my_hostname": "ubuntu-server",
        "my_os": "Linux",
        "my_python_version": "3.14.4",
        "my_cpu_count": 1
    }
'''


def main():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    import platform
    import socket
    import os
    result = {
        'changed': False,
        'ansible_facts': {
            'my_hostname': socket.gethostname(),
            'my_os': platform.system(),
            'my_python_version': platform.python_version(),
            'my_cpu_count': os.cpu_count()
        }
    }
    module.exit_json(**result)


if __name__ == '__main__':
    main()

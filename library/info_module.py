#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: info_module
short_description: Модуль информации
description:
    - Возвращает базовую информацию о модуле
options: {}
author:
    - "Кошелева А.А."
'''

EXAMPLES = '''
- name: Получить информацию
  info_module:
'''

RETURN = '''
info:
    description: Информация о модуле
    type: dict
    returned: always
    sample: {
        "message": "Это модуль информации",
        "version": "1.0"
    }
'''


def main():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    import platform
    import socket
    result = {
    'changed': False,
    'info': {
        'message': 'Это модуль информации',
        'version': '1.0',
        'author': 'Кошелева А.А.',
        'status': 'работает',
        'hostname': socket.gethostname(),
        'os': platform.system(),
        'python_version': platform.python_version()
    }
}


if __name__ == '__main__':
    main()

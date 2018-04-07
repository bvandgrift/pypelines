#!/usr/bin/env python3

import importlib

if __name__ == '__main__':
    print(__name__)

    module = importlib.import_module('hellos')
    print(module)
    khello = getattr(module, 'Hello')
    print(khello)
    kgoodbye = getattr(module, 'Goodbye')
    print(kgoodbye)

    hello = khello()
    goodbye = kgoodbye()

    hello.sayIt()
    hello.sayIt('Ben')

    goodbye.sayIt()
    goodbye.sayIt('Cruel World')

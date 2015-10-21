#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import nose

_base_dir, _ = os.path.split(__file__)

def run(to_str=False):
    result = nose.run(argv=['', '-s', '--where={}'.format(_base_dir), '--verbosity=2'])
    status = int(not result)
    return status


if __name__ == '__main__':
    status = run()
    print('Exit status: {}'.format(status))
    sys.exit(status)





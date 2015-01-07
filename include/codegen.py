"""Simple script for generating thin wrappers using ctypeslib."""

from __future__ import print_function
import os
import shutil
import glob
import subprocess

# Headers to convert
includes = ['wiringPi.h']

# Process
for include in includes:
    prefix = include.split('.')[0]
    try:
        subprocess.check_call(
            ['h2xml', include, '-I.', '-c', '-o%s.xml' % prefix])
    except subprocess.CalledProcessError:
        print('h2xml failed for ' + include)
        continue
    try:
        subprocess.check_call(
            ['xml2py', '%s.xml' % prefix, '-o%s.py' % prefix])
    except subprocess.CalledProcessError:
        print('xml2py failed for ' + include)
        continue

# Move generated Python files
pyfiles = glob.glob('*.py')
for pyfile in pyfiles:
    if pyfile != 'codegen.py':
        try:
            shutil.copy(pyfile, '../wiringpy')
        except shutil.Error:
            print('Error moving ' + pyfile + '. Does it already exist?')

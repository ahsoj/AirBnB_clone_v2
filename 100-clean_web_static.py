#!/usr/bin/python3
"""
     Fabric script (based on the file 3-deploy_web_static.py) \
	that deletes out-of-date archives,
"""
from fabric.api import run, env, local


def do_clean(number=0):
    """
    number is the number of the archives, including the most recent, to keep.
    If number is 0 or 1, keep only the most recent version of your archive.
    if number is 2, keep the most recent, and second most recent versions of your archive.
    """
    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))

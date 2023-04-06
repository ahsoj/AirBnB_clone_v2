#!/usr/bin/python3
"""
   Fabric script (based on the file 2-do_deploy_web_static.py) \
	that creates and distributes an archive to your web servers
"""
import os
from datetime import datetime
from fabric.api import env, run, runs_once, put

env.hosts = ['52.91.136.103', '18.235.248.251']

do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack


def deploy():
    """
        Call the do_pack() function and store the path of the created archive
        Return False if no archive has been created
        Call the do_deploy(archive_path) function, using the new path of the new archive
        Return the return value of do_deploy
    """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False

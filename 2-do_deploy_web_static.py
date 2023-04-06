#!/usr/bin/python3
"""
   Fabric script (based on the file 1-pack_web_static.py) \
	 that distributes an archive to your web servers
"""
from fabric.api import put, env, run, runs_once, sudo
import os
#import logging
from datetime import datetime

env.hosts = ['18.235.248.251', '52.91.136.103']
env.sudo_prefix = "sudo -S '%(sudo_prompt)s' " % env

#logging.basicConfig(level=logging.INFO)


def do_deploy(archive_path):
    """
	upload to /tmp/
	uncompress to /data/web_static/releases
	rtype: archive_path ? True : False
    """
    if not os.path.exists(archive_path):
        return False
    dirs = (archive_path).rsplit(".")[0].rsplit("/")[1]
    ld = "/data/web_static/releases/{}".format(dirs)
    base_n = os.path.basename(archive_path)
    try:
        put(archive_path, '/tmp/{}'.format(base_n))
        run("sudo mkdir -p {}/".format(ld))
        run("sudo tar -xzf /tmp/{} -C {}/".format(base_n, ld))
        run("sudo rm -rf /tmp/{}".format(base_n))
        run("sudo mv {}/web_static/* {}/".format(ld, ld))
        run("sudo rm -rf {}/web_static".format(ld))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -fs {}/ /data/web_static/current".format(ld))
        print('New version deployed!')
    except Exception:
        return False

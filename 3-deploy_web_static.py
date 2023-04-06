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


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    tss = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(tss)
    try:
        print("Packing web_static to {}".format(path))
        local("tar -cvzf {} web_static".format(path))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(path, archize_size))
    except Exception:
        path = None
    return path


def deploy():
    """"""
    pack_Path = do_pack()
    return do_deploy(archive_path) if archive_path else False

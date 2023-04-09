#!/usr/bin/python3
"""
   Fabric script (based on the file 1-pack_web_static.py) \
         that distributes an archive to your web servers
"""

from fabric.api import put, env, run, runs_once, sudo
import os
from datetime import datetime

env.hosts = ['18.235.248.251', '52.91.136.103']
env.sudo_prefix = "sudo -S '%(sudo_prompt)s' " % env


def do_pack():
    """pack web_static folder to deploy"""
    tss = datetime.now().strftime("%Y%m%d%H%M%S")
    path = ("versions/web_static_{}.tgz".format(tss))
    result = local("tar -cvzf {} web_static".format(path))
    if result.failed:
        return None
    tgz_size = os.stat(path).st_size
    print("web_static packed: {} -> {} Bytes".format(path, tgz_size))
    return path


def do_deploy(archive_path):
    """
        upload to /tmp/
        uncompress to /data/web_static/releases
        rtype: archive_path ? True : False
    """
    if not archive_path:
        return False
    dirs = (archive_path).rsplit(".")[0].rsplit("/")[1]
    ld = "/data/web_static/releases/{}".format(dirs)
    base_n = os.path.basename(archive_path)

    try:
        put(archive_path, '/tmp/{}'.format(base_n))
        run("mkdir -p {}/".format(ld))
        run("tar -xzf /tmp/{} -C {}/".format(base_n, ld))
        run("rm -rf /tmp/{}".format(base_n))
        run("mv {}/web_static/* {}/".format(ld, ld))
        run("rm -rf {}/web_static".format(ld))
        run("rm -rf /data/web_static/current")
        run("ln -fs {}/ /data/web_static/current".format(ld))
        print('New version deployed!')
        return True
    except Exception:
        return False


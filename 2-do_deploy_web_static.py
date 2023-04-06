#!/usr/bin/python3
"""
   Fabric script (based on the file 1-pack_web_static.py) \
	 that distributes an archive to your web servers
"""
from fabric.api import put, env, run
import os
env.hosts = ['52.91.136.103', '18.235.248.251']


def do_deploy(archive_path):
    """
	upload to /tmp/
	uncompress to /data/web_static/releases
	rtype: archive_path ? True : False
    """
    if not archive_path:
        return False
    dirs = (archive_path).rsplit(".")[0].rsplit("/")[1]
    ld = "/data/web_static/releases"
    try:
        put(archive_path, '/tmp/{}'.format(dirs))
        run("mkdir -p /data/web_static/releases/{}/".format(dirs))
        run("tar -xzf /tmp/{} -C {}/{}/".format(os.path.basename(archive_path), ld, dirs))
        run("rm -rf /tmp/{}".format(archive_path))
        run("mv {}/{}/web_static/* {}/{}".format(ld, dirs, ld, dirs))
        run("rm -rf {}/{}/web_static".format(ld, dirs))
        run("rm -rf /data/web_static/current")
        run("ln -fs {}/{}/ /data/web_static/current".format(ld, dirs))
        print('New version deployed!')
    except Exception:
        return False

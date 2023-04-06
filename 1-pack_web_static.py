#!/usr/bin/python3
"""
    generates a .tgz archive from the contents of \
    the web_static folder of your AirBnB Clone repo
"""
import os
from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """
        create a folder versions
        file name -> web_static<y_m_d_h_M_s>.tgz
        rtyp: file
    """
    local("mkdir -p versions")
    tss = datetime.now().strftime("%Y%m%d%H%M%S")
    path = ("versions/web_static_{}.tgz".format(tss))
    result = local("tar -cvzf {} web_static".format(path))
    if result.failed:
        return None
    tgz_size = os.stat(path).st_size
    print("web_static packed: {} -> {} Bytes".format(path, tgz_size))
    return path

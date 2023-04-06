#!/usr/bin/python3
"""
    generates a .tgz archive from the contents of \
    the web_static folder of your AirBnB Clone repo
"""
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
    tss = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    path = "versions/web_static_{}.tgz".format(tss)
    res = local(
        "tar -czvf {} web_static".format(
            path))
    if res.failed:
        return None
    return path

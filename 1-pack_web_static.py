#!/usr/bin/python3
# use a fabfile to compares the payload.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the entire directory web_static."""
    DT = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(DT.year,
                                                         DT.month,
                                                         DT.day,
                                                         DT.hour,
                                                         DT.minute,
                                                         DT.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file

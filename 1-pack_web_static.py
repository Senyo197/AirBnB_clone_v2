#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        # Create the 'versions' folder if it doesn't exist
        if not os.path.exists("versions"):
            local("mkdir versions")

        # Create the name of the archive
        now = datetime.utcnow()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)

        # Compress web_static contents into a .tgz archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if the archive has been correctly generated
        return "versions/{}".format(archive_name)

    except Exception as e:
        return None

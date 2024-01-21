#!/usr/bin/python3
"""
Distributes an archive to your web servers using the function do_deploy
"""
import os
from fabric.api import env, put, run

env.hosts = ['54.152.172.214', '54.175.148.101']
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files
    Returns:
        True if all operations done correctly, otherwise returns False
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Extract archive to /data/web_static/releases/
        # <archive filename without extension>
        file_name = os.path.basename(archive_path)
        folder_name = file_name.replace(".tgz", "")
        folder_path = "/data/web_static/releases/{}/".format(folder_name)
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))

        # Delete the archive from the web server
        run("rm -rf /tmp/{}".format(file_name))

        # Move contents to the correct folder and remove unnecessary folder
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        run("ln -sf {} /data/web_static/current".format(folder_path))

        print('New version deployed!')
        return True
    except Exception as e:
        print(e)
        return False

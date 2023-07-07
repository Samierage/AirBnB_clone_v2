from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    local("mkdir -p versions")
    time_format = "%Y%m%d%H%M%S"
    archive_name = "web_static_{}.tgz".format(datetime.now().strftime(time_format))
    command = "tar -cvzf versions/{} web_static".format(archive_name)
    result = local(command)
    if result.failed:
        return None
    return "versions/{}".format(archive_name)

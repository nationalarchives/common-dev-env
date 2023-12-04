import subprocess

from conf import applications_directory
from lib import get_service_keys


def pull():
    for name in get_service_keys():
        subprocess.run(["git", "-C", f"{applications_directory}/{name}", "pull"])


if __name__ == "__main__":
    pull()

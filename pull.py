import subprocess

from conf import applications_directory
from lib import get_service_keys
from start import start


def pull():
    for name in get_service_keys():
        print(f"Pulling {name}...")
        subprocess.run(["git", "-C", f"{applications_directory}/{name}", "pull"])
    start()


if __name__ == "__main__":
    pull()

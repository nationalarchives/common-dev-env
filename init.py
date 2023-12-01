import subprocess
from os import mkdir, path

from conf import applications_directory, temp_directory
from lib import get_services
from start import start


def init():
    if not path.isfile("./config.json"):
        print("No config found.")
        repo = prompt_for_repo()
        clone_config_repo(repo)
        if not check_config_from_repo():
            print("No config.json found in repository. Exiting.")
            exit()
        use_config_from_repo()
    setup_applications()
    start()


def prompt_for_repo():
    repo = ""
    while repo == "":
        print("Enter the URL of a configuration repository:")
        repo = input()
    return repo


def clone_config_repo(url):
    remove_config_repo()
    subprocess.run(["git", "clone", url, temp_directory])


def check_config_from_repo():
    return path.isfile("%s/config.json" % temp_directory)


def use_config_from_repo():
    subprocess.run(["cp", "%s/config.json" % temp_directory, "./config.json"])
    remove_config_repo()


def remove_config_repo():
    subprocess.run(["rm", "-fR", temp_directory])


def setup_applications():
    if not path.isdir(applications_directory):
        mkdir(applications_directory)
    for name, properties in get_services().items():
        clone_application(name, properties)


def clone_application(name, properties):
    clone_location = "%s/%s" % (applications_directory, name)
    if "repo" in properties and not path.isdir(clone_location):
        subprocess.run(
            [
                "git",
                "clone",
                properties["repo"],
                clone_location,
            ]
        )


if __name__ == "__main__":
    init()

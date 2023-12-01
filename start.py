import json
import subprocess
from os import path

from conf import (applications_directory, commodities_directory,
                  docker_project_name)
from lib import get_services, get_used_commodities


def start():
    for name in get_services():
        start_service(name)
    for name in get_used_commodities():
        start_commodity(name)


def start_service(name):
    commands = [
        "docker-compose",
        "-f",
        "%s/%s/docker-compose.yml" % (applications_directory, name),
        "-p",
        docker_project_name,
        "--env-file",
        ".commodities.env",
    ]
    if path.isfile(".env"):
        commands = commands + [
            "--env-file",
            ".env",
        ]
    application_env_file = "%s/%s/.env" % (applications_directory, name)
    if path.isfile(application_env_file):
        commands = commands + [
            "--env-file",
            application_env_file,
        ]
    commands = commands + [
        "up",
        "--remove-orphans",
        "--build",
        "-d",
    ]
    subprocess.run(commands)


def start_commodity(name):
    commands = [
        "docker-compose",
        "-f",
        "%s/%s/docker-compose.yml" % (commodities_directory, name),
        "-p",
        docker_project_name,
        "--env-file",
        ".commodities.env",
        "up",
        "--remove-orphans",
        "--build",
        "-d",
    ]
    subprocess.run(commands)


if __name__ == "__main__":
    start()

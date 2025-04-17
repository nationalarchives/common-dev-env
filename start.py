import subprocess
from os import path

from conf import applications_directory, commodities_directory
from lib import get_services, get_used_commodities, get_project_name


def start():
    services = get_services()
    for name in services:
        start_service(name, services[name]["services"])
    for name in get_used_commodities():
        start_commodity(name)


def start_service(name, services=[]):
    commands = [
        "docker",
        "compose",
        "-f",
        f"{applications_directory}/{name}/docker-compose.yml",
        "-p",
        f"{get_project_name()}-{name}",
        "--env-file",
        ".env",
    ]
    application_env_file = f"{applications_directory}/{name}/.env"
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
    ] + services
    subprocess.run(commands)


def start_commodity(name):
    commands = [
        "docker",
        "compose",
        "-f",
        f"{commodities_directory}/{name}/docker-compose.yml",
        "-p",
        f"{get_project_name()}-{name.split(':')[0]}",
        "--env-file",
        ".env",
        "up",
        "--remove-orphans",
        "--build",
        "-d",
    ]
    subprocess.run(commands)


if __name__ == "__main__":
    start()

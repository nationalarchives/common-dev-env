import json
from os import walk

from conf import commodities_directory


def get_config():
    data = {}
    with open("config.json", "r") as f:
        data = json.load(f)
    return data


def commodities():
    commodities = []
    for dirpath, dirnames, filenames in walk(commodities_directory):
        commodities.extend(dirnames)
        break
    return commodities


def get_used_commodities():
    get_config()
    return [
        commodity
        for commodity, properties in get_config().items()
        if commodity in commodities() and properties["enabled"] == "true"
    ]


def get_services():
    services = {}
    for name, properties in get_config().items():
        if name not in commodities():
            services[name] = properties
    return services


def get_service_keys():
    return [name for name in get_services()]

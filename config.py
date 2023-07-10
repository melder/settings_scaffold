# pylint: skip-file
# TODO: migrate constants to config
import os
import yaml


def parse_yaml_vendors():
    with open("config/vendors.yml", "r") as f:
        return yaml.safe_load(f)


def parse_yaml_settings():
    with open("config/settings.yml", "r") as f:
        return yaml.safe_load(f)


class DictAsMember(dict):
    """
    Converts yml to attribute for cleaner access
    """

    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = DictAsMember(value)
        return value


conf = DictAsMember(parse_yaml_settings() | parse_yaml_vendors())

version = conf.version

if conf.get("discord_webhooks"):
    discord_webhooks = conf.discord_webhooks

if conf.get("redis"):
    import redis as r

    redis_host = conf.redis.host
    redis_port = conf.redis.port
    redis = r.Redis(host=redis_host, port=redis_port, decode_responses=True)

    if conf.redis.get("om"):
        os.environ["REDIS_OM_URL"] = f"redis://@{redis_host}:{redis_port}"

if conf.get("polygon"):
    polygon_api_key = conf.polygon.api_key

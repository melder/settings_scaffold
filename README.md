# settings_scaffold

Configuration scaffold for projects requiring similar settings / vendor connection strings. 

Converts YML keys to python attributes to make code more readable. e.g:

```
config.redis.host

# rather than

config['redis']['host']```

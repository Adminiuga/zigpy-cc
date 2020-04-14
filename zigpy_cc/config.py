import voluptuous as vol
from zigpy.config import (  # noqa: F401 pylint: disable=unused-import
    CONF_DATABASE,
    CONF_DEVICE,
    CONF_DEVICE_PATH,
    CONFIG_SCHEMA,
    cv_boolean,
)

CONF_DEVICE_BAUDRATE = "baudrate"
CONF_DEVICE_BAUDRATE_DEFAULT = 115200

SCHEMA_DEVICE = vol.Schema(
    {
        vol.Required(CONF_DEVICE_PATH): vol.Any(vol.PathExists(), "auto"),
        vol.Optional(CONF_DEVICE_BAUDRATE, default=CONF_DEVICE_BAUDRATE_DEFAULT): int,
    }
)

CONFIG_SCHEMA = CONFIG_SCHEMA.extend({vol.Required(CONF_DEVICE): SCHEMA_DEVICE, })

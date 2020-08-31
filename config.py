""" This module contains the configuration variables needed by the app"""
import json


def _json_read_key(data, key):
    """
    Read the value of a key
    Args:
        data (str): The value of the parameter
        key (str): The name of the parameter
    Returns:
        data[key]: The value of the key, None if not provided
    """
    try:
        return data[key]
    except KeyError:
        return None


def _require_key(value, name):
    """
    Check if a key is provided if required to continue
    (Method not currently in use)
    Args:
        value (str): The value of the parameter
        name (str): The name of the parameter
    Raises:
        KeyError: If key/value is not specified in config.json
    """

    # Currently not required
    if value is None:
        raise KeyError("Missing required configuration key: '%s'" % name)


class Config:
    """
    The configuration of the Flask app, can be used to update the app object
    """

    def __init__(self):
        self.port = None
        self.host = None
        self.cors_origins = None

    def from_json(self, data):
        """
        Pulls information from config.json. Should be updated as json is modified.
        Args:
            data (str): config.json
        Updates:
            self.port (int): port to run Flask app on
            self.host (str): ip to run Flask app on
        """
        data = json.loads(data)
        self.port = _json_read_key(data, "port")
        self.host = _json_read_key(data, "host")
        self.cors_origins = _json_read_key(data, "cors_origins")

        # Set port and host to default if not specified
        if self.port is None:
            self.port = 5000

        if self.host is None:
            self.host = "127.0.0.1"

    def get_dict(self):
        """
        Returns the parameters for configuration of the app object
        Returns:
            configs (dict): Contains all parameters in config.json
        """
        # Require that CORS_DOMAINS has been provided and it can be iterated
        _require_key(self.cors_origins, "CORS_DOMAINS")
        if not hasattr(self.cors_origins, "__iter__"):
            raise TypeError

        return {
            "PORT": self.port,
            "HOST": self.host,
            "CORS_ORIGINS": self.cors_origins
        }

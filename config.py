import os
import sys
from logger import logger
from pathlib import Path


class ConfigClass(object):
    def __init__(self):
        self.version_info = {
            "version": "v0.1.0.20250720",
            "runtime": sys.version,
        }

        self.server_name = os.getenv('SERVER_NAME') or 'MCP Bridge'
        self.log_level = os.getenv('LOG_LEVEL') or 'info'
        self.mcp_endpoint = os.getenv('MCP_ENDPOINT')

        self.config_path = Path(os.getenv('CONFIG_PATH') or 'config.json')
        if not self.config_path.exists():
            logger.error(f'config file not exists：{self.config_path.absolute()}')
            exit(-1)

        # log config items
        logger.info('=================================')
        for k, v in self.__dict__.items():
            logger.info(f'{k}={v}')
        logger.info('=================================')


Config = ConfigClass()


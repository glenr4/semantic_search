
import time
import logging
import subprocess
from pathlib import Path

import requests


logger = logging.getLogger("haystack")
ELASTICSEARCH_CONTAINER_NAME = "elasticsearch"
OPENSEARCH_CONTAINER_NAME = "opensearch"
WEAVIATE_CONTAINER_NAME = "weaviate"


def launch_persistent_es(sleep=15, delete_existing=False, volume=''):
    """
    Start an Elasticsearch server via Docker.
    """
    elasticDataDir = '/usr/share/elasticsearch/data'
    defaultVolume = '~/.local/share/elasticData'

    logger.debug("Starting Elasticsearch ...")
    if delete_existing:
        _ = subprocess.run(
            [f"docker rm --force {ELASTICSEARCH_CONTAINER_NAME}"], shell=True, stdout=subprocess.DEVNULL)

    dockerCmd = f'docker start {ELASTICSEARCH_CONTAINER_NAME} > /dev/null 2>&1 || docker run -d -p 9200:9200 -e "discovery.type=single-node" --name {ELASTICSEARCH_CONTAINER_NAME} elasticsearch:7.9.2'
    if volume != '':
        dockerCmd += f' -v {volume}:{elasticDataDir}'
    else:
        dockerCmd += f' -v {defaultVolume}:{elasticDataDir}'

    logger.debug(f'Starting Docker with: {dockerCmd}')

    status = subprocess.run(
        [
            dockerCmd
        ],
        shell=True,
    )

    if status.returncode:
        logger.warning(
            "Tried to start Elasticsearch through Docker but this failed. "
            "It is likely that there is already an existing Elasticsearch instance running. "
        )
    else:
        time.sleep(sleep)

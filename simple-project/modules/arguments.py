"""Arguments."""

import argparse

from .logger import get_logger

logger = get_logger('app.arguments')


def parse_args(args):
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        description='A description of the cli program.')
    parser.add_argument('message', type=str)
    parsed_args = parser.parse_args(args)

    logger.info('Parsed')

    return parsed_args

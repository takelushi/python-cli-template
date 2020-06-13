"""Simple CLI application."""

import sys

from proj.arguments import parse_args
from proj.logger import get_logger


def main():
    """Run application."""
    logger = get_logger('app', init=True)
    args = parse_args(sys.argv[1:])

    logger.debug('Message: %s', args.message)

    if args.message.lower() != 'hello':
        logger.error('Please say "hello".')
        exit(1)

    logger.info('Hello.')
    exit(0)


if __name__ == '__main__':
    main()

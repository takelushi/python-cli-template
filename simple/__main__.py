"""Simple CLI application."""

import argparse
import logging
import sys


def parse_args(args):
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        description='A description of the cli program.')
    parser.add_argument('message', type=str)
    return parser.parse_args(args)


def main():
    """Run application."""
    logging.root.setLevel(logging.DEBUG)
    args = parse_args(sys.argv[1:])

    logging.debug('Message: %s', args.message)

    if args.message.lower() != 'hello':
        logging.error('Please say "hello".')
        exit(1)

    logging.info('Hello.')
    exit(0)


if __name__ == '__main__':
    main()

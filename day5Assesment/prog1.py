import logging
import sys

def throws():
    raise RuntimeError('this is the error message')

def main():
    logging.basicConfig(filename='example.log',level=logging.WARNING)
    log = logging.getLogger('example')
    try:
        throws()
        return 0
    except Exception, err:
        log.exception('Error from throws():')
        return 1

if __name__ == '__main__':
    sys.exit(main())
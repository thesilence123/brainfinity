from theorm import Theorm, Clause
from numbers_wrapper import NaturalNumber
import os
import json
import logging.config
from theorms import commutative_addition, zero_axiom


def setup_logging(
        default_path='logging.json', default_level=logging.INFO):
    """
    Setup logging configuration
    """
    path = default_path

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    theorms = [commutative_addition, zero_axiom]

    givens = [given for given in [NaturalNumber('m'), 5, 8, 8, 8, 8, 0, 8]]

    for therom_ in theorms:
        logger.debug('Going to match: %s' % therom_.name)
        if therom_.given.is_match(givens):
            logging.debug('Matched! Given: %s, Result: %s' % (therom_.given.clauses, therom_.result,))


if __name__ == '__main__':
    main()

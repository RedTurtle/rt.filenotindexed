# -*- extra stuff goes here -*-

from Globals import DevelopmentMode
import logging
import os

logger = logging.getLogger('rt.filenotindexed')


TRUISMS = ['yes', 'y', 'true', 'on']
ENABLED = os.environ.get('DISABLE_FILE_INDEXING', None)

if (ENABLED is not None and ENABLED.lower() in TRUISMS) or \
   (ENABLED is None and DevelopmentMode is True):
    # Yes! I copied this all from Products.PrintingMailHost
    logger.warning("Hold on to your hats folks, I'm a-patchin'")
    import monkeys


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

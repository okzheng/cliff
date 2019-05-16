import logging

from cliff.command import Command


class Simple(Command):
    "A simple command that prints a message."

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('Simple Command sending greeting')
        self.log.debug('debugging')
        self.app.stdout.write('hi!\n')


class Error(Command):
    "Always raises an error"

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('Error Command causing error')
        raise RuntimeError('this is the expected exception')

class Found(Command):
    "A Found command for test."
        
    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('Found command is working!')
        self.app.stdout.write('good Found! \n')
    

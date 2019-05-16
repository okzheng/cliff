import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class DemoCli(App):

    def __init__(self):
        super(DemoCli, self).__init__(
            description='first demo command line tool',
            version='1.0',
#CommandManager 实例用于载入各个子命令的插件，第一个参数为namespace，用来指定setuptools entry points
            command_manager=CommandManager('demo.cli'),
            deferred_help=True,
            )
#在主程序解析完命令行参数后被调用一次，唯一的一次。
    def initialize_app(self, argv):
        self.LOG.debug('initialize_app')
#子命令执行前被调用
    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)
#子命令完成后被调用
    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    firstapp = DemoCli()
    return firstapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

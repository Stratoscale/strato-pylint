from astroid import MANAGER
from astroid import scoped_nodes

def register(linter):
    pass

def transform(module):
    # Ignore dynamically added properties to logging
    # Based on an exmaple here: http://docs.pylint.org/plugins.html
    if module.name == 'logging':
        module.locals['progress'] = [scoped_nodes.Class('progress', None)]
        module.locals['success'] = [scoped_nodes.Class('success', None)]
    elif module.name == 'twisted.internet.reactor':
        resultOfCallLater = scoped_nodes.Class('callLater', None)
        resultOfCallLater.locals['cancel'] = [scoped_nodes.Class('callLater_cancel', None)]
        module.locals['callLater'] = resultOfCallLater
        module.locals['callFromThread'] = [scoped_nodes.Class('callFromThread', None)]
        module.locals['callInThread'] = [scoped_nodes.Class('callInThread', None)]
        module.locals['run'] = [scoped_nodes.Class('run', None)]
        module.locals['stop'] = [scoped_nodes.Class('stop', None)]

MANAGER.register_transform(scoped_nodes.Module, transform)

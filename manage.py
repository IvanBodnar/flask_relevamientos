import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from relevamientos.app import app

manager = Manager(app)

# Add runserver command
manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='localhost',
    port=5000
))

# Add migrate command
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
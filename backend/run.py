from core.app import app, HOST, PORT
from core.controllers.users import bp as bp_users
from core.controllers.groups import bp as bp_groups
from core.controllers.permissions import bp as bp_permissions
from core.controllers.modules import bp as bp_modules
from core.controllers.dinosaurs import bp as bp_dinosaurs
from core.controllers.searches import bp as bp_searches


app.register_blueprint(bp_users, url_prefix='/api/users')
app.register_blueprint(bp_groups, url_prefix='/api/groups')
app.register_blueprint(bp_modules, url_prefix='/api/modules')
app.register_blueprint(bp_permissions, url_prefix='/api/permissions')
app.register_blueprint(bp_dinosaurs, url_prefix='/api/dinosaurs')
app.register_blueprint(bp_searches, url_prefix='/api/searches')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)

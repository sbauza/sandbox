# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import flask
import six
from werkzeug import exceptions as werkzeug_exceptions

from sandbox.api.middleware import debug
from sandbox.api.v1 import utils as api_utils
from sandbox.api.v1.endpoints import shopping
from sandbox import conf

CONF = conf.CONF

CONF.add_opt('log_exchange', True)
CONF.add_opt('debug', True)


def make_json_error(ex):
    if isinstance(ex, werkzeug_exceptions.HTTPException):
        status_code = ex.code
        description = ex.description
    else:
        status_code = 500
        description = str(ex)
    return api_utils.render({'error': status_code,
                             'error_message': description},
                            status=status_code)


def make_app():
    """App builder (wsgi).

    Entry point for REST API server.
    """
    app = flask.Flask('sandbox.api')

    app.register_blueprint(shopping.rest, url_prefix='/v1')

    for code in six.iterkeys(werkzeug_exceptions.default_exceptions):
        app.error_handler_spec[None][code] = make_json_error

    if CONF.debug and not CONF.log_exchange:
        print('Logging of request/response exchange could be enabled '
              'using flag --log_exchange')

    if CONF.log_exchange:
        app.wsgi_app = debug.Debug.factory(app.config)(app.wsgi_app)

    # TODO(sbauza): Add auth factory middleware

    return app

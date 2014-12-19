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

from sandbox.api.v1 import utils as api_utils

rest = api_utils.Rest('v1_0', __name__)


# TODO(sbauza): Create _api interface

# Leases operations

@rest.get('/shopping')
def shopping_list():
    return api_utils.render(_api.get_shopping_list())


@rest.post('/shopping')
def shopping_create(data):
    return api_utils.render(_api.create_shopping(data))


@rest.get('/shopping/<shopping_id>')
def shopping_get(shopping_id):
    return api_utils.render(_api.get_shopping(shopping_id))


@rest.put('/shopping/<shopping_id>')
def shopping_update(shopping_id, data):
    return api_utils.render(_api.update_shopping(shopping_id, data))


@rest.delete('/shopping/<shopping_id>')
def shopping_delete(shopping_id):
    _api.delete_lease(shopping_id)
    return api_utils.render()

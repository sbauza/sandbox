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


import pkgutil
import sys

import sandbox

package = sandbox
prefix = package.__name__ + "."


def _warn_imports(name):
    print ("WARNING: Import issue when importing %s, no configuration found",
           name)


def main():
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__,
                                                      prefix):
        try:
            __import__(name)
        except ImportError:
            print ("WARNING: Import issue with %s" %
                   name)

    try:
        filename = sys.argv[1]
    except IndexError:
        sandbox.conf.CONF.save()
    else:
        with open(filename, 'wb') as configfile:
            sandbox.conf.CONF.save(configfile)


if __name__ == '__main__':
    main()

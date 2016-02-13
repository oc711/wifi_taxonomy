#!/usr/bin/python
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# pylint: disable=line-too-long

"""Routines for handling Ethernet OUI information.
"""

# The IEEE publishes an enormous list of registered Ethernet OUIs,
# but we don't benefit from having that entire list here. Instead
# we track the OUIs which let us distinguish devices which are
# otherwise very similar, such as distinguishing LG G2 from Samsung
# Galaxy S4.
database = {
    '00:bb:3a': ['amazon'],
    '10:ae:60': ['amazon'],
    '74:75:48': ['amazon'],
    '84:d6:d0': ['amazon'],
    'a0:02:dc': ['amazon'],
    'f0:27:2d': ['amazon'],
    'f0:4f:7c': ['amazon'],
    'f0:a2:25': ['amazon'],

    '30:85:a9': ['asus'],
    '5c:ff:35': ['asus'],
    '74:d0:2b': ['asus'],
    'ac:22:0b': ['asus'],

    '30:8c:fb': ['dropcam'],

    '00:1a:11': ['google'],
    '54:60:09': ['google'],
    '94:eb:2c': ['google'],
    'a4:77:33': ['google'],
    'f4:f5:e8': ['google'],
    'f8:8f:ca': ['google'],

    # These are registered to AzureWave, but used for Chromecast v1.
    '6c:ad:f8': ['azurewave', 'google'],
    'd0:e7:82': ['azurewave', 'google'],

    '00:23:76': ['htc'],
    '00:ee:bd': ['htc'],
    '1c:b0:94': ['htc'],
    '38:e7:d8': ['htc'],
    '50:2e:5c': ['htc'],
    '64:a7:69': ['htc'],
    '7c:61:93': ['htc'],
    '90:e7:c4': ['htc'],
    'b4:ce:f6': ['htc'],
    'd8:b3:77': ['htc'],
    'e8:99:c4': ['htc'],

    '0c:48:85': ['lg'],
    '10:68:3f': ['lg'],
    '2c:54:cf': ['lg'],
    '40:b0:fa': ['lg'],
    '58:3f:54': ['lg'],
    '64:89:9a': ['lg'],
    '64:bc:0c': ['lg'],
    '78:f8:82': ['lg'],
    '8c:3a:e3': ['lg'],
    'a0:39:f7': ['lg'],
    'a0:91:69': ['lg'],
    'c4:43:8f': ['lg'],
    'c4:9a:02': ['lg'],
    'f8:95:c7': ['lg'],
    'f8:a9:d0': ['lg'],

    '28:18:78': ['microsoft'],
    '50:1a:c5': ['microsoft'],
    '60:45:bd': ['microsoft'],
    '7c:ed:8d': ['microsoft'],

    '14:30:c6': ['motorola'],
    '1c:56:fe': ['motorola'],
    '24:da:9b': ['motorola'],
    '3c:43:8e': ['motorola'],
    '44:80:eb': ['motorola'],
    '5c:51:88': ['motorola'],
    '60:be:b5': ['motorola'],
    '80:6c:1b': ['motorola'],
    '84:10:0d': ['motorola'],
    '90:68:c3': ['motorola'],
    '98:4b:4a': ['motorola'],
    '9c:d9:17': ['motorola'],
    'cc:c3:ea': ['motorola'],
    'e8:91:20': ['motorola'],
    'f8:7b:7a': ['motorola'],
    'f8:cf:c5': ['motorola'],
    'f8:e0:79': ['motorola'],
    'f8:f1:b6': ['motorola'],

    '00:26:e8': ['murata'],
    '10:a5:d0': ['murata'],
    '14:7d:c5': ['murata'],
    '1c:99:4c': ['murata'],
    '20:02:af': ['murata'],
    '44:a7:cf': ['murata'],
    '5c:da:d4': ['murata'],
    '78:4b:87': ['murata'],
    '90:b6:86': ['murata'],
    '98:f1:70': ['murata'],
    'f0:27:65': ['murata'],
    'fc:c2:de': ['murata'],
    'fc:db:b3': ['murata'],

    '18:b4:30': ['nest'],

    '00:27:09': ['nintendo'],
    '34:af:2c': ['nintendo'],

    '00:26:37': ['samsung'],
    '08:d4:2b': ['samsung'],
    '08:ec:a9': ['samsung'],
    '14:32:d1': ['samsung'],
    '24:4b:81': ['samsung'],
    '30:19:66': ['samsung'],
    '34:23:ba': ['samsung'],
    '38:aa:3c': ['samsung'],
    '3c:8b:fe': ['samsung'],
    '40:0e:85': ['samsung'],
    '48:5a:3f': ['samsung', 'wisol'],
    '5c:0a:5b': ['samsung'],
    '5c:f6:dc': ['samsung'],
    '6c:2f:2c': ['samsung'],
    '6c:83:36': ['samsung'],
    '78:d6:f0': ['samsung'],
    '80:65:6d': ['samsung'],
    '84:38:38': ['samsung'],
    '88:32:9b': ['samsung'],
    '8c:77:12': ['samsung'],
    '90:18:7c': ['samsung'],
    '94:35:0a': ['samsung'],
    'a0:0b:ba': ['samsung'],
    'a8:06:00': ['samsung'],
    'ac:36:13': ['samsung'],
    'b0:df:3a': ['samsung'],
    'b0:ec:71': ['samsung'],
    'b4:07:f9': ['samsung'],
    'c0:bd:d1': ['samsung'],
    'c4:42:02': ['samsung'],
    'cc:07:ab': ['samsung'],
    'cc:3a:61': ['samsung'],
    'd0:22:be': ['samsung'],
    'e0:99:71': ['samsung'],
    'e4:12:1d': ['samsung'],
    'e8:3a:12': ['samsung'],
    'e8:50:8b': ['samsung'],
    'ec:1f:72': ['samsung'],
    'ec:9b:f3': ['samsung'],
    'f0:25:b7': ['samsung'],
    'f4:09:d8': ['samsung'],

    '00:d9:d1': ['sony'],
    '28:0d:fc': ['sony'],
    '30:17:c8': ['sony'],
    '40:b8:37': ['sony'],
    'b4:52:7e': ['sony'],

    '00:24:e4': ['withings'],
}


def LookupOUI(mac):
  """Return a list of manufacturer(s) from a MAC address."""
  mac = mac.lower().split(':')
  oui = ':'.join(mac[0:3])
  return database.get(oui, [])

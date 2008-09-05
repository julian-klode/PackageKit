#!/usr/bin/python
#
# Copyright (C) 2007 Richard Hughes <richard@hughsie.com>
# Copyright (C) 2007 Red Hat Inc, Seth Vidal <skvidal@fedoraproject.org>
#
# Licensed under the GNU General Public License Version 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import sys

options = sys.argv[1]
searchterms = sys.argv[2]

from yumBackend import PackageKitYumBackend

backend = PackageKitYumBackend(sys.argv,lock=False)
backend.run_command()
sys.exit(0)


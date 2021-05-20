#!/usr/bin/python
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import pysftp
import glob
import os
import settings

# get latest image for upload
list_of_files = glob.glob('/home/pi/motion/*')
latest_file = max(list_of_files, key=os.path.getctime)

# upload latest motion webcam image
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
sftp = pysftp.Connection(host=settings.hostName, username=settings.userName, password=settings.passwd, private_key=".ppk", cnopts=cnopts)
sftp.put(latest_file, settings.hostPath + settings.webcamImage)

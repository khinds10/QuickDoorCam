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

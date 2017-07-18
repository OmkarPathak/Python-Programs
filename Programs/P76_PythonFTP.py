# Author: OMKAR PATHAK

# For transfering files to your another/local computer, you will have to install a FTP
# Daemon. Execute following for doing the same:
# 1. sudo apt-get install vsftpd
# 2. service vsftpd start
# 3. sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.orig
# 4. sudo nano /etc/vsftpd.conf

# Now change the following settings in that file:
#
# anonymous_enable=NO             # disable  anonymous login
# local_enable=YES		# permit local logins
# write_enable=YES		# enable FTP commands which change the filesystem
# local_umask=022		        # value of umask for file creation for local users
# dirmessage_enable=YES	        # enable showing of messages when users first enter a new directory
# xferlog_enable=YES		# a log file will be maintained detailing uploads and downloads
# connect_from_port_20=YES        # use port 20 (ftp-data) on the server machine for PORT style connections
# xferlog_std_format=YES          # keep standard log file format
# listen=NO   			# prevent vsftpd from running in standalone mode
# listen_ipv6=YES		        # vsftpd will listen on an IPv6 socket instead of an IPv4 one
# pam_service_name=vsftpd         # name of the PAM service vsftpd will use
# userlist_enable=YES  	        # enable vsftpd to load a list of usernames
# tcp_wrappers=YES  		# turn on tcp wrappers

import ftplib

def ftp_upload(ftpObj, pathToSend, pathToRecv, fileType='TXT'):
    """
    A function for uploading files to an FTP server
    @param ftpObj: The file transfer protocol object
    @param path: The path to the file to upload
    """
    with open(pathToSend, 'rb') as fobj:
        ftpObj.storlines('STOR ' + pathToRecv, fobj)

if __name__ == '__main__':
    ftp = ftplib.FTP('127.0.0.1')
    ftp.login('omkarpathak', '8149omkar')
    print('Logged in..')

    pathToSend = '/home/omkarpathak/Desktop/output.txt'
    pathToRecv = '/home/omkarpathak/Documents/output.txt'
    ftp_upload(ftp, pathToSend, pathToRecv)

    ftp.quit()

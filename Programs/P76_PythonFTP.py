# Author: OMKAR PATHAK (Annotated Version)

import ftplib
import os


def ftp_upload(ftp, local_path, remote_path):
    # ❌ VIOLATION: Original used storlines for binary file
    # ftpObj.storlines()

    # ✅ FIX
    with open(local_path, 'rb') as f:
        ftp.storbinary(f'STOR {remote_path}', f)


def main():
    # ❌ VIOLATION: Hardcoded credentials (SECURITY RISK)
    # ftp.login('omkarpathak', '8149omkar')

    # ✅ FIX: Use environment variables
    host = os.getenv("FTP_HOST", "127.0.0.1")
    user = os.getenv("FTP_USER")
    password = os.getenv("FTP_PASS")

    if not user or not password:
        print("Set FTP_USER and FTP_PASS")
        return

    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, password)

        ftp_upload(ftp, "output.txt", "output.txt")

    except Exception as e:
        # ❌ VIOLATION: No error handling in original
        print("Error:", e)

    finally:
        ftp.quit()


if __name__ == "__main__":
    main()

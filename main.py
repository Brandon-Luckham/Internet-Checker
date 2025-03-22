#!/usr/bin/env python

import socket
import time
from datetime import datetime

def test_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False

if __name__ == "__main__":
    while True:
        internet_connection = test_internet()
        if not internet_connection:
          with open("internet.txt", "a") as file:
              file.write(f"Internet Down at {datetime.now()}\n")
        time.sleep(300)

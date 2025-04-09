#!/usr/bin/env python

import socket
from time import sleep
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
          print("No Internet")
          with open("internet.txt", "a") as file:
              file.write('Internet Down at {}'.format(datetime.now()))
        else:
            print("Internet Up")
        sleep(300)

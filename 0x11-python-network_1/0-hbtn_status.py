#!/usr/bin/python3
<<<<<<< HEAD
"""Fetches https://intranet.hbtn.io/status."""
=======
"""Fetches https://alx-intranet.hbtn.io/status."""
>>>>>>> 527639dc3bb64bda2c92de36616894dcf9cfb258
import urllib.request


if __name__ == "__main__":
<<<<<<< HEAD
    request = urllib.request.Request("https://intranet.hbtn.io/status")
=======
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
>>>>>>> 527639dc3bb64bda2c92de36616894dcf9cfb258
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

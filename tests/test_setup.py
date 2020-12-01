import unittest
from unittest import mock
import os
from colab_ssh import setup_ssh


# @mock.patch.dict(os.environ, {"IS_TESTING_CI": "TRUE"})
class TestSetup(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        print("Running setup test")

    def test_setup(self):
        # Test setup SSH with notification
        os.environ['IS_TESTING_CI'] = "TRUE"
        webhook_address = os.environ.get("TEAMS_WEBHOOK_ADDRESS")
        ssh_public_key = os.environ.get("TEST_SSH_PUBLIC_KEY")
        print(list(os.environ.keys()))
        print(ssh_public_key)
        if webhook_address is None:
            print("Lol this shit is none")
        setup_ssh(ssh_public_key, webhook_address)

if __name__ == '__main__':
    unittest.main()

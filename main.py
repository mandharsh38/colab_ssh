"""Just look at the name, it's main"""
import time
from typing import List, Optional, Union
from config import config_root_password, install_common_tool
from ssh import config_ssh_server, parse_public_key
from tunel import config_argo_tunnel
from utils import check_gpu_available, get_instance_info


def setup_ssh(public_key: Union[str, List[str]], mattermost_webhook_address: Optional[str] = None):
    """
    Setup an SSH tunel to the current Colab notebook instance with SSH public key authentication

    Parameters:
        public_key:
            - (str): The public key that will be able to authenticate the SSH connection
            - (List[str]): A list of public keys that will be able to authenticate the SSH connection
            - (str): Link to a text file (authorized_keys) that cotains all the public keys that will be
            able to authenticate the SSH connection
        webhook_address:
            - (str): The webhook address of Mattermost for push notification

    After about 2 minutes of running, the bash command to initialize the SSH connection will be print out
    """
    public_key = parse_public_key(public_key)

    if not check_gpu_available():
        return  # pragma: no cover

    # Config password for root user
    msg = ""
    msg = config_root_password(msg)

    # Config ssh server
    msg = config_ssh_server(public_key, msg)

    # Config other common tool and library
    install_common_tool()

    # Config Argo Tunnel
    msg, ssh_command, ssh_config, hostname = config_argo_tunnel(msg)


    print(msg)
    
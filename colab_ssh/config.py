"""Install and config many of the tool that I use for my day to day work"""

import secrets
import subprocess

from colab_ssh.utils import AptManager, run_command


def config_root_password(msg):
    """
    Create a random password, set it for the root user and attach it to the final log
    """
    root_password = secrets.token_urlsafe()
    subprocess.run(
        ["chpasswd"], input=f"root:{root_password}", universal_newlines=True, check=False)
    msg += "✂️"*24 + "\n"
    msg += f"Root password: {root_password}\n"
    msg += "✂️"*24 + "\n"
    return msg


def install_apt_pkg():
    """
    Install my own usefull package, won't explain more about why :P
    """
    apt_manager = AptManager()
    apt_manager.commit()
    all_pkg = ['nano', 'htop', 'cmake',
               'libncurses5-dev', 'libncursesw5-dev', 'git',
               'tree', 'zip']
    apt_manager.install_pkg(*all_pkg)
    apt_manager.commit()


def install_nvtop():
    """
    Install nvtop which is an amazing tool for monitoring NVIDIA GPU
    """
    print("Installing nvtop")
    command = """git clone https://github.com/Syllo/nvtop.git
                 mkdir -p nvtop/build && cd nvtop/build && cmake .. && make && make install && cd
                 rm -rf nvtop"""
    run_command(command)


def install_pip_dependencies():
    pass


def config_bashrc():
    pass

def install_gdrive_rclone():
    pass


def install_iterm_shell_integration():
    """
    Install iTerm shell integration, only work on MacOS iTerm client only,
    I use `imgcat` a lot, loving it.
    """
    print("Installing iterm shell integration")
    command = "curl -L https://iterm2.com/shell_integration/install_shell_integration_and_utilities.sh | bash"
    run_command(command)


def install_vim_tmux():
    pass


def install_common_tool():
    """
    Install many of the tool that I use for my day to day work. Other might want to
    modify this function.
    """
    config_bashrc()
    install_apt_pkg()
    install_nvtop()
    install_pip_dependencies()
    install_gdrive_rclone()
    install_iterm_shell_integration()
    install_vim_tmux()

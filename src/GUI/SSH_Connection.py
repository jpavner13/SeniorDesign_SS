import paramiko
import time

class SSH:
    def __init__(self, host, username, password):
        """
        Initializes the SSH connection parameters.
        """
        self.host = host
        self.username = username
        self.password = password
        self.ssh_client = None

    def connect(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(
            hostname=self.host,
            username=self.username,
            password=self.password,
            timeout=7  # Set a 10-second timeout
        )
        return "SSH connection established successfully."

    def execute_command(self, command):
        """
        Executes a command on the remote host.
        """
        if self.ssh_client:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            return output.strip(), error.strip()
        return "SSH not connected."

    def close(self):
        """
        Closes the SSH connection.
        """
        # Make sure to clean up GPIO pins
        if self.ssh_client:
            self.ssh_client.close()
            self.ssh_client = None



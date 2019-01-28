class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_list = [] # Empty credential list

    def __init__(self,email,platform,password):

      # docstring removed for simplicity

        self.email = email
        self.platform = platform
        self.password = password


class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_list = [] # Empty credential list
    def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

	def __init__(self,user_name,site_name,account_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

	def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
		# global users_list
		Credential.credentials_list.append(self)
	
	def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass

	@classmethod
	def display_credentials(cls,user_name):
		'''
		Class method to display the list of credentials saved
		'''
		user_credentials_list = []
		for credential in cls.credentials_list:
			if credential.user_name == user_name:
				user_credentials_list.append(credential)
		return user_credentials_list
				

	
	@classmethod
	def platform(cls, platform):
		'''
		Method that takes in a platform and returns a credential that matches that platform.
		'''
		for credential in cls.credentials_list:
			if credential.platform == platform:
				return credential

	@classmethod
	def copy_credential(cls,platform):
		'''
		Class method that copies a credential's info after the credential's site name is entered
		'''
		find_credential = Credential.platform(platform)
		return pyperclip.copy(platform.password)

   

    def __init__(self,email,platform,password):

      # docstring removed for simplicity

        self.email = email
        self.platform = platform
        self.password = password


class User:
    def __init__(self, user_email, user_name, user_password, user_current_job):
        self.email = user_email
        self.name = user_name
        self.password = user_password
        self.current_job_title = user_current_job

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = str(new_job_title)

    def get_user_info(self):
        print(f'User {self.name} is currently working as {self.current_job_title}')




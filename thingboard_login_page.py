from playwright.sync_api import Page as page

class Thingsboardloginpage:
    def __init__(self, page:page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username (email)") 
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button =   page.get_by_role("button", name="Login")
        
    def click_login(self):
        self.login_button.click()
            
    def enter_username(self, username: str):
        self.username_input.fill(username)
        
    def enter_password(self, password: str):  
        self.password_input.fill(password)
        
    def click_login(self):
        self.login_button.click()
        
        
          

    
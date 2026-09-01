import logging

from playwright.sync_api import Page

from models.BasePage import BasePage
logger_ui = logging.getLogger('ui')
# page.goto("/")
# expect(page.locator("section")).to_contain_text(
#     "With the help of the Hillel auto project, you will have the opportunity to get hands-on experience in manual testing.")
# page.get_by_role("button", name="About").click()
# expect(page.get_by_text("Keep track of your")).to_be_visible()
# LoginPage(page)login_in_to_account()
# expect(page.locator('//p[@class="alert alert-danger"]')).to_have_text("Wrong email or password")



class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path_to_this_page = '/'
        self.section_locator = page.locator("section")
        self.button_about_locator = page.get_by_role("button", name="About")
        self.some_text_locator = page.get_by_text("Keep track of your")
        self.button_sign_in_locator = page.get_by_role("button", name="Sign In")
        self.email_sign_in_tab_locator = page.get_by_label("Email")
        self.password_sign_in_tab_locator = page.get_by_label("Password")
        self.button_login_in_sign_in_tab_locator = page.get_by_role("button", name="Login")
        self.error_email_incr = page.locator('//div[@class="invalid-feedback"]/p')
        self.error_wrong_email = page.locator('p[class="alert alert-danger"]')

    def go_to(self):
        logger_ui.info("forward to main page")
        self.page.goto(self.path_to_this_page)


    def login_in_to_account(self, email_str: str, password_str: str, some_exp:str | None = None) -> None:
        '''
        This function is used to log in to your account.
        click button "Sign In", enter your email and password and click button "Login"
        :param email_str:
        :param password_str:
        :return:
        '''
        logger_ui.info("Click button 'Sign In'")
        self.button_sign_in_locator.click()
        logger_ui.info(f"Fill field Email with credential {email_str}")
        self.email_sign_in_tab_locator.fill(email_str)
        logger_ui.info(f"Fill field Password with credential {email_str}")
        self.password_sign_in_tab_locator.fill(password_str)
        if some_exp != 'email_problem':

            logger_ui.info('Click on button Enter to account')
            self.button_login_in_sign_in_tab_locator.click()



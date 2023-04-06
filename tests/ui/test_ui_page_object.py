from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    #Create an Object
    sign_in_page = SignInPage()

    #Open github page
    sign_in_page.go_to()

    #Login with wrong credentionals
    sign_in_page.try_login("page_object@gmail.com", "wrong_password")

    #Check that title name is correct
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    #close browser
    sign_in_page.close()
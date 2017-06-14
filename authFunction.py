from twython import Twython
import webbrowser as wb
from selenium import webdriver


def authenticate():

    app_key = " **YOUR APP KEY** "
    app_secret = " **YOUR APP SECRET** "

    twitter = Twython(app_key, app_secret)
    auth = twitter.get_authentication_tokens(callback_url='https://google.com')

    Oauth_Token = auth['oauth_token']
    Oauth_Token_Secret = auth['oauth_token_secret']

    driver = webdriver.Firefox(executable_path = " **YOUR PATH TO FIREFOX DRIVER** ")

    driver.get(auth['auth_url'])
    try:
        driver.find_element_by_name('session[username_or_email]').send_keys(" **YOUR USERNAME OR EMAIL** ")
        driver.find_element_by_name('session[password]').send_keys(" **YOUR PASSWORD** ")
        driver.find_element_by_id('allow').click()
    except NoSuchElementException:
        print("ERROR")
    time.sleep(5)
    ex = re.compile('(?<=oauth_verifier=)[a-zA-Z0-9]+')
    verifier = ex.findall(driver.current_url)
    driver.close()
    t = Twython(app_key, app_secret, Oauth_Token, Oauth_Token_Secret)
    final_step = t.get_authorized_tokens(verifier)
    tw = Twython(app_key, app_secret, final_step['oauth_token'], final_step['oauth_token_secret'])

    return tw

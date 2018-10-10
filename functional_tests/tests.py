from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn(row_text, [row.text for row in rows])

        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)
        self.assertIn('DJ NoBangers', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('DJ NoBangers', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a youtube link'
        )

        inputbox.send_keys('Eminem')
        inputbox.send_keys(Keys.ENTER)
        
        self.wait_for_row_in_list_table('1: Eminem')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('SWOG')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Eminem')
        self.wait_for_row_in_list_table('2: SWOG')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # original user
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('SWOG')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: SWOG')

        drew_list_url = self.browser.current_url
        self.assertRegex(drew_list_url, '/lists/.+')

        # new user - opens up new page
        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('SWOG', page_text)
        self.assertNotIn('Rihanna', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Kendrick Lamar')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Kendrick Lamar')

        user_list_url = self.browser.current_url
        self.assertRegex('/lists/.+')
        self.assertNotEqual(user_list_url, drew_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('SWOG', page_text)
        self.assertIn('Kendrick Lamar', page_text)




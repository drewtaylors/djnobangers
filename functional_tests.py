from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_generate_and_retrieve_youtube_list(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('DJ NoBangers', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('DJ NoBangers', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a youtube link'
        )

        inputbox.send_keys('Eminem')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        self.check_for_row_in_list_table('1: Eminem')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('SWOG')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Eminem')
        self.check_for_row_in_list_table('2: SWOG')

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

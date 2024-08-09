from playwright.sync_api import sync_playwright,expect
from src.login import handle_login
from src.config import Config
from tests.test_ui import test_chatbot_page_elements, test_file_query_page_elements, test_image_upload_page_elements

# Expected values
EXPECTED_CHATBOT_HEADER = "OTPP Secured ChatGPT"
EXPECTED_FILE_QUERY_HEADER = "File Query with ChatGPT"
EXPECTED_IMAGE_ANALYZER_HEADER = "Image Analyzer"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_context().new_page()
        handle_login(page)
        
        ## Testing the landing tab
        # Locating the header element
        header = page.locator("h1#otpp-chatgpt-homepage")
        # Fetching the text
        #actual_header_text = header.inner_text()

        # Verify the header text matches the expected value
        expect(header).to_have_text(Config.EXPECTED_TITLE)
        ## If completed we want to print success
        print(f"Test passed! Page title is: {Config.EXPECTED_TITLE}")

        tab_selectors = [
            'a[href="https://dna.dev.otpp.com/otpp-chatgpt-playground/Chatbot"]',        # Selector for Chatbot
            'a[href="https://dna.dev.otpp.com/otpp-chatgpt-playground/File_Query"]',     # Selector for File Query
            'a[href="https://dna.dev.otpp.com/otpp-chatgpt-playground/Image_Upload"]',   # Selector for Image Upload
            'a[href="https://dna.dev.otpp.com/otpp-chatgpt-playground/Translate_Files"]',# Selector for Translate Files
            'a[href="https://dna.dev.otpp.com/otpp-chatgpt-playground/Docu_Compare"]'    # Selector for Docu Compare
        ]

        pages_to_test = [
            (test_chatbot_page_elements, EXPECTED_CHATBOT_HEADER),
            (test_file_query_page_elements, EXPECTED_FILE_QUERY_HEADER),
            (test_image_upload_page_elements, EXPECTED_IMAGE_ANALYZER_HEADER)
        ]

        # Loop through each tab and perform the respective tests
        for i, (test_func, expected_header) in enumerate(pages_to_test):
            page.click(tab_selectors[i])
            ## Adding some wait time to allow the page to load
            page.wait_for_timeout(5000)
            ## Running the test function
            test_func(page, expected_header)

        browser.close()

if __name__ == "__main__":
    main()
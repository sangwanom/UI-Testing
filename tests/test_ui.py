import pytest
from playwright.sync_api import Page, expect
from src.login import handle_login
from src.config import Config

@pytest.fixture(scope="module")
def authenticated_page(page: Page):
    handle_login(page)
    return page


def test_chatbot_page_elements(authenticated_page: Page, EXPECTED_CHATBOT_HEADER):
    # Navigate to the chatbot page
    #authenticated_page.goto(Config.WEBSITE_URL + "/chatbot")
    
    # Locate the header element
    header = authenticated_page.locator("h2#otpp-secured-chatgpt")
    
    # Get the actual header text
    actual_header_text = header.inner_text()
    
    # Print the actual header text
    print(f"Actual header text: {actual_header_text}")
    
    # Verify the header text matches the expected value
    expect(header).to_have_text(EXPECTED_CHATBOT_HEADER)
    print(f"Test passed! Page title is: {EXPECTED_CHATBOT_HEADER}")
    
    # Locate the text box element
    text_box = authenticated_page.locator("textarea[data-testid='stChatInputTextArea']")
    
    # Verify the text box is present
    expect(text_box).to_be_visible()
    print("Test passed! Text box is visible.")



def test_file_query_page_elements(authenticated_page: Page, EXPECTED_FILE_QUERY_HEADER):
    # Locate the header element
    header = authenticated_page.locator("h3#file-query-with-chatgpt")
    
    # Get the actual header text
    actual_header_text = header.inner_text()
    
    # Print the actual header text
    print(f"Actual header text: {actual_header_text}")
    
    # Verify the header text matches the expected value
    expect(header).to_have_text(EXPECTED_FILE_QUERY_HEADER)
    print(f"Test passed! Page title is: {EXPECTED_FILE_QUERY_HEADER}")
    
    # Locate the input box element
    input_box = authenticated_page.locator("input[aria-label='Session Name']")
    
    # Verify the input box is present
    expect(input_box).to_be_visible()
    print("Test passed! Input box is visible.")
    
    # Locate the file upload component
    file_upload = authenticated_page.locator("input[data-testid='stFileUploaderDropzoneInput']")
    
    # Verify the file upload component is present
    #expect(file_upload).to_be_visible()
    #print("Test passed! File upload component is visible.")
    
    # Upload a sample file
    file_upload.set_input_files('Sample.pdf')
    print("Test passed! File uploaded successfully.")
    
    # Verify the uploaded file name appears in the specified element
    uploaded_file_name = authenticated_page.locator("div[data-testid='stFileUploaderFileName']")
    expect(uploaded_file_name).to_have_text("Sample.pdf")
    print("Test passed! Uploaded file name is visible.")



def test_image_upload_page_elements(authenticated_page: Page, EXPECTED_IMAGE_ANALYZER_HEADER):
    # Navigate to the image upload page
    # authenticated_page.goto(Config.WEBSITE_URL + "/image-upload")
    
    # Locate the header element
    header = authenticated_page.locator("h1#image-analyzer")
    
    # Get the actual header text
    actual_header_text = header.inner_text()
    
    # Print the actual header text
    print(f"Actual header text: {actual_header_text}")
    
    # Verify the header text matches the expected value
    expect(header).to_have_text(EXPECTED_IMAGE_ANALYZER_HEADER)
    print(f"Test passed! Page title is: {EXPECTED_IMAGE_ANALYZER_HEADER}")
    
    # Locate the file upload component
    file_upload = authenticated_page.locator("input[data-testid='stFileUploaderDropzoneInput']")
    
    # Verify the file upload component is present
    #expect(file_upload).to_be_visible()
    #print("Test passed! File upload component is visible.")
    
    # Upload a sample file
    file_upload.set_input_files('Sample.jpg')
    print("Test passed! File uploaded successfully.")
    
    # Verify the uploaded file name appears in the specified element
    uploaded_file_name = authenticated_page.locator("div[data-testid='stFileUploaderFileName']")
    expect(uploaded_file_name).to_have_text("Sample.jpg")
    print("Test passed! Uploaded file name is visible.")
    
    # Locate the input component for question
    input_component = authenticated_page.locator("input[aria-label='Enter your question:']")
    
    # Verify the input component is present
    expect(input_component).to_be_visible()
    print("Test passed! Input component is visible.")
    
    # Locate the submit button
    submit_button = authenticated_page.locator("div.row-widget.stButton button[data-testid='baseButton-secondary']")
    
    # Verify the submit button is present
    expect(submit_button).to_be_visible()
    print("Test passed! Submit button is visible.")
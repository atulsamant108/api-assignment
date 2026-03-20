from playwright.sync_api import Page


def test_ui_elements(page: Page):
    # Open website
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # 1. Click Radio Button
    page.locator("input[value='radio2']").click()
    assert page.locator("input[value='radio2']").is_checked()

    # 2. Select Dropdown
    page.select_option("#dropdown-class-example", "option2")
    selected = page.locator("#dropdown-class-example").input_value()
    assert selected == "option2"

    # 3. Enter Text in Input Box
    page.fill("#autocomplete", "India")
    assert page.locator("#autocomplete").input_value() == "India"

    # 4. Checkbox interaction
    page.locator("#checkBoxOption1").check()
    assert page.locator("#checkBoxOption1").is_checked()
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://docs.temenos.com/"
STATE_FILE = "storage_state.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(LOGIN_URL)

    print("=" * 60)
    print("Please login manually in the browser.")
    print("After successful login, press ENTER here.")
    print("=" * 60)

    input()

    context.storage_state(path=STATE_FILE)
    print(f"Session saved to {STATE_FILE}")

    browser.close()

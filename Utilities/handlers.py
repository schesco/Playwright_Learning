def handle_cookie_banner(page):
    try:
        page.click("button:has-text('Accept')", timeout=2000)
    except:
        pass

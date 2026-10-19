from playwright.sync_api import sync_playwright


def before_all(context):
    """
    Start Playwright and launch browser once for the test run.
    """
    context.playwright = sync_playwright().start()

    context.browser = context.playwright.chromium.launch(
        headless=True
    )


def before_scenario(context, scenario):
    """
    Create a fresh browser context and page for every scenario.
    """
    context.context = context.browser.new_context()

    context.page = context.context.new_page()

    context.page.set_viewport_size({
        "width": 1280,
        "height": 720
    })


def after_scenario(context, scenario):
    """
    Close the browser context after each scenario.
    """

    context.context.close()


def after_all(context):
    """
    Clean up Playwright resources.
    """
    context.browser.close()
    context.playwright.stop()
from behave import given, when, then
from playwright.sync_api import expect


@given('I am on the "Lägg till bok"-page and that I write the title and author of the book')
def step_fill_book_information(context):

    context.page.goto(
        "https://tap-vt26-testautomatisering.github.io/exam/"
    )

    context.book_title = "Unfamiliar scents: How to make perfume out or car tires"
    context.book_author = "Star"

    # Navigate to Add Book page
    context.page.locator("[data-testid='add-book']").click()

    # Fill out form
    context.page.locator(
        "[data-testid='add-input-title']"
    ).fill(context.book_title)

    context.page.locator(
        "[data-testid='add-input-author']"
    ).fill(context.book_author)


@when('I click the "Lägg till en ny bok"-button')
def step_click_add_book_button(context):

    context.page.locator(
        "[data-testid='add-submit']"
    ).click()


@then('the new book appears on the "Katalog"-page')
def step_verify_book_is_added(context):

    # Navigate to Catalog
    context.page.locator("[data-testid='catalog']").click()

    new_book = context.page.locator(
        f"text={context.book_title}"
    )

    expect(new_book).to_be_visible()

    expect(
        context.page.locator(
            f"text={context.book_author}"
        )
    ).to_be_visible()
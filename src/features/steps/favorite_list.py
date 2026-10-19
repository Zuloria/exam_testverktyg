from behave import given, when, then
from playwright.sync_api import expect


@given("that a book is visible in the catalog")
def step_book_visible(context):
    context.page.goto("https://tap-vt26-testautomatisering.github.io/exam/")

    context.book_text = 'Ormar på ett plan: En Python-berättelse'
    context.book_favorite_button = context.page.locator("[data-testid='star-Ormar på ett plan: En Python-berättelse']")

    expect(context.book_favorite_button).to_be_visible()


@when("I click on the book I want to add to favorite list")
def step_add_book_to_favorites(context):
    context.book_favorite_button.click()


@then("the book gets marked as a favorite and appears in the favorite list")
def step_verify_book_in_favorites(context):

    expect(context.book_favorite_button).to_have_class("star selected")

    context.page.locator("[data-testid='favorites']").click()

    favorite_books = context.page.locator(
        "[data-testid='fav-Ormar på ett plan: En Python-berättelse']"
    )

    expect(favorite_books).to_contain_text(
        context.book_text
    )

# -----------------------------------

@given("the book is visible in the catalog with a marking")
def step_book_already_favorited(context):
    context.page.goto("https://tap-vt26-testautomatisering.github.io/exam/")

    context.book_text = '"Ormar på ett plan: En Python-berättelse", Guido van Rossum'
    context.book_favorite_button = context.page.locator("[data-testid='star-Ormar på ett plan: En Python-berättelse']")
    context.book_favorite_button.click()

    expect(context.book_favorite_button).to_be_visible()


@when("I click on the book I want to remove")
def step_remove_book(context):
    context.book_favorite_button.click()


@then("the marking disappears from the book and the book is no longert visible on the favorite list")
def step_verify_book_removed(context):

    expect(context.book_favorite_button).not_to_have_class("star selected")

    context.page.locator("[data-testid='favorites']").click()

    favorite_books = context.page.locator(
        "[data-testid='book-list']"
    )

    expect(favorite_books).not_to_contain_text(
        context.book_text
    )

# -----------------------------------

@given("that there are a few books in the favorite list")
def step_favorites_exist(context):
    context.page.goto("https://tap-vt26-testautomatisering.github.io/exam/")

    book1 = context.page.locator("[data-testid='star-Ormar på ett plan: En Python-berättelse']")
    book2 = context.page.locator("[data-testid='star-The Pragmatic Procrastinator']")
    book3 = context.page.locator("[data-testid='star-Python för folk som hatar ormar']")

    book1.click()
    book2.click()
    book3.click()


@when('I click on the tab "Mina böcker"')
def step_open_favorites_tab(context):
    context.page.locator("[data-testid='favorites']").click()


@then("a clear list shows all books that have been previously marked")
def step_verify_favorite_list(context):

    favorites = context.page.locator(
        "[class='book']"
    )

    expect(favorites).to_have_count(3)
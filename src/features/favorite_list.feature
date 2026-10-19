Feature: Favorite list

  Scenario: Add a book to favorite list
    Given that a book is visible in the catalog
    When I click on the book I want to add to favorite list
    Then the book gets marked as a favorite and appears in the favorite list

  Scenario: Remove a book to favorite list
    Given the book is visible in the catalog with a marking
    When I click on the book I want to remove
    Then the marking disappears from the book and the book is no longert visible on the favorite list

  Scenario: View favorite list
    Given that there are a few books in the favorite list
    When I click on the tab "Mina böcker"
    Then a clear list shows all books that have been previously marked
Feature: Catalog

  Scenario: Add a new book to catalog
    Given I am on the "Lägg till bok"-page and that I write the title and author of the book
    When I click the "Lägg till en ny bok"-button
    Then the new book appears on the "Katalog"-page
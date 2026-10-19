# Theoretical questions

## 1. What is the difference between unit testing, integration testing, regression testing, and performance testing?

### Unit Testing

Tests a single component or function in isolation. 
The goal is to verify that a small piece of code works correctly.
Usually fast and automated.
Example: Testing a function that calculates the total number of favourite books.

### Integration Testing

Tests how multiple components work together.
The goal is to verify that communication between systems or modules functions correctly.
Example: Testing that a book added through the frontend is successfully stored in the backend database.

### Regression Testing

Ensures that previously working functionality still works after changes have been made.
The goal is to detect unintended side effects of new code.
Example: After implementing a "Favourite Books" feature, automated tests verify that adding books to the catalogue still works.

### Performance Testing

Measures how well a system performs under different levels of load.
The goal is to evaluate response times, scalability, and stability.
Example: Testing whether the application can handle thousands of books and many simultaneous users without slowing down.

## 2. Describe how TDD works

Test-Driven Development (TDD) is a development approach where tests are written before the actual code.

The process follows a cycle often called Red-Green-Refactor:

### Red 🟥

Write a test for a new feature.
Run the test and verify that it fails because the feature does not exist yet.

### Green 🟩

Write the minimum amount of code necessary to make the test pass.
Run the test again and verify that it succeeds.

### Refactor ⬛

Improve and clean up the code without changing its behaviour.
Run the tests again to ensure nothing broke.

This cycle is repeated continuously while developing the application.

## 3. Describe how BDD differs from TDD

Behaviour-Driven Development (BDD) is an extension of TDD that focuses on business requirements and user behaviour rather than technical implementation details. See table of contents below:

| **TDD** | **BDD** |
| ------------- | ------------- |
| Focuses on code correctness.  | Focuses on user behaviour and business value. |
| Tests are often written by developers.  | Scenarios can be written and understood by developers, testers, and stakeholders. |
| Uses unit and integration tests.  | Uses scenarios written in natural language. |
| Describes how the system should work technically.  |  Describes what the user should be able to do. |
| ------------- | ------------- |

In summary, TDD focuses on building the code correctly, while BDD focuses on building the correct behaviour for the user.

## 4. Imagine you are building a website similar to Läslistan, including both frontend and backend. Which types of tests would you use and why?

### Unit tests: 
Verify that individual functions and components work correctly in isolation. For example, testing a function that validates book information before it is saved.

### Integration tests:
Verify that different parts of the application work together correctly, such as the frontend communicating with the backend and the backend storing data in the database.

### End-to-end (E2E) tests:
Verify complete user workflows from start to finish. For example, adding a book, marking it as a favourite, and viewing it in the favourites list using Playwright.

### Regression tests:
Re-run existing automated tests after changes have been made to ensure that previously working functionality has not been broken.

I would choose these tests because they provide a good balance between test coverage and development effort. Unit tests quickly catch coding errors, integration tests ensure the different systems work together, and E2E tests verify that the application behaves correctly from the user's perspective. Regression testing helps ensure that new features do not introduce bugs into existing functionality
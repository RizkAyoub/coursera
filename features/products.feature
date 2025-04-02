Feature: Product Management

  Scenario: List all products
    Given I have products in the database
    When I visit the "Products Page"
    Then I should see a list of all products

  Scenario: Search by category
    Given I have products in the database
    When I search for products in the "Electronics" category
    Then I should see only products in the "Electronics" category

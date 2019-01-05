# Created by neev at 2018-12-23
@search_hotels
Feature: Search for Hotels
  As an
  # Enter feature description here
  Background:
    Given I am an authenticated user in the Home page

  Scenario Outline: A list of hotel is displayed
    When I search with inputing <city>,<checkin_date>,<checkout_date>,<family_size>
    Then The search results are displayed
    Examples:
      | city  | checkin_date | checkout_date | family_size     |
      | Paris | 24/12/2018   | 25/12/2018    | 2 Adult 0 Child |
      | Pune  | 01/01/2019   | 26/02/2019    | 1 Adult 1 Child |
    # Enter steps here
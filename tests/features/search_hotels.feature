@search_hotels
# Created by neev at 2018-12-23
Feature: Search for Hotels
  As an authenticated user
  I want to be able to input a given city,date, and family size
  So I can see a list of hotels matching my query

  # Enter feature description here
  Background:
    Given I am an authenticated user in the "hotels_page"

  @successful
  Scenario Outline: A list of hotel is displayed
    When The user enters the query data <city>,<checkin_date>,<checkout_date>,<family_size>
    Then The search results are displayed
    Examples:
      | city  | checkin_date | checkout_date | family_size |
      | Paris | 24/12/2018   | 25/12/2018    | 3_5         |
      | Pune  | 01/01/2019   | 26/02/2019    | 2_1         |
      |       | 01/01/2019   | 26/02/2019    | 0_5         |


  @unsuccessful
  Scenario: Incomplete search data
    When The user enters "incomplete" data
    Then The web page reloads with a warning message on missing the data
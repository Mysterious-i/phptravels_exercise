@login
# Created by neev at 2018-12-21
Feature: Login
  As a registered user
  I want to be able to login,
  So that I can see my account page

  Background:
    Given the phptravels Login page is displayed
#TODO: change this to refelect the use of commons
# successful/authenticated : Happy Paths
  @successful
  Scenario Outline: Successful Login
    When I input <email> and <password>
    Then I should be redirected to my "account_page"
    Examples:
      | email | password |
      | user@phptravels.com | demouser |

#TODO seperate logout scenario to a seperate feature file
  @logout
  Scenario: Logout successful
    Given I am logged in
    And I am an authenticated user in the "account_page"
    When I select the Logout option
    Then I should not be able to access my "account_page"


  @authenticated
  Scenario: Already logged in
    Given I am logged in
    And   I am an authenticated user in the "home_page"
    When  I select the Login option from the My Account drop down
    Then  I should be redirected to my "account_page"

# unsuccessful : Edge Cases
  @unsuccessful
  Scenario: Unsuccessful login
    When I input incorrect email or password
    Then I should see the Login page with a warning message



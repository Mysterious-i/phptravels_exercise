@login
# Created by neev at 2018-12-21
Feature: Login
  As an anonymous  user
  I want to login
  So that I see my account page

  Background:
    Given a web browser is on the "home_page"
    And the user selects the "Login" option from the "My Account" menu

#  @successful
#  \Scenario Outline: Successful Login
# \   When I input <email> and <password>
#   \ Then I should be redirected to my Account page
#    \Examples:
#     \ | email | password |
#      \| user@phptravels.com | demouser |
  @successful
  Scenario: successful login
    When  a web browser is on the "login_page"
    And   the user fills in the "email" field with a <registered_email_address>
    And   the user enters the "password"
    Then  the webpage reloads successfully to the "account page"


  @authenticated
  Scenario: already logged in
    Given the user is logged in
    Then  the webpage reloads successfully to the "account page"

  @authenticated
  Scenario:
    Given the user is logged in
    And   I am an authenticated user in the Home page
    When  I select the Login option from the My Account drop down
    Then  I should be redirected to my Account Page
# empty email/password field
  @unsuccessful
  Scenario: Unsuccessful Login
    When I input incorrect email or password
    Then I should see the Login page with a warning message

  # Error messages for the email field
  #___________________________________
  # Please include an '@' in the email address
  # Please enter a part following '@' <entered_email> is incomplete
  # a part followed by '@' should not contain the symbol <symbol> \\space punctuations such as: "(),:;<>@[\]
  # a part following '@' should not contain the symbol <symbol>


  # error_message : '.' is used at  a wrong position in <entered_email>
  # domain part of the email address ends with '.'

  # '@'is followed '.'

#Please enter an email address
  # hyphen -, the first or last character after in the domain part.
  # each label in the series of labels concatenated with dots to make up the hostname must be from 1 to 63 characters
    # domain part of the email address contains '..'
    # hostname made of labels of length => 64



  #
# Created by neev at 2019-01-29
@todo @password_recovery
Feature: Forgot Password
  # Enter feature description here
  As a registered user
  I want to be able to recover my password
  So that I can login
  # then we could refer the functionality to the login feature
  Background:
    Given the phptravels Login page is displayed

  @successful
  # TODO Happy Path
  Scenario: Successful password reset
    # Enter steps here
    # The user is a registered user
    When  the user submits a reset_password request by inputing a "valid" email
    Then  the web page alerts the user with the "successful_password_reset" message

@unsuccessful
# TODO Negative Path 1

  Scenario: User is not registered
    When  the user submits a reset_password request by inputing "valid_unregistered" email
    Then  the web page alerts the user with the email_not_found message

@invalid
# TODO Negative Path 2

  Scenario: Invalid email input
    # Enter steps here
    When  the user submits a reset_password request by providing an invalid_email
    Then  the web page alerts the user with a warning message
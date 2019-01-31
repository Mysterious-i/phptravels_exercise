@login
# Created by neev at 2018-12-21
# TODO BE CONSISTENT Change the 'I's to user
Feature: Login
  As a registered user
  I want to be able to login,
  So that I can see my account page

  Background:
    Given the phptravels Login page is displayed
# TODO: change this to refelect the use of commons
# successful/authenticated : Happy Paths
  @successful
  Scenario Outline: Successful Login
    When the user inputs valid <email> and <password>
    Then the web page reloads successfully to the account_page
    Examples:
      | email | password |
      | user@phptravels.com | demouser |

# TODO seperate logout scenario to a separate feature file
  @logout
  Scenario: Logout successful
    Given the user is logged in
    And   there is an authenticated user in the account_page
    When  the user selects the Logout option
    Then  the user should not be able to access the account_page


  @authenticated
  Scenario: Already logged in
    Given the user is logged in
    And   there is an authenticated user in the home_page
    When  the user selects the Login option from the My Account drop down
    Then  the web page reloads successfully to the account_page

# TODO parametize the warning message
# unsuccessful : Edge Cases
  @unsuccessful
  Scenario: Unsuccessful login
    When the user inputs incorrect email xor password
    Then the web page reloads the login_page with a warning message


# TODO : note comments below and clean
# Error messages for the email field
#  #___________________________________
#  # Please include an '@' in the email address
#  # Please enter a part following '@' <entered_email> is incomplete
#  # a part followed by '@' should not contain the symbol <symbol> \\space punctuations such as: "(),:;<>@[\]
#  # a part following '@' should not contain the symbol <symbol>
#
#
#  # error_message : '.' is used at  a wrong position in <entered_email>
#  # domain part of the email address ends with '.'
#
#  # '@'is followed '.'
#
##Please enter an email address
#  # hyphen -, the first or last character after in the domain part.
#  # each label in the series of labels concatenated with dots to make up the hostname must be from 1 to 63 characters
#    # domain part of the email address contains '..'
#    # hostname made of labels of length => 64
#
#
#
#  #Verify that User is able to Login with Valid Credentials
#
#  #Verify that User is not able to Login with invalid Username and invalid Password
#  #Verify that User is not able to Login with Valid Username and invalid Password
#  #Verify that User is not able to Login with invalid Username and Valid Password
#
#  #Verify that whether User is still logged in after series of actions such as sign in,
#  # close browser and reopen the application.
#
#  #Verify that the ways to retrieve the password if the User forgets the password
#  #Verify that User is redirected to Forgot password page when clicking on Forgot Password link
#  #Verify that User is redirected to Create an account page when clicking on Sign up / Create an account link
#
#  #Verify that validation message is displayed in case when User leaves Username or Password as blank
#  #Verify that validation message is displayed in case of exceeding the character limit of the Username and Password fields
#  #Verify that validation message is displayed in case of entering special character in the Username and password fields
#
#  #Verify that clicking on browser back button after successful login should not take User to log out mode
#  #Verify that clicking on browser back button after successful logout should not take User to logged in mode
#  #Verify that encrypted characters in “Password” field should not allow deciphering if copied
#  #Verify that User should be able to login with the new password after changing the password
#  #Verify that User should not be able to login with the old password after changing the password
#
#  #Verify whether the login form is revealing any security information by viewing page source
#  #Verify that there is a limit on the total number of unsuccessful login attempts (No. of invalid attempts should be
#  # based on business logic.
#  # Based on the business logic, User will be asked to enter captcha and try again or user will be blocked)
#  #
#  #Verify that the password is in encrypted form when entered
#  #Verify the password can be copy-pasted
#  #Verify that encrypted characters in “Password” field should not allow deciphering if copied
#  #Verify that User should be able to login with the new password after changing the password
#  #Verify that User should not be able to login with the old password after changing the password
#
#  #Verify that spaces should not be allowed before any password characters attempted
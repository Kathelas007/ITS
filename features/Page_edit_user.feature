# author: xmusko00

Feature: Navigation and functionality of Edit User page

  Background: Logged in as Admin, At least 2 Users exists


  Scenario: Edit User's username
    Given "Users" displayed
    When User's "Username" changed
    Then New "Username" displayed

  Scenario: Edit User's state
    Given "Users" displayed
    When User's "State" changed
    Then New "State" displayed

  Scenario Outline: Edit non-visible User info
    Given "Users" displayed
    When User's '<info>' changed
    Then "Users" displayed
    Examples:
      | info       |
      | First Name |
      | Last Name  |



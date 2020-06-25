# author: xmusko00

Feature: Navigation and functionality of Users page

  Background: Logged in as Admin, At least 2 Users exists

  Scenario Outline: Sort Users
    Given "Users" displayed
    When Sort by '<sort>'
    Then Users sorted by '<sort>'
    Examples:
      | sort       |
      | Status     |
      | Date Added |
      | Username   |

  Scenario: Add User
    Given "Users" displayed
    When "Add new" clicked
    Then  "Add User" displayed

  Scenario: Edit User
    Given "Users" displayed
    When "Edit" clicked
    Then  "Edit User" displayed

  Scenario: Delete no User
    Given "Users" displayed
    When "Delete" clicked
    Then "Users" displayed

#  Scenario: Delete User
#    Given "Users" displayed
#    When User is selected
#    And "Delete" clicked
#    Then  User is not displayed

  Scenario: Delete all User
    Given "Users" displayed
    When All Users selected
    And "Delete" clicked
    Then All Users Displayed




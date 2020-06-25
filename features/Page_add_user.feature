# xmusko00

Feature: Navigation and functionality of Add Users page

  Background: Logged in as Admin, At least 2 Users exists

  Scenario: Nothing filled out
    Given "Add User" displayed
    When Nothing filled out
    And Save
    Then "Add User" displayed

  Scenario: Cancel
    Given "Add User" displayed
    When Cancel
    Then Users still displayed

  Scenario Outline: One obligatory row missing
    Given "Add User" displayed
    And All obligatory filled out
    When Cleared one '<Obligatory>'
    And Save
    Then "Add User" displayed
    Examples:
      | Obligatory |
      | Username   |
      | First Name |
      | Last Name  |
      | Confirm    |
      | Password   |

  Scenario Outline: Wrong Password Confirm
    Given "Add User" displayed
    And All obligatory filled out
    When '<Password>' and '<Confirm>' filled out
    And Save
    Then "Add User" displayed
    Examples:
      | Password        | Confirm               |
      | aaaa            | aa                    |
      | secret password | secretpassword        |
      | s               | sssssssssssssssssssss |

  Scenario: Same User Name
    Given  User with "nickname" exists
    And "Add User" displayed
    When Create another User with "nickname"
    Then "Add User" displayed



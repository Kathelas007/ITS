# xmusko00

Feature: Log in User in different states
"""
  By logging in is checked whether User really exists in system and has access to it
  """

  Background: Admin and Enabled User exists

  Scenario: Admin Logs in
    Given Admin exists
    When Admin logs in
    Then Log in succeeded

  Scenario: Enabled User Logs in
    Given Enabled User exists
    When Enabled User logs in
    Then Log in succeeded

  Scenario: Enabled User Logs in with Admin password
    Given Enabled User exists
    When Enabled User logs in with Admin password
    Then Log in failed

  Scenario: Enabled User Logs in twice
    Given Enabled User logs in with Admin password
    When Enabled User logs in with his password
    Then Log in succeeded

  Scenario: User Logs in with old password
    Given Users password is changed
    When User Logs in with old password
    Then Log in failed

  Scenario: User Logs in with new user name
    Given Users user name is changed
    When User Logs in with new user name
    Then Log in succeeded

  Scenario: Disabled User Logs in
    Given User is disabled
    When Disabled User logs in
    Then Log in failed

  Scenario: Fake User Logs in
    Given Log in displayed
    When Fake User logs in
    Then Log in failed






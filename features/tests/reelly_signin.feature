
Feature: Reelly main page signin Test
  # Enter feature description here

  Scenario: Logged out user can Sign In
    Given Open Reelly signin page
    When Enter correct email and password combination
    When Click signin button
    Then Verify user is logged in
# Created by yusuf at 8/29/2024
Feature: Test for Main menu
  @smoke
  Scenario: Verify language can be changed to Russian
    Given Open Reelly signin page
    When Enter correct email and password combination
    When Click signin button
    Then Verify user is logged in
    When Click Main Menu nav link
    When Click EN language
    When Click RU language
    Then Verify language is changed
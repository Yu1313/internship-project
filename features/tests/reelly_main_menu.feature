# Created by yusuf at 8/29/2024
Feature: Test for Main menu web and mobile
  @smoke
#  Scenario: Verify language can be changed to Russian, web test
#    Given Open Reelly signin page
#    When Enter correct email and password combination
#    When Click signin button
#    Then Verify user is logged in
#    When Click Main Menu web nav link
#    When Click EN language
#    When Click RU language
#    Then Verify language is changed

  Scenario: Verify language can be changed to Russian, mobile test
    Given Open Reelly signin page
    When Enter correct email and password combination
    When Click signin button
    Then Verify user is logged in
    When Click Main Menu mobile nav link
    When Click EN language mobile dropdown
    When Click RU language mobile dropdown
    Then Verify language is changed
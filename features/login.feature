Feature: Login

  Scenario: Successful login
    Given I have username "user1" and password "pass123"
    When I log in
    Then I should see "Welcome user1"

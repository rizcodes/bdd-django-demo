Feature: Test REST API

  Background:
    Given I set sample API url

    Scenario: Base url validation
      When Send GET HTTP request to api url
      Then I received valid HTTP response code 200

    Scenario: GET users API validation
      Given I set GET api endpoint as "api/v1/users"
      When I send GET HTTP request
      Then I receive valid HTTP response code 200
        And Response BODY is not-empty

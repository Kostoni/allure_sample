Feature: testing feature

  Scenario: testing scenario
    Given we have behave installed
    When we send "get" request to "http://httpbin.org/ip"
    Then should be received correct status code
    And should be received response with correct structure

  Scenario Outline: testing outline scenario
    Given we have behave installed
    When we send "get" request to "http://httpbin.org/get" with parameter "<parameter>" and value "<value>"
    Then should be received correct status code
    And should be received response with correct structure
    And "args" block should contain parameter "<parameter>" and value "<value>"
    Examples: parameters
      | parameter | value |
      | foo-1     | bar-1 |
      | foo-2     | bar-2 |

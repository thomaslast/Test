
Feature: This test set is for basic haiku testing

Background:
Given the haiku object has been created

Scenario Outline: Expected to work, happy path...
When i pass the string <string> to the the haiku review code
Then the output will confirm that it is a haiku
And the syllable counts for the lines will be 5, 7, 5 respectively
Examples:
  | string                                                                      |
  | happy purple frog/eating bugs in the marshes/get indigestion                |


Scenario Outline: test the non-haiku strings
When i pass the string <string> to the the haiku review code
Then the output will confirm that it is NOT a haiku
And the syllable counts for the lines will be <syl> respectively
Examples:
  | string                                                            | syl     |
  | computer programs/the bugs try to eat my code/i will not let them | 5, 8, 5 |



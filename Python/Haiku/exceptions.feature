Feature: This test set is for exceptions

Background:
Given the haiku object has been created
  
Scenario Outline: pass some values that aren't accepted
When i pass the string <string> to the the haiku review code
Then the code will throw a value error
Examples:
  | string |
  | 12     |

Scenario Outline: pass an incorrect type
When i pass the integer <integer> to the the haiku review code
Then the code will throw a type error
Examples:
  | integer  |
  | 1234     |
  | 5678     |
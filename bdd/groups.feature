Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
  | name | header | footer |
  | name1 |header1 | footer1 |
  | name2 |header2 | footer2 |


Scenario Outline: Delete a group
  Given a non-empty group list
  Given a random group from the list
  When I delete group from the list
  Then the new group list is equal to the old list group without the deleted group

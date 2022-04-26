Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <email1>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname | lastname | email1 |
  | firstname1 |lastname1 | email1@test.test |
  | firstname2 |lastname2 | email1@add.test |


Scenario Outline: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete contact from the list
  Then the new contact list is equal to the old list contact without the deleted contact


Scenario Outline: Update a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I update the contact from the list with <firstname> and <middlename>
  Then the new contact list is equal to the old list with updated contact

  Examples:
  | firstname | middlename |
  | firstname432 | middlename234 |
  | firstname465 | middlename154 |
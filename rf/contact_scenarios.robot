*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures



*** Test Cases ***
Add new contact
    ${contact}=  New Contact  firstname1  middlename1
    ${old_list}=  Get Contact List
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  get from list  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${old_list}  ${new_list}

Update contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  get from list  ${old_list}  ${index}
    ${contact_data}=  New Contact  firstnameUpdate  middlenameUpdated
    Update Contact  ${contact}  ${contact_data}
    ${new_list}=  Get Contact List
    Contact Lists Should Be Equal  ${old_list}  ${new_list}
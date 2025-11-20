*** Settings ***
Resource        resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username               arto
    Set Password               abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username               ar
    Set Password               abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Registration Should Fail With Message    Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username               arto
    Set Password               short1
    Set Password Confirmation  short1
    Submit Registration
    Registration Should Fail With Message    Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    # salasana ei sisällä halutunlaisia merkkejä (vain kirjaimia)
    Set Username               arto
    Set Password               password
    Set Password Confirmation  password
    Submit Registration
    Registration Should Fail With Message    Password must contain numbers or special characters

Register With Nonmatching Password And Password Confirmation
    Set Username               arto
    Set Password               abcd1234
    Set Password Confirmation  abcd9999
    Submit Registration
    Registration Should Fail With Message    Password and password confirmation do not match

Register With Username That Is Already In Use
    # Test Setup luo käyttäjän kalle / kalle123
    Set Username               kalle
    Set Password               abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Registration Should Fail With Message    Username is already taken

*** Keywords ***
Set Username
    [Arguments]    ${username}
    Input Text     username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Set Password Confirmation
    [Arguments]    ${password_confirmation}
    Input Password    password_confirmation    ${password_confirmation}

Submit Registration
    Click Button   Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To Register Page

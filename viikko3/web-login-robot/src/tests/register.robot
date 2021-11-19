*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testib
    Set Password  testi1123
    Set Password Confirmation  testi1123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Fail with Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  testic
    Set Password  tes
    Set Password Confirmation  tes
    Submit Credentials
    Register Should Fail with Message  Password is too short 

Register With Nonmatching Password And Password Confirmation
    Set Username  testid
    Set Password  testi2123
    Set Password Confirmation  testi1234
    Submit Credentials
    Register Should Fail with Message  Password and password confirmation do not match 

*** Keywords ***
Create User And Go To Register Page
    Create User  testi  testi123
    Go To Register Page
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
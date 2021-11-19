*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle
    Set Password  kalle123
#    Submit Credentials
    Submit Logincredentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
#    Submit Credentials
    Submit Logincredentials
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  testi
    Set Password  testi123
#    Submit Credentials
    Submit Logincredentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

## Tämä laitettu toiselle sivulle
#Login Should Succeed
#    Main Page Should Be Open
#
## Tämä laitettu toiselle sivulle
#Login Should Fail With Message
#    [Arguments]  ${message}
#    Login Page Should Be Open
#    Page Should Contain  ${message}
#
## Tämä laitettu toiselle sivulle
#Submit Credentials
#    Click Button  Login
#
## Tämä on jo toisella sivulla
#Set Username
#    [Arguments]  ${username}
#    Input Text  username  ${username}
#
## Tämä on jo toisella sivulle
#Set Password
#    [Arguments]  ${password}
#    Input Password  password  ${password}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open

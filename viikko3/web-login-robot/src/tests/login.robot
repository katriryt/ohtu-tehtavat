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
    Submit Logincredentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
    Submit Logincredentials
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  testi
    Set Password  testi123
    Submit Logincredentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open

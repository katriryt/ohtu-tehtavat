*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testib
    Set Password  testi1123
    Set Password Confirmation  testi1123
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Registration
    Register Should Fail with Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  testic
    Set Password  tes
    Set Password Confirmation  tes
    Submit Registration
    Register Should Fail with Message  Password is too short 

Register With Nonmatching Password And Password Confirmation
    Set Username  testid
    Set Password  testi2123
    Set Password Confirmation  testi1234
    Submit Registration
    Register Should Fail with Message  Password and password confirmation do not match 

Login After Successful Registration
    Register Successfully
    Continue To Main Page And Log Out
    Login Successfully

Login After Failed Registration
    Register Unsuccessfully
    Move To Login Page
    Login Failure

*** Keywords ***
Create User And Go To Register Page
    Create User  testi  testi123
    Go To Register Page
    Register Page Should Be Open

Move To Login Page
    Click Link  Login
    Login Page Should Be Open
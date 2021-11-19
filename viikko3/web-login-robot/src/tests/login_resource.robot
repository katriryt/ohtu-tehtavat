*** Settings ***
Resource  resource.robot

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}

Submit Registration
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Submit Logincredentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Successfully
    Set Username  testid
    Set Password  testid123
    Set Password Confirmation  testid123
    Submit Registration
    Register Should Succeed

Continue To Main Page And Log Out
    Click Link  ohtu
    Click Button  Logout

Login Successfully
    Set Username  testid
    Set Password  testid123
    Submit Logincredentials
    Login Should Succeed

Register Unsuccessfully
    Set Username  testiz
    Set Password  testiasd2123
    Set Password Confirmation  testi1234as
    Submit Registration
    Register Should Fail with Message  Password and password confirmation do not match

Login Failure
    Set Username  testiz
    Set Password  testiasd2123
    Submit Logincredentials
    Login Should Fail With Message  Invalid username or password

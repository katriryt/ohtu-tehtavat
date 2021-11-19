*** Settings ***
Resource  resource.robot
Test Setup  Input New Command and Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testi1  testi1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  testi  testi123
    Output Should Contain  User with username testi already exists

Register With Too Short Username And Valid Password
    Input Credentials  te  testi123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  testi2  tes
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testi3  testestes
    Output Should Contain  Password should not contain only letters

*** Keywords ***
Input New Command and Create User
    Input New Command
    Create User  testi  testi123

*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${URL}              https://opensource-demo.orangehrmlive.com/
${USERNAME}         Admin
${PASSWORD}         admin123
${EXPECTED_TITLE}   OrangeHRM

*** Test Cases ***
Login Test
    [Documentation]    This test case logs into OrangeHRM and verifies the title of the page.
    [Tags]    ${BROWSER}
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Element Is Visible    name=username    10s
    Input Text    name=username    ${USERNAME}
    Input Text    name=password    ${PASSWORD}
    Click Button    xpath=//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
    Wait Until Title Contains    ${EXPECTED_TITLE}    10s
    ${ACTUAL_TITLE}=    Get Title
    Should Be Equal As Strings    ${ACTUAL_TITLE}    ${EXPECTED_TITLE}
    Close Browser

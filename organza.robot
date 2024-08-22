*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}              https://opensource-demo.orangehrmlive.com/
${BROWSER}          chrome
${USERNAME}         Admin
${PASSWORD}         admin123
${CHROMEDRIVER}     C:/Users/namratab/Documents/chromedriver-win64/chromedriver.exe
${EXPECTED_TITLE}   OrangeHRM

*** Test Cases ***
Login Test
    [Documentation]    This test case logs into OrangeHRM and verifies the title of the page.
    Open Browser    ${URL}    ${BROWSER}    executable_path=${CHROMEDRIVER}
    Wait Until Element Is Visible    name=username    10s
    Input Text    name=username    ${USERNAME}
    Input Text    name=password    ${PASSWORD}
    Click Button    xpath=//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
    Wait Until Title Contains    ${EXPECTED_TITLE}    10s
    ${ACTUAL_TITLE}=    Get Title
    Should Be Equal As Strings    ${ACTUAL_TITLE}    ${EXPECTED_TITLE}
    Close Browser

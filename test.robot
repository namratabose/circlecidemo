*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${url}  https://www.google.com/
${browser}  chrome

*** Test Cases ***
Google
   insidegoogle

*** Keywords ***
insidegoogle
   Open Browser  ${url}   ${browser}
   Maximize Browser Window
   Sleep  10
   Close Browser

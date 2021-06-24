*** Settings ***
Documentation                                      This is a basic test
Library                                            Selenium2Library

*** Variables ***
${url}                                              https://www.google.com
${browser}                                          chrome
${text}                                             xpath=//*[@id="lst-ib"]
${search_button}                                    css=input.lsb

*** Test Cases ***
User can open page
    [Documentation]                                 As a user I can open the google page
    open browser                                    ${URL}    ${BROWSER}
    wait until page contains                        ${url}
    close browser

User fill in the Search text box
    [Documentation]                                 The user search 'Test Definition'
    open browser                                    ${URL}    ${browser}
    wait until page contains                        ${URL}
    input text                                      ${text}  Test Definition
    click element                                    ${search_button} 
    wait until page contains                        Test
    sleep     5s
    Close Browser
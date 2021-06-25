*** Settings ***
Documentation                                      This is a basic test
Library                                            SeleniumLibrary


*** Variables ***
| ${GoogleBaseUrl} | https://www.google.com/
| ${GoogleForm} | css=form[name=f]
| ${GoogleQuery} | css=input[name=q]

*** Test Cases ***
Google search
    Open Google Search
    Do Google Search  test

*** KeyWords ***
Open Google Search
    Open browser  ${GoogleBaseUrl}
    Wait until element is visible  ${GoogleQuery}

Do Google Search
    [Arguments]    ${term}
    Log to console  Do Google Search with "${term}"
    input text  ${GoogleQuery}  ${EMPTY}
    input text  ${GoogleQuery}   ${term}
    submit form
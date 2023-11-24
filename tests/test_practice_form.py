from selene import browser, be, have


def test_registration():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Sergey')
    browser.element('#lastName').should(be.blank).type('Dobrovolskiy')
    browser.element('#userEmail').should(be.blank).type('dobrovolskiy@qa.ru')
    browser.element('#gender-radio-1').should(have.value('Male')).with_(click_by_js=True).click()
    browser.element('#userNumber').should(be.blank).type('1002003040')
    # TODO date of birth
    ...


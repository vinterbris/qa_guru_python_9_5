from selene import browser, be, have, command


def test_registration():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Sergey')
    browser.element('#lastName').should(be.blank).type('Dobrovolskiy')
    browser.element('#userEmail').should(be.blank).type('dobrovolskiy@qa.ru')
    browser.element('#gender-radio-1').should(have.value('Male')).with_(click_by_js=True).click()
    browser.element('#userNumber').should(be.blank).type('1002003040')
    browser.element('#dateOfBirthInput').click()

    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select>option').should(have.size(12))
    browser.all('.react-datepicker__month-select>option').should(have.exact_texts('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))
    browser.element('.react-datepicker__month-select>option[value="0"]').click()

    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select>option').should(have.size(201))
    browser.all('.react-datepicker__year-select>option').first.should(have.exact_text('1900'))
    browser.all('.react-datepicker__year-select>option')[-1].should(have.exact_text('2100'))
    browser.element('.react-datepicker__year-select>option[value="1990"').perform(command.js.scroll_into_view)
    browser.element('.react-datepicker__year-select>option[value="1990"').click()

    browser.element('#subjectsContainer').click().type('Math').press_enter()
    # browser.element('.subjects-auto-complete__control').click()
    # browser.element('.subjects-auto-complete__value-container').type('Math').press_enter()
    browser.element('#hobbies-checkbox-1').with_(click_by_js=True).click()
    browser.element('#hobbies-checkbox-2').with_(click_by_js=True).click()
    browser.element('#hobbies-checkbox-3').with_(click_by_js=True).click()
    browser.element('#currentAddress').should(be.blank).type('Test Address')
    ...


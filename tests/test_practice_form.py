import os

from selene import browser, be, have, command


def test_registration():
    browser.open('/automation-practice-form')
    # name, email, gender, phone
    browser.element('#firstName').should(be.blank).type('Sergey')
    browser.element('#lastName').should(be.blank).type('Dobrovolskiy')
    browser.element('#userEmail').should(be.blank).type('dobrovolskiy@qa.ru')
    browser.element('#gender-radio-1').should(have.value('Male')).with_(click_by_js=True).click()
    browser.element('#userNumber').should(be.blank).type('1002003040')
    # date of birth
    browser.element('#dateOfBirthInput').click()
    # month
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select>option').should(
        have.exact_texts('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                         'October', 'November', 'December'))
    browser.element('.react-datepicker__month-select>option[value="0"]').click()
    # year
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select>option').should(have.size(201))
    browser.all('.react-datepicker__year-select>option').first.should(have.exact_text('1900'))
    browser.all('.react-datepicker__year-select>option')[-1].should(have.exact_text('2100'))
    browser.element('.react-datepicker__year-select').type("2100").press_enter()
    # day
    browser.element('.react-datepicker__day--002').click()
    # subjects
    browser.element('#subjectsContainer').click()
    browser.element('#subjectsInput').type('m')
    browser.all('.subjects-auto-complete__option').should(have.exact_texts(
        'Maths', 'Chemistry', 'Computer Science', 'Commerce', 'Economics'))
    browser.all('.subjects-auto-complete__option').first.click()
    browser.element('#subjectsInput').type('m')
    browser.all('.subjects-auto-complete__option').should(have.exact_texts(
        'Chemistry', 'Computer Science', 'Commerce', 'Economics'))
    browser.all('.subjects-auto-complete__option').first.click()
    # browser.element('#subjectsInput').type('Math').press_enter()
    # browser.element('#subjectsInput').type('English').press_enter()

    # hobbies
    browser.element('#hobbies-checkbox-1').with_(click_by_js=True).click()
    browser.element('#hobbies-checkbox-2').with_(click_by_js=True).click()
    browser.element('#hobbies-checkbox-3').with_(click_by_js=True).click()
    # picture
    browser.element("#uploadPicture").send_keys(os.path.abspath("../resources/nolan.jpg"))
    # current address
    browser.element('#currentAddress').should(be.blank).type('Test Address')
    # state and city
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('#react-select-3-option-0').click()
    # browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    # browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').perform(command.js.click)
    browser.all('.table>tbody>tr>td:last-child').should(have.exact_texts(
        'Sergey Dobrovolskiy', 'dobrovolskiy@qa.ru', 'Male', '1002003040', '02 January,2100', 'Maths, Chemistry',
        'Sports, Reading, Music', 'nolan.jpg', 'Test Address', 'NCR Delhi'))
    browser.element('#closeLargeModal').perform(command.js.scroll_into_view).click()

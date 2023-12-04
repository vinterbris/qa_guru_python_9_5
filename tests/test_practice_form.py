import os

from selene import browser, be, have, command


def test_registration():
    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').should(be.blank).with_(type_by_js=True).type('Sergey')
    browser.element('#lastName').should(be.blank).with_(type_by_js=True).type('Dobrovolskiy')
    browser.element('#userEmail').should(be.blank).with_(type_by_js=True).type('dobrovolskiy@qa.ru')
    # browser.element('[name=gender][value=Male]').with_(click_by_js=True).click()
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
    browser.element('#userNumber').should(be.blank).with_(type_by_js=True).type('1002003040')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('January')
    browser.element('.react-datepicker__year-select').type("2100")
    browser.element('.react-datepicker__day--002').click()

    browser.element('#subjectsContainer').click()
    browser.element('#subjectsInput').type('m')
    browser.all('.subjects-auto-complete__option').should(have.exact_texts(
        'Maths', 'Chemistry', 'Computer Science', 'Commerce', 'Economics'))
    browser.all('.subjects-auto-complete__option').first.click()
    browser.element('#subjectsInput').type('m')
    browser.all('.subjects-auto-complete__option').should(have.exact_texts(
        'Chemistry', 'Computer Science', 'Commerce', 'Economics'))
    browser.all('.subjects-auto-complete__option').first.click()

    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Sports')).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Reading')).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Music')).click()

    browser.element("#uploadPicture").send_keys(os.path.abspath("../resources/nolan.jpg"))

    browser.element('#currentAddress').should(be.blank).type('Test Address')

    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.text('NCR')).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.text('Delhi')).click()

    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.all('.table>tbody>tr>td:last-child').should(have.exact_texts(
        'Sergey Dobrovolskiy', 'dobrovolskiy@qa.ru', 'Male', '1002003040', '02 January,2100', 'Maths, Chemistry',
        'Sports, Reading, Music', 'nolan.jpg', 'Test Address', 'NCR Delhi'))
    browser.element('#closeLargeModal').perform(command.js.scroll_into_view).click()

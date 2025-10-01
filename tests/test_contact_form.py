from pages.contact_page import ContactPage
import os

def get_local_url():
    import os
    if os.getenv("GITHUB_ACTIONS") == "true":
        return "http://127.0.0.1:8000/contact_form.html"
    else:
        path = os.path.abspath("contact_form.html")
        return "file://" + path


def test_positive_contact_form(driver):
    page = ContactPage(driver, get_local_url())
    page.open()

    page.fill_form(
        name="Антон Дебеляк",
        email="test@example.com",
        message="Привет, это автотест!"
    )
    page.submit()

    success_text = page.get_success_text()
    assert "Форма успешно отправлена!" in success_text

def test_negative_contact_form_empty_email(driver):
    page = ContactPage(driver, get_local_url())
    page.open()

    page.fill_form(
        name="Антон Дебеляк",
        email="",  # обязательное поле не заполнено
        message="Сообщение"
    )
    page.submit()

    error_text = page.get_email_error()
    assert "Введите корректный email" in error_text

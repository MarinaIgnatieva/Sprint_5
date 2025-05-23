#форма регистрации
NAME_REGISTRATION = "//label[text()='Имя']/parent::div/input"
EMAIL_REGISTRATION = "//label[text()='Email']/parent::div/input"
PASSWORD_REGISTRATION = "//input[@type='password']"
BUTTON_REGISTRATION = "//button[text()='Зарегистрироваться']"

#форма входа в аккаунт
LOGIN_MAIN_PAGE_BUTTON = "//button[text() = 'Войти в аккаунт']"
LOGIN_FORM = "//h2[text()='Вход']"
LOGIN_FORM_EMAIL = "//label[text()='Email']/parent::div/input"
LOGIN_FORM_PASSWORD = "//input[@name='Пароль']"
LOGIN_FORM_BUTTON = "//button[text()='Войти']"

#кнопка Оформить заказ
BUTTON_PLACE_ORDER = "//button[text()='Оформить заказ']"

#кнопка Личный кабинет
BUTTON_PERSONAL_ACCOUNT = "//a[@href='/account']"

#кнопка Войти в форме регистрации
BUTTON_LOGIN_REGISTRATION = "//a[@href='/login']"

#кнопка Войти в форме восстановления пароля
BUTTON_LOGIN_FORGOT_PASSWORD = "//a[@href='/login']"

#ссылка на Профиль
LINK_PROFILE = "//a[@href='/account/profile']"

#кнопка Выйти в Личном Кабинете
BUTTON_LOGOUT = "//button[text()='Выход']"

#кнопка Конструктор
BUTTON_CONSTRUCTOR = "//p[text()='Конструктор']"

#логотип Stellar Burgers
LOGO_STELLAR_BURGERS = "//div[@class='AppHeader_header__logo__2D0X2']/a"

#секция "булки"
SECTION_BUNS = "//span[text()='Булки']/parent::div"

#секция "соусы"
SECTION_SAUCE = "//span[text()='Соусы']/parent::div"

#секция "начинки"
SECTION_FILLINGS = "//span[text()='Начинки']/parent::div"
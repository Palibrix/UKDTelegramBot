# favorites
from bot.storage.placeholders import buttons

SELECT_FROM_LIST = 'Виберіть зі списку:'
NOT_PICKED_ANY_GROUP = 'Схоже, ви не додали жодної групи в обрані!'
NOT_FOUND_OR_DELETED = 'Схоже, даний розклад не було знайдено або його було видалено'

# menu
PICK_OPTION = 'Будь ласка, виберіть бажану опцію'
TIP = 'От халепа! Схоже, ви ще не додали основний розклад! Підказати як це зробити?'

# schedule buttons
MENU = '<em><strong>Головне меню!</strong></em>'
TIP_ANSWER = f'Натисніть кнопку <b><i>{buttons.FIND_SCHEDULE}</i></b>.\n\nЗдійсніть пошук за групою чи викладачем/-кою. ' \
             'Щойно розклад відобразиться, оберіть пункт <b><i>"Позначити основним"</i></b>.\n\n' \
             'Виконавши ці кроки, обраний розклад з\'явиться в даній панелі ' \
             'наступного разу при натисканні кнопки <b><i>"Мій розклад"</i></b>.'

# search
SEARCH_PARAMS = 'Будь ласка, оберіть параметри пошуку розкладу'
CHOOSE_ROLE = 'Вкажіть роль'
GROUP_FULL_NAME = 'Надішліть повну назву шуканої групи'

PICK_SPECIALITY = 'Оберіть спеціальність'
PICK_SPECIALITY_FAIL = 'Будь ласка, оберіть спеціальність'

TEACHER_SELECT = "Оберіть викладача із запропонованих"
TEACHER_INITIALS = "Введіть П.І.Б. викладача/-ки"
TEACHER_INITIALS_FAIL = "Будь ласка, введіть П.І.Б. викладача/ки"
TEACHER_NOT_FOUND = 'Вчителя не знайдено! Спробуйте ще раз!'

COURSE_NUM = '%s курс'
COURSE_SELECT = 'Оберіть курс'
COURSE_SELECT_FAIL = 'Будь ласка, оберіть курс'

GROUP_SELECT = 'Оберіть групу'
GROUP_SELECT_FAIL = 'Будь ласка, оберіть групу'
GROUP_NOT_FOUND = 'Групу не знайдено! Спробуйте ще раз!'

# settings
SETTINGS_INFO = 'Тут ви можете змінювати ваші налаштування'
YOUR_SETTINGS = 'Ваші поточні налаштування:'

# start
WELCOME = """Привіт та ласкаво просимо! 🤗
Моя мета - полегшити пошук розкладу для всіх відвідувачів Університету Короля Данила!
Для отримання детальнішої інформації про мою роботу, можете перейти на сторінку допомоги /help.\n
Отож, розпочнімо!⚡️"""

#    UTILS
# render_schedule
NO_CLASSES = '\nЦього дня у вас немає пар, хорошого відпочинку!'
BREAK_LINE = '_' * 35
CLASSES_QUANTITY = f'{BREAK_LINE}\n' \
                   '<code>Загальна кількість пар: %s </code>'
SEARCH_NAME = '<code><u>%s</u></code>'
DAY_AND_DATE = '<code><u>%s, %s</u></code>'
LESSON = '%s <b>%s</b> | %s\n' \
         '<i>%s</i> (%s)\n' \
         '<pre>%s</pre>\n'
# schedule_utils
YOUR_SCHEDULE = 'Ваш розклад:'

# help text
HELP = """
<i><b>Функціонал</b></i>:
Для пошуку розкладу за критеріями потрібно обрати <i>спеціальність, курс та групу</i>.
Для пошуку розкладу за назвою групи потрібно ввести <i>повну назву вашої групи</i> (наприклад "ІПЗс-21-2").
Для пошуку розкладу за викладачем/кою потрібно ввести <i>П.І.Б. викладача/ки</i> (наприклад "Іваненко Іван Іванович", або ж просто "Іваненко").
<i>За замовчуванням бот видає розклад на сьогоднішній день.</i>

Щоб позначити розклад основним, знайдіть бажаний розклад на натисніть кнопку <b>"Позначити основним"</b> на клавіатурі нижче.
Тепер цей розклад буде доступним за одним лише натиском кнопки <b>"Мій розклад"</b> в головному меню. Також, якщо в налаштуваннях обрано <b>"Надсилати розклад зранку: Так"</b>, о 6:00 ранку ви отримуватимете повідомлення з цим розкладом на сьогодні.

Щоб додати розклад в обрані, знайдіть бажаний розклад та натисніть кнопку <b>"В обране"</b> на клавіатурі нижче.
Тепер цей розклад можна буде швидко знайти в списку обраних, що доступний за кнопкою <b>"Обрані"</b> в головному меню.


<i><b>Команди</b></i>:
/start - перезапуск бота;
/cancel - скасування дії;
/settings - налаштування бота;
/help - виклик допомоги;


При виявленні будь-яких технічних несправностей, просимо звертатись на пошту tel.admin@ukd.edu.ua.
<code>З найкращими побажаннями, 
розробники.</code>
"""


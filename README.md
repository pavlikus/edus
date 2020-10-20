# Обучающий сайт на выбранную тему
## Описание

### Главная страница
* Показывает доступные курсы для регистрации.

### Страница курсов
* Показывает все курсы.
* После авторизации суперюзера в меню доступна кнопка добавления курса.

### Конечная страница курса
* Показывает полную информацию о курсе.
* После авторизации суперюзера в меню доступны кнопки добавления, правки и удаления курса.
![Admin Buttons](media/images/admin_buttons.png)

### Страница преподавателей
* Показывает всех преподователей.

### Конечная страница преподователя
* Показывает полную информацию о преподавателе и читаемых курсах.

## Цель:
### В этой самостоятельной работе мы тренируем умения:

1. Создавать проект на django
2. Использовать django orm
3. Использовать механизм миграций
4. Разрабатывать модели для предметной области
5. Использовать cbv
6. Тестировать проекты на django
7. Генерировать тестовые данные

### Данное домашнее задание это первая часть проекта "Обучающий сайт" рассчитано на материал следующих занятий:

* Django settings, orm, админка, миграции, superuser
* Django cbv, шаблоны, наследование шаблонов
* Django forms. Наследование моделей. Абстрактные классы и proxy в django
* Тестирование django приложений. Тестирование моделей. mixer для создания фейковых данных
* Django. фабрики: mixer, Factory Boy, Faker

## Задача:
1. Создать проект "Обучающий сайт". По нему будут задания до конца курса, сначала backend потом frontend. Рекомендуется создать для проекта отдельный репозиторий
2. Придумать тему (чему будем обучать на сайте) можно любую какая вам наиболее интересна.
3. Примерное описание работы сайта:
Сайт будет похож на OTUS + дополнительный функционал в зависимости от темы. На нем будут курсы, категории, преподаватели, занятия, расписание, ... + доп. функционал в зависимости от выбранной темы.
Будут как классические страницы (созданные на сервере), так и api в json
4. Необходимо создать модели данных (Преподаватель, студент, курс, расписание, ...). Можно не все сразу, а какую то часть и постепенно добавлять новые
5. Создать связи между моделями
6. Сделать миграции
7. Настроить стандартную админку
8. Заполнить базу некоторыми реальными или тестовыми данными
В проекте добавляем страницы (у нас будут как классические страницы с рендерингом на сервере, так и api с рендерингом на клиенте)
9. Пока добавляем классические страницы с рендерингом на сервере
10. Добавить страницу для просмотра списка курсов
11. Добавить страницу для просмотра одного курса
12. Добавить страницы для создания, удаления, редактирования курса
13. Дополнительно можно добавить любой полезный функционал
14. Так же в проект рекомендуется добавить необходимые базовые и включенные шаблоны
Рекомендуется все view делать с использованием CBV
15. По возможности покрыть проект тестами, как методов моделей, так и view (для генерации фейковых данных удобно использовать фабрики)

16. Сдать сайт в виде ссылки на репозиторий (базу используем пока тестовую sqlite) сам файл с базой в репозиторий рекомендуется не заливать

17. Рекомендуется добавить в репозиторий файл readme с кратким описанием работы системы

18. Если будет возможность запуска в docker будет вообще супер

## Критерии оценки:
### Задание считается выполненным, когда:
* в проекте есть минимум 2 модели данных,
* проходят миграции (python manage.py migrate),
* минимум 2 модели (не считая модель пользователя), добавлены в стандартную админку,
* есть рабочие страницы для списка курсов и одного курса - 10 баллов

### Дополнительно:
* Есть readme с кратким описанием работы системы 1 балл
* Есть 3 модели 2 балла
* Есть 4 и более моделей 1 балл
* Есть страницы:
    * Создания 1 балл
    * Редактирования 1 балл
    * Удаления 1 балл
* Во всех view используется CBV 2 балла
* Есть хотя бы 1 тест методов моделей 1 балл
* Есть хотя бы 1 тест для view 1 балл


Итого: 10 + 1 + 2 + 1 + 1 + 1 + 1 + 2 + 1 + 1 = 20 максимум баллов
Рекомендуем сдать до: 08.07.2020

TODO:
- [X] Eсть минимум 2 модели данных,
- [X] Проходят миграции (python manage.py migrate),
- [X] Минимум 2 модели (не считая модель пользователя), добавлены в стандартную админку,
- [X] Есть рабочие страницы для списка курсов и одного курса
- [X] Есть readme с кратким описанием работы системы 1 балл
- [X] Есть 3 модели 2 балла
- [X] Есть 4 и более моделей 1 балл
- [X] Есть страницы(Создания 1 балл, Редактирования 1 балл, Удаления 1 балл)
- [X] Вовсех view используется CBV 2 балла
- [X] Есть хотя бы 1 тест методов моделей 1 балл
- [X] Есть хотя бы 1 тест для view 1 балл

## Добавить страницу с контактами и отправкой сообщения с помощью очереди задач
## Цель:
### В этой самостоятельно работе мы тренируем умения работает с очередями задачи. Для того чтобы использовать их в своей работе
1. Добавить страницу с контактами
2. На странице создать форму для отправки сообщения
3. После отправки формы отправлять письмо на почту администратора (о том что нам отправили сообщение)
4. И второе письмо на почту указанную в форме (о том что мы приняли его сообщение)
5. Отправку писем реализовать через очередь задач (Можно использовать rq или любую другую библиотеку)
## Критерии оценки:
### Задание считается выполненным, когда:
* реализована работа с очередями задач - 6 баллов

## Дополнительно:
* Есть страница для отправки нам письма 2 балла
* Письмо отправляется нам 1 балл
* Письмо отправляется клиенту 1 балл

Итого 6 + 2 + 1 + 1 = 10 максимум баллов
Рекомендуем сдать до: 26.07.2020

TODO:
- [X] Есть страница для отправки нам письма 2 балла,
- [X] Письмо отправляется нам 1 балл,
- [X] Письмо отправляется клиенту 1 балл,

## Создание rest-api для сайта
## Цель:
### В этой самостоятельной работе мы тренируем умения:
1. Проектировать и писать rest-api
2. Добавлять систему прав и авторизацию
3. Использовать GraphQL
4. Писать тесты для api
### Данное домашнее задание это часть api проекта "Обучающий сайт" рассчитано на материал следующих занятий:
* Введение в django-rest-framework
* Django-rest-api авторизация
* API. GraphQL и его реализация в Python. GraphQL и Django
* Тестирование django приложений. Тестирование views. Тестирование api

1. Продолжаем работать с проектом
2. Подумать для каких частей сайта будет rest api
3. Реализовать rest api (можно использовать django-rest-framework или любые другие средства)
4. Продумать систему прав
5. Какие права будут по умолчанию для всех страниц?
6. Какие права будут для каждой страницы?
7. Дописать свои права если они требуются
8. Подумать систему авторизации
9. Реализовать систему авторизации
10. Рекомендуется в систему авторизации включить авторизацию по токену (из за большой популярности) и реализовать возможность создания токена для конкретного пользователя (например в личном кабинете)
12. С помощью GraphQL создать схему, которая позволяет получать одновременно курсы, преподавателей и всех студентов записанных на курс
13. Покрыть api тестами (чем больше тем лучше)

## Критерии оценки:
### Задание считается выполненным,
* когда есть api хотя бы для 1-ой модели,
* есть система прав и система авторизации
* Схема GraphQL позволяет одновременно получать вместе 2 из 3. Хотя бы курсы+преподаватели, курсы+студенты - 10 баллов

## Дополнительно:
* Есть api более чем для одной модели 3 балла
* Есть авторизация по токену 2 балла
* У пользователя есть возможность создавать/пересоздавать токен 1 балл
* Схема GraphQL позволяет получать одновременно курсы, преподавателей и всех студентов записанных на курс в одном запросе - 3 баллов
* Есть хотя бы 1 тест для api - 1 балл


Итого 10 + 3 + 2 + 1 + 3 + 1 = 20 баллов
Рекомендуем сдать до: 05.08.2020


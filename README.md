# Django Home — Интернет-магазин на Django 4

[![Django](https://img.shields.io/badge/Django-4.x-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Проект включает всё необходимое для реального онлайн-магазина: каталог, категории, детальные страницы товаров, поиск, корзину с AJAX, оформление заказа, личный кабинет, кэширование и оптимизацию запросов.

## Основные возможности

- Адаптивная вёрстка (Bootstrap + кастомный CSS)
- Каталог товаров с категориями и подкатегориями
- Детальная страница товара (фото, описание, цена)
- Поиск по товарам + фильтры
- Пагинация каталога
- Корзина (хранится в сессиях, обновление без перезагрузки через AJAX)
- Оформление заказа (модели Order / OrderItem)
- Личный кабинет пользователя + история заказов
- Регистрация, авторизация, сброс пароля
- Кэширование страниц и queryset'ов (включая cache mixin)
- Оптимизация запросов (select_related, prefetch_related)
- Админ-панель с удобным управлением товарами / заказами

## Технологии

- **Backend:** Python 3.8+, Django 4.x
- **Frontend:** HTML, CSS (Bootstrap), JavaScript (AJAX / fetch)
- **База данных:** SQLite (для разработки) → легко переключается на PostgreSQL
- **Дополнительно:** Django sessions, caching framework, class-based views

## Быстрый запуск

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/PythonHubStudio/Django-4-course-Home.git
cd Django-4-course-Home

# 2. Создайте виртуальное окружение и активируйте
python -m venv venv
source venv/bin/activate          # Linux / macOS
# или
venv\Scripts\activate             # Windows

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Выполните миграции
python manage.py migrate

# 5. (Опционально) Создайте суперпользователя
python manage.py createsuperuser

# 6. Запустите сервер
python manage.py runserver

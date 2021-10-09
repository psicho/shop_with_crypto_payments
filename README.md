# Магазин с оплатой в Ethereum

### Установка зависимостей и запуск проекта
    Для работы проекта необходимо установить следующие зависимости:
      pip install django==3.2.7
      pip install Pillow==8.3.2
      pip install Celery==4.1.0
      pip install rabbitmq==0.2.0
      pip install flower==0.9.2
      pip install infura==0.2.1
      pip install requests-cache
      pip install requests

    
## Запуск проекта

1. Запустить Django сервер:
   python manage.py runserver
2. Запуск брокера RabbitMQ:
   rabbit-server


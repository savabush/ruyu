# RU-YU

Палитры цветов. REST API реализован на Django 5.0.4. Аутентификация - JWT, сервис интеграции для получения наименований цветов [colorapi](https://www.thecolorapi.com/). 

# Запуск

1. Скопируйте файл `.env.example` в `.env`
2. Запустите приложение через консоль
```bash
docker-compose up -d
```
3. Создайте супер-пользователя
```bash
docker-compose exec web python manage.py createsuperuser 
```
4. Готово! Можно пользоваться:
- [Админка](http://0.0.0.0:8000/admin/)
- [Swagger](http://0.0.0.0:8000/api/schema/swagger-ui/#/)
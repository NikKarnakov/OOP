# MACHINE (ГОРОСКОПЫ)

## Цель проекта

Создать модель, которая будет генерировать гороскопы на основе данных с рамблера. Данная модель связывается с телеграм ботом. И в итоге получается готовый продукт: MACHINE (ГОРОСКОПЫ) - телеграм бот, который по знаку зодиака пользователя будет отправлять ему случайно сгенерированный гороскоп.

## Дальнейшие перспективы проекта

Обучение модели на выборке в 2, 3 раза больше, чем сейчас. А также генерирование гороскопов уже по разным дням недели, возможно, создание сайта со следующей рекламой "Нейросеть с вероятностью 99,9 процентов сгенерирует Вам гороскоп на ближайший день, неделю, месяц, год!!! Век новых технологий настал!"

![Снимок экрана (35)](https://user-images.githubusercontent.com/115116690/212328517-864c73a6-a869-40f9-9f39-6e9b09aaf158.png)

Проект выполнили: 

| ФИО  | ГРУППА  | ЗАДАЧИ |
| :------------ |:---------------:| -----:|
| Карнаков Н.Д.      | М8О-206Б-21 | Модель, обучение |
| Шляхтина И.И.      | М8О-206Б-21        |   Телеграм бот |
| Беспалов В.А. | М8О-206Б-21        |    Модель, докер |

## Этапы реализации проекта

1. Выбор набора данных и реализация модели
2. Парсинг сайта и получение датасета
3. Обучение модели на основе датасета
4. Реализация telegram-бота
5. Сборка docker-образа генератора и telegram-бота

## Описание

Проект включает себя две составляющие: реализиация дообучения модели и реализация телеграм-бота с его инфраструктурой.

## Паттерн, который был использован (АДАПТЕР)

Ссылка на исходный код: [adapter](bot_telegram/handlers/users/adapter.py)

### Neural_network.ipynb

Данный файл содержит реализацию дообучения модели gpt2-small от Сбербанка на датасете, состоящим из гороскопов.

### bot_telegram/handlers/users/gen.py

В данной программе реализована функция message_handler, ожидающая сообщение (ввод знака зодиака после обнаружения '/gen', запускающей файл gen.py). Дальше происходит генерация гороскопа через предзагруженную модель. 

### bot_telegram/data/config.py

Данный файл содержит конфиг бота (токен бота и id администраторов).

### bot_telegram/app.py

Данный файл содержит реализацию бота, из него подключаются все папки.

## Использование

1. Необходимо скачать полученную обученную модель `Neural_network.ipynb` и поместить в папку с ботом.
2. Заполнить информацию о боте в `bot_telegram/.env` токеном бота.
3. Собрать docker-образ из `Dockerfile`:

```
docker build --pull --rm -f "Dockerfile" -t test "."
```

4. Запустить docker-контейнер:

```
docker run -it test
```

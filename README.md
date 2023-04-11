# Описание
Синхронизирует данные в Google Sheet с БД

# Как подключить таблицу?
1. Создать проект в консоли Google Cloud Platform и включить для него API Google Таблицы и получить json для аутентификации
2. Переименовать файл в credentials.json и перенести в корень проекта
3. Заполнить файл .env:
  - SPREADSHEET_ID (id таблицы – обычно есть в ссылке на нее: ...google.com/spreadsheets/d/**YEhCnCsW_hEqFfLw-nnyU28-TIx**/)
  - DB_NAME
  - DB_USER
  - DB_PASSWORD
  - DB_HOST
  - DB_PORT

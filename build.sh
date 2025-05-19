#!/usr/bin/env bash

# 1. Установить зависимости (если нужно)
pip install -r requirements.txt

# 2. Перейти в папку Vue и собрать фронтенд
cd frontend || exit
npm install
npm run build

# 3. Вернуться и скопировать результат сборки в Django
cd ..
rm -rf static/assets
cp -r Vue_real_estate_sale-main/dist/assets static/

# 4. Копировать index.html в templates
mkdir -p templates
cp Vue_real_estate_sale-main/dist/index.html templates/index.html

python manage.py collectstatic --noinput

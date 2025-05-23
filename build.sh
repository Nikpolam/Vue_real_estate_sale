#!/usr/bin/env bash

# 1. Установить Python зависимости
pip install -r requirements.txt

# 2. Установить Node-зависимости и собрать Vue
npm install
npm run build

# 3. Копировать ассеты в Django static/
rm -rf static/assets
mkdir -p static/assets
mkdir -p real_estate_backend/api/templates
cp -r dist/assets/* static/assets/
cp dist/index.html templates/index.html

# 4. Собрать статику Django
python manage.py collectstatic --noinput

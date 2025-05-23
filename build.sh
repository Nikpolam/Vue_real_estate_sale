#!/usr/bin/env bash

# 1. Установить Python зависимости
pip install -r requirements.txt

# 2. Установить Node-зависимости и собрать Vue
npm install
npm run build

# 3. Копировать ассеты в Django static/
mkdir -p static/assets
mkdir -p real_estate_backend/api/templates
cp -r dist/assets/* static/assets/
cp dist/index.html real_estate_backend/api/templates/index.html

# 4. Собрать статику Django
python manage.py collectstatic --noinput

FROM python:3.9

# copy everything from this folder to docker
COPY . .

# install python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# внутри приложения
# CMD ['gunicorn', '-b', '0.0.0.0:8080', 'app:app']
# выход из контейнера - связь с внешним миром
# EXPOSE 6666
ENTRYPOINT ['python']
CMD ['bot.py']




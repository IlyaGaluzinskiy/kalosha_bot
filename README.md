## kalosha_bot - telegram bot that recommends musical artist
Attention - bot works best with the artists that perform in english

### In order to get a recommendation from the bot:
- send a musical artist name you are interested in;
- bot will check if the artist exists in Genius database, correct spelling if required and using Genius API will upload lyrics in order to suggest similar artists;
- recommendation system of the bot was built using Sklearn TF-IDF (TfidfVectorizer), cosine similarity that allow to find artist with similar lyrics;
- bot will show top 5 similar artists.
- you are also able to check what artists bot currently knows - /list

### Available commands:
- /start - restart;
- /about - describes the purpose of the bot and shows available commands;
- /list - list of 20 random artists that are in bot database.

### In order to start bot on your machine:
- Create a bot with a help of @BotFather in telegram
- Clone repository
- Create '.env' file in main directory which will contain your Genius API TOKEN, telegram bot TOKEN and your telegram user id(you can check it with a help of @ShowJsonBot).
- Install required libraries (pip install -r requirements.txt)
- Run 'bot.py' to start the bot

## kalosha_bot - telegram bot, для рекомендации музыкальных исполнителей
Внимание - бот лучше всего работает при подборе музыкантов, чьи тексты песен написаны на английском языке

### Для получения рекомендации от бота необходимо:
- отправить боту имя интересующего вас исполнителя;
- бот проверит существует ли данный исполнитель в библиотеке Genius, загрузит тесты песен данного исполнителя с использование Genius Api для подбора похожих исполнителей;
- рекомендательная система бота построена с использованием TF-IDF и позволяет находить артистов, имеющих схожие тексты песен;
- бот отобразит топ 5 наиболее похожих артистов;
- есть возможность проверить исполнителей, которые уже имеются в базе бота, используя команду - /list

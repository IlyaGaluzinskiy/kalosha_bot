## kalosha_bot - telegram bot that recommends musical artist
Attention - bot works best with the artists that perform in english

In order to get a recommendation from the bot:
- send a musical artist name you are interested in;
- bot will check if the artist exists in Genius database and using Genius API will upload lyrics in order to suggest similar artists;
- recommendation system of the bot was build using TF-IDF and allows to find artist that have similar lyrics;
- bot will show top 5 similar artists;
- you are also able to check what artists bot currently knows - /list 

## kalosha_bot - telegram bot, для рекомендации музыкальных исполнителей
Внимание - бот лучше всего работает при подборе музыкантов, чьи тексты песен написаны на английском языке

Для получения рекомендации от бота необходимо:
- отправить боту имя интересующего вас исполнителя;
- бот проверит существует ли данный исполнитель в библиотеке Genius, загрузит тесты песен данного исполнителя с использование Genius Api для подбора похожих исполнителей;
- рекомендательная система бота построена с использованием TF-IDF и позволяет находить артистов, имеющих схожие тексты песен;
- бот отобразит топ 5 наиболее похожих артистов;
- есть возможность проверить исполнителей, которые уже имеются в базе бота, используя команду - /list
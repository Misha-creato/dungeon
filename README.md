# dungeon

Консольная игра, в которой игрок уничтожает случайных монстров в подземелье с сохранением прогресса и прокачкой уровня. 
Игра при запуске проверяет файла сохранения. Если файл сохранения присутствует и содержит корректные данные, у игрока имеется возможность продолжить предыдущую игру, в противном случае только начать новую. У игрока есть уровень, опыт, опыт до следующего уровня и энергия. В процессе игрок встречает монстров со случайным шансом на победу. Он может либо вступить в бой, либо сбежать. Энергия расходуется при каждом ходе, опыт увеличивается в случае победы. При поражении есть возможность сразиться с монстром еще раз. Побежденные монстры сохраняются в список игрока.

## Установка и запуск

1. Скачайте проект с репозитория.
2. Установите зависимости: `pip install -r requirements.txt`.
3. Запустите проект: `python main.py`.

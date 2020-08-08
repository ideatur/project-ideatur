># project-ideatur
>Educational front-end project for IT-Step school and friends
>
>Список гілок (branches)
>git branch
>
>Переключитись в іншу гілку (branch)
>git chechkout <branchname>
>
>Створити собі гілку для роботи
>git checkout <основна гілка>, для фронтенда це UI
>git pull
>git branch <своя нова гілка>
>git checkout <своя нова гілка>
>git push #створення гілки на гітхаб
>
>Зберегти зміни і надіслати зміни в гілку
>git add . #додати всі змінені файли в індекс
>git commit -m "message" #додати коміт
>git push origin <branch_name> #закинути на гітхаб
>
>Синхронізувати зміни з головної гілки в свою робочу гілку.
>Рекомендується робити після кожного змерженого PR в головну гілку, що б на стаціонарній машині завжди була остання актуальна версія.
>Для чого: запобігає конфліктам при наступних Pull Requests з робочої гілки в головну гілку.

>Зберегти зміни і надіслати зміни в гілку (див. попередній пункт)
>git checkout UI
>git pull
>git checkout <своя гілка>
>git merge UI # мерж UI собі в гілку

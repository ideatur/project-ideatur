<h1>project-ideatur
>Educational front-end project for IT-Step school and friends
>
>Список гілок (branches)<br>
>git branch
>
>Переключитись в іншу гілку (branch)<br>
>git chechkout <branchname><br>
>
>Створити собі гілку для роботи<br>
>git checkout <основна гілка>, для фронтенда це UI<br>
>git pull<br>
>git branch <своя нова гілка><br>
>git checkout <своя нова гілка><br>
>git push #створення гілки на гітхаб<br>
>
>Зберегти зміни і надіслати зміни в гілку<br>
>git add . #додати всі змінені файли в індекс<br>
>git commit -m "message" #додати коміт<br>
>git push origin <branch_name> #закинути на гітхаб<br>
>
>Синхронізувати зміни з головної гілки в свою робочу гілку.<br>
>Рекомендується робити після кожного змерженого PR в головну гілку, що б на стаціонарній машині завжди була остання актуальна версія.<br>
>Для чого: запобігає конфліктам при наступних Pull Requests з робочої гілки в головну гілку.<br>
>
>Зберегти зміни і надіслати зміни в гілку (див. попередній пункт)<br>
>git checkout UI<br>
>git pull<br>
>git checkout <своя гілка><br>
>git merge UI # мерж UI собі в гілку

***
Author:   by Umbrellla777 <br/>
Telegram: [@Umbrellla777](https://t.me/Umbrellla777) <br/>
VK:       [@Umbrellla777](https://vk.com/umbrellla777) <br/>
[Мой канал для обсуждения](https://t.me/umbrellla777bot) <br/>
***
> [!NOTE]
> Проект развивается и ведётся работа над добавлением новых команд, следите за новостями.
# Umbrellla777-bot
Python скрипт для красивого оформления текста в Telegram

# Установка Termux
Termux - это бесплатный эмулятор терминала с открытым исходным кодом для Android <br/>
Есть несколько вариантов установки приложения: <br/>
* Установка через [F-Droid](https://f-droid.org)
  > Устанавливаете приложение с [сайта](https://f-droid.org). <br/>
  > Открываете и ищете в поиске Termux. <br/>
  > Устанавливаете и запускаете. <br/>
  > Готово. <br/>
* Установка с [4PDA](https://4pda.to/forum/index.php?showtopic=741456)
  > Выбираете и устанавливаете нужную вам версию. <br/>
  > Готово. <br/>
# После установки Termux
1) Переходим на https://my.telegram.org/  <br/>
Вводим свой номер телефона в поле **Your Phone Number**  <br/>
После того, как придёт код подтверждения, вводим его в поле **Confirmation code**  <br/>
И нажимаем кнопку **Sign In**  <br/>

2) Создаём своё "приложение"
В поле **App Tittle** пишем **Ваше название**  <br/>
В поле **Short** Name пишем **Ваше название**  <br/>
В **Platform** выбираем **Other**  <br/>
И нажимаем кнопку **Create Application**  <br/>

3) Копируем куда-либо **api_id** и **api_hash**  <br/>
**api_id** это такие цифорки типа **1234567**  <br/>
**api_hash** это и буквы и цифры типа **123sdf123sdf234...**  <br/>

4) Устанавливаем приложение **Termux**.  <br/>

5) Открываем Termux и вставляем в него следующую команду:
```bash
pkg update -y && pkg install -y git && pkg install -y python3 && git clone https://github.com/Umbrellla777/Umbrellla777-bot && cd Umbrellla777-bot && chmod +777 install.sh && sh install.sh && cd ..
```
Коротко объясню команды:
```bash
pkg update -y # Проверка наличия обновлений пакетов и их установка
pkg install -y git # Установка системы контроля версий git
pkg install -y python3 # Установка интерпретатора ЯП python 3
git clone https://github.com/Umbrellla777/Umbrellla777-bot # После установки git, загружем репозиторий со скриптом
cd Umbrellla777-bot # Переходим в директорию со скриптом
chmod +777 install.sh # Даем все права файлу в т.ч на исполнение
sh install.sh # Запуск скрипта
cd .. # Выход в из директории Umbrellla777-bot
```

После того, как вставили команду жмём Enter (новая строка).  <br/>
Пойдет установка скрипта.   <br/>
Если вы всё сделали правильно, то увидите надписи:  <br/>
***[Завершено] Установка успешна завершена!"***  <br/>
***[Запуск] Выполните ./start api_id api_hash"***

6) Запуск скрипта.  <br/>
В Termux пишем **./start ваш_api_id ваш_api_hash**  <br/>
Пример команды **./start 1234567 1d12d45fg56g563**  <br/>
И жмём Enter. Через пару секунд вас попросят еще раз ввести свой номер, вводим, получаем код, вводим код и всё!  <br/>

При успешном запуске будет полоска:  <br/>
***[PROFILE: Моё_Имя | Id: 123345567 | Uname: @MyUserName]***

7) Команды  <br/>
Весь список команд после запуска бота вызывается командой .help <br/>

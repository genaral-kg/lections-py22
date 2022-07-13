GIT-Распределеная система контроля версий
Это система для отслеживенеи и ведение историй изменений вашихфайлов или проеекта 

Репеозиторий - хранилище ваших файлов, которые вы отслеживаете при помощи гита ,и их изменений.

Команды Git:

1. git init - она создает новый гит репозиторий локально на вашем пк, создаст она в той директории где вы запускаете эту командую

2.git add - когда мы создаем и изменяем файлы б то при помощи это команды мы загружаем вссе изменеиния промежуточное место хранилище

git add<file_name>
git add.->все в текущей директории

3. git commit - как только мы достигаем определенного момента вразработки б то мы сохраняем и комментируем все наши измениения в репозиторийю
(фиксация изменений в репо.)

git commit -m '<comment>'

   git --version

   sudo apt install git
   
   git config --global user.name "general-kg"
   git config --global user.email "kutmanvip01@gmail.com"
   git config --list
   
   
   cd .ssh
   ls


   git status-проверка статуса
   On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   gitlessons/commands.py
	new file:   linux/commands.txt
	new file:   linux/kutman2.txt


4.  git remote add-жто команда для того чтобы связать ваш локаьный репозиторий с удаленным репозиторием(репо в гитхабе)

    git remote add<название подключение><ссыла на репозиторий >
   
    git remote add origin <url>
   
5.  git push -после измениения при помощи этой команды мы отправляем наши измениения в файлах на удаленный репозиторий.

    git push <origin><название ветки(main)>
    
    git push origin main
     
     
     
1. git init 
2. git branch -M main (переимменовывам главную ветку с master на main)
3. git add .
4. git commit -m 'comment' (все добавлено в локальный репо)
5. git remote add origin <url>
6. git push origin main

////////////////////


git add .
git commit -m 'comment'
git push origin main
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        

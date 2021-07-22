# Backup to telegram as free cloud backup service
the way I want to do it is:
create fat like catalog of all files on client computer
send all files to telegram and create online catalog of existing files
the catalog would enable syncs of all files

## Main initiative is to have one media library synced between many clients
later on I think to make it into a full cloud backup solution

## additional ideas:



from here it is the forked readme + trunslation
# Backup files to telegram
The program is designed for backup copies (RK) of small files and directories. 
PK files are sent to one or several telegram chats, which are specified in the configuration file. 

- RK catalogs 

If a catalog is specified in the configuration file, then it will be placed in a zip archive (LZMA) before being sent to telegrams. 
After archiving, the hash (sha256) the sum of the directory archive will be calculated, this hash sum will be used in the future to determine the changes in the directory. For RK directories, you can specify the filters "include": "pattern" or "exclude": "pattern", regular expressions (regexp) 
 - PK files
of RK files are used as pattern. At startup, the program calculates the hash sum of the file if it differs from the one written in configuration file, the file is considered changed and must be sent to telegrams to the corresponding chats. 
If the "archive": "true" option is specified in the configuration file, the files will be archived before sending.

Run / Run: python ./run.py ./mybkp.conf 

Recommended for use with the task scheduler.









# Backup files to telegram
Программа предназначена для резервной копии (РК) не больших файлов и каталогов.
Файлы РК пересылаются в один или несколько чатов телеграм, которые указаны в файле конфигурации.

- РК каталогов

Если в файле конфигурации указан каталог, то перед отправкой в телеграм он будет помещен в архив zip (LZMA).
После архивации, будет посчитана хеш (sha256) сумма архива каталога, эта хеш сумма и будет использоваться в дальнейшем для определения изменений в каталоге.
Для РК каталогов можно указать фильтры "include": "pattern" или "exclude": "pattern", в качестве pattern используются регулярные выражения (regexp)

- РК файлов

При запуске, программа считает хеш сумму файла, если она отличается от той что записана в файле конфигурации, файл считается измененным и подлежит отправке в телеграм в соответствующие чаты.
Если в файле конфигурации указана опция "archive": "true" то файлы перед отправкой будут архивироваться.

Запуск / Run:
- python ./run.py ./mybkp.conf

Рекоммендуется использовать совместно с планировщиком заданий.



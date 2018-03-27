# Тестовый сценарий с отчетом Allure

## Пререквезиты
1. Python 3
2. Модули из requirements.txt:
    * allure-behave==2.3.2b1
    * behave==1.2.6
    * jsonschema==2.6.0
    * requests==2.18.4
3. Allure

## Установка

### Установка пакетов для Python

```bash
pip install -r /path/to/requirements.txt
```

### Установка Allure

For Windows, Allure is available from the Scoop commandline-installer.

To install Allure, download and install Scoop and then execute in the Powershell:

```bash
scoop install allure
```
Also Scoop is capable of updating Allure distribution installations. To do so navigate to the Scoop installation directory and execute

```bash
\bin\checkver.ps1 allure -u
```
This will check for newer versions of Allure, and update the manifest file. Then execute

```bash
scoop update allure
```

## Использование 

Для выполнения тестов и генерации результатов в необходимом для Allure виде выполнить

```bash
behave -f allure_behave.formatter:AllureFormatter -o result
```

Для генерации отчета на основе результатов прогона тестов выполнить

```bash
allure serve result/
```

Как результат сгенерируется отчет Allure, поднимется http сервер на свободном порту, и откроется дефолтный браузер с этим отчетом
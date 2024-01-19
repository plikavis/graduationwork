## Проект UI и API автотестов TestRail.com 


<!-- Технологии -->
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

<!-- Тест кейсы -->
### Что проверяем
UI-тесты:
* Создание нового проекта 
* Создание проекта с некорректными данными и сообщение об ошибке
* Редактирование проекта и сообщение об успешном обновлении данных
* Работу всех вкладок на странице проекта  
* Создание нового тест-кейса
* Создание нового тест-кейса с пустым названием и сообщение об ошибке
* Редактирование тест-кейса и сообщение об успешном обновлении данных

API-тесты: 
## [Documentation](https://support.testrail.com/hc/en-us/articles/7077792415124-Projects)
* Работу системы под пользователем с полными правами и правами на чтение
* Отправку запросов 
* Тело ответа (реализована проверка на json-схему)
* Код ответа
* Тело ответа (реализована проверка на json-схему)
* Данные в ответе 

### <img width="5%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/008_plika_vis_testrail/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.
![This is an image](images/screenshot/jenkins_run.png)

<!-- Allure report -->

### <img width="5%" title="Allure Report" src="images/logo/allure_report.png"> Allure report
### [Report](https://jenkins.autotests.cloud/job/008_plika_vis_testrail/)
##### После прохождения тестов, результаты можно посмотреть в Allure отчете, ссылка так же содержится  на Jenkins
![This is an image](images/screenshot/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshot/allure_graph.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](images/screenshot/allure_video.png)

##### Видео прохождение теста
![This is an image](images/screenshot/video.gif)

<!-- Allure TestOps -->

### <img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/2291/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](images/screenshot/allure_testops_dashboard.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](images/screenshot/allure_testops_suites.png)



<!-- Telegram -->

### <img width="5%" title="Telegram" src="images/logo/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](images/screenshot/telegram.png)

# Учебные проекты Яндекс.Практикум по основам Data Science

В этом репозитории собраны все учебные проекты, выполненные в рамках курса Яндекс.Практикум "Специалист по Data Science". В результате было создано множество качественных моделей машинного обучения, неоднократно был произведен полноценный исследовательский анализ действительных данных.

# Таблица для навигации по проектам

| Проект  | Описание | Используемые библиотеки |
| ------------- | ------------- | ------------- |
| **[Музыка больших городов](big_cities_music)** | Сравнение предпочтений пользователей Яндекс.Музыки из Москвы и Санкт-Петербурга в зависимости от времени (утро и вечер) и дня недели (понедельник, среда, пятница)  | *pandas* |
| **[Исследование надёжности заёмщиков](research_of_borrower_reliability)** | Заказчик — кредитный отдел банка. Нужно разобраться, влияет ли семейное положение и количество детей клиента на факт погашения кредита в срок. Входные данные от банка — статистика о платёжеспособности клиентов. Результаты исследования будут учтены при построении модели кредитного скоринга — специальной системы, которая оценивает способность потенциального заёмщика вернуть кредит банку.  | *pandas <br> pymystem3* | 
| **[Исследование объявлений о продаже квартир](research_of_apartment_listings)** | Имеются данные сервиса Яндекс Недвижимость — архив объявлений о продаже квартир в Санкт-Петербурге и соседних населённых пунктах за несколько лет. Нужно определить рыночную стоимость объектов недвижимости. Это позволит построить автоматизированную систему: она отследит аномалии и мошенническую деятельность. | *pandas <br> matplotlib* | 
| **[Определение перспективного тарифа для телеком-компании](tariff_for_telecom_company)** | Провести анализ данных компании «Мегалайн» — федерального оператора сотовой связи, при помощи которых коммерческий департамент сможет скорректировать рекламный бюджет, в зависимости от того, какой тариф приносит больше денег. | *pandas <br> matplotlib <br> numpy <br> scipy* | 
| **[Прогнозирование популярного продукта для интернет-магазина по продаже компьютерных игр](forecasting_popular_game)** | Используя исторические данные о продажах компьютерных игр, оценки пользователей и экспертов, жанры и платформы, выявить закономерности, определяющие успешность игры | *pandas <br> matplotlib <br> scipy* | 
| **[Рекомендация тарифов](tariff_recommendation)** | Оператор мобильной связи «Мегалайн» планирует разработать систему для анализа поведения клиентов, использующих архивные тарифы. Цель проекта - предложить пользователям новые тарифы «Смарт» или «Ультра».  | *pandas <br> numpy <br> scikit-learn*  | 
| **[Прогнозирование оттока клиентов из банка](customer_churn)**  | Из банка стали уходить клиенты. Каждый месяц. Немного, но заметно. Банковские маркетологи посчитали: сохранять текущих клиентов дешевле, чем привлекать новых. Нужно спрогнозировать, уйдёт клиент из банка в ближайшее время или нет. Предоставлены исторические данные о поведении клиентов и расторжении договоров с банком.  | *pandas <br> matplotlib <br> numpy <br> scikit-learn <br> warnings* | 
| **[Выбор локации для скважины](well_location_Selecting)** | Предоставлены пробы нефти в трёх регионах. Характеристики для каждой скважины в регионе уже известны. Нужно построить модель для определения региона, где добыча принесёт наибольшую прибыль.  | *pandas <br> matplotlib <br> scikit-learn <br> scipy <br> numpy <br> warnings* | 
| **[Восстановление золота из руды](recovery_of_gold_from_ore)**  | Создание прототипа модели машинного обучения для компании, занимающейся разработкой решений для промышленных предприятий с целью оптимизировать производственные процессы и предотвратить запуск предприятий с убыточными характеристиками.   | *pandas <br> matplotlib <br> seaborn <br> numpy <br>warnings* | 
| **[Защита персональных данных клиентов](protection_personal_data)**  | Обеспечение защиты данных клиентов страховой компании «Хоть потоп» путем разработки метода их преобразования, который затруднит восстановление персональной информации. Основная цель заключается в обеспечении безопасности данных при сохранении качества моделей машинного обучения, без необходимости подбора наилучшей модели. | *pandas <br> scikit-learn <br> numpy* |

# Исследование надёжности заёмщиков

## Описание проекта
Заказчик — кредитный отдел банка. Нужно разобраться, влияет ли семейное положение и количество детей клиента на факт погашения кредита в срок. Входные данные от банка — статистика о платёжеспособности клиентов.

Результаты исследования будут учтены при построении модели кредитного скоринга — специальной системы, которая оценивает способность потенциального заёмщика вернуть кредит банку.

## Описание данных
- `children` — количество детей в семье
- `days_employed` — общий трудовой стаж в днях
- `dob_years` — возраст клиента в годах
- `education` — уровень образования клиента
- `education_id` — идентификатор уровня образования
- `family_status` — семейное положение
- `family_status_id` — идентификатор семейного положения
- `gender` — пол клиента
- `income_type` — тип занятости
- `debt` — имел ли задолженность по возврату кредитов
- `total_income` — ежемесячный доход
- `purpose` — цель получения кредита
---
# Вывод
**В ходе исследования получили следующую информацию:**

- если у клиента `есть дети`, то процент невозврата кредита в срок выше на **`0.7 - 1,1%`** по отношению к бездетным клиентам;
- если клиент `состоит в браке`, то процент невозврата кредита в срок меньше на **`1.4%`** по отношению к "одиноким" клиентам;
- у клиентов с `"высокой ЗП"` процент невозврата кредита в срок меньше по сравнению с остальными, а у клиентов со `"средней ЗП"` процент невозврата кредита в срок выше чем у остальных (на **`0,7%`** больше по отношению к клиентам с `"низкой ЗП"` и на **`1,6%`** больше по отношению к клиентам с `"высокой ЗП"`);
- так же стало ясно, что самый высокий процент не возврата кредита в срок у клиентов, чья цель - `"автомобиль"` и `"образование"`, а для клиентов которые берут кредит для `"недвижимости"` и `"свадьбы"` процент не возврата меньше на **`1,2% - 2,2%`** по сравнению с предыдущими.

## Используемые библиотеки
*pandas, pymystem3*

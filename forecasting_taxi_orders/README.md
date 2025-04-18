# Прогнозирование заказов такси

## Описание проекта

Компания «Чётенькое такси» собрала исторические данные о заказах такси в аэропортах. Чтобы привлекать больше водителей в период пиковой нагрузки, нужно спрогнозировать количество заказов такси на следующий час. Постройте модель для такого предсказания.

Значение метрики RMSE на тестовой выборке должно быть не больше 48.

## Описание данных

Данные лежат в файле `/datasets/taxi.csv`.

Количество заказов находится в столбце `'num_orders'` (от англ. number of orders, «число заказов»).

---
# Вывод
В процессе проведения исследовательского анализа данных мы открыли и изучили файл, проанализировали данные. Написали функции для обучения и тестирования моделей. Выяснили, что линейные модели показали практически одинаковый результат по RMSE. Наилучшие результаты даёт скользящее окно размером примерно 40-50 часов. Модель Lasso получила заметно меньшее RMSE по сравнению с базовой моделью. И в итоге мы увидели, что модель отлично определяет тестовые данные, но испытывает проблемы с редкими большими значениями.

## Используемые библиотеки
*pandas, matplotlib, numpy, seaborn, display, seasonal_decompose, sklearn, warnings*

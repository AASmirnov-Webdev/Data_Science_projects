# Восстановление золота из руды

## Описание проекта
Необходимо подготовить прототип модели машинного обучения для «Цифры». Компания разрабатывает решения для эффективной работы промышленных предприятий.

Модель должна предсказать коэффициент восстановления золота из золотосодержащей руды. Используйте данные с параметрами добычи и очистки. 

Модель поможет оптимизировать производство, чтобы не запускать предприятие с убыточными характеристиками.
## Описание данных
Данные находятся в трёх файлах:
*	`gold_recovery_train_new.csv` — обучающая выборка;
*	`gold_recovery_test_new.csv` — тестовая выборка;
*	`gold_recovery_full_new.csv` — исходные данные.

Данные индексируются датой и временем получения информации (признак date). Соседние по времени параметры часто похожи.

Некоторые параметры недоступны, потому что замеряются и/или рассчитываются значительно позже. Из-за этого в тестовой выборке отсутствуют некоторые признаки, которые могут быть в обучающей. Также в тестовом наборе нет целевых признаков.

Исходный датасет содержит обучающую и тестовую выборки со всеми признаками.
---
# Вывод
В процессе проведения исследовательского анализа данных мы открыли и изучили файлы, проанализировали признаки, недоступные в тестовой выборке, проверили формулы вычисления эффективности обогащения. Провели предобработку данных на обучающей и тестовой выборке, обработали пропущенные и нулевые значения в данных. 

В процессе анализа данных, выполнили следующие действия:
* исследовали изменения концентрации элементов на каждом этапе;
* проанализировали распределения размеров гранул на обучающей и тестовой выборках;
* провели исследование суммарных концентраций.

Написали функцию для вычисления итогового sMAPE, произвели разбивку данных на признаки и целевые признаки. Выбрали для сравнения три модели регрессии (Linear Regression, Random Forest Regressor, Decision Tree Regressor) и выяснили, что лучшей себя показала модель **`Random Forest Regressor`**. Ну и наконец мы проверили нашу лучшую модель на тестовых данных и сравнили ее с константной моделью.
## Используемые библиотеки
*pandas, matplotlib, numpy, seaborn, sklearn, warnings*

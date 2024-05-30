## Название команды: Magnum Scopum
## Участники: 
- Дмитрий Казанский 
- Александр Бережной, 
- Валерий Лысиков, 
- Наталья Матвеева, 
- Марат Галиулин

## Цели работы:

1. Hайти наиболее эффективную модель атрибуции по каналам трафика для различных групп товаров, представленных в датасете.
2. Определить влияние различных каналов коммуникации (рекламы / орг.трафика итд) на продажи различных категорий продуктов
3. Дать рекомендации относительно перераспределения рекламного бюджета из менее эффективных средств коммуникации в более эффективные
4. Выяснить, сколько касаний происходит при приобретении того или иного продукта
5. Определить, есть ли общий цикл принятия решений клиентом о приобретении продукта
6. На основе этого определить, какие модели исследования применимы в каждом случае, какие нет


## Задачи работы: 

1. Подготовить данные :
    * Очистить данные от ошибочных записей, дубликатов, выбросов, аномалий
    * Привести записи в данных к единому формату
    * Заполнить пропущенные значения в данных
    * удалить ненужные поля
2. Разделить продукты, представленные в датасетах, на однородные группы. Продукты в датасете достаточно разнородны, вследствие чего применение одной и той же модели аттрибуции к разным продуктом вероятнее всего будет неверным.
3. Соединить табличные данные в единый датасет / сводную таблицу на основе данных клиентов (user_id, user_phone), представленных в таблицах.
4. Внутри каждой группы товаров разделить данные по средствам коммуникации и классифицировать их от наиболее выгодных к наименее выгодным/убыточным. При классификации нами планируется сравнить результаты различных классификационных моделей - линейной классификации (SGDClassifier), KNN, RandomForest. 
5. Классифицировать важность признаков, которые обусловили принадлежность исследуемых элементов к той или иной классификационной категории (например, посредством использования метода feature_importances, который имеется во многих моделях машинного обучения)
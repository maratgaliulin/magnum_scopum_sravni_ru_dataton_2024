[Вернуться на главную...](../README.md)

# Исходные данные
## Общая информация

> Цель все та же - найти самую эффективную модель атрибуции по каналам трафика

>The `datasets` folder contains the initial input data provided by the tournament organizer for completing the tasks:

### event_data.csv - лог событий

`event_data.csv` - хранит лог событий

```SQL
CREATE TABLE event_data (
    id TEXT,
    user_phone TEXT,
    event_type TEXT,
    event_dtm TIMESTAMP,
    event_status TEXT,
    update_dtm TIMESTAMP,
    payout FLOAT,
    currency TEXT,
    product_type TEXT
);
```
•  event_dtm - дата создания события 
•  update_dtm - дата обновления статуса события
•  event_status - текущий статус события
•  event_type - тип события (клик, показ), клик может преобразоваться в конверсию

### adv_data.csv - затраты на привлечение клиентов

`adv_data.csv` - хранит затраты на привлечение клиентов

```SQL
CREATE TABLE adv_data (
    user_id TEXT,
    campaign_type TEXT,
    campaign_start_dtm TIMESTAMP,
    campaign_end_dtm TIMESTAMP,
    source_medium TEXT,
    utm_campaign TEXT,
    interface TEXT,
    currency TEXT,
    campaign_cost FLOAT
);
```

•  campaign_start_dtm - дача начала рекламной кампании
•  campaign_end_dtm - дата окончания рекламной кампании
•  event_dtm - дата создания события 
•  campaign_type - тип цели рекламной кампании (клик, показ, конверсия
•  source_medium - UTM метки, которые улетели в событие
•  utm_campaign - маркетинговое название кампании

### users_data.csv - хранит инфу о клиентах

`users_data.csv` - хранит инфу о клиентах

```SQL
CREATE TABLE user_data (
    user_phone TEXT,
    user_id TEXT,
    registration_dtm TIMESTAMP,
    delete_dtm TIMESTAMP
);

```

## Использование хранилища huggingface.co

Пример кода: загрузка датасета "Лог событий" в `jupyter`-ноутбук для исследования с помощью бибилиотеки pandas

```python
import pandas as pd
from huggingface_hub import hf_hub_download
import tqdm as notebook_tqdm

# Исходные файлы загружены на ресурс https://huggingface.co/datasets
REPO_ID = "DmitriiMiptEdu/event_data"

event_data = 'event_data.csv' # хранит лог событий
adv_data = 'adv_data.csv' # хранит затраты на привлечение клиентов
users_data = 'users_data.csv' # хранит инфу о клиентах

# Импортируем `event_data.csv` (лог событий) в ppandas
event_df = pd.read_csv(hf_hub_download(repo_id=REPO_ID, filename=event_data, repo_type="dataset"), low_memory=False)
event_df.info()
```


## Использование хранилища Google Disk

Ссылки на датасеты:

* `event_data.csv` id:[1z9QeNXmygRAGnrT32Z_5BT_8BDnvfn4o](https://drive.google.com/file/d/1z9QeNXmygRAGnrT32Z_5BT_8BDnvfn4o/view?usp=sharing)
* `adv_data.csv`   id:[1RIWBiZErIsuHKhE1Y9k_UhXpZhq_Hi5i](https://drive.google.com/file/d/1RIWBiZErIsuHKhE1Y9k_UhXpZhq_Hi5i/view?usp=sharing)
* `users_data`     id:[1QNFHL0AcFSjXUdSfKy3wMMbLA5sSoAw4](https://drive.google.com/file/d/1QNFHL0AcFSjXUdSfKy3wMMbLA5sSoAw4/view?usp=sharing)

Пример кода: загрузка датасетов во временное хранилище colab.google

```python
!pip install gdown
# In google-colab you have to use ! before bash commands.
# download `event_data.csv`
!gdown --id 1z9QeNXmygRAGnrT32Z_5BT_8BDnvfn4o

# download `adv_data.csv`
!gdown --id 1RIWBiZErIsuHKhE1Y9k_UhXpZhq_Hi5i

# download `users_data`
!gdown --id 1QNFHL0AcFSjXUdSfKy3wMMbLA5sSoAw4

```

Просмотрел часть лекции про наше задание. Надо: 

А) определить влияние различных каналов коммуникации (рекламы / орг.трафика итд) на продажи,

Б) посоветовать как перераспределить рекламный бюджет из менее эффективных средств коммуникации в более эффективные

В) выяснить, сколько касаний происходит при приобретении того или иного продукта

Г) определить, есть ли общий цикл принятия решений клиентом о приобретении продукта

Д) на основе этого определить, какие модели исследования применимы в каждом случае, какие нет


Для этого думаю, нам нужно:

1)	Как сказал Дима, разделить все их продукты (кредиты, ипотеки, купля/продажа домов, квартир, ОСАГО, страхование итд) на однородные группы, т.к. как можно логично предположить (и как было сказано И.Серачевым на встрече) одну и ту же модель нельзя применить к разнородным продуктам.

2)	Также считаю что нужно сшить все таблицы, т.к. данные о каналах коммуникации записаны в одной таблице, а данные о совершении/несовершении клиентом покупки (столбец payout) – в другой таблице. Эти 2 таблицы надо связать через таблицу с данными клиентов (их id и номер телефона).

3)	Внутри каждой группы товаров разделить данные по средствам коммуникации и классифицировать их от наиболее выгодных к наименее выгодным/убыточным.



То есть, мне кажется, у нас по сути 2 задачи классификации: классификация продуктов по их однородности, и классификация каналов коммуникации по их выгодности. Можно попробовать как поведут себя различные модели – линейная классификация, KNN, RandomForest. Единственное что нам еще нужно от кураторов – это расшифровка полей (названий столбцов) датасета; что означают названия столбцов:
•	campaign_start_dtm
•	campaign_end_dtm
•	event_dtm
•	update_dtm
•	event_status
Также – в чем разница между campaign_type в таблице adv_data.csv и event_type в таблице event_data.csv, а также между полями source_medium и utm_campaign в таблице adv_data.csv

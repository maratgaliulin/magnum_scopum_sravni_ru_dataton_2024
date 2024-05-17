[Вернуться на главную...](../README.md)

# Исходные данные
## Общая информация

> Цель все та же - найти самую эффективную модель атрибуции по каналам трафика

>The `datasets` folder contains the initial input data provided by the tournament organizer for completing the tasks:

* `event_data.csv` - хранит лог событий
* `adv_data.csv` - хранит затраты на привлечение клиентов
* `users_data.csv` - хранит инфу о клиентах

## Использование хранилища huggingface.co

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


## Cсылки на хранилище файлов

* `event_data.csv` id:[1z9QeNXmygRAGnrT32Z_5BT_8BDnvfn4o](https://drive.google.com/file/d/1z9QeNXmygRAGnrT32Z_5BT_8BDnvfn4o/view?usp=sharing)
* `adv_data.csv`   id:[1RIWBiZErIsuHKhE1Y9k_UhXpZhq_Hi5i](https://drive.google.com/file/d/1RIWBiZErIsuHKhE1Y9k_UhXpZhq_Hi5i/view?usp=sharing)
* `users_data`     id:[1QNFHL0AcFSjXUdSfKy3wMMbLA5sSoAw4](https://drive.google.com/file/d/1QNFHL0AcFSjXUdSfKy3wMMbLA5sSoAw4/view?usp=sharing)

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


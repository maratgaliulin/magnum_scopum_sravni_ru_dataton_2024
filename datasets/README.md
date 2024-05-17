[Вернуться на главную...](../README.md)

# Исходные данные
## Общая информация

> Цель все та же - найти самую эффективную модель атрибуции по каналам трафика

>The `datasets` folder contains the initial input data provided by the tournament organizer for completing the tasks:

* `event_data.csv` - хранит лог событий
* `adv_data.csv` - хранит затраты на привлечение клиентов
* `users_data.csv` - хранит инфу о клиентах

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


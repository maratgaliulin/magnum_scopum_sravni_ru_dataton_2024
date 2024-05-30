import pandas as pd

def basic_stats(df:pd.DataFrame, prod_type:str) -> None:
    df = df.drop('product_type', axis=1)
    df = pd.get_dummies(
        df, columns=['event_type', 'event_status'])

    # Суммы касаний кликов, показов и конверсий

    sum_of_touches = df[[
        'event_type_click', 'event_type_show', 'event_type_conversion']].sum()
    
    # Сумма показов без конверсий

    sum_of_touches_wo_conversions = sum_of_touches['event_type_click'] + \
        sum_of_touches['event_type_show']
    
    # Процент конверсий от общего числа касаний:

    conversion_touches_percent = round(
        sum_of_touches['event_type_conversion'] / sum_of_touches.sum() * 100, 3)

    # Общий доход как сумма столбца payout

    total_payout = round(df['payout'].sum(), 3)

    # Положительные решения банков:

    bank_positive_decisions = df.loc[(df['event_status_approve'] > 0) |
                                               (df['event_status_deal'] > 0) |
                                               (df['event_status_sale'] > 0)
                                               ][['event_status_approve', 'event_status_deal',
                                                  'event_status_sale']].sum()
    
    # Отрицательные решения банков:

    bank_negative_decisions = df.loc[df['event_status_reject']
                                               > 0]['event_status_reject'].sum()
    
    results_dict = {
        'Сумма показов без конверсий': sum_of_touches_wo_conversions,
        'Процент конверсий от общего числа касаний': conversion_touches_percent,
        f'Общий доход продукта {prod_type}': total_payout,
        'Положительные решения банков': bank_positive_decisions.sum(),
        'Отрицательные решения банков': bank_negative_decisions
    }

    print('Суммы касаний кликов, показов и конверсий')
    print('Клики:', sum_of_touches['event_type_click'])
    print('Показы:', sum_of_touches['event_type_show'])
    print('Конверсии:', sum_of_touches['event_type_conversion'])

    for key in results_dict:
        print(key, ':', results_dict[key])


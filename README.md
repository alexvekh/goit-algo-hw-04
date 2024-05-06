# Тестування алгоритмів сортування

## Тестування:

В цьому коді реалізовано тестування алгоритмів сортування:

- сотрування вставками
- сортування злиттям
- та внутрішніх функцій Timsort (.sort(), sorted)

на різних масивах даних:

- малий список (10 записів)
- зворотній список (10 записів)
- список з дублікатими (12 записів)
- список з літер (9 записів)
- float (20 записів)
- великий список (500 записів)

## Результати:

Внутрішні фуунткції sort() та sorted показали кращі результати на всіх тестованих списках, особливо на великому списку:

- **Малий список**: в 2 рази швидше
- **Зворотний список** (як найгірший ввипадок): в 2.6 рази швидше
- **Список з дублікатами**: в 2.1 рази швидше за сортування злиттям, але не суттєво швидше за сотрування вставками
- **Список з букв**: в 2.75 рази швидше
- **Float_numbers**: в 2.6 разів швидше
- **Великий список** в середньому в 14 зазів швидше
  - найгірше великий список сортується вставками,
  - злиттям в 4,75 разів швидше ніж встакави,
  - а .sort() - в 24 рази швидше ніж вставками

## Загальні висновки:

- sort() та sorted є універсальними та ефективними виборами для сортування більшості списків, особливо великих.
- різниця sort() та sorted абсолютьно не суттєва (на рівні погрішності)
- Список з дублікатами помітно гірше сортується внутрішніми функціями при рівній довжині масиву, тоді як методом вставок сотрується так само швидко.

## Рекомендації:

- Для більшості випадків рекомендується використовувати sort() чи sorted.
- Особливо сильно рекомендується sort() або sorted для великих списків.
- Список з дублікатими доцільно сортувати методом вставок
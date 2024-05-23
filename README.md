# Порівняння алгоритмів сортування

Цей проект порівнює продуктивність трьох алгоритмів сортування: сортування вставками, сортування злиттям та Timsort (вбудований алгоритм сортування Python). Порівняння виконане на різних наборах даних для емпіричної перевірки теоретичних оцінок складності алгоритмів.

## Алгоритми

1. **Сортування вставками (Insertion Sort):**

- Складність: O(n^2)
- Добре підходить для невеликих масивів.

2. **Сортування злиттям (Merge Sort):**

- Складність: O(n log n)
- Підходить для великих масивів завдяки стабільній продуктивності.

3. **Timsort:**

- Складність: O(n log n)
- Використовується вбудованою функцією sorted() у Python.
- Оптимізований для реальних даних і показує відмінні результати на практиці.

На основі проведених тестів, Timsort є найбільш ефективним вибором для сортування масивів будь-яких розмірів у Python.

# In place quick sort
It is training task.

## The task description
Тимофей решил организовать соревнование по спортивному программированию, чтобы найти талантливых стажёров. Задачи подобраны, участники зарегистрированы, тесты написаны. Осталось придумать, как в конце соревнования будет определяться победитель.

Каждый участник имеет уникальный логин. Когда соревнование закончится, к нему будут привязаны два показателя: количество решённых задач Pi и размер штрафа Fi. Штраф начисляется за неудачные попытки и время, затраченное на задачу.

Тимофей решил сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот, у которого решено больше задач. При равенстве числа решённых задач первым идёт участник с меньшим штрафом. Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.

Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин. В своё отсутствие он поручил вам реализовать алгоритм быстрой сортировки (англ. quick sort) для таблицы результатов. Так как Тимофей любит спортивное программирование и не любит зря расходовать оперативную память, то ваша реализация сортировки не может потреблять O(n) дополнительной памяти для промежуточных данных (такая модификация быстрой сортировки называется "in-place").

## Example
Input:
```
$ python ./main.py
5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80
```
Output:
```
gena
timofey
alla
gosha
rita
```

## Install requirements
1. Python >= 3.9

## Sources
* /deque/deque/deque.py - main module with a algorithm logic.  
  Project submodules:
* /deque/main.py - provides a console tools for the deque.
* /deque/deque/tests/test_deque.py - packages tests.


## RUN TEST 
* cd into project dir
* run `python -m unittest discover ./mypackages/tests`

## License
[LICENSE MIT](LICENSE)
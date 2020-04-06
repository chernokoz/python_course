import random
import time


# 1
def empty():
    for i in ():
        yield i


# 2
def heapify(value, heap1, heap2):
    head1, heap1 = extract_head(heap1)
    head2, heap2 = extract_head(heap2)
    if head1 is None and head2 is None:
        yield (value, 1, 1)
        yield empty()
        yield empty()
    elif head1 is None and value <= head2[0]:
        yield (value, head2[1] + 1, head2[2] + 1)
        yield empty()
        yield heap2
    elif head2 is None and value <= head1[0]:
        yield (value, head1[1] + 1, head1[2] + 1)
        yield heap1
        yield empty()
    elif head1 is None and value > head2[0]:
        next(heap2, None)
        yield (head2[0], head2[1] + 1, head2[2] + 1)
        yield empty()
        yield heapify(value, next(heap2, None), next(heap2, None))
    elif head2 is None and value > head1[0]:
        next(heap1, None)
        yield (head1[0], head1[1] + 1, head1[2] + 1)
        yield heapify(value, next(heap1, None), next(heap1, None))
        yield empty()
    elif value <= head1[0] and value <= head2[0]:
        yield (value, head1[1] + head2[1] + 1, max(head1[2], head2[2]) + 1)
        yield heap1
        yield heap2
    elif head1[0] <= head2[0]:
        next(heap1, None)
        yield (head1[0], head1[1] + head2[1] + 1, max(head1[2], head2[2]) + 1)
        yield heapify(value, next(heap1, None), next(heap1, None))
        yield heap2
    else:
        next(heap2, None)
        yield (head2[0], head1[1] + head2[1] + 1, max(head1[2], head2[2]) + 1)
        yield heap1
        yield heapify(value, next(heap2, None), next(heap2, None))


# 3
def print_heap(heap, prefix=''):
    current = next(heap, None)
    if current is not None:
        print(f"{prefix}[{current[1]}, {current[2]}]: {current[0]}")
        left = next(heap, None)
        if left is not None:
            print_heap(left, prefix + '    ')
        right = next(heap, None)
        if right is not None:
            print_heap(right, prefix + '    ')


# 4
def build_heap(seq):
    to_build = list(seq)
    size = len(to_build)
    if size == 0:
        return empty()
    for i in range(size - 1, -1, -1):
        left = to_build[2 * i + 1] if 2 * i + 1 < size else empty()
        right = to_build[2 * i + 2] if 2 * i + 2 < size else empty()
        to_build[i] = heapify(to_build[i], left, right)
    return to_build[0]


def extract_head(heap):
    current = next(heap, None)
    if current is None:
        yield None
        yield empty()
    else:
        yield (current[0], current[1], current[2])
        yield heapify(current[0], next(heap), next(heap))


# 5
def extract_last(heap):
    head = next(heap, None)
    if head is None:
        yield None
        yield empty()
    else:
        head1, left = extract_head(next(heap))
        head2, right = extract_head(next(heap))
        if head1 is None and head2 is None:
            yield head[0]
            yield empty()
        elif head2 is None:
            result = extract_last(left)
            yield next(result)
            yield heapify(head[0], next(result), right)
        elif head1[2] > head2[2]:
            result = extract_last(left)
            yield next(result)
            yield heapify(head[0], next(result), right)
        else:
            result = extract_last(right)
            yield next(result)
            yield heapify(head[0], left, next(result))


# 6
def extract_min(heap):
    head, heap = extract_head(heap)
    if head is None:
        yield None
        yield empty()
    else:
        last, heap = extract_last(heap)
        yield head[0]
        if next(heap, None) is None:
            yield empty()
        else:
            left = next(heap, None)
            right = next(heap, None)
            yield heapify(last, left, right)


# 7
def heap_sort(seq):
    heap = build_heap(seq)
    minimum, other = extract_min(heap)
    while minimum is not None:
        yield minimum
        minimum, other = extract_min(other)


# 8
def bench():

    """
    1) empty() НУО работает за O(1)

    2) heapify выдает генератор, ничего не вычисляя,
    это происходит за O(1). Если же мы захотим
    сделать next, то он дойдет до yield также за константу,
    поскольку он лишь поймет, куда просеивать value,
    и выдаст элемент, который будет в голове.
    Дальше должен выдать генератор - левую подкучу,
    что он и сделает, не вычисляя что в ней самой. Далее,
    heapify аналогично действует лениво.

    3) print_heap работает за O(n), поскольку он
    рекурсивно проходит про всем вершинам сверху вниз,
    печатая каждое значение. Рекурсия тут нужна только
    для правильного порядка. Тут уже никакой ленивости
    нет, поскольку это не генератор - печатаем полностью.

    4) build_heap работает за O(n) - пробегается по
    массиву справа налево, пересчитывая каждое
    значение за константу (обращается к двум другим
    элементам массива), делая с ними heapify, который
    возвращает генераторы за O(1).

    5) Мой вспомогательный генератор extract_head делает
    next за O(1), а дальше вызывает heapify, который
    также работает за O(1).

    6) extract_last обязательно спускается на самый
    нижний уровень рекурсивными вызовами, которых
    в следствии этого будет O(logn). Причем в каждом
    рекурсивном вызове используются второй yield
    для пересборки новой кучи, это делается с помощью
    heapify, который работает за O(1). Поэтому
    extract_last работает за O(logn).

    7) extract_min использует extract_last и
    extract_head, которые работают за O(logn) и O(1).
    Также, extract_min пересобирает кучу с помощью
    heapify, присоединяя на вершину на каждом
    уровне. Поскольку уровней logn, то общее время
    работы O(logn).

    8) heap_sort находит минимум и оставшуюся кучу с
    помощью функции extract_min за O(logn). Так
    происходит на каждом шаге, всего шагов n.
    Итого время работы O(nlogn).

    Для сравнения скорости работы реализованной
    сортировки с сортировкой из стандартной
    библиотеки они были протестированы на трех
    видах массивов: полностью отсортированном,
    обращенным полностью отсортированным,
    состоящим из рандомных элементов.

    Видно, что по сортировка из стандартной
    библиотеки по времени быстрее реализованной
    сортировки больше, чем в 10000 раз. Видимо
    это связано с тем, что генераторы все-таки
    довольно медленно работают для создания
    сортировки на них. Плюс используется много
    доп памяти, для промежуточных генераторов,
    на обращение и запись в котороую тратится
    много времени.

sorted_heap with heap_sort--- 4.828887462615967
reserved_sorted_heap with heap_sort--- 4.806397199630737
random_heap with heap_sort--- 4.843030214309692
sorted_heap with heap_sort--- 1.2159347534179688e-05
reserved_sorted_heap with heap_sort--- 9.5367431640625e-06
random_heap with heap_sort--- 0.00011897087097167969

    """

    sorted_arr = ([i for i in range(1000)])
    reversed_sorted_arr = ([i for i in range(1000)])
    random_arr = (random.sample(range(1000), 1000))

    start_time = time.time()
    list(heap_sort(sorted_arr))
    print(f"sorted_heap with heap_sort--- {time.time() - start_time}")

    start_time = time.time()
    list(heap_sort(reversed_sorted_arr))
    print(f"reserved_sorted_heap with heap_sort--- {time.time() - start_time}")

    start_time = time.time()
    list(heap_sort(random_arr))
    print(f"random_heap with heap_sort--- {time.time() - start_time}")

    start_time = time.time()
    sorted(sorted_arr)
    print(f"sorted_heap with heap_sort--- {time.time() - start_time}")

    start_time = time.time()
    sorted(reversed_sorted_arr)
    print(f"reserved_sorted_heap with heap_sort--- {time.time() - start_time}")

    start_time = time.time()
    sorted(random_arr)
    print(f"random_heap with heap_sort--- {time.time() - start_time}")


if __name__ == "__main__":
    bench()

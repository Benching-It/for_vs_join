import timeit

from memory_profiler import profile


def populating_array_with_data(function_array, function_option):
    if function_option == 1:
        for i in range(0, 10):
            function_array.append("test_{}".format(i))
    elif function_option == 2:
        for i in range(0, 1000):
            function_array.append("test_{}".format(i))
    elif function_option == 3:
        for i in range(0, 100000):
            function_array.append("test_{}".format(i))
    elif function_option == 4:
        for i in range(0, 1000000):
            function_array.append("test_{}".format(i))

    return function_array


@profile
def join_function(join_array):
    return " ".join(join_array)


@profile
def for_loop_function(loop_array):
    result = ""
    for element in loop_array:
        result += "{} ".format(element)

    return result


if __name__ == '__main__':
    for option in range(1, 5):
        array = []
        print("#"*10, " {} CASE ".format(option), "#"*10)
        populating_array_with_data(array, function_option=option)
        join_time = timeit.timeit(lambda: join_function(array), number=1)
        for_time = timeit.timeit(lambda: for_loop_function(array), number=1)

        print("Time processing data for 'join': {}".format(join_time))
        print("Time processing data for 'for loop': {}".format(for_time))
        print("")

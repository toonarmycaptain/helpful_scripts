def function_name_to_class_name(function_name):
    # Split function name into words.
    function_list = function_name.split('_')

    # Capitalise words
    for word in function_list:
        capped_word = word[0].upper() + word[1:]
        function_list[function_list.index(word)] = capped_word

    # Rejoin the words without spaces.
    rejoined = ''.join(function_list)
    return rejoined


def function_name_to_test_class_name(function_name):
    test_class_name = 'Test' + function_name_to_class_name(function_name)
    return test_class_name


def function_name_to_test_function_name(function_name):
    test_function_name = 'test_' + function_name
    return test_function_name


def sentence_to_function_name(sentence):
    return sentence.replace(' ', '_')


def sentence_to_class_name(sentence):
    func_form = sentence_to_function_name(sentence)
    return function_name_to_class_name(func_form)


def sentence_to_test_class_name(sentence):
    func_form = sentence_to_function_name(sentence)
    return function_name_to_test_class_name(func_form)


def sentence_to_test_function_name(sentence):
    function_name = sentence_to_function_name(sentence)
    return function_name_to_test_function_name(function_name)


def list_functions_in_module(module_name):
    """
    Returns a list of functions in the given module.
    Returns a warning if module is not currently imported.
    """
    try:
        function_list = [func for func in dir(module_name) if '__' not in func]
    except NameError:
        return f'Module is not in current namespace, please import {module_name}'
    return function_list


def module_functions_to_test_class_names(module_name):
    module_test_class_names = []
    for function_name in list_functions_in_module(module_name):
        test_class_name = function_name_to_test_class_name(function_name)
        module_test_class_names.append(test_class_name)
    return module_test_class_names


def module_functions_to_test_function_names(module_name):
    module_test_function_names = []
    for function_name in list_functions_in_module(module_name):
        test_function_name = function_name_to_test_function_name(function_name)
        module_test_function_names.append(test_function_name)
    return module_test_function_names


def print_test_class_test_func_name_for_module(module_name):
    module_test_class_names = module_functions_to_test_class_names(module_name)
    module_test_function_names = module_functions_to_test_function_names(module_name)
    for function in range(len(module_test_class_names)):
        print(f'{module_test_class_names[function]}, {module_test_function_names[function]}')

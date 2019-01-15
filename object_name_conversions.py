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

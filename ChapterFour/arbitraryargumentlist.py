def product_of_arbitary_argument_list(*argument):
    product_of_integers = 1
    for number in argument:
        product_of_integers *= number
    return product_of_integers


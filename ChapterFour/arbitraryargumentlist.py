def product(*argument):
    product_of_integers = 1
    for number in argument:
        product_of_integers *= number
    return product_of_integers
print(product(1,4,6,2))

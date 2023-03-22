class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [product for product in self.products if product[0] == first_letter]
        # filtered = []
        # for product in self.products:
        #     if product[0] == first_letter:
        #         filtered.append(product)
        #
        # return filtered

    # def __repr__(self):
    #     result = f"Items in the {self.name}:"
    #
    #     self.products = sorted(self.products)
    #
    #     for product in self.products:
    #         result += '\n' + product
    #
    #     return result
    def __repr__(self):
        result = "Items in the {0} catalogue:\n" \
            "{1}".format(self.name, '\n'.join(sorted(self.products)))
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

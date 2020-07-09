class ProductManager(models.Manager):
    def search_substitutes(self, product_name):
        substitutes = []
        product = Product.objects.filter(name__icontains=product_name)
        if product:
            # rechercher des substituts et affecter la liste de résultats à
            # la variable substitutes
        else:
            product = None
        return product, substitutes
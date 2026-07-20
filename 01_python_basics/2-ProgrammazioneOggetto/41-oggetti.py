# Crea in Python due classi, Product e ShoppingCart, per simulare il carrello della spesa.
# Product deve avere name e price, con metodispeciali per la stampa e il confronto.
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price:.2f}€"
    
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price
        
# ShoppingCart deve permettere di aggiungere items, rimuoverli e calcolare il totale e stampare il contenuto.
class ShoppingCart:
    def __init__(self):
        self.items: list[Product] = []

    def add_product(self, product: Product):
        self.items.append(product)

    def remove_product(self, product: Product):
        if product in self.items:
            self.items.remove(product)

    def total_price(self):
        return sum(product.price for product in self.items)
    
# Implementa  l'overloading dell'operatore + (unione carrelli), len() e str().
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        if not self.items:
            return "Carrello vuoto"
        lines = ["Prodotti: "]
        for product in self.items:
            lines.append(f" - {product}")
        lines.append(f"Totale: {self.total_price():.2f}€")
        return "\n".join(lines)

    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.items = self.items + other.items
        return new_cart

# Scrivi un programma che crei alcuni items, li aggiunga a due carrelli diversi, mostri le funzionalità richieste.

if __name__ == "__main__":
    p1 = Product("Mela", 1)
    p2 = Product("Banana", 2)
    p3 = Product("Arancia", 3)

    cart1 = ShoppingCart()
    cart1.add_product(p1)
    cart1.add_product(p2)

    cart2 = ShoppingCart()
    cart2.add_product(p3)

    print("Carrello 1:")
    print(cart1)

    print("\nCarrello 2:")
    print(cart2)

    print("\nCarrello 1 dopo rimozione:")
    cart1.remove_product(p1)
    print(cart1)

    cart3 = cart1 + cart2
    print("\nCarrello 3 (unione):")
    print(cart3)
    print("Numero di prodotti:", len(cart3))
class Producto():
    
    def __init__(self, codigo, nombre, precio, tipo):
        
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        
        print(f"Se acaba de crear el producto {self.nombre} con codigo {self.codigo} con precio {self.precio} del tipo {self.tipo}")   
        
        def __str__ (self):
            return "self.codigo {}, self.nombre {}, self.precio {}, self.tipo {}".format (self.codigo, self.nombre, self.precio, self.tipo)
        
producto = Producto("076423755s", "Red Socks", "50", "Camiseta")
print (producto)

producto1 = ["076423755s", "Red Socks", "50", "Camiseta"]
producto2 = ["086445655e", "Pelicans", "50", "Camiseta"]

producto1.remove("50")
producto1.insert(2, "39")
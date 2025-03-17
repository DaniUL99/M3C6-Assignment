class Usuario:

    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

dani = Usuario("DaniUL99", "password")

print(dani.usuario, dani.contraseña)
        
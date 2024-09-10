class Lampara:
    _ESTADOS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
                '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, esta_encendida):
        self.esta_encendida = esta_encendida

    def encender(self):
        self.esta_encendida = True
        self.muestra_lampara()

    def apagar(self):
        self.esta_encendida = False
        self.muestra_lampara()

    def muestra_lampara(self):
        if self.esta_encendida:
            print(self._ESTADOS[0])
        else:
            print(self._ESTADOS[1])


def main():
    lamp = Lampara(esta_encendida=False)
    menu = '''Menu:
  0 > Apagar Lampara
  1 > Encender lampara
  x > Salir'''
    while True:
        print(menu)
        op = input("Por Favor Loco1 Que opcion desea : ")
        if op == '0':
            lamp.apagar()
        elif op == '1':
            lamp.encender()
        else:
            break


if __name__ == "__main__":
    main()

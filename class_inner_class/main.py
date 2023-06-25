class One:
    class Two:
        def show(self):
            print('Show Two')
            One.show(super())

    def show(self):
        print('Show One')

class Three():
    class Four(One):
        def show(self):
            print('Four')
            super().show()

    def show(self):
        print('Show Three')

one = One()
one.show()
one.Two().show()

three = Three()
three.show()
three.Four().show()
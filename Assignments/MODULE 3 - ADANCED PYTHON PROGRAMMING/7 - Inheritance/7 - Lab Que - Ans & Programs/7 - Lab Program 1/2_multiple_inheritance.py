class father:
    def show_father(self):
        print("father class")

class mother:
    def show_mother(self):
        print("mother class")

class child(father,mother):
    def show_child(self):
        print("child class")

c = child()
c.show_father()
c.show_mother()
c.show_child()


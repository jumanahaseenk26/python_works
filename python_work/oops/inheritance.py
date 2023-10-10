class parent:

    phone="SamsungA32"
    vehicle="passionpro"

    def mobile(self):
        print(self.phone)

    def bike(self):
        print(self.vehicle)

class child(parent):
    pass

obj=child()
obj.mobile()
obj.bike()
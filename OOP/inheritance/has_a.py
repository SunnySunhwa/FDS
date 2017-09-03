#HAS-A
class Gun:
    def __init__(self, kind):
        self.kind = kind

    def bang(self):
        print('bang bang!')

class Police:
    def __init__(self, gun_kind = ''):
        if gun_kind:
            self.gun = Gun(gun_kind)
        else:
            self.gun = None

    def get_gun(self, gun_kind):
        self.gun = Gun(gun_kind)

    def shoot(self):
        if self.gun:
            self.gun.bang()
        else:
            print("Unable to shoot")

if __name__ == "__main__":
    p1 = Police('리볼버')
    p1.shoot()

    p2 = Police()
    p2.shoot()

    p2.get_gun('기관총')
    p2.shoot()

    

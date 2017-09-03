from abc import *

class Character(metaclass = ABCMeta):
    def __init__(self, name, hp, power):
        self.name = name
        self.HP = hp
        self.power = power

    @abstractmethod
    def attack(self, other, attack_kind):
        pass

    @abstractmethod
    def get_damage(self, power, attack_kind):
        pass

    def __str__(self):
        return '{} : {}'.format(self.name, self.HP)

class Player(Character):
    def __init__(self, name = 'player', hp = 100, power = 10, *attack_kinds):
        super().__init__(name, hp, power)

        self.skills = []
        for attack_kind in attack_kinds:
            self.skills.append(attack_kind)

    def attack(self, other, attack_kind):
        if attack_kind in self.skills:
            other.get_damage(self.power, attack_kind)

    def get_damage(self, power, attack_kind):
        '''
        만약 공격 종류가
        플레이어의 기술 중 하나라면
        절반의 데미지를 얻습니다. 
        '''
        if attack_kind in self.skills:
            self.HP -= (power//2)
        else:    
            self.HP -= power
        
class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attack_kind = 'None'

    def attack(self, other, attack_kind):
        if self.attack_kind == attack_kind:
            other.get_damage(self.power, attack_kind)

    def get_damage(self, power, attack_kind):
        '''
        몬스터는 자신과 타입이 같은 공격을 당하면
        오히려 체력이 늘어납니다.
        조심해서 공격하세요.
        '''
        if self.attack_kind == attack_kind:
            self.HP += power
        else:
            self.HP -= power

    def get_attack_kind(self):
        return self.attack_kind

class IceMonster(Monster):
    def __init__(self, name = 'Ice monster', hp = 50, power = 10):
        super().__init__(name, hp, power)
        self.attack_kind = 'ICE'

class FireMonster(Monster):
    def __init__(self, name = 'Fire monster', hp = 50, power = 20):
        super().__init__(name, hp, power)
        self.attack_kind = 'FIRE'
        
    #메서드 추가
    #FireMonster만의 행동
    def fireball(self):
        '''
        FireMonster는 1분마다 3미터 내의 모든 객체에
        파이어볼을 쏩니다.
        플레이어의 스킬에 'FIRE'가 있다고 해도
        이 공격을 반감시키지는 못합니다.
        '''
        #구현 코드
        print('fireball')

if __name__ == "__main__":
    player = Player('sword master',100, 30, 'ICE', 'FIRE')
    monsters = []
    monsters.append(IceMonster())
    monsters.append(FireMonster())
    
    for monster in monsters:
        print(monster)

    for monster in monsters:
        player.attack(monster, 'ICE')

    print('after the player attacked')

    for monster in monsters:
        print(monster)
    print('')
    
    print(player)
    
    for monster in monsters:
        monster.attack(player, monster.get_attack_kind())
    print('after monsters attacked')
    
    print(player)        
        

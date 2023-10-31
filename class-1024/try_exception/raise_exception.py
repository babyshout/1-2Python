
class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    pass
    def fly(self):
        print('very fast')

eagle = Eagle()
eagle.fly()
type(eagle)

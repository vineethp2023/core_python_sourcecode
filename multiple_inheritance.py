class apple:
    color = 'red'
    shape = 'round'
    def details(self):
        print('My color is ',self.color,' and my shape is ',self.shape)
class orange:
    taste = 'sweet\'N\'soure'
    shape = 'perfect round'
    def details_new(self):
        print('My color is orange as well as my shape is ',self.shape, ' and taste : ',self.taste)
class fruit(apple,orange):
    pass
ob = fruit()
ob.details()
ob.details_new()

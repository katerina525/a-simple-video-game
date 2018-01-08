class StudentFighter(object):
    def __init__(self, strength, health, name):
    	self.strength = strength
    	self.name = name
    	self.health = health


eunice = StudentFighter(strength=3, health=100, name="Eunice")
linda = StudentFighter(strength=5, health=100, name="Linda")

print(eunice.name, eunice.strength, eunice.health)
print(linda.name, linda.strength, linda.health)

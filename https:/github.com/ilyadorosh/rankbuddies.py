class User:
    def __init__(self, interests, name):
        self.interests = interests
        self.name = name

me = User({}, "Illia")
mostafa = User({}, "Mostafa")
lida = User({}, "Lida")

me.interests['hoockey']=0.5
me.interests['ai']=0.99
me.interests['adidas']=0.01

mostafa.interests['ai']=0.99
mostafa.interests['hoockey']=0.01
mostafa.interests['adidas']=0.01

lida.interests['hoockey']=0.01
lida.interests['yoga']=1

users=[me,mostafa,lida]


def rankbuddies(user):
    for inter in user.interests:
        for u in users:
            inter in u.interests.keys()

rankbuddies(me)

lida.interests['hoockey']*me.interests['hoockey']

for inter in me.interests:
    print(inter)


for inter in me.interests:
    print(me.interests[inter])

count=0

for herin in lida.interests:
    count += me.interests[inter]*lida.interests[herin]
    print(count)


for inter in lida.interests:
    print(lida.interests[inter])

for inter in mostafa.interests:
    print(mostafa.interests[inter])

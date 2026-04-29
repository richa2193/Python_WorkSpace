import random

x = random.random()
print(x)

y = random.randint(1111,9999)
print(y)

captcha=['Hjw3','Ks4h','KMxo','Pkw9','YHw9','Vs8q','Pcm5','Tcu8','Jw9w']
z = random.choice(captcha)
print(z)

random.shuffle(captcha)
print(captcha)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def is_prime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i+=1
    return True

print(is_prime(73))
print(is_prime(75))

enemies = "Skeleton"

def increase_enemies():
    enemies = "Zombie"
    print(enemies)

increase_enemies()

print(enemies)
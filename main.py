from utils import random
randomValue = random.Simple()
def run():
    print("manipulating")
    # print("My random number: ",randomValue.value)
    values = [random.Simple().value for _ in range(1000)]
    print("Generated values:", values)
    # print(randomValue._eq)
if __name__ == "__main__":
    run()
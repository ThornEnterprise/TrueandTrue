
def main():
    its = int(input("Enter Number of Iterations: "))
    print("AND operator")
    count = 0
    for i in range(its):
        two = i%2
        three = i%3
        if two == 0 and three == 0:
            count += 1
            print(f'{i} is divisible by two and three!')
    print(f'Total Found : {count}')

if __name__ == "__main__" :
    main()

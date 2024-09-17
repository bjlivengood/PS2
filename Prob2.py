#====================================================
# Filename: Prob2.py
# 
# Your name: Baily Livengood
# Who did you work with (if anyone)?: Nobody
# Estimate for time spent (in hrs)?: 3
#====================================================

# Define your function here
def divisible_by_six_or_seven(x, y):
    for i in range(40,60):
        if i % 6 == 0:
            if not i % 7 == 0:
                print(i)
        if i % 7 == 0:
            if not i % 6 == 0:
                print(i)
    if divisible_by_six_or_seven == True:
        return count + 1 # Couldnt figure out how to return a count
    






# Boilerplate
if __name__ == '__main__':
    # Same basic testing here, but you should test MORE!
    count = divisible_by_six_or_seven(40,60)
    print(count)

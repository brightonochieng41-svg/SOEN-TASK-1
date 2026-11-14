print("Hello world")
marks = 40
if marks >= 80:
    print("Passed")
elif marks <= 49:
    print("failed")

def count_total(g):
    count = 0
    for char in g:
        if char.isdigit():
            count += 1
    return count  
result = count_total("He is a 6 year old boy 6 7")  

print(result)





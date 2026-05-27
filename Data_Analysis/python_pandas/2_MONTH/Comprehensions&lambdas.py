#SYNTAXIS
new_value = "lo que quieres guardar"
item = "Cada elemento individual"
iterable = "lista, tuple,range,etc"

[new_value for item in iterable]



#COMPREHENTIONS
numbers = [1,2,3,4,5]
squares =[]

for n in numbers:
    squares.append(n * n)
    
print(squares)


#COMPREHETIONS WITH CONDITION
evens = [n for n in numbers if n % 2 == 0]
print(evens)


#TRANSFORMING VALUES DEPENDING ON THE CONDITION

labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)

#LAMBDA
def funcion_normal(x):
    return x * x
#funcion lambda
square = lambda x: x * x
print(square(5))

#MAP X LAMBDA
result = list(map(lambda x: x * 2,numbers))
print(result)

#FILTER X LAMBDA
filter(function, iterable)

result = list(filter(lambda x: x > 3, numbers))
print(result)

#PANDAS X LAMBDA
import pandas as pd

df = pd.DataFrame({
    "sales": [100,200,300]
})

df["tax"] = df["sales"].apply(lambda x: x * 0.07)
print(df)

names =[" ANA "," Juan "," peDRO "]
cleaned = list(map(lambda x: x.strip().lower(), names))

print(cleaned)

#NOTAS
LIST = "filter","Map","etc"
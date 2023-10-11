brasil={"Norte":{"Amazonas":"Manaus","Para":"Belem"},"Sul":{"Rio Grande do Sul":"Porto Alegre", "Santa Catarina":"Floripa"}}
print(len(brasil))
print(brasil)

brasil["Sudeste"]={"São Paulo":"São Paulo"}
print(brasil)
print(len(brasil))

r="Centro-oeste"
est="Mato-Grosso"
cap="Cuiabá"

brasil[r]={est:cap}
print(brasil)
print(len(brasil))

r="Centro-oeste"
est="Goias"
cap="Goiânia"

brasil[r][est]={cap}
print(brasil)
print(len(brasil))
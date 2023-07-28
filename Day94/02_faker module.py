from faker import Faker
fk = Faker()


print(fk.month())   # month Number
print()
print(fk.timezone())   # fake csv
print()
print(fk.language_name())   # fake csv
print()
print(fk.words())   # fake csv
print()
print(fk.month_name())   # fake csv
print()
print(fk.password())   # fake csv
print()
print(fk.random_digit())   # fake csv
print()
print(fk.random_int())   # fake csv
print()
print(fk.random_letter())   # fake csv
print()
print(fk.random_letters())   # fake csv
print()

print(fk.sentences())   # fake csv
print()
print(fk.zipcode())   # fake csv
print()
print(fk.profile())   # fake csv
print()

# generate hindi names
fk=Faker('hi-IN')
print(fk.name())
print()
print(fk.country())   # fake csv
print()
print(fk.address())   # fake csv
print()
print(fk.words())   # fake csv
print()




Faker.seed(1)
print(fk.profile())   # fake csv
print()
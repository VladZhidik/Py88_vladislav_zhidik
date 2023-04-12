baza = {
    'Dima':'123',
    'Maks':'345'
}
baza2 = {}
for i in baza:
    baza2.update({baza[i]:i})
print(baza2)
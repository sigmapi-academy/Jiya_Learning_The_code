import keyword

print("The list of keywords")

kw = keyword.kwlist

# print(kw)
slno = 1
for k in kw:
    print(slno,'. ',k, sep='')
    slno += 1

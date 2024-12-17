salery = int(input("your salery: "))
tax_free = 10000
if(salery<=tax_free):
  print("your tax free ")
  exit()
else:
  temp_salery = salery - tax_free
  # if(temp_salery<=10000):
print("your temp salery is ",temp_salery*0.1)
    
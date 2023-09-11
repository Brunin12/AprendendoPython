import random as rd

bt = "-"*10
isDuo = 0
time = 0
while isDuo < 5:
  print(f"{bt}Round {time + 1}{bt}")
  nums = [rd.randint(0,10), rd.randint(0,10), rd.randint(0,10), rd.randint(0,10), rd.randint(0,10)]

  print(f"numeros: {nums}")

  rep = []
  for i, elemento in enumerate(nums):
    if elemento in nums[i+1:]:
      if not elemento in rep:
        rep.append(elemento)

  if len(rep) > 0:
    print(f"numeros repetidos: {rep}", end="\n\n")
    isDuo+=1
  else:
    print("não existe numeros repetidos,", end="\n\n")
  time+=1
print(f"{bt}Fim{bt}")

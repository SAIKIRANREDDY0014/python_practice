for i in range(2,21):
    with open(f"./13-year_old_boy/table{i}.txt","a") as f:
      for j in range(1,11):
         f.write(f"{i} * {j} = {i*j}\n")  
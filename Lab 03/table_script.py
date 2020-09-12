def mult_table(nr,nc):
  table = "  "
  for c1 in range(1,nc+1):
    table += "{:4}".format(c1)
  table += "\n"
  print(table)
  
  for r in range(1,nr+1):
    table += "{:2}".format(r)
    for c2 in range(1,nc+1):
      table += "{:4}".format(r*c2)
    table += "\n"
  return(table)
    

if _name_ == "_main_":
  print(mult_table(12,12))

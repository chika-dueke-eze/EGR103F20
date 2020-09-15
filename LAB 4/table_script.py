def mult_table(nr=12,nc=12):         #define function that takes in two input, no of rows (nr) and no of columns (nc)
  table = "  "
  for c1 in range(1,nc+1):
    table += "{:4}".format(c1)
  table += "\n"
  
  for r in range(1,nr+1):
    table += "{:2}".format(r)
    for c2 in range(1,nc+1):
      table += "{:4}".format(r*c2)
    table += "\n"
  return(table)
    

if __name__ == "__main__":
  print(mult_table(12,12))

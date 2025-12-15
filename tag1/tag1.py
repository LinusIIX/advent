
ergebnis = 50
nullen = 0

with open("tag1in.txt") as f:
  for x in f:
    if x.startswith("R"):
      ergebnis = (ergebnis + int(x.split("R")[1]))%100
    elif x.startswith("L"):
      ergebnis = (ergebnis - int(x.split("L")[1]))%100
    if ergebnis == 0:
        nullen += 1
    
print(nullen)
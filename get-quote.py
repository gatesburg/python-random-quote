import random
def main():
    # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 16
  rnd = random.randint(0, last)
  print(quotes[rnd])
  print("\n".join(quotes)) #https://stackoverflow.com/questions/6167731/printing-list-elements-on-separated-lines-in-python



if __name__== "__main__":
  main()

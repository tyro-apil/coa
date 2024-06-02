from utils import FullSubtractor

def main():
  a=input("Enter first number: ")
  b=input("Enter second number: ")
  sub = FullSubtractor(a,b)
  print(sub)

if __name__=="__main__":
  main()
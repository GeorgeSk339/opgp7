from tvary import stvorec
from tvary import obdlznik
import tvary.kruh

print(f"Obvod štvorca o veľkosti 10 je {stvorec.obvod(10)}")
print(f"Obvod obdĺžnika o veľkosti 10 x 15 je {obdlznik.obvod(10, 15)}")
print(f"Obvod kruhu o veľkosti 10 je {tvary.kruh.obvod(10)}")

def faktorial(n):
    if n == 0: return 1
    return n * faktorial(n - 1)

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)

def obrat(s):
    if len(s) < 2: return s
    return s[-1] + obrat(s[:-1])

def main():
    print("V tomto module su nasledovné funkcie:")
    print(f"- Faktoriál (faktoriál čísla 30 je {faktorial(30)})")
    print(f"- Fibonacciho číslo (fibonacci na pozícii 30 je {fib(30)})")
    print(f"- Obrátenie reťazca ({obrat("Obrátenie reťazca")})")

if __name__ == '__main__':
    main()
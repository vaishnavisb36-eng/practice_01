import sys

def calculate_si(principal,rate,time):
    return (principal*rate*time)

if __name__=="__main__":
        
        p=int(sys.argv[1])
        r=float(sys.argv[2])
        t=int(sys.argv[3])



print("Simple Interest :",calculate_si(p,r,t))
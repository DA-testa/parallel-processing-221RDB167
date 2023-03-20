# python3

def parallel_processing(n, m, data):
    output = []
    nxt_free_time = [0]*n
    for i in range(m):
        min_free_time = min(nxt_free_time)
        j=nxt_free_time.index(min_free_time)
        output.append((j,min_free_time))
        nxt_free_time[j] += data[i]

    return output



def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    
    n,m = map(int,input(),split())
    data=list(map(int,input().split()))
    
    
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread, start_time in result:
        print(thread, start_time)


if __name__ == "__main__":
    main()

import numpy as np

def queue_time(customers,n):
    """Constructive solution; Recreation of the Queue Matrix"""
    if len(customers) == 0: return 0
    elif len(customers) <= n: return max(customers) 
    queues = np.zeros(shape=(n,len(customers))).astype('int')
    queues[:,0] = np.array([[customers[i]] for i in range(n)]).T
    for customer in customers[n:]:
        row_index = np.argmin(queues.sum(axis=1))
        queues[row_index,np.argmin(queues[row_index])] = customer
    return np.max(queues.sum(axis=1) , axis = 0)


def main():
    queue = [1,2,3,4,1,3,5,7,1,2]
    total_time = 12
    assert total_time == queue_time(queue,3)

    queue = np.random.randint(1,10,10)
    total_time = queue_time(queue,3)
    print(total_time)


if __name__ == "__main__": main()
























# def queue_time_silly(customers,n):
#     if len(customers) == 0: return 0
#     elif len(customers) <=n: return max(customers) 
#     queues = np.zeros(shape=(n,ceil(len(customers)/float(n)))).astype('int')
#     queues[:,0] = np.array([[customers[i]] for i in range(n)]).T
#     col , temp = 1 , queues[:,0].copy()
#     for c in customers[n:]:
#         if (queues[:,col] == 0).sum() == 0:
#             col += 1
#             temp = queues[:,col - 1].copy()
#         idx = np.argmin(temp)
#         queues[idx,col] = c
#         temp[idx] = temp.max() + 1
#     print(queues)
#     return np.max(queues.sum(axis=1) , axis = 0)

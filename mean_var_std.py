import numpy as np

def calculate(list) :
    if len(list) != 9 :
        raise ValueError("List must contain nine numbers.")

    matric = np.array(list).reshape(3,3)
    mean_results = [
        matric.mean(axis=0).tolist(),
        matric.mean(axis=1).tolist(),
        matric.mean().tolist()
    ]

    variance_results = [
        matric.var(axis=0).tolist(),
        matric.var(axis=1).tolist(),
        matric.var().tolist()
    ]

    std_results = [
        matric.std(axis=0).tolist(),
        matric.std(axis=1).tolist(),
        matric.std().tolist()
    ]

    max_results =[
        matric.max(axis=0).tolist(),
        matric.max(axis=1).tolist(),
        matric.max().tolist()
    ]

    min_results =[
        matric.min(axis=0).tolist(),
        matric.min(axis=1).tolist(),
        matric.min().tolist()
    ]

    sum_results =[
        matric.sum(axis=0).tolist(),
        matric.sum(axis=1).tolist(),
        matric.sum().tolist()
    ]

    calculations = {
        'mean': mean_results,
        'variance': variance_results,
        'standard deviation': std_results,
        'max': max_results,
        'min': min_results,
        'sum': sum_results
    }
    return calculations




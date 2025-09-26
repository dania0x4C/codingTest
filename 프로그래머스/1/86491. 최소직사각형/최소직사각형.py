def solution(sizes):
    W, H = 0, 0
    for a, b in sizes:
        h = max(a, b) # 60 70 60 80
        w = min(a, b) # 50 30 30 40
        
        H = max(h, H)
        W = max(w, W)
        
    return H * W
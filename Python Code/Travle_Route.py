from collections import deque 

# BFS
def BFS(tickets) :
    answer = []

    travel_q = deque()
    travel_q.append( ("ICN", ["ICN"], []) )

    while travel_q :
        current, path, used_idx = travel_q.popleft()

        if len(path) == len(tickets)+1 :
            answer.append(path)
        
        for idx, ticket in enumerate(tickets) :
            if ticket[0] == current and not idx in used_idx :
                travel_q.append( (ticket[1], path+[ticket[1]], used_idx+[idx]) )
    
    return sorted(answer)[0] 

def solution(tickets) :

    return BFS(tickets)



# 예제 실행 
data_1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
data_2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print("1번 문제 :", solution(data_1) )

print("2번 문제 :", solution(data_2) )
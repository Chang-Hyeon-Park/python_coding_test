'''
문제 설명
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간	     다리를 지난 트럭	다리를 건너는 트럭	  대기 트럭
0	            []	            []	                [7,4,5,6]
1~2	            []	            [7]	                [4,5,6]
3	            [7]	            [4]	                [5,6]
4	            [7]	            [4,5]	            [6]
5	            [7,4]	        [5]	                [6]
6~7	            [7,4,5]	        [6]	                []
8	            [7,4,5,6]	    []	                []
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

제한 조건
bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.
입출력 예
bridge_length	weight	truck_weights	                    return
2	            10	    [7,4,5,6]	                        8
100	            100	    [10]	                            101
100	            100	    [10,10,10,10,10,10,10,10,10,10]	    110
출처

※ 공지 - 2020년 4월 06일 테스트케이스가 추가되었습니다.
'''

'''
[전략]
1. 일단 truck_weights의 처음은 popleft를 함
2. count_time 변수가 필요함
3. 그 다음 popleft한거랑 아까 popleft한거랑 더한게 weight보다 낮거나 같으면 넣음
4. 그럼 이 current_weight변수가 업데이트가 필요함. 그래야 그 다음 popleft한거를 더해서 아직도 weight보다 작은지를 확인해야함
'''

# import sys
# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     dq = deque(truck_weights)
#     count_time = 0
#     current_weight = 0
#     current_bridge = [bridge_length]
#     while dq:
#         current_bridge.append(dq.popleft())
#         count_time += 1
#         if bridge_length > 1:
#             if current_weight + current_bridge[-1] > weight:
#                 dq.appendleft(current_bridge[-1])
#             else:
#                 current_bridge.append(dq.popleft())
#         else:
#             return len(truck_weights) + 1
        
#         if current_bridge[-1] == truck_weights[-1]:
#             return count_time + 1

# def main():
#     bridge_length = int(sys.stdin.readline())
#     weight = int(sys.stdin.readline())
#     truck_weights = list(map(int, sys.stdin.readline().split()))
#     print(solution(bridge_length, weight, truck_weights))

# if __name__ == "__main__":
#     main()
    
    


# Claude 답변
import sys
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    time = 0
    current_weight = 0
    
    while trucks:
        time += 1
        current_weight -= bridge.popleft()
        
        if current_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)
    
    return time + bridge_length

def main():
    bridge_length = int(sys.stdin.readline())
    weight = int(sys.stdin.readline())
    truck_weights = list(map(int, sys.stdin.readline().split()))
    print(solution(bridge_length, weight, truck_weights))
    
if __name__ == "__main__":
    main()
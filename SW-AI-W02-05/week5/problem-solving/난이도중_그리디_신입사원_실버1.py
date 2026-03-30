# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
import sys

def solve():
    # 테스트 케이스 개수 입력
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        n = int(sys.stdin.readline())
        # 성적 리스트 입력 (서류, 면접)
        applicants = []
        for _ in range(n):
            applicants.append(list(map(int, sys.stdin.readline().split())))
            
        # 1. 서류 성적(첫 번째 원소) 기준으로 오름차순 정렬
        applicants.sort()
        
        # 2. 첫 번째 사람(서류 1등)은 무조건 선발
        count = 1
        # 현재까지 선발된 사람 중 가장 우수한 면접 등수
        min_interview_rank = applicants[0][1]
        
        # 3. 두 번째 사람부터 비교
        for i in range(1, n):
            # 현재 사람의 면접 등수가 기준보다 높다면(숫자가 작다면) 선발
            if applicants[i][1] < min_interview_rank:
                count += 1
                # 기준을 현재 사람의 면접 등수로 갱신
                min_interview_rank = applicants[i][1]
                
        print(count)

if __name__ == "__main__":
    solve()
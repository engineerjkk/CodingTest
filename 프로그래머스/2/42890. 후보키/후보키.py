from itertools import combinations

def solution(relation):
    row_count = len(relation)   # 릴레이션의 행(row) 개수
    col_count = len(relation[0]) # 릴레이션의 열(column) 개수

    # 모든 열의 조합을 저장할 리스트
    all_combinations = []
    
    # 1개부터 col_count개까지의 열 조합을 생성
    for i in range(1, col_count + 1):
        all_combinations.extend(combinations(range(col_count), i))

    # 유일성을 만족하는 조합을 저장할 리스트
    unique_combinations = []

    # 유일성 체크
    for comb in all_combinations:
        # 각 조합에 대해 모든 튜플의 해당 열 값을 추출
        projected_tuples = []

        # 릴레이션의 각 행(row)에 대해 반복합니다.
        for row in relation:
            # 현재 행에서 조합(comb)에 해당하는 열(column)의 값만 추출합니다.
            current_tuple = []
            for col in comb:
                current_tuple.append(row[col])

            # 추출한 값들을 튜플로 변환하여 결과 리스트에 추가합니다.
            projected_tuples.append(tuple(current_tuple))

        # 추출한 튜플의 집합(set) 길이가 원래 행(row) 개수와 같다면 유일성을 만족
        if len(set(projected_tuples)) == row_count:
            unique_combinations.append(comb)

    # 최소성을 만족하는 조합만 남기기 위한 집합
    candidate_keys = set(unique_combinations)

    # 최소성 체크
    for i in range(len(unique_combinations)):
        for j in range(i + 1, len(unique_combinations)):
            # 하나의 조합이 다른 조합의 부분집합이면 최소성에 어긋남
            if set(unique_combinations[i]).issubset(set(unique_combinations[j])):
                candidate_keys.discard(unique_combinations[j])

    # 최종 후보 키의 개수를 반환
    return len(candidate_keys)

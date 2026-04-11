def solution(n, lost, reserve):
    # 도난당했지만 여벌도 가져온 학생은
    # 본인 체육복 1개는 입을 수 있으므로
    # 남에게 빌려줄 수 없고, 빌릴 필요도 없음
    # 따라서 lost와 reserve에 동시에 있는 학생은 먼저 제외
    real_lost = sorted([x for x in lost if x not in reserve])
    real_reserve = sorted([x for x in reserve if x not in lost])

    # 처음에는 체육복이 없는 학생 수만큼 수업을 못 듣는 상태이므로
    # 전체 학생 수에서 real_lost 길이를 뺀 값으로 시작
    answer = n - len(real_lost)

    # 체육복이 없는 학생들을 번호 순서대로 확인
    for student in real_lost:
        # 앞번호 학생이 여벌 체육복이 있으면 먼저 빌림
        if student - 1 in real_reserve:
            # 빌려준 학생은 더 이상 여벌이 없으므로 목록에서 제거
            real_reserve.remove(student - 1)
            # 체육복을 빌렸으니 수업 가능한 학생 수 1 증가
            answer += 1

        # 앞번호 학생에게 못 빌렸다면 뒷번호 학생에게 빌릴 수 있는지 확인
        elif student + 1 in real_reserve:
            # 빌려준 학생의 여벌 체육복 사용 처리
            real_reserve.remove(student + 1)
            # 체육복을 빌렸으니 수업 가능한 학생 수 1 증가
            answer += 1

    # 최종적으로 체육수업을 들을 수 있는 학생 수 반환
    return answer
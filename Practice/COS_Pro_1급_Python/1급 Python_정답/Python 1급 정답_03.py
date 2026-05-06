def solution(projects):
    projects.sort(key=lambda x: x[0])
    projects.sort(key=lambda x: x[2], reverse=True)
    projects.sort(key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in projects]
    return answer
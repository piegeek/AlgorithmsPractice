class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        S = []

        people = sorted(people)

        min_pointer = 0
        max_pointer = len(people) - 1

        visited = [False for _ in range(len(people))]

        while min_pointer < max_pointer:
            if people[min_pointer] + people[max_pointer] <= limit:
                S.append([people[min_pointer], people[max_pointer]])

                visited[min_pointer] = True
                visited[max_pointer] = True

                min_pointer += 1
                max_pointer -= 1

            elif people[max_pointer] <= limit:
                S.append([people[max_pointer]])

                visited[max_pointer] = True

                max_pointer -= 1

            elif people[min_pointer] <= limit:
                S.append([people[min_pointer]])

                visited[min_pointer] = True

                min_pointer += 1

        for i in range(len(people)):
            if visited[i] == False:
                S.append([people[i]])

        return len(S)
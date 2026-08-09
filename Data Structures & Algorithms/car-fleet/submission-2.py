class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []
        stack.append((target - cars[0][0]) / cars[0][1])
        print(cars)
        for car in cars:
            curr_t = (target - car[0]) / car[1]
            if stack and stack[-1] < curr_t:
                stack.append(curr_t)
        return len(stack)
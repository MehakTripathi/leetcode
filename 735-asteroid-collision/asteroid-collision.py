from typing import List

class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []
        for i in ast:
            # Only process collisions when the top is moving right and current is moving left
            while stack and stack[-1] > 0 and i < 0:
                if stack[-1] < -i:      # stack asteroid is smaller → it explodes
                    stack.pop()
                    continue
                elif stack[-1] == -i:  # both are same size → both explode
                    stack.pop()
                break
            else:
                # No collision → just push
                stack.append(i)
        return stack

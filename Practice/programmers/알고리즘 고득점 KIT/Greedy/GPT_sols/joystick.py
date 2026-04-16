def solution(name):
    n = len(name)
    
    # -----------------------------
    # Step 0: Vertical cost (independent)
    # -----------------------------
    vertical = 0
    for c in name:
        diff = ord(c) - ord('A')
        vertical += min(diff, 26 - diff)
    
    # -----------------------------
    # Step 1: Choose initial conditions
    # (no turn = baseline)
    # -----------------------------
    move = n - 1  # go straight right
    
    # -----------------------------
    # Step 2: Sweep in one direction
    # -----------------------------
    for i in range(n):
        
        # -----------------------------
        # Step 3: Forced action
        # Find next non-A position
        # -----------------------------
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1
        
        # Now:
        # i = turning point
        # j = next meaningful position
        
        # -----------------------------
        # Evaluate forced patterns
        # -----------------------------
        
		# See the below two cases are symmetrical
        # Case 1: go right → back → end
		# 0 -> i (to the right) -> 0 -> j (to the left)
        move1 = i * 2 + (n - j)
        
        # Case 2: go end → back → i
		# 0 -> j (to the left) -> 0 -> i (to the right)
        move2 = (n - j) * 2 + i
        
        move = min(move, move1, move2)
    
    # -----------------------------
    # Step 4: Validate (take min)
    # -----------------------------
    return vertical + move
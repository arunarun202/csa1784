import itertools

def solve_crypt_arithmetic():
    # Equation: SEND + MORE = MONEY
    words = ["SEND", "MORE", "MONEY"]
    
    # Get all unique characters
    unique_chars = set("".join(words))
    assert len(unique_chars) <= 10, "Too many unique characters!"
    
    chars = list(unique_chars)
    first_letters = {w[0] for w in words}

    # Try every permutation of numbers 0-9 for the unique characters
    for perm in itertools.permutations(range(10), len(chars)):
        char_map = dict(zip(chars, perm))
        
        # Leading digits cannot be zero
        if any(char_map[char] == 0 for char in first_letters):
            continue
            
        # Helper to convert word to integer based on mapping
        def word_to_val(word):
            return int("".join(str(char_map[c]) for c in word))
            
        send_val = word_to_val("SEND")
        more_val = word_to_val("MORE")
        money_val = word_to_val("MONEY")
        
        if send_val + more_val == money_val:
            print(f"Solution Found:")
            print(f"SEND: {send_val}, MORE: {more_val}, MONEY: {money_val}")
            print("Mapping:", char_map)
            return

    print("No solution found.")

solve_crypt_arithmetic()

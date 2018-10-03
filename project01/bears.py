# Returns whether it is not possible to win the bear game by starting with n bears.
# (Why bears?)

def bears(n):
    return (
        # The goal of the game is to end up with EXACTLY 42 bears
        n == 42 if n <= 42 else
        
        # If n is even, then you may give back n/2 bears.
        (n % 2 == 0 and bears(n / 2)) or
            
        # If n is divisible by 3 or 4, then you may multiply the last two digits of n and give back this many bears.
        ((n % 3 == 0 or n % 4 == 0) and bears(n - (n % 10) * (n // 10 % 10))) or
        
        # If n is divisible by 5, then you may give back 42 bears.
        (n % 5 == 0 and bears(n - 42))
    )
# array.py
import sys

def get_scores_from_argv():
    # join all argv parts except program name -> allows "python array.py 10 20 30" or "python array.py '10 20 30'"
    if len(sys.argv) <= 1:
        return None
    # If someone passed one argument that contains spaces, support that too:
    if len(sys.argv) == 2 and " " in sys.argv[1]:
        raw = sys.argv[1]
    else:
        # join all numeric arguments separated by spaces
        raw = " ".join(sys.argv[1:])
    try:
        return [int(x) for x in raw.split()]
    except ValueError:
        print("ERROR: All scores must be integers. Received:", raw)
        return None

def get_scores_from_input():
    raw = input("Enter scores separated by spaces: ")
    try:
        return [int(x) for x in raw.split()]
    except ValueError:
        print("ERROR: All scores must be integers.")
        return None

def main():
    scores = get_scores_from_argv()
    if scores is None:
        # fall back to interactive input when run locally
        scores = get_scores_from_input()
        if scores is None:
            return

    total = sum(scores)
    avg = total / len(scores) if scores else 0
    maximum = max(scores) if scores else None
    minimum = min(scores) if scores else None

    print("Scores:", scores)
    print("Sum:", total)
    print("Average:", avg)
    if maximum is not None and minimum is not None:
        print("Maximum:", maximum)
        print("Minimum:", minimum)

if __name__ == "__main__":
    main()
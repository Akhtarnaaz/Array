def get_scores():
    raw = input("Enter scores separated by spaces: ")
    scores = [float(score) for score in raw.split()]
    return scores

def main():
    scores = get_scores()
    total = sum(scores)
    average = total / len(scores) if scores else 0
    highest = max(scores) if scores else None
    lowest = min(scores) if scores else None
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Maximum: {highest}")
    print(f"Minimum: {lowest}")

if __name__ == "__main__":
    main()
    

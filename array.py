def get_scores():
    raw = input("Enter scores separated by spaces: ")
    scores = [float(score) for score in raw.split()]
    return scores

def main():
    scores = get_scores()
    total = sum(scores)
    average = total / len(scores) if scores else 0
    print(f"Sum: {total}")
    print(f"Average: {average}")

if __name__ == "__main__":
    main()

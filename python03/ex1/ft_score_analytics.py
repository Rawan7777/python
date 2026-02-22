#!/usr/bin/env python3

import sys

if __name__ == "__main__":

    scores = []

    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            for i in range(1, len(sys.argv)):
                scores.append(int(sys.argv[i]))
        except ValueError as error:
            print(f"Error: {error}")
        else:
            total_players = len(scores)
            total_scores = sum(scores)
            high_scores = max(scores)
            low_scores = min(scores)

            print(f"Scores processed: {scores}")
            print(f"Total players: {total_players}")
            print(f"Total score: {total_scores}")
            print(f"Average score: {total_scores / total_players}")
            print(f"High score: {high_scores}")
            print(f"Low score: {low_scores}")
            print(f"Score range: {high_scores - low_scores}")

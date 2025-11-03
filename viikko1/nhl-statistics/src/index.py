from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader

def main():
    stats = StatisticsService(
        PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt")
    )

    print("Top point getters:")
    for p in stats.top(5, SortBy.POINTS):
        print(p)

    print()
    for p in stats.top(5):
        print(p)

    print("\nTop goal scorers:")
    for p in stats.top(5, SortBy.GOALS):
        print(p)

    print("\nTop by assists:")
    for p in stats.top(5, SortBy.ASSISTS):
        print(p)

if __name__ == "__main__":
    main()

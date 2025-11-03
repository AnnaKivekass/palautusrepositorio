from player_reader import PlayerReader
from statistics_service import StatisticsService

def main():
    stats = StatisticsService(
        PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt")
    )

    print("Top 10 by points:")
    for p in stats.top(10, "points"):
        print(p)

    print("\nTeam TOR (first 5):")
    for p in stats.team("TOR")[:5]:
        print(p)

    one = stats.search("Connor McDavid")
    print("\nSearch Connor McDavid:", one or "not found")

if __name__ == "__main__":
    main()

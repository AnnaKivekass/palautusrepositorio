import re
from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table


def show_players(players, nationality, season):
    console = Console()
    if not players:
        console.print(f"[bold red]No players found for {nationality} in {season}[/bold red]")
        return

    table = Table(title=f"Top scorers from {nationality} ({season})")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Team", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="bold yellow")

    for p in players:
        table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.points))

    console.print(table)


def normalize_season(s: str) -> str:
    s = s.strip()
    if re.fullmatch(r"\d{4}", s):
        y = int(s)
        return f"{y}-{str((y+1) % 100).zfill(2)}"
    if re.fullmatch(r"\d{4}-\d{2}", s):
        return s
    raise ValueError("Season must be in format YYYY or YYYY-YY")


def main():
    season_input = input("Enter season (e.g. 2024-25): ").strip()
    season = normalize_season(season_input)
    nationality = input("Enter nationality (e.g. FIN, SWE, USA): ").strip().upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    show_players(players, nationality, season)


if __name__ == "__main__":
    main()

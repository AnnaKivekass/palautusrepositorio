import ssl
import urllib.request
from player import Player

class PlayerReader:
    def __init__(self, url: str):
        self._url = url

    def get_players(self):
        req = urllib.request.Request(
            self._url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; ohtu-course/1.0)"}
        )

        def fetch(context):
            with urllib.request.urlopen(req, context=context) as res:
                if hasattr(res, "status") and res.status != 200:
                    raise RuntimeError(f"HTTP {res.status} from {self._url}")
                return res.read().decode("utf-8", errors="replace")

        try:
            text = fetch(ssl.create_default_context())
        except Exception:
            text = fetch(ssl._create_unverified_context())

        text = text.strip()
        if not text:
            raise RuntimeError(f"Empty response from {self._url}")

        players = []
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            parts = [p.strip() for p in line.split(";")]
            if len(parts) < 4:
                continue

            name = parts[0]
            team = parts[1]
            try:
                goals = int(parts[-2] or 0)
                assists = int(parts[-1] or 0)
            except ValueError:
                continue

            team = team.split(",")[0].strip()

            players.append(Player(name, team, goals, assists))

        return players

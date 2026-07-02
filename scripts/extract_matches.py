import os
import json
import pandas as pd

matches = []

folder = "../raw_json"

for file in os.listdir(folder):

    if file.endswith(".json"):

        match_id = file.replace(".json", "")

        try:

            with open(
                os.path.join(folder, file),
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

            info = data["info"]

            teams = info["teams"]

            winner = ""

            outcome = info.get("outcome", {})

            if "winner" in outcome:
                winner = outcome["winner"]

            matches.append({
                "MatchID": match_id,
                "Date": info["dates"][0],
                "Team1": teams[0],
                "Team2": teams[1],
                "Venue": info["venue"],
                "Winner": winner,
                "TossWinner": info["toss"]["winner"],
                "TossDecision": info["toss"]["decision"]
            })

        except Exception as e:
            print(f"Error in {file}: {e}")

df = pd.DataFrame(matches)

print("Matches Found:", len(df))

os.makedirs("../processed_data", exist_ok=True)

df.to_csv(
    "../processed_data/matches.csv",
    index=False
)

print("matches.csv created successfully")
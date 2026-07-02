import os
import json
import pandas as pd

deliveries = []

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

            teams = data["info"]["teams"]
            team1 = teams[0]
            team2 = teams[1]

            innings_list = data["innings"]

            for innings_no, innings in enumerate(innings_list, start=1):

                batting_team = innings["team"]

                # Determine bowling team
                if batting_team == team1:
                    bowling_team = team2
                else:
                    bowling_team = team1

                for over in innings["overs"]:

                    over_no = over["over"]

                    for ball_no, delivery in enumerate(
                        over["deliveries"],
                        start=1
                    ):

                        wicket = 0

                        if "wickets" in delivery:
                            wicket = len(delivery["wickets"])

                        deliveries.append({
                            "MatchID": match_id,
                            "Innings": innings_no,
                            "BattingTeam": batting_team,
                            "BowlingTeam": bowling_team,
                            "Over": over_no,
                            "Ball": ball_no,
                            "Batter": delivery["batter"],
                            "Bowler": delivery["bowler"],
                            "NonStriker": delivery["non_striker"],
                            "Runs_Batter": delivery["runs"]["batter"],
                            "Runs_Extras": delivery["runs"]["extras"],
                            "Runs_Total": delivery["runs"]["total"],
                            "Wicket": wicket
                        })

        except Exception as e:
            print(f"Error in {file}: {e}")

df = pd.DataFrame(deliveries)

os.makedirs("../processed_data", exist_ok=True)

df.to_csv(
    "../processed_data/deliveries.csv",
    index=False
)

print("\nSUCCESS")
print("Rows:", len(df))
print("deliveries.csv updated with BowlingTeam")
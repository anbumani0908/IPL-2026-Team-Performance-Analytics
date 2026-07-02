import pandas as pd

df = pd.read_csv("../processed_data/deliveries.csv")

batting = (
    df.groupby(["Batter"])
    .agg(
        Runs=("Runs_Batter", "sum"),
        Balls=("Batter", "count"),
        Fours=("Runs_Batter", lambda x: (x == 4).sum()),
        Sixes=("Runs_Batter", lambda x: (x == 6).sum())
    )
    .reset_index()
)

batting["StrikeRate"] = (
    batting["Runs"] / batting["Balls"]
) * 100

batting = batting.sort_values(
    by="Runs",
    ascending=False
)

batting.to_csv(
    "../processed_data/batting_summary.csv",
    index=False
)

print("batting_summary.csv created")
print("Players:", len(batting))
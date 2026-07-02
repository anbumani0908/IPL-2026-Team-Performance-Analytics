import pandas as pd

df = pd.read_csv("../processed_data/deliveries.csv")

bowling = (
    df.groupby("Bowler")
    .agg(
        Balls=("Bowler", "count"),
        Runs=("Runs_Total", "sum"),
        Wickets=("Wicket", "sum")
    )
    .reset_index()
)

bowling["Overs"] = bowling["Balls"] / 6

bowling["Economy"] = (
    bowling["Runs"] / bowling["Overs"]
)

bowling = bowling.sort_values(
    by="Wickets",
    ascending=False
)

bowling.to_csv(
    "../processed_data/bowling_summary.csv",
    index=False
)

print("bowling_summary.csv created")
print("Bowlers:", len(bowling))
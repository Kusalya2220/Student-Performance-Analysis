import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("data/student_performance.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("STUDENT PERFORMANCE ANALYSIS")
print("\nDataset preview:")
print(df.head())

print("\nAverage scores:")
print(df[["math_score", "reading_score", "writing_score", "final_score"]].mean().round(2))

print("\nAverage final score by study-hours group:")
df["study_group"] = pd.cut(df["study_hours"], bins=[0, 2, 4, 6, 10], labels=["0-2", "2-4", "4-6", "6-10"])
print(df.groupby("study_group", observed=False)["final_score"].mean().round(2))

plt.scatter(df["study_hours"], df["final_score"])
plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours per Day")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "study_hours_vs_score.png")
print("\nChart saved to outputs/study_hours_vs_score.png")

df.groupby("attendance")["final_score"].mean().plot(kind="bar", title="Average Final Score by Attendance", xlabel="Attendance (%)", ylabel="Average Final Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "score_by_attendance.png")
print("Chart saved to outputs/score_by_attendance.png")

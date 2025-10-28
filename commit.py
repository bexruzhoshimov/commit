import os
import random
import datetime

start_date = datetime.date(2022, 10, 10)
end_date = datetime.date.today()
current_date = start_date

while current_date <= end_date:
    commit_count = random.randint(10, 20)
    print(f"{current_date} → {commit_count} commit...")

    with open("log.txt", "a") as f:
        for i in range(commit_count):
            f.write(f"{current_date} - commit {i}\n")

    os.system("git add log.txt")

    for i in range(commit_count):
        date_str = f"{current_date}T12:{i:02d}:00"
        os.environ["GIT_COMMITTER_DATE"] = date_str
        os.environ["GIT_AUTHOR_DATE"] = date_str
        os.system(f'git commit -m "Commit {i} on {current_date}" --date="{date_str}" >nul 2>&1')

    current_date += datetime.timedelta(days=1)

print("✅ Barcha commitlar chaqmoqdek tez bajarildi!")
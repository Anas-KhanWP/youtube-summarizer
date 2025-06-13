text = """- Title: Complicated Family Ties
- Summary: Two families, the Kamals and the Khans, have a tumultuous history with each other.

- Title: Love in Jeopardy
- Summary: Moiz falls in love with Shaani, Kiran's daughter, but their relationship is threatened when Kiran tries to take custody of her away from him.

- Title: Hidden Intentions
- Summary: Kiran's true intentions are revealed: he wants to take custody of Shaani because he feels abandoned by his wife and wants to keep his daughter close.

- Title: Loyalty and Betrayal
- Summary: Fizza is torn between her loyalty to her sister and her growing feelings for Moiz, as well as her desire to uncover the truth about Shaani's father.

- Title: Family Secrets Revealed
- Summary: Bilawal shares his understanding of life challenges with Kiran, warning him about the dangers of loneliness, but also encouraging him to talk to Shaani about his changing desires.

- Title: New Beginnings
- Summary: Feroz Bhai shares good news with Fizza about Anika's surgery and discovers some truth about their marriage breaking, giving Fizzo a new phone and a chance at a better life.

- Title: Deception and Manipulation
- Summary: Kiran tries to manipulate Fizza into telling the judge uncle that his biological father hits him, leading to a dramatic confrontation.
"""

titles_summaries = []
lines = text.strip().splitlines()
title = summary = None

for line in lines:
    line = line.strip()
    if line.startswith("- Title:"):
        title = line.replace("- Title:", "").strip()
    elif line.startswith("- Summary:"):
        summary = line.replace("- Summary:", "").strip()
        if title:  # Save only if title is present
            titles_summaries.append((title, summary))
            title = summary = None  # reset

# Output
print(f"Total Matches: {len(titles_summaries)}\n")
for i, (t, s) in enumerate(titles_summaries, 1):
    print(f"{i}. Title: {t}\n   Summary: {s}\n")

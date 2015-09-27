import csv
from empathy_at_work.scoring.scoring import EQ_SCORER, SQ_SCORER
from empathy_at_work.sources.fetcher import fetcher


def main():
    scored_rows = []

    for row in fetcher():
        eq_score = EQ_SCORER.score_row(row)
        sq_score = SQ_SCORER.score_row(row)

        row["EQ"] = eq_score
        row["SQ"] = sq_score

        scored_rows.append(row)

    with open("output_file.csv", "w") as of:
        fieldnames = sorted(scored_rows[0].keys())
        writer = csv.DictWriter(of, fieldnames=fieldnames)
        writer.writerow({f: f for f in fieldnames})
        writer.writerows(scored_rows)

if __name__ == '__main__':
    main()
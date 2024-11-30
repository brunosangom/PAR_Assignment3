# PAR - Assignment 3

## Linguistic Variables

1. Ratio of Null Hyperlinks (f60) → float [0, 100] (%)
   1. Low → [0, 0, 10, 25]
   2. Moderate → [15, 25, 35, 50]
   3. High → [45, 55, 100, 100]
2. Number of External CSS (f61) → int [0, 20] (#)
   1. Very Few → [0, 0, 1, 2]
   2. Few → [1, 2, 4, 5]
   3. Normal → [4, 5, 20, 20]
3. Domain Registration Length (f82) → int [1, 10] (years)
   1. Short → [1, 1, 2, 3]
   2. Medium → [2, 3, 5, 7]
   3. Long → [5, 7, 10, 10]
4. Web traffic (f84) → int [0, 100] (Percentile)
   1. Very Low → [0, 0, 10, 20]
   2. Low → [10, 20, 60, 70]
   3. Moderate → [60, 70, 80, 90]
   4. High → [80, 90, 100, 100]
5. Page rank (f87) → int [0, 10] (popularity score)
   1. Popular → [0, 0, 2, 3]
   2. Moderately known → [2, 3, 5, 7]
   3. Not very known → [5, 7, 10, 10]
6. Phishing risk (output) → int [0, 100] (%)
   1. Safe → [0, 0, 15, 25]
   2. Weakly Suspicious → [15, 25, 35, 45]
   3. Strongly Suspicious → [45, 55, 65, 75]
   4. Phishing → [65, 75, 100, 100]

## Rules

| Rule | Null Hyperlinks | External CSS | Domain Registration | Web Traffic | Page Rank        | Phishing Risk |
| ---- | --------------- | ------------ | ------------------- | ----------- | ---------------- | ------------- |
| 1    | High            | Very Few     | Short               | Very Low    | Not very known   | Very High     |
| 2    | High            | Few          | Short               | Low         | Not very known   | Very High     |
| 3    | High            | Normal       | Short               | Moderate    | Not very known   | Very High     |
| 4    | High            | Very Few     | Medium              | Low         | Moderately known | High          |
| 5    | High            | Few          | Medium              | Moderate    | Moderately known | High          |
| 6    | High            | Normal       | Medium              | High        | Moderately known | High          |
| 7    | High            | Very Few     | Long                | Moderate    | Popular          | Moderate      |
| 8    | High            | Few          | Long                | High        | Popular          | Moderate      |
| 9    | High            | Normal       | Long                | High        | Popular          | Moderate      |
| 10   | Moderate        | Very Few     | Short               | Very Low    | Not very known   | High          |
| 11   | Moderate        | Few          | Short               | Low         | Not very known   | High          |
| 12   | Moderate        | Normal       | Short               | Moderate    | Not very known   | High          |
| 13   | Moderate        | Very Few     | Medium              | Low         | Moderately known | Moderate      |
| 14   | Moderate        | Few          | Medium              | Moderate    | Moderately known | Moderate      |
| 15   | Moderate        | Normal       | Medium              | High        | Moderately known | Moderate      |
| 16   | Moderate        | Very Few     | Long                | Moderate    | Popular          | Low           |
| 17   | Moderate        | Few          | Long                | High        | Popular          | Low           |
| 18   | Moderate        | Normal       | Long                | High        | Popular          | Low           |
| 19   | Low             | Very Few     | Short               | Very Low    | Not very known   | Moderate      |
| 20   | Low             | Few          | Short               | Low         | Not very known   | Moderate      |
| 21   | Low             | Normal       | Short               | Moderate    | Not very known   | Moderate      |
| 22   | Low             | Very Few     | Medium              | Low         | Moderately known | Low           |
| 23   | Low             | Few          | Medium              | Moderate    | Moderately known | Low           |
| 24   | Low             | Normal       | Medium              | High        | Moderately known | Low           |
| 25   | Low             | Very Few     | Long                | Moderate    | Popular          | Very Low      |
| 26   | Low             | Few          | Long                | High        | Popular          | Very Low      |
| 27   | Low             | Normal       | Long                | High        | Popular          | Very Low      |
| 28   | High            | Very Few     | Short               | High        | Not very known   | Very High     |
| 29   | Moderate        | Few          | Medium              | Very Low    | Moderately known | High          |
| 30   | Low             | Normal       | Long                | Very Low    | Popular          | Low           |
| 31   | High            | Few          | Medium              | Very Low    | Not very known   | Very High     |
| 32   | Moderate        | Normal       | Short               | High        | Moderately known | High          |
| 33   | Low             | Very Few     | Medium              | Very Low    | Moderately known | Moderate      |
| 34   | High            | Normal       | Long                | Low         | Popular          | Moderate      |
| 35   | Low             | Few          | Short               | High        | Not very known   | Moderate      |

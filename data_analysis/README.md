# Data Analysis

Back to the [repository README](../README.md).

Every data project starts with two questions: *where does the data come from?* and *can I trust and use it?* This folder has one project for each.

| Project | Question it answers | Input | Output |
|---|---|---|---|
| [web_scraping/](web_scraping/README.md) | How do I get data that only exists on a website? | URLs | Python lists of dicts |
| [data_preparation_visualization/](data_preparation_visualization/README.md) | How do I turn a raw table into something a model can learn from? | A CSV file | Train/test splits |

## How the projects fit together

```
website ──(web_scraping)──► structured records ──(save as table)──► raw dataset
                                                                        │
model-ready splits ◄──(data_preparation_visualization)── clean, explore, test, engineer
```

The two projects are independent and use different datasets, but they form the front half of a typical machine-learning workflow: **acquire**, then **prepare**. Modeling comes next.

## Skills practiced

- **Acquisition:** HTTP requests, HTML parsing, pagination, JSON APIs, JSON-LD, sessions and CSRF tokens, headless browsers, infinite scroll.
- **Preparation:** type fixing, missing-value strategies, deduplication, feature engineering, encoding, scaling, stratified splitting.
- **Analysis:** distribution plots, correlation, hypothesis testing (chi-square, Welch t-test).

## Next

- Start with [web_scraping/](web_scraping/README.md), or
- Go to [data_preparation_visualization/](data_preparation_visualization/README.md).

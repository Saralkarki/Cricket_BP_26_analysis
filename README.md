# An Analysis of Player's Performances in the 2014 Twenty20 World Cup Series

**Final Report:** https://medium.com/@Saral.karki/an-analysis-of-players-performances-in-the-2014-twenty20-world-cup-series-607930504939

## Overview

This study is a replication of "AN ANALYSIS OF PLAYERS' PERFORMANCES IN THE FIRST CRICKET TWENTY20 WORLD CUP SERIES" by Hermanus H. LEMMER. In this research, LEMMER examines how batting and bowling performance measures developed for One Day Internationals can be adapted for use in Twenty20 matches, particularly in cases with very small match samples. These measures are then applied to rank the best-performing batsmen and bowlers in the entire T20 series.

LEMMER's original analysis focused on 2007 data. This replication extends the analysis to the 2013 T20 World Cup held in Bangladesh, with a specific focus on comparing Nepali batsmen playing in their first international T20 World Cup against other players. Additionally, this project serves as a practice dataset for data analysis using Python.

## Introduction

The Twenty20 form of cricket, where each team bats for twenty overs, has become increasingly popular since its introduction in 2003. With only twenty overs per side, T20 cricket is fast-paced and exciting, encouraging aggressive batting strategies aimed at maximizing run accumulation. The first T20 World Cup was held in South Africa in 2007, won by India.

Various batting and bowling performance measures have been developed for Test matches and One Day Internationals. However, adapting these measures to T20 cricket presents unique challenges due to:
- The very short history of T20 cricket during the first World Cup
- Small sample sizes for individual batsmen
- The need for measures that account for not-out scores and strike rates

This analysis applies necessary modifications to existing performance measures to rank players from Nepal and other countries based on their tournament performance.

## Batting Analysis Methodology

### Data Collection
The maximum number of matches played by any batsman in this tournament was seven. Only batsmen with three or more innings were considered for the analysis. All scores were obtained from Cricinfo.

### Performance Measures

#### Limitations of Traditional Averages
While batting average (AVE = R/out) is commonly used, it is not suitable for batsmen with a small number of innings and a high proportion of not-out scores.

#### The e2 and e6 Measures
Based on Lemmer (2008), two key performance measures were adopted:

**e2 = (Sumout + 2 × Sumno) / n**

Where:
- Sumout = sum of all scores when batsman was out
- Sumno = total runs scored when not out
- n = number of innings played

The rationale: if a batsman was not out, they could have potentially doubled their score had they continued batting until dismissal.

**e6 = (Sumout + f6 × Sumno) / n**

Where f6 = 2.2 – 0.01 × avno (avno is the average of not-out scores)

Studies show that e6, with its adaptive factor, provides the best overall measure, with e2 as a close second.

#### The e26 Measure
For batsmen with large not-out proportions showing significant differences between e2 and e6:

**e26 = (e2 + e6) / 2**

### The BP26 Measure

The final performance measure combines the batting average adjustment with strike rate adjustment:

**BP26 = e26 × (SR / avSR)^0.50**

Where:
- e26 = the combined batting measure
- SR = individual batsman's strike rate
- avSR = average strike rate across the tournament
- 0.50 = the strike rate exponent (updated from 0.43)

For batsmen playing their first international T20, career consistency and career strike rate (required in original Lemmer formulas) are not available. Therefore, this analysis ranks batsmen solely on tournament performance using the BP26 measure.

## Key Findings

### Nepali Batsmen Performance
Nepali batsmen performed well in the tournament and rank within the top 50 worldwide:

- **Gyanendra Malla** achieved the highest ranking among Nepali batsmen at **29th position**
- Despite not having the highest average among Nepali batsmen, Malla's BP26 score reflects superior tournament effectiveness through better strike rate and consistency

### Notable Observations
- Batsmen with significant not-out innings who would be underrepresented by traditional averages are better captured by the BP26 measure
- Example: T Maruma from Zimbabwe (35th position) had three not-out innings and would have no ranking using average-based rankings alone

## Technologies & Data Sources

- **Language:** Python
- **Data Source:** Cricinfo (ESPN Cricket Info)
- **Analysis Focus:** 2013 T20 World Cup (Bangladesh)

## References

- BASEVI, T. & BINOY, G. (2007). The world's best Twenty20 players. Cricinfo. Retrieved from http://contentrsa.cricinfo.com/columns/content/story/311962.html

- CRICINFO (2014). Statsguru. Retrieved from http://stats.espncricinfo.com/world-t20/engine/records/averages/batting.html?id=8083;type=tournament

- CRICINFO (2014). Cricket Statistics. Retrieved from http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;host=25;orderby=batting_average;season=2013%2F14;template=results;trophy=89;type=batting;view=innings

- LEMMER, H.H. (2002). The combined bowling rate as a measure of bowling performance in cricket. South African Journal for Research in Sport, Physical Education and Recreation, 24(2): 37–44.

- LEMMER, H.H. (2004). A measure for the batting performance of cricket players. South African Journal for Research in Sport, Physical Education and Recreation, 26(1): 55–64.

- LEMMER, H.H. (2005). A method for the comparison of the bowling performances of bowlers in a match or a series of matches. South African Journal for Research in Sport, Physical Education and Recreation, 27(1): 91–103.

- LEMMER, H.H. (2006). A measure of the current bowling performance in cricket. South African Journal for Research in Sport, Physical Education and Recreation, 28(2): 91–103.

- LEMMER, H.H. (2007). The allocation of weights in the calculation of batting and bowling performance measures. South African Journal for Research in Sport, Physical Education and Recreation, 29(2): 75–85.

- LEMMER, H.H. (2008). An analysis of players performance in the first cricket Twenty20 world cup series. South African Journal for Research in Sport, Physical Education and Recreation, 30(2): 71–77.

- LEMMER, H.H. (2008a). Measures of batting performance in a short series of cricket matches. South African Statistical Journal, 42(1): 83–105.

- LEMMER, H.H. (2008b). Batting and bowling performance measures for List-A and First Class matches. South African Journal for Research in Sport, Physical Education and Recreation.
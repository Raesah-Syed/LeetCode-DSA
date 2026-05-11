-- Last updated: 5/11/2026, 12:18:54 PM
# Write your MySQL query statement below
SELECT score,
dense_rank() over (order by score desc) as 'rank'
from Scores
1. Display all the data from the houseware table.

```
SELECT *
FROM houseware
```

2. Get just the name of every houseware.

```
SELECT name
FROM houseware
```

3. Get just the name and price of every houseware.

```
SELECT name, buy_price
FROM houseware
```

4. [DISTINCT] Get the name of every recipe material (no duplicates).

```
SELECT DISTINCT material
FROM recipe
```

5. [WHERE] What houseware items can be sold for at least 1000 bells? 

```
SELECT *
FROM houseware
WHERE sell_price >= 1000
```

6. [WHERE] I want to find any houseware that can fit in a 1x1 space (width x height) that costs less than 1000 bells.

```
SELECT *
FROM houseware
WHERE buy_price < 1000 AND width <= 1 AND height<= 1
```

7. [WHERE, LIKE] I'm looking for stuff that involves the word office, but there's no office tag. Get me a list of all the names that involve the word 'office'.

```
SELECT name
FROM houseware
WHERE name LIKE '%office%'
```

8. [COUNT] How many houseware items are there?

```
SELECT COUNT(*)
FROM houseware
```

9. [WHERE with COUNT] How many many items can be bought for less than 1000 bells?

```
SELECT COUNT(*)
FROM houseware
WHERE buy_price < 1000
```

10. [AGGREGATION] How much is the average buying price divided by selling price?

```
SELECT AVG(buy_price/sell_price)
FROM houseware
```

11. [AGGREGATION, TYPES] How much is the average selling price divided by buying price, rounded to two decimal places?

```
SELECT ROUND(AVG(sell_price*1.0/buy_price),2)
FROM houseware
```

12. [ORDER] Produce a list of all the names of the houseware items and their sell price, ordered by their sell price.

```
SELECT name, sell_price
FROM houseware
ORDER BY sell_price
```

13. [ORDER, LIMIT] Now produce the list of names+buy_price, ordered by buy_price descending, limited to the top 10.

```
SELECT name, buy_price
FROM houseware
ORDER BY buy_price DESC
LIMIT 10
```

14. [ORDER, ALIAS] The hha_base is a number indicating how "nice" the item is. I want to find items that are have a higher hha_base per square unit of space. Produce a list of the names of items, sorted by their hha_base divided by the area they take up.

```
SELECT name, hha_base/(width*height) AS RatingPerArea
FROM houseware
ORDER BY hha_base/(width*height)DESC
```

15. [GROUP BY] How many houseware items are in each tag? Make sure you order them by frequency!

```
SELECT tag, COUNT(*)
FROM houseware
GROUP BY tag
ORDER BY COUNT(tag)
```

16. [GROUP BY, ALIAS] There's actually only a few different possible areas for the given objects. How many are there of each possible area?

```
SELECT width*height AS Area, COUNT(*) as Count
FROM houseware
GROUP BY width*height

```

17. [GROUP BY, AGGREGATION] How much would it cost to buy all the items, within each tag? For example, the Audio tag's items would cumulatively cost 103600

```
SELECT tag, SUM(buy_price)
FROM houseware
GROUP BY tag
```

18. [GROUP BY, WHERE, AGGREGATION] How much area would all the interactable houseware items take, within each tag?

```
SELECT tag, SUM(height*width) AS TotalArea
FROM houseware
WHERE interact = 1
GROUP BY tag
```

19. [JOIN, GROUP BY] For each item, how many distinct materials does it require?

```
SELECT houseware_recipe.houseware_id, houseware_recipe.recipe_id,
 houseware.name, COUNT(recipe.material) AS NumMaterials
FROM ((houseware_recipe
INNER JOIN recipe
ON recipe.recipe_id = houseware_recipe.recipe_id)
INNER JOIN houseware 
ON houseware.id = houseware_recipe.houseware_id)
GROUP BY name
ORDER BY houseware_recipe.recipe_id
```

20 [GROUP BY, ORDER, LIMIT] What are the top 10 materials used in recipes (calculated by totaling the amounts per material).

```
SELECT material, SUM(amount)
FROM recipe
GROUP BY material
ORDER BY SUM(amount) DESC
LIMIT 10
```

21. [JOIN, WHERE] List all the recipes that require at least 10 star fragments

```
SELECT houseware_recipe.houseware_id, houseware_recipe.recipe_id,
 houseware.name, recipe.material, recipe.amount
FROM ((houseware_recipe
INNER JOIN recipe
ON recipe.recipe_id = houseware_recipe.recipe_id)
INNER JOIN houseware 
ON houseware.id = houseware_recipe.houseware_id)
WHERE material='star fragment' AND amount >= 10
```

22. [JOIN, WHERE, GROUP BY, ORDER] What tag has the most recipes that require 'stone'?

```
SELECT tag, COUNT(*)
FROM ((houseware_recipe
INNER JOIN recipe
ON recipe.recipe_id = houseware_recipe.recipe_id)
INNER JOIN houseware 
ON houseware.id = houseware_recipe.houseware_id)
WHERE material='stone'
GROUP BY tag
ORDER BY COUNT(*) DESC
LIMIT 1
```

23. [JOIN, WHERE] Get the names and colors of all housewares.

```
SELECT name, variation
FROM houseware
INNER JOIN variation
ON houseware.id = variation.houseware_id
```
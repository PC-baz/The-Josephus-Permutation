# The Josephus Permutation

This program is use for Solve the **Josephus problem** (or **Josephus permutation**) .



# Usage

Calling main Script.
```
> python ./main.py [-h] number
```
Calling application(.exe).
```
> ./Josephus.exe [-h] number
```

## [About Josephus Problem](https://en.wikipedia.org/wiki/Josephus_problem)

From [Wikipedia](https://en.wikipedia.org), the free encyclopedia
In  [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science")  and  [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), the  **Josephus problem**  (or  **Josephus permutation**) is a theoretical problem related to a certain  [counting-out game](https://en.wikipedia.org/wiki/Counting-out_game "Counting-out game"). Such games are used to pick out a person from a group, e.g.  [eeny, meeny, miny, moe](https://en.wikipedia.org/wiki/Eeny,_meeny,_miny,_moe "Eeny, meeny, miny, moe").

[![](https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/JosephusProblemDrawing.png/220px-JosephusProblemDrawing.png)](https://en.wikipedia.org/wiki/File:JosephusProblemDrawing.png)

A drawing for the Josephus problem sequence for 500 people and skipping value of 6. The horizontal axis is the number of the person. The vertical axis (top to bottom) is time (the number of cycle). A live person is drawn as green, a dead one is drawn as black.[[1]](https://en.wikipedia.org/wiki/Josephus_problem#cite_note-formulae.org-1)

In the particular counting-out game that gives rise to the Josephus problem, a number of people are standing in a  [circle](https://en.wikipedia.org/wiki/Circle "Circle")  waiting to be executed. Counting begins at a specified point in the circle and proceeds around the circle in a specified direction. After a specified number of people are skipped, the next person is executed. The procedure is repeated with the remaining people, starting with the next person, going in the same direction and skipping the same number of people, until only one person remains, and is freed.

The problem—given the number of people, starting point, direction, and number to be skipped—is to choose the position in the initial circle to avoid execution.
....
[Read more on wikipedia.](https://en.wikipedia.org/wiki/Josephus_problem)

##  Contributing
For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

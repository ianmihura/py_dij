# Dijkstra's algorithm in Python

Using Dijkstra's basic path-finding algorithm to search simple, bi-directional, weighted graphs.

The shape of the graph should be:

```json
{
    "AB": 2,
    ...
}
```

Where A & B are two nodes connected with an edge of weight 2

The object constructed in the file main.py has to be instanciated with this json, and when called will compute the shortest path.
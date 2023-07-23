# hemapriya-project
PYGAME PROJECT
Certainly! Let's go through the program step by step, explaining each part for beginners:

1. Import the `turtle` module:
   The first step is to import the `turtle` module, which provides the tools for drawing graphics. It allows us to control a small turtle that can draw lines, shapes, and patterns on the screen.

2. Define drawing functions:
   Next, we define four functions: `draw_square`, `draw_triangle`, `draw_circle`, and `draw_petal`. These functions define the shapes that the turtle will draw on the screen.

3. Set up the turtle:
   We set up the turtle by specifying some initial settings like the drawing speed, background color, and pen size. The turtle's initial position is at the center of the screen.

4. Draw the first pattern using squares, triangles, and circles:
   The first part of the pattern involves drawing 36 repetitions of a combination of squares, triangles, and circles. The turtle will draw each shape one after the other, and after completing one pattern, it will rotate slightly and start drawing the next pattern. This process continues until all 36 patterns are drawn.

5. Reset the turtle's position:
   After drawing the first pattern, we reset the turtle's position and orientation so that it moves to the right side of the screen. This way, we'll have space between the two patterns.

6. Draw the second pattern (flower-like pattern):
   The second part of the pattern involves drawing 36 repetitions of a colorful flower-like shape. The `draw_petal` function is used to draw each petal of the flower. Like in the first pattern, the turtle rotates slightly after drawing each petal.

7. Hide the turtle:
   Once both patterns are drawn, we hide the turtle, so it's not visible on the screen.

8. Keep the window open:
   The `turtle.done()` function keeps the window open until you manually close it. This allows you to observe the completed artwork.

The program's primary components are the drawing functions and the use of loops to create repetitive patterns. By combining basic shapes and rotating the turtle at different angles, we can create visually appealing patterns and artworks. Feel free to modify the shapes, colors, and rotations to create your unique drawings using the Turtle graphics library!

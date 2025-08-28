#drawing the moon and the sun 
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Sun and Moon")
screen.setup(width=800, height=600)

# Function to create gradient background
def create_gradient_background():
    """Step 1: Create a beautiful gradient sky background"""
    artist.speed(0)  # Fastest speed for background
    
    # Draw horizontal strips from top to bottom with changing colors
    colors = ["#000428", "#004e92", "#1e3c72", "#2a5298", "#3b73c4"]  # Dark blue to lighter blue
    
    # Each strip is 120 pixels tall (600/5 = 120)
    strip_height = 120
    
    for i, color in enumerate(colors):
        artist.penup()
        artist.goto(-400, 300 - (i * strip_height))  # Start from top-left
        artist.pendown()
        artist.color(color)
        artist.begin_fill()
        
        # Draw rectangle for this color strip
        for _ in range(2):
            artist.forward(800)  # Width of screen
            artist.right(90)
            artist.forward(strip_height)  # Height of strip
            artist.right(90)
        
        artist.end_fill()

# Create a turtle
artist = turtle.Turtle()
artist.speed(5)

# Function to draw the sun
def draw_sun():
    # Move to sun position (left side)
    artist.penup()
    artist.goto(-200, 100)
    artist.pendown()
    
    # Draw sun body (yellow circle)
    artist.color("yellow")
    artist.begin_fill()
    artist.circle(60)
    artist.end_fill()
    
    # Draw sun rays
    artist.color("orange")
    artist.pensize(3)
    
    # Move to center of sun
    artist.penup()
    artist.goto(-200, 160)
    artist.pendown()
    
    # Draw 8 rays around the sun
    for i in range(8):
        artist.forward(40)
        artist.backward(40)
        artist.right(45)

# Function to draw the moon
def draw_moon():
    # Move to moon position (right side)
    artist.penup()
    artist.goto(200, 100)
    artist.pendown()
    
    # Draw moon body (light gray circle)
    artist.color("lightgray")
    artist.begin_fill()
    artist.circle(50)
    artist.end_fill()
    
    # Draw craters on the moon
    artist.color("gray")
    
    # Crater 1
    artist.penup()
    artist.goto(185, 120)
    artist.pendown()
    artist.begin_fill()
    artist.circle(8)
    artist.end_fill()
    
    # Crater 2
    artist.penup()
    artist.goto(210, 110)
    artist.pendown()
    artist.begin_fill()
    artist.circle(5)
    artist.end_fill()
    
    # Crater 3
    artist.penup()
    artist.goto(195, 95)
    artist.pendown()
    artist.begin_fill()
    artist.circle(6)
    artist.end_fill()

# Function to draw stars
def draw_stars():
    artist.color("white")
    artist.pensize(1)
    
    # Draw several small stars
    star_positions = [(-100, 200), (50, 250), (-300, 150), (300, 180), 
                     (-50, 50), (100, 30), (-250, 50), (250, 50)]
    
    for x, y in star_positions:
        artist.penup()
        artist.goto(x, y)
        artist.pendown()
        
        # Draw a simple star
        for i in range(5):
            artist.forward(10)
            artist.right(144)

# Draw everything
draw_sun()
draw_moon()
draw_stars()

# Add some text
artist.penup()
artist.goto(-100, -200)
artist.pendown()
artist.color("white")
artist.write("Sun and Moon", align="center", font=("Arial", 20, "bold"))

# Hide the turtle and keep window open
artist.hideturtle()
screen.exitonclick()  # Click to close

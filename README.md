# Shopping List App :shopping_cart:
A shopping list app that allows you to organise your grocery list easier. You can search for recipes, add ingredients to your shopping list from any recipe. You can also add items to your fridge that you already have at home. The shopping list will take them into account for you! 
## :computer: [Click here](https://shopping-list-app-vjul.onrender.com/) to register!
## :page_facing_up: About
**How to use the app:**
1. Sign up to the app.
2. Log in into your personal shopping list.
3. Add ingredients into your Fridge list that you already have at home.
4. You can add new, remove and update your shopping list items as much as you want, as well as your fridge items.
5. Search for recipes to cook for the week.
6. Click on a recipe that you like and tick the ingredients.
7. Press 'Add ingredients to the shopping list' to add them into your personal shopping list.
8. Then take the list to a grocery shop with you! 
9. As you pick up the items from the store you can delete them from your shopping list.
 
<img src="./readme_img_resources/app_preview.png" alt="image of the app preview" width="auto" height="800px">

## :pencil2: Planning & Problem Solving
I started off by dotting down the key requirements of the MVP that I'll have to meet, which were then integrated into a plan:
1. Render a game in the browser
2. Switch turns between more than one player.
3. Design logic for winning & visually display which player won.
4. Use Javascript (JS) for DOM manipulation.

To meet the requirements of the MVP I had to write three separate files for HTML, CSS and JS. The major stages of ther project were written out as below:
1. Write two headings and establish 9 divs for the future Tic Tac Toe squares inthe HTML file.
2. Edit the CSS file to organise the divs in a 3x3 grid.
3. In the JS create a function to take turns that doesn’t allow players click more than once on a grid's square.
4. Still in JS write if statements to determine a winner and if it’s a draw.

After writing out exactly how I would achieve each of the above I was able to go forward and start writing my code, testing the code and fixing any bugs that came up along the way.
![picture of notes with code startegy](./resources/screenshot1.png)

### :sunglasses: Post-MVP
After the MVP was delivered with the remaining time I decided to add more features to the game to make it more user-friendly: 
1. A button that resets the game.
2. A game tracker that will count game rounds and the players' wins. 
![picture of notes with code startegy](./resources/screenshot2.png)

I also played around with the CSS by adding a background image, replacing the original images of crosses and noughts with fried shrimps and dumplings, and addinf some animations for fun.

## :rocket: Cool tech
- JS, HTML, CSS, DOM manipulation;
- Libraries: Animate.css, Bootstrap;
- Animation: change in the color of the 'game name', animation on the shrimp and dumpling with the help of Animate.css;
- Added emojis in CSS and HTML for the shrimp and dumpling instead of images.

## :scream: Bugs to fix :poop:
- Website needs to be adjusted for screens of other sizes, e.g. the mobile interface.

## :sob: Lessons learnt
- Planning is important for the wellbeing of the code, as well as my mental wellbeing.
- Get different people to test the game ahead of the deadline to find unnoticed bugs.

## :white_check_mark: Future features
- A feature that allows a player to enter their name.
- A feature that allows to pick a Yum-Cha food to play with instead of only fried shrimp and dumpling.
- Sound effects for game immersion: player clicks and background music.
- An option to play against the computer with different levels of difficulty.

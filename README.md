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


## :rocket: Cool tech
- HTML, CSS, Python, Psycopg2, Flask, requests, CRUD, gunicorn, Render, Postgresql;
- External API: [Sponacular](https://spoonacular.com/food-api);
- Libraries: Animate.css, Bootstrap;
- Animation: when a page loads the content fades in for a more pleasant user experience (Animate.css);
- All the passwords are securely stored through bcrypt hashing and salthing.

## :scream: Bugs to fix :poop:
- If an item exists in the shopping list and a user adds the same item to their fridge list then for it to be removed from the shopping list the page needs to be reloaded.
- If an item is in the shopping list already, then it cannot be added again. It would be better to improve this => when an exisiting item gets added the shopping list will show "2x" that item. 
- Website is not adjusted for screens of different sizes, e.g. the mobile interface.

## :sob: Lessons learnt
- Planning is important for the wellbeing of the code, as well as my mental wellbeing.
- Get different people to test the game ahead of the deadline to find unnoticed bugs.

## :white_check_mark: Future features
- Save button for recipes.
- A page with saved recipes.
- Displaying the fridge items on the main screen as a list, so that the user can view them without needing to click on the 'View and edit all' link.
- Add a 'Check all' button on the individual recipe pages to save the user time checking all the items.
- When an item already exists in the fridge and a user tries to add it to their shopping list: display a message ‘Item already exists, are you sure you want to add it?’. This will give the user an option to add an exisiting item to the shopping list.
- Add update all button instead of individual updates for the shopping list and fridge in case a user wants to bulk-update their items.

# Animal Trading Card Instructions

The Lab starts with the following files:

* `card.html`
* `clownfish.jpg`
* `design-prototype.jpg`
* `styles.css`

Your job is to try and recreate what you see in the `design-prototype.jpg`. You’ll need to modify `card.html` to include `attributes` and use CSS `selectors` to style specific elements.

## ⚠️ Important ⚠️

**Please do not remove or alter any existing `id` attributes in `card.html`!**

The `card.html` file comes with some initial HTML. A few HTML elements already have `id` attributes. The validation code _requires_ these exact `id`s on these exact elements, so do not remove them or the validation will fail.

## 🛠 Required Changes ⚙️

Make the following changes to `card.html`

1. Change the heading to the name of your favorite animal
2. Replace the placeholder image with your favorite animal's image.

    Also, change the image's `alt` attribute to the name of your animal.
    So, `alt="name-of-your-animal"` should be replaced with the actual name of your animal.

    Note: You will want to use an image with a `width` of 300 pixels. If your image is larger, you can set the image's width to 300 pixels in your CSS, but be aware that your image might end up squished or distorted. Later, we’ll talk about how you can fix this problem using responsive images.

3. Edit the interesting fact paragraph
4. Edit the key characteristics
5. Edit the informational paragraph

## 💃 Style the Page 🕺

The CSS must apply these styles to match the design prototype:

  1. link your stylesheet `styles.css` to the HTML or else your CSS will not be applied.
  2. give the interesting facts `<div>` a CSS class of `animal-info`
  3. italicize the text for the animal's interesting fact
  4. bold the labels for the animal's list items (e.g. 'Habitat')
  5. remove dots from the animal's list items
  6. add a border around the animal's name, image, and information
  7. add a border around the animal's information
  8. add spacing between the animal's name, image, and information (you will need to use the property [padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding))

## ✅ Test Your Code ❌

To pass the Lab, follow the instructions above to get `card.html` to render similarly to what's seen in `design-prototype.jpg`.

To test how close you are, click the "RUN CODE" button located in the bottom right of the Workspace. This will run the validator against your code. A popup window will appear and run through all of the tests. If something still needs to be done, it will appear in this popup window in red. Also, there's no limit on the number of times you can use the "RUN CODE" feature, so keep checking it until you pass!

Good luck!
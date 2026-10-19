# Image placeholders

The website currently uses CSS-drawn ornamental placeholders so it works without downloading images.

To add family photographs:
1. Copy an image into this folder, for example `tanya-portrait.jpg`.
2. In `templates/bride.html`, replace the `.portrait-placeholder` block with:
   `<img class="portrait-photo" src="{{ url_for('static', filename='images/tanya-portrait.jpg') }}" alt="Tanya, the bride">`
3. Repeat in `templates/groom.html` for Deepak.
4. Add `.portrait-photo { width:100%; max-width:440px; aspect-ratio:4/5; object-fit:cover; border:1px solid var(--gold); }` to `static/css/style.css`.

Use photographs you have permission to publish. Avoid putting private guest information in publicly accessible image files.

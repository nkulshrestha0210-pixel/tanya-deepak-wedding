# Tanya & Deepak — Royal Indian Wedding Invitation

A complete Flask/Jinja multi-page wedding invitation site with a royal maroon, burgundy, antique-gold and ivory theme.

## Pages and routes

1. `/` — royal envelope, monogram and countdown
2. `/invitation` — formal invitation
3. `/bride` — Tanya's profile placeholder
4. `/groom` — Deepak's profile placeholder
5. `/family` — parents and grandparents
6. `/event/mehendi` — Mehendi, 8 February 2027
7. `/event/sangeet` — Sangeet, 9 February 2027
8. `/event/haldi` — Haldi, 10 February 2027
9. `/wedding` — Wedding ceremony, 10 February 2027
10. `/reception` — Reception details (unconfirmed)
11. `/venue` — venue and guest information
12. `/rsvp` — validated RSVP form and WhatsApp option (when configured)

## Requirements

- Python 3.10 or newer recommended
- Flask (installed from `requirements.txt`)
- A modern web browser

## Install and run locally

### Windows
1. Install Python from https://www.python.org/downloads/ and select “Add Python to PATH”.
2. Extract this project ZIP.
3. Open Command Prompt or PowerShell in the `tanya_deepak_wedding` folder.
4. Create a virtual environment (recommended):

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   py -m pip install -r requirements.txt
   py app.py
   ```

### macOS / Linux
1. Install Python 3.10+ from your operating system or https://www.python.org/downloads/.
2. Open a terminal in this project folder.
3. Run:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install -r requirements.txt
   python3 app.py
   ```

Open http://127.0.0.1:5000 in your browser. Stop the server with Ctrl+C.

## Central configuration

Edit `config.py` for:
- Couple names, invitation wording, hosts and wedding date
- Parents and grandparents
- Event dates, times, venue, address and dress code
- Venue map link
- WhatsApp RSVP number and guest assistance contact
- Optional music file

Do not invent details that are still marked “to be confirmed”. Verify every spelling, date, time and address before publishing. The provided Google Maps short link is the one supplied in the brief; verify it opens the intended venue.

### WhatsApp RSVP
Set `WEDDING["whatsapp_number"]` in `config.py` to an international number with digits only (country code included), e.g. `919876543210`. Until configured, no WhatsApp link is shown.

### Optional music
Add licensed audio to `static/audio/` and set `WEDDING["music_file"] = "audio/your-file.mp3"`. The visitor must press the music control; audio does not autoplay.

### Photographs
See `static/images/README.md` for replacing the CSS portrait placeholders with local photos and accessible alt text.

## RSVP behaviour and privacy

The `/rsvp` route accepts POST requests and validates the invitee group, attendance choice and optional message length server-side. This starter project deliberately does **not** save RSVP submissions to a database or file. After valid submission it displays a notice explaining that the response was validated but not saved permanently. Do not rely on this form to collect real responses until you configure persistent storage. Use the WhatsApp link or a host contact instead.

For real use, add a database (for example SQLite with appropriate backups), CSRF protection, rate limiting and a privacy notice before collecting guest information. Keep Flask's debug mode disabled in production.

## Test the app

Run:

```bash
python -m unittest
```

The included tests check key routes, a 404 page, RSVP invalid-input validation, and the honest non-persistence message.

## Publishing

This is source code, not a live website. To publish:
1. Upload the project to a Python-capable host (for example a service that supports Flask web apps).
2. Set a strong `SECRET_KEY` environment variable; `app.py` reads it from the environment.
3. Use a production WSGI server supported by your host (commonly Gunicorn on Linux; install it if needed).
4. Keep `debug=False`, test all links on mobile, and use HTTPS.
5. Check your host's current pricing and deployment instructions. Free tiers and hosting steps can change.

A simple local run is for testing only; do not expose Flask's development server as a production service.

## Accessibility and performance notes

- Responsive layout and mobile navigation
- Keyboard-visible focus, skip link, labels, semantic landmarks and image descriptions
- Reduced-motion preferences respected
- No autoplay audio or paid API dependency
- Google Fonts are optional external fonts; if blocked, local serif/sans-serif fallbacks are used.


### Recent design update
- Added the supplied Tanya & Deepak gold monogram to the header, home page and celebration cards.
- Added Lord Ganesha above `॥ श्री गणेशाय नमः ॥` on the home page.
- Removed automated envelope movement, countdown updates, and automatic JavaScript effects. The page is static.
- Add your real photographs to `static/images/` and update the relevant templates when ready.


### Background music
The website includes an original synthesized traditional Indian-inspired instrumental. Tap the envelope on the home page to start it. A Play/Pause button is also available in the footer. To use your own licensed music, replace `static/audio/wedding-music.mp3` with your MP3 using the same filename.

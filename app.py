import os
import re
from urllib.parse import quote
from flask import Flask, abort, flash, redirect, render_template, request, url_for
from config import WEDDING, FAMILY, EVENTS, RSVP_GROUPS, WBCF_GROUPS, SPECIAL_INVITE

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "local-development-key-change-before-deployment")

PAGE_SEQUENCE = [
    ("home", "Welcome", "index"),
    ("invitation", "Invitation", "invitation"),
    ("bride", "The Bride", "bride"),
    ("groom", "The Groom", "groom"),
    ("family", "Our Families", "family_page"),
    ("mehendi", "Mehendi", "mehendi"),
    ("sangeet", "Sangeet", "sangeet"),
    ("haldi", "Haldi", "haldi"),
    ("wedding", "Wedding", "wedding"),
    ("venue", "Venue & Guest Info", "venue"),
    ("rsvp", "RSVP", "rsvp"),
]

@app.context_processor
def shared_template_values():
    return {
        "wedding": WEDDING,
        "family": FAMILY,
        "events": EVENTS,
        "page_sequence": PAGE_SEQUENCE,
        "rsvp_groups": RSVP_GROUPS,
        "wbcf_groups": WBCF_GROUPS,
        "special_invite": SPECIAL_INVITE,
        "whatsapp_url": make_whatsapp_url(),
        "page_urls": {
            "home": url_for("home"),
            "invitation": url_for("invitation"),
            "bride": url_for("bride"),
            "groom": url_for("groom"),
            "family": url_for("family_page"),
            "mehendi": url_for("event_page", event_key="mehendi"),
            "sangeet": url_for("event_page", event_key="sangeet"),
            "haldi": url_for("event_page", event_key="haldi"),
            "wedding": url_for("wedding_page"),
            "venue": url_for("venue"),
            "rsvp": url_for("rsvp"),
        },
    }

def make_whatsapp_url(message=None):
    number = re.sub(r"\D", "", WEDDING.get("whatsapp_number", ""))
    if not number:
        return None
    text = message or f"Hello, I'd like to RSVP for {WEDDING['bride']} and {WEDDING['groom']}'s wedding."
    return f"https://wa.me/{number}?text={quote(text)}"

@app.get("/")
def home():
    return render_template("index.html", page_key="home", page_title="A Royal Celebration of Love")

@app.get("/invitation")
def invitation():
    return render_template("invitation.html", page_key="invitation", page_title="Formal Invitation")

@app.get("/bride")
def bride():
    return render_template("bride.html", page_key="bride", page_title="The Bride")

@app.get("/groom")
def groom():
    return render_template("groom.html", page_key="groom", page_title="The Groom")

@app.get("/family")
def family_page():
    return render_template("family.html", page_key="family", page_title="Our Families")

@app.get("/event/<event_key>")
def event_page(event_key):
    if event_key not in EVENTS:
        abort(404)
    return render_template("event.html", page_key=event_key, page_title=EVENTS[event_key]["title"], event=EVENTS[event_key])

@app.get("/wedding")
def wedding_page():
    return render_template("event.html", page_key="wedding", page_title="Wedding Ceremony", event=EVENTS["wedding"])

@app.get("/venue")
def venue():
    return render_template("venue.html", page_key="venue", page_title="Venue & Guest Information")

@app.route("/rsvp", methods=["GET", "POST"])
def rsvp():
    if request.method == "POST":
        invitee_group = request.form.get("invitee_group", "").strip()
        attendance = request.form.get("attendance", "").strip()
        message = request.form.get("message", "").strip()
        allowed_groups = set(RSVP_GROUPS + WBCF_GROUPS + ["Special invite", "Other / not listed"])
        errors = []
        if invitee_group not in allowed_groups:
            errors.append("Please select your invitation group.")
        if attendance not in {"yes", "no"}:
            errors.append("Please select whether you can attend.")
        if len(message) > 1000:
            errors.append("Your message must be 1,000 characters or fewer.")
        if errors:
            for error in errors:
                flash(error, "error")
            return render_template("rsvp.html", page_key="rsvp", page_title="RSVP", form_values=request.form), 400

        # Privacy-first starter: validate the request, but do not claim it was saved.
        # Add a database or another persistent store before using this for real RSVPs.
        flash(
            "Your form passed validation, but this demo is not configured to save RSVP responses. "
            "Please use the WhatsApp RSVP button or contact the hosts directly.",
            "notice",
        )
        return redirect(url_for("rsvp"), code=303)

    return render_template("rsvp.html", page_key="rsvp", page_title="RSVP", form_values={})

@app.get("/health")
def health():
    return {"status": "ok"}

@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html", page_key=None, page_title="Page Not Found"), 404

@app.errorhandler(500)
def server_error(_error):
    return render_template("500.html", page_key=None, page_title="Something Went Wrong"), 500

if __name__ == "__main__":
    app.run(debug=True)

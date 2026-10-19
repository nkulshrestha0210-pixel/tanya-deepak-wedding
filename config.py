"""Central editable wedding configuration for Tanya & Deepak.

Edit values here instead of hunting through templates. Leave unknown details blank
or as TODO placeholders; the site will label them as not yet confirmed.
"""
from datetime import date

WEDDING = {
    "bride": "Tanya",
    "groom": "Deepak",
    "date": date(2027, 2, 10),
    "date_display": "10 February 2027",
    "monogram": "T & D",
    "invitation_heading": "A Royal Celebration of Love",
    "invitation_text": (
        "With immense joy and the blessings of the Almighty, we invite you to "
        "celebrate the wedding of our beloved daughter, Tanya, with Deepak. "
        "Your presence and blessings will make this special occasion truly "
        "memorable as our families come together to celebrate love, happiness "
        "and a beautiful new beginning."
    ),
    "hosts": "Our families",
    "closing": (
        "Your presence and blessings will make our celebration truly special. "
        "We look forward to welcoming you."
    ),
    "venue_name": "The Keyaan Saloni",
    "venue_address": "Fatehabad Rd, Kalal Kheria, Agra, Uttar Pradesh 282006",
    "maps_url": "https://maps.app.goo.gl/s2HgsdRdPvLtDne97",
    # Set to a WhatsApp number with country code and digits only, e.g. 919876543210.
    "whatsapp_number": "919359489234",
    "contact_name": "",
    "contact_phone": "",
    "music_file": "audio/wedding-music.mp3",  # Din Shagna Da instrumental supplied by the user.
}

FAMILY = {
    "bride_mother": "Smt. Lalita Kulshrestha",
    "bride_father": "Shri Sanjeev Kulshrestha",
    "groom_mother": "Smt. Poonam Bansal",
    "groom_father": "Shri Surendra Bansal",
    "bride_paternal_grandparents": "Smt. Omvati Kulshrestha and Late Shri Satish Chandra Kulshrestha",
    "bride_maternal_grandparents": "Late Smt. Premlata Kulshrestha and Late Shri Bhagwan Kulshrestha",
    "groom_paternal_grandparents": "Names to be confirmed",
    "groom_maternal_grandparents": "Names to be confirmed",
    "bride_intro": "",
    "groom_intro": "",
    "family_blessings": "With the love and blessings of our families.",
}

EVENTS = {
    "mehendi": {
        "title": "Mehendi",
        "date": date(2027, 2, 8),
        "date_display": "8 February 2027",
        "time": "3 PM onwards",
        "venue": "45 Pushpanjali Vihar",
        "address": "45 Pushpanjali Vihar, Sikandra Bodla Road, Agra",
        "maps_url": "https://maps.app.goo.gl/ML8p7u7sM4HMrD1b8",
        "dress_code": "Celebrate the Mehendi in Shades of Green 🌿",
        "description": "An afternoon of henna, flowers, laughter and joyful traditions.",
        "theme": "mehendi",
    },
    "sangeet": {
        "title": "Sangeet",
        "date": date(2027, 2, 9),
        "date_display": "9 February 2027",
        "time": "6 PM onwards",
        "venue": "Clarks Inn Suites, Agra",
        "address": "Plot No. E-1/6, Tora Chowki, 125 Feet Fatehabad-Samsabad Link Road, Taj Nagari Phase 2, Tajganj, Agra, Uttar Pradesh 282004",
        "maps_url": "https://maps.app.goo.gl/nJgMWcgRuiavveYf8",
        "dress_code": "Festive and Fabulous",
        "description": "An evening of music, dance, celebration and golden memories.",
        "theme": "sangeet",
    },
    "haldi": {
        "title": "Haldi",
        "date": date(2027, 2, 10),
        "date_display": "10 February 2027",
        "time": "10 AM onwards",
        "venue": "The Keyaan Saloni",
        "address": "Fatehabad Rd, Kalal Kheria, Agra, Uttar Pradesh 282006",
        "maps_url": "https://maps.app.goo.gl/s2HgsdRdPvLtDne97",
        "dress_code": "A splash of yellow, a touch of blue and a pop of pink!",
        "description": "Marigold hues, blessings and the warmth of family.",
        "theme": "haldi",
    },
    "wedding": {
        "title": "Wedding Ceremony",
        "date": date(2027, 2, 10),
        "date_display": "10 February 2027",
        "time": "8 PM onwards",
        "venue": "The Keyaan Saloni",
        "address": "Fatehabad Rd, Kalal Kheria, Agra, Uttar Pradesh 282006",
        "description": "The sacred beginning of a beautiful forever.",
        "theme": "wedding",
    },

}

RSVP_GROUPS = [
    "Sunita & Pradeep Kulshrstha (Tai-Tauji)",
    "Mradula & Ravindra Pal Kulshrestha (Bua-Fufaji)",
    "Namrata & Sanjay Kulshrestha (Mausi-Mausaji)",
    "Alka & Manmohan Kulshrestha (Mami-Mamaji)",
    "Deepa & Ravi Mohan Kulshrestha (Mami-Mamaji)",
]
WBCF_GROUPS = [
    "Parul & Ankur Kulshrestha",
    "Aanchal & Anshul Kulshrestha",
    "Shivangi & Mayank Kulshrestha",
    "Runjan & Shashank Kulshrestha",
    "Medha & Sarthak",
    "Shubham",
    "Dhruv",
    "Nikita",
]
SPECIAL_INVITE = {
    "heading": "A Special Invite",
    "message": "My Bua is becoming a beautiful bride, and it’s time to celebrate! Come join us and make her wedding even more special.",
    "from": "Trishika, Prakul, Anaisha, Rushank",
}

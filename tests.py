import unittest
from app import app

class WeddingSiteTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True, SECRET_KEY="test-secret")
        self.client = app.test_client()

    def test_all_main_pages_load(self):
        paths = [
            "/", "/invitation", "/bride", "/groom", "/family",
            "/event/mehendi", "/event/sangeet", "/event/haldi",
            "/wedding", "/reception", "/venue", "/rsvp",
        ]
        for path in paths:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertIn(b"<!doctype html>", response.data.lower())

    def test_unknown_event_returns_404(self):
        self.assertEqual(self.client.get("/event/unknown").status_code, 404)

    def test_unknown_path_returns_404_page(self):
        response = self.client.get("/not-a-page")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"404", response.data)

    def test_invalid_rsvp_rejected(self):
        response = self.client.post("/rsvp", data={
            "invitee_group": "fake group",
            "attendance": "maybe",
            "message": "Hello",
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Please select your invitation group", response.data)
        self.assertIn(b"Please select whether you can attend", response.data)

    def test_valid_rsvp_does_not_claim_saved(self):
        from config import RSVP_GROUPS
        response = self.client.post("/rsvp", data={
            "invitee_group": RSVP_GROUPS[0],
            "attendance": "yes",
            "message": "Looking forward to it!",
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"does not save RSVP responses", response.data)

    def test_health_endpoint(self):
        self.assertEqual(self.client.get("/health").json, {"status": "ok"})

if __name__ == "__main__":
    unittest.main()

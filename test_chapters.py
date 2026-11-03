# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch


def chapter(number):
    name = f"chapter_{number}"
    spec = importlib.util.spec_from_file_location(name, Path(__file__).resolve().parent / f"Chapitre{number}/app.py")
    module = importlib.util.module_from_spec(spec)
    import sys
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class ChapterTests(unittest.TestCase):
    def test_basic_routes(self):
        client = chapter(2).app.test_client()
        self.assertEqual(client.get("/").data, b"Hello, World!")
        self.assertEqual(client.get("/about").status_code, 200)

    def test_template_escaping(self):
        client = chapter(3).app.test_client()
        self.assertEqual(client.get("/").status_code, 200)
        response = client.get("/user/%3Cscript%3E")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"<script>", response.data)
        self.assertIn(b"&lt;script&gt;", response.data)

    def test_random_range_endpoints(self):
        for number in (4, 6):
            module = chapter(number)
            for value in (1, 100):
                with patch.object(module.random, "randint", return_value=value) as generator:
                    response = module.app.test_client().get("/")
                self.assertEqual(response.status_code, 200)
                self.assertIn(str(value).encode(), response.data)
                generator.assert_called_once_with(1, 100)


if __name__ == "__main__":
    unittest.main()

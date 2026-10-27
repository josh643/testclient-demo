import os
import subprocess
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "with-playwright-browser.sh"


class PlaywrightBrowserPathTest(unittest.TestCase):
    def test_defaults_to_shared_browser_install(self):
        env = os.environ.copy()
        env.pop("PLAYWRIGHT_BROWSERS_PATH", None)

        result = subprocess.run(
            ["sh", str(SCRIPT), "sh", "-c", "printf '%s' \"$PLAYWRIGHT_BROWSERS_PATH\""],
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )

        self.assertEqual(result.stdout, "/opt/ms-playwright")

    def test_preserves_explicit_browser_install(self):
        env = os.environ.copy()
        env["PLAYWRIGHT_BROWSERS_PATH"] = "/tmp/custom-playwright-browsers"

        result = subprocess.run(
            ["sh", str(SCRIPT), "sh", "-c", "printf '%s' \"$PLAYWRIGHT_BROWSERS_PATH\""],
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )

        self.assertEqual(result.stdout, "/tmp/custom-playwright-browsers")


if __name__ == "__main__":
    unittest.main()

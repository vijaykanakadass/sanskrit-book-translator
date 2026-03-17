"""Generate a comprehensive PDF guide: Testing Python Modules."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch, mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Preformatted, KeepTogether,
    HRFlowable
)
from reportlab.lib.colors import black, white, gray

OUTPUT = "/home/user/sanskrit-book-translator/testing-python-modules-guide.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    topMargin=0.8*inch,
    bottomMargin=0.8*inch,
    leftMargin=0.9*inch,
    rightMargin=0.9*inch,
)

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    name='CoverTitle',
    fontName='Helvetica-Bold',
    fontSize=28,
    leading=34,
    alignment=TA_CENTER,
    spaceAfter=12,
    textColor=HexColor('#1a1a2e'),
))
styles.add(ParagraphStyle(
    name='CoverSubtitle',
    fontName='Helvetica',
    fontSize=14,
    leading=18,
    alignment=TA_CENTER,
    spaceAfter=6,
    textColor=HexColor('#555555'),
))
styles.add(ParagraphStyle(
    name='ChapterTitle',
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=28,
    spaceBefore=6,
    spaceAfter=14,
    textColor=HexColor('#16213e'),
))
styles.add(ParagraphStyle(
    name='SectionTitle',
    fontName='Helvetica-Bold',
    fontSize=16,
    leading=20,
    spaceBefore=16,
    spaceAfter=8,
    textColor=HexColor('#0f3460'),
))
styles.add(ParagraphStyle(
    name='SubSection',
    fontName='Helvetica-Bold',
    fontSize=12,
    leading=16,
    spaceBefore=12,
    spaceAfter=6,
    textColor=HexColor('#333333'),
))
styles.add(ParagraphStyle(
    name='BodyText2',
    fontName='Helvetica',
    fontSize=10.5,
    leading=15,
    spaceBefore=4,
    spaceAfter=4,
    alignment=TA_JUSTIFY,
    textColor=HexColor('#222222'),
))
styles.add(ParagraphStyle(
    name='BulletItem',
    fontName='Helvetica',
    fontSize=10.5,
    leading=15,
    leftIndent=20,
    spaceBefore=2,
    spaceAfter=2,
    bulletIndent=8,
    textColor=HexColor('#222222'),
))
styles.add(ParagraphStyle(
    name='CodeStyle',
    fontName='Courier',
    fontSize=9,
    leading=12,
    leftIndent=16,
    rightIndent=16,
    spaceBefore=6,
    spaceAfter=6,
    backColor=HexColor('#f4f4f8'),
    borderColor=HexColor('#cccccc'),
    borderWidth=0.5,
    borderPadding=8,
    textColor=HexColor('#1a1a1a'),
))
styles.add(ParagraphStyle(
    name='Tip',
    fontName='Helvetica-Oblique',
    fontSize=10,
    leading=14,
    leftIndent=20,
    spaceBefore=6,
    spaceAfter=6,
    textColor=HexColor('#2e7d32'),
    borderColor=HexColor('#a5d6a7'),
    borderWidth=1,
    borderPadding=8,
    backColor=HexColor('#f1f8e9'),
))
styles.add(ParagraphStyle(
    name='Warning',
    fontName='Helvetica-Oblique',
    fontSize=10,
    leading=14,
    leftIndent=20,
    spaceBefore=6,
    spaceAfter=6,
    textColor=HexColor('#c62828'),
    borderColor=HexColor('#ef9a9a'),
    borderWidth=1,
    borderPadding=8,
    backColor=HexColor('#ffebee'),
))

S = styles

def title(text):
    return Paragraph(text, S['ChapterTitle'])

def section(text):
    return Paragraph(text, S['SectionTitle'])

def subsection(text):
    return Paragraph(text, S['SubSection'])

def body(text):
    return Paragraph(text, S['BodyText2'])

def bullet(text):
    return Paragraph(f"&#8226;  {text}", S['BulletItem'])

def code(text):
    return Preformatted(text, S['CodeStyle'])

def tip(text):
    return Paragraph(f"TIP: {text}", S['Tip'])

def warning(text):
    return Paragraph(f"WARNING: {text}", S['Warning'])

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=HexColor('#cccccc'),
                      spaceBefore=8, spaceAfter=8)

def sp(h=6):
    return Spacer(1, h)


# ── BUILD CONTENT ──────────────────────────────────────────────

story = []

# ── COVER PAGE ──
story.append(Spacer(1, 2*inch))
story.append(Paragraph("Testing Python Modules", S['CoverTitle']))
story.append(Spacer(1, 12))
story.append(Paragraph("A Comprehensive Guide", S['CoverSubtitle']))
story.append(Spacer(1, 8))
story.append(Paragraph("From Fundamentals to Advanced Patterns", S['CoverSubtitle']))
story.append(Spacer(1, 1.5*inch))
story.append(hr())
story.append(Spacer(1, 12))
story.append(Paragraph("Covers: pytest, unittest, mocking, fixtures, coverage,<br/>"
                        "parametrize, test organization, and real-world patterns",
                        ParagraphStyle('CoverDesc', parent=S['CoverSubtitle'], fontSize=11)))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("March 2026", S['CoverSubtitle']))
story.append(PageBreak())


# ── TABLE OF CONTENTS ──
story.append(title("Table of Contents"))
story.append(sp())

toc_items = [
    ("1", "Why Test?"),
    ("2", "Python's Import System & Module Basics"),
    ("3", "Test Project Layout"),
    ("4", "unittest — The Built-in Framework"),
    ("5", "pytest — The Modern Standard"),
    ("6", "Assertions In Depth"),
    ("7", "Fixtures — Setup & Teardown"),
    ("8", "Mocking — Isolating Code Under Test"),
    ("9", "Parametrize — Data-Driven Tests"),
    ("10", "Testing Exceptions"),
    ("11", "Markers, Skipping & Expected Failures"),
    ("12", "Test Coverage"),
    ("13", "Monkeypatching"),
    ("14", "Testing I/O, Files & Environment Variables"),
    ("15", "Unit vs Integration vs End-to-End Tests"),
    ("16", "Test Doubles — Stubs, Spies, Fakes, Dummies"),
    ("17", "Async Testing"),
    ("18", "Testing CLI Applications"),
    ("19", "tox & nox — Multi-Environment Testing"),
    ("20", "Best Practices & Common Pitfalls"),
    ("21", "Quick Reference Cheat Sheet"),
]

for num, name in toc_items:
    story.append(Paragraph(
        f"<b>Chapter {num}</b> — {name}", S['BodyText2']
    ))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 1 — WHY TEST?
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 1: Why Test?"))
story.append(body(
    "Testing is the practice of writing code that verifies your application code "
    "works correctly. Tests act as a safety net — they catch bugs before users do, "
    "give you confidence to refactor, and serve as living documentation of how your "
    "code is supposed to behave."
))
story.append(sp())
story.append(section("Benefits of Testing"))
story.append(bullet("<b>Catch bugs early</b> — Find problems during development, not in production."))
story.append(bullet("<b>Enable refactoring</b> — Change code confidently knowing tests will catch regressions."))
story.append(bullet("<b>Document behavior</b> — Tests show exactly how functions are expected to work."))
story.append(bullet("<b>Design feedback</b> — Hard-to-test code often signals poor design."))
story.append(bullet("<b>Save time</b> — Automated tests run in seconds vs. minutes of manual testing."))

story.append(sp())
story.append(section("Types of Tests"))
story.append(body(
    "<b>Unit tests</b> verify a single function or class in isolation. They are fast, focused, "
    "and form the bulk of your test suite."
))
story.append(body(
    "<b>Integration tests</b> verify that multiple components work together correctly — e.g., "
    "your API handler connects to the database and returns the right response."
))
story.append(body(
    "<b>End-to-end (E2E) tests</b> test the full application from the user's perspective — "
    "e.g., a browser test that clicks buttons and fills forms."
))
story.append(sp())
story.append(section("The Testing Pyramid"))
story.append(body(
    "The testing pyramid suggests you should have many unit tests (fast, cheap), fewer "
    "integration tests (moderate cost), and very few E2E tests (slow, expensive). This gives "
    "you maximum confidence with minimum maintenance burden."
))
story.append(sp())
story.append(code(
    "        /\\          <- Few E2E tests\n"
    "       /  \\\n"
    "      /    \\\n"
    "     /------\\       <- Some integration tests\n"
    "    /        \\\n"
    "   /          \\\n"
    "  /------------\\    <- Many unit tests\n"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 2 — IMPORT SYSTEM
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 2: Python's Import System & Module Basics"))
story.append(body(
    "Understanding Python's import system is critical for testing because test runners need "
    "to import your code. Many testing headaches come from import errors, not test logic."
))

story.append(section("Modules vs Packages"))
story.append(body(
    "A <b>module</b> is a single .py file. A <b>package</b> is a directory containing an "
    "__init__.py file (which can be empty). Packages can contain sub-packages and modules."
))
story.append(code(
    "mypackage/\n"
    "    __init__.py        # Makes this directory a package\n"
    "    math_utils.py      # A module\n"
    "    string_utils.py    # Another module\n"
    "    sub/\n"
    "        __init__.py    # Sub-package\n"
    "        helpers.py     # Module inside sub-package"
))

story.append(section("How Python Finds Modules"))
story.append(body(
    "When you write <font face='Courier'>import mypackage</font>, Python searches these "
    "locations in order:"
))
story.append(bullet("The directory of the script being run"))
story.append(bullet("Directories in the PYTHONPATH environment variable"))
story.append(bullet("The standard library directories"))
story.append(bullet("Site-packages (where pip installs packages)"))

story.append(sp())
story.append(body(
    "You can inspect the search path at runtime:"
))
story.append(code(
    "import sys\n"
    "print(sys.path)  # List of directories Python searches"
))

story.append(section("Absolute vs Relative Imports"))
story.append(code(
    "# Absolute import — full path from project root\n"
    "from mypackage.math_utils import add\n\n"
    "# Relative import — relative to current module\n"
    "from .math_utils import add        # Same package\n"
    "from ..other_pkg.utils import fmt  # Parent package"
))
story.append(sp())
story.append(warning(
    "Relative imports only work inside packages. Running a file directly "
    "(python mypackage/math_utils.py) breaks relative imports. Use "
    "python -m mypackage.math_utils instead."
))

story.append(section("Editable Installs"))
story.append(body(
    "The recommended way to make your project importable during testing is an "
    "<b>editable install</b>. This adds your project root to sys.path:"
))
story.append(code(
    "# In your project root, create pyproject.toml:\n"
    "[project]\n"
    "name = \"mypackage\"\n"
    "version = \"0.1.0\"\n\n"
    "# Then install in editable mode:\n"
    "pip install -e ."
))
story.append(sp())
story.append(tip(
    "An editable install is the cleanest way to avoid ImportError in tests. "
    "It makes your package importable from anywhere, just like any pip-installed library."
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 3 — TEST PROJECT LAYOUT
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 3: Test Project Layout"))

story.append(section("Recommended Layout"))
story.append(code(
    "project-root/\n"
    "    pyproject.toml        # Project metadata\n"
    "    src/\n"
    "        mypackage/\n"
    "            __init__.py\n"
    "            core.py\n"
    "            utils.py\n"
    "    tests/\n"
    "        __init__.py       # Optional with pytest\n"
    "        conftest.py       # Shared fixtures\n"
    "        test_core.py\n"
    "        test_utils.py\n"
    "        integration/\n"
    "            conftest.py\n"
    "            test_api.py"
))

story.append(section("Naming Conventions"))
story.append(body("pytest discovers tests automatically using these rules:"))
story.append(bullet("Test files must be named <font face='Courier'>test_*.py</font> or <font face='Courier'>*_test.py</font>"))
story.append(bullet("Test functions must start with <font face='Courier'>test_</font>"))
story.append(bullet("Test classes must start with <font face='Courier'>Test</font> (no __init__ method)"))

story.append(code(
    "# test_calculator.py\n\n"
    "def test_addition():          # Discovered\n"
    "    assert 1 + 1 == 2\n\n"
    "def helper_function():        # NOT discovered (no test_ prefix)\n"
    "    return 42\n\n"
    "class TestCalculator:         # Discovered\n"
    "    def test_subtract(self):  # Discovered\n"
    "        assert 5 - 3 == 2"
))

story.append(section("conftest.py — Shared Test Configuration"))
story.append(body(
    "conftest.py is a special file that pytest loads automatically. Fixtures defined in "
    "conftest.py are available to all tests in the same directory and below — no import needed."
))
story.append(code(
    "# tests/conftest.py\n"
    "import pytest\n\n"
    "@pytest.fixture\n"
    "def sample_user():\n"
    "    return {\"name\": \"Alice\", \"age\": 30}\n\n\n"
    "# tests/test_users.py — no import needed!\n"
    "def test_user_name(sample_user):\n"
    "    assert sample_user[\"name\"] == \"Alice\""
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 4 — UNITTEST
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 4: unittest — The Built-in Framework"))

story.append(body(
    "unittest is Python's built-in testing framework, inspired by Java's JUnit. It uses "
    "classes and special assertion methods. While pytest is more popular, you'll encounter "
    "unittest in many existing codebases."
))

story.append(section("Basic Structure"))
story.append(code(
    "import unittest\n\n"
    "class TestStringMethods(unittest.TestCase):\n\n"
    "    def setUp(self):\n"
    "        \"\"\"Runs before EACH test method.\"\"\"\n"
    "        self.greeting = \"hello world\"\n\n"
    "    def tearDown(self):\n"
    "        \"\"\"Runs after EACH test method.\"\"\"\n"
    "        pass  # Clean up resources\n\n"
    "    def test_upper(self):\n"
    "        self.assertEqual(self.greeting.upper(), \"HELLO WORLD\")\n\n"
    "    def test_split(self):\n"
    "        result = self.greeting.split()\n"
    "        self.assertEqual(result, [\"hello\", \"world\"])\n"
    "        self.assertEqual(len(result), 2)\n\n"
    "if __name__ == \"__main__\":\n"
    "    unittest.main()"
))

story.append(section("Common Assertion Methods"))

assertion_data = [
    ["Method", "Checks that"],
    ["assertEqual(a, b)", "a == b"],
    ["assertNotEqual(a, b)", "a != b"],
    ["assertTrue(x)", "bool(x) is True"],
    ["assertFalse(x)", "bool(x) is False"],
    ["assertIs(a, b)", "a is b"],
    ["assertIsNone(x)", "x is None"],
    ["assertIn(a, b)", "a in b"],
    ["assertIsInstance(a, b)", "isinstance(a, b)"],
    ["assertRaises(exc)", "exception is raised"],
    ["assertAlmostEqual(a, b)", "round(a-b, 7) == 0"],
]

t = Table(assertion_data, colWidths=[2.8*inch, 3*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), HexColor('#16213e')),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (0,-1), 'Courier'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('GRID', (0,0), (-1,-1), 0.5, HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, HexColor('#f8f8f8')]),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
]))
story.append(t)

story.append(section("Running unittest"))
story.append(code(
    "# Run all tests in a module\n"
    "python -m unittest test_strings\n\n"
    "# Run a specific test class\n"
    "python -m unittest test_strings.TestStringMethods\n\n"
    "# Run a specific test method\n"
    "python -m unittest test_strings.TestStringMethods.test_upper\n\n"
    "# Discover and run all tests\n"
    "python -m unittest discover -s tests -p 'test_*.py'\n\n"
    "# Verbose output\n"
    "python -m unittest -v"
))

story.append(section("setUpClass and tearDownClass"))
story.append(body(
    "For expensive setup that should only happen once per class (e.g., database connection):"
))
story.append(code(
    "class TestDatabase(unittest.TestCase):\n\n"
    "    @classmethod\n"
    "    def setUpClass(cls):\n"
    "        \"\"\"Runs once before all tests in this class.\"\"\"\n"
    "        cls.db = connect_to_test_database()\n\n"
    "    @classmethod\n"
    "    def tearDownClass(cls):\n"
    "        \"\"\"Runs once after all tests in this class.\"\"\"\n"
    "        cls.db.close()"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 5 — PYTEST
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 5: pytest — The Modern Standard"))

story.append(body(
    "pytest is the most widely used Python testing framework. It's simpler than unittest — "
    "you write plain functions with plain assert statements. pytest provides better error "
    "messages, powerful fixtures, and a rich plugin ecosystem."
))

story.append(section("Installation"))
story.append(code("pip install pytest"))

story.append(section("Your First pytest Test"))
story.append(code(
    "# test_math.py\n\n"
    "def add(a, b):\n"
    "    return a + b\n\n"
    "def test_add_integers():\n"
    "    assert add(2, 3) == 5\n\n"
    "def test_add_strings():\n"
    "    assert add(\"hello \", \"world\") == \"hello world\"\n\n"
    "def test_add_negative():\n"
    "    result = add(-1, 1)\n"
    "    assert result == 0\n"
    "    assert isinstance(result, int)"
))

story.append(section("Running pytest"))
story.append(code(
    "# Run all tests in current directory (recursive)\n"
    "pytest\n\n"
    "# Run a specific file\n"
    "pytest test_math.py\n\n"
    "# Run a specific test function\n"
    "pytest test_math.py::test_add_integers\n\n"
    "# Run tests matching a keyword expression\n"
    "pytest -k \"add and not string\"\n\n"
    "# Verbose output\n"
    "pytest -v\n\n"
    "# Stop on first failure\n"
    "pytest -x\n\n"
    "# Show print statements (captured by default)\n"
    "pytest -s\n\n"
    "# Run last failed tests only\n"
    "pytest --lf\n\n"
    "# Show local variables in tracebacks\n"
    "pytest -l"
))

story.append(section("Why pytest Over unittest"))
story.append(bullet("<b>Simpler syntax</b> — Plain functions + plain assert, no classes required."))
story.append(bullet("<b>Better error messages</b> — pytest rewrites assert to show actual vs expected values."))
story.append(bullet("<b>Powerful fixtures</b> — Dependency injection, scoping, and composition."))
story.append(bullet("<b>Parametrize</b> — Run the same test with many inputs in one decorator."))
story.append(bullet("<b>Plugin ecosystem</b> — pytest-cov, pytest-mock, pytest-asyncio, pytest-xdist, etc."))
story.append(bullet("<b>Backwards compatible</b> — pytest can run unittest tests without changes."))

story.append(sp())
story.append(code(
    "# unittest style — verbose\n"
    "class TestMath(unittest.TestCase):\n"
    "    def test_add(self):\n"
    "        self.assertEqual(add(2, 3), 5)\n\n"
    "# pytest style — clean\n"
    "def test_add():\n"
    "    assert add(2, 3) == 5"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 6 — ASSERTIONS
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 6: Assertions In Depth"))

story.append(body(
    "In pytest, you use Python's built-in <font face='Courier'>assert</font> statement. "
    "pytest rewrites assert expressions at import time to provide detailed failure messages "
    "showing the actual values involved."
))

story.append(section("Basic Assertions"))
story.append(code(
    "def test_assertions():\n"
    "    # Equality\n"
    "    assert 1 + 1 == 2\n"
    "    assert \"hello\".upper() == \"HELLO\"\n\n"
    "    # Truthiness\n"
    "    assert [1, 2, 3]       # Non-empty list is truthy\n"
    "    assert not []          # Empty list is falsy\n\n"
    "    # Membership\n"
    "    assert 3 in [1, 2, 3]\n"
    "    assert \"key\" in {\"key\": \"value\"}\n\n"
    "    # Identity\n"
    "    assert None is None\n\n"
    "    # Comparison\n"
    "    assert 10 > 5\n"
    "    assert len(\"hello\") == 5\n\n"
    "    # Type checking\n"
    "    assert isinstance(42, int)\n"
    "    assert isinstance(\"hi\", (str, bytes))  # Multiple types"
))

story.append(section("Assertion Messages"))
story.append(code(
    "def test_with_message():\n"
    "    value = get_result()\n"
    "    assert value > 0, f\"Expected positive, got {value}\""
))

story.append(section("Comparing Complex Objects"))
story.append(code(
    "def test_dict_comparison():\n"
    "    expected = {\"name\": \"Alice\", \"age\": 30, \"city\": \"NYC\"}\n"
    "    actual = get_user()\n"
    "    assert actual == expected\n"
    "    # pytest shows exactly which keys/values differ!\n\n"
    "def test_list_comparison():\n"
    "    assert sorted(result) == [1, 2, 3, 4, 5]\n\n"
    "def test_approximate_equality():\n"
    "    # For floating point comparisons\n"
    "    from pytest import approx\n"
    "    assert 0.1 + 0.2 == approx(0.3)\n"
    "    assert [0.1, 0.2] == approx([0.1, 0.2])\n"
    "    assert 100 == approx(101, abs=2)    # Within 2\n"
    "    assert 100 == approx(102, rel=0.05) # Within 5%"
))

story.append(section("What pytest Shows On Failure"))
story.append(code(
    "# If this test fails:\n"
    "def test_example():\n"
    "    x = {\"a\": 1, \"b\": 2}\n"
    "    y = {\"a\": 1, \"b\": 3}\n"
    "    assert x == y\n\n"
    "# pytest output:\n"
    "# >   assert x == y\n"
    "# E   AssertionError: assert {'a': 1, 'b': 2} == {'a': 1, 'b': 3}\n"
    "# E     Differing items:\n"
    "# E     {'b': 2} != {'b': 3}"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 7 — FIXTURES
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 7: Fixtures — Setup & Teardown"))

story.append(body(
    "Fixtures provide a way to set up preconditions for your tests and clean up afterward. "
    "In pytest, fixtures use dependency injection — you request a fixture by adding it as a "
    "parameter to your test function."
))

story.append(section("Basic Fixture"))
story.append(code(
    "import pytest\n\n"
    "@pytest.fixture\n"
    "def sample_list():\n"
    "    return [1, 2, 3, 4, 5]\n\n"
    "def test_list_length(sample_list):\n"
    "    assert len(sample_list) == 5\n\n"
    "def test_list_sum(sample_list):\n"
    "    assert sum(sample_list) == 15"
))

story.append(section("Fixtures with Teardown (yield)"))
story.append(code(
    "@pytest.fixture\n"
    "def database_connection():\n"
    "    # SETUP — code before yield\n"
    "    conn = create_connection(\"test.db\")\n"
    "    conn.execute(\"CREATE TABLE users (name TEXT)\")\n\n"
    "    yield conn  # This value is passed to the test\n\n"
    "    # TEARDOWN — code after yield (always runs)\n"
    "    conn.execute(\"DROP TABLE users\")\n"
    "    conn.close()\n\n"
    "def test_insert_user(database_connection):\n"
    "    database_connection.execute(\n"
    "        \"INSERT INTO users VALUES ('Alice')\"\n"
    "    )\n"
    "    # After this test, teardown runs automatically"
))

story.append(section("Fixture Scopes"))
story.append(body(
    "The scope controls how often the fixture is created and destroyed:"
))
story.append(code(
    "@pytest.fixture(scope=\"function\")   # Default: new for each test\n"
    "def per_test(): ...\n\n"
    "@pytest.fixture(scope=\"class\")      # Once per test class\n"
    "def per_class(): ...\n\n"
    "@pytest.fixture(scope=\"module\")     # Once per test file\n"
    "def per_module(): ...\n\n"
    "@pytest.fixture(scope=\"session\")    # Once per entire test run\n"
    "def per_session(): ..."
))

story.append(section("Fixture Composition"))
story.append(body("Fixtures can depend on other fixtures:"))
story.append(code(
    "@pytest.fixture\n"
    "def user_data():\n"
    "    return {\"name\": \"Alice\", \"email\": \"alice@test.com\"}\n\n"
    "@pytest.fixture\n"
    "def authenticated_client(user_data):\n"
    "    client = TestClient()\n"
    "    client.login(user_data[\"email\"])\n"
    "    yield client\n"
    "    client.logout()\n\n"
    "def test_profile(authenticated_client):\n"
    "    response = authenticated_client.get(\"/profile\")\n"
    "    assert response.status_code == 200"
))

story.append(section("autouse Fixtures"))
story.append(body("Apply a fixture to every test automatically:"))
story.append(code(
    "@pytest.fixture(autouse=True)\n"
    "def reset_database():\n"
    "    \"\"\"Runs before and after every test.\"\"\"\n"
    "    yield\n"
    "    db.rollback()  # Undo any changes after each test"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 8 — MOCKING
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 8: Mocking — Isolating Code Under Test"))

story.append(body(
    "Mocking replaces real objects with controlled stand-ins during testing. This lets you "
    "test a function without actually calling a database, sending emails, or making HTTP "
    "requests. Python provides mocking through <font face='Courier'>unittest.mock</font>."
))

story.append(section("Why Mock?"))
story.append(bullet("<b>Speed</b> — Avoid slow operations (network, disk, database)."))
story.append(bullet("<b>Isolation</b> — Test YOUR code, not external services."))
story.append(bullet("<b>Determinism</b> — Remove randomness and timing issues."))
story.append(bullet("<b>Edge cases</b> — Simulate errors that are hard to trigger naturally."))

story.append(section("unittest.mock Basics"))
story.append(code(
    "from unittest.mock import Mock, MagicMock, patch\n\n"
    "# Create a simple mock\n"
    "mock = Mock()\n"
    "mock.some_method.return_value = 42\n"
    "result = mock.some_method(\"arg1\", \"arg2\")\n\n"
    "assert result == 42\n"
    "mock.some_method.assert_called_once_with(\"arg1\", \"arg2\")"
))

story.append(section("The patch Decorator"))
story.append(body(
    "patch() temporarily replaces an object in a specific module with a mock:"
))
story.append(code(
    "# myapp/service.py\n"
    "import requests\n\n"
    "def get_user_name(user_id):\n"
    "    response = requests.get(f\"https://api.example.com/users/{user_id}\")\n"
    "    return response.json()[\"name\"]\n\n\n"
    "# tests/test_service.py\n"
    "from unittest.mock import patch, Mock\n"
    "from myapp.service import get_user_name\n\n"
    "@patch(\"myapp.service.requests.get\")  # Patch WHERE it's used\n"
    "def test_get_user_name(mock_get):\n"
    "    # Configure the mock\n"
    "    mock_response = Mock()\n"
    "    mock_response.json.return_value = {\"name\": \"Alice\"}\n"
    "    mock_get.return_value = mock_response\n\n"
    "    # Call the function under test\n"
    "    result = get_user_name(123)\n\n"
    "    # Verify\n"
    "    assert result == \"Alice\"\n"
    "    mock_get.assert_called_once_with(\n"
    "        \"https://api.example.com/users/123\"\n"
    "    )"
))

story.append(sp())
story.append(warning(
    "Always patch where the object is USED, not where it's DEFINED. "
    "If service.py does 'import requests', patch 'myapp.service.requests', "
    "NOT 'requests'."
))

story.append(section("patch as Context Manager"))
story.append(code(
    "def test_with_context_manager():\n"
    "    with patch(\"myapp.service.requests.get\") as mock_get:\n"
    "        mock_get.return_value.json.return_value = {\"name\": \"Bob\"}\n"
    "        result = get_user_name(456)\n"
    "        assert result == \"Bob\"\n"
    "    # mock is automatically removed after 'with' block"
))

story.append(section("MagicMock"))
story.append(body(
    "MagicMock is a subclass of Mock that supports magic methods (__len__, __iter__, etc.):"
))
story.append(code(
    "mock = MagicMock()\n"
    "mock.__len__.return_value = 5\n"
    "assert len(mock) == 5\n\n"
    "mock.__iter__.return_value = iter([1, 2, 3])\n"
    "assert list(mock) == [1, 2, 3]"
))

story.append(section("side_effect — Dynamic Responses"))
story.append(code(
    "# Raise an exception\n"
    "mock.method.side_effect = ConnectionError(\"Network down\")\n\n"
    "# Return different values on consecutive calls\n"
    "mock.method.side_effect = [1, 2, 3]\n"
    "assert mock.method() == 1  # First call\n"
    "assert mock.method() == 2  # Second call\n\n"
    "# Use a function for complex logic\n"
    "def custom_response(url):\n"
    "    if \"users\" in url:\n"
    "        return Mock(status_code=200)\n"
    "    return Mock(status_code=404)\n\n"
    "mock.get.side_effect = custom_response"
))

story.append(section("pytest-mock (mocker fixture)"))
story.append(body("The pytest-mock plugin provides a cleaner API:"))
story.append(code(
    "# pip install pytest-mock\n\n"
    "def test_with_mocker(mocker):\n"
    "    mock_get = mocker.patch(\"myapp.service.requests.get\")\n"
    "    mock_get.return_value.json.return_value = {\"name\": \"Charlie\"}\n\n"
    "    result = get_user_name(789)\n"
    "    assert result == \"Charlie\"\n"
    "    # Mock is automatically cleaned up by the fixture"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 9 — PARAMETRIZE
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 9: Parametrize — Data-Driven Tests"))

story.append(body(
    "Parametrize lets you run the same test function with different inputs and expected "
    "outputs. Instead of writing five nearly identical test functions, you write one and "
    "provide the data."
))

story.append(section("Basic Parametrize"))
story.append(code(
    "import pytest\n\n"
    "@pytest.mark.parametrize(\"input_val, expected\", [\n"
    "    (1, 1),\n"
    "    (2, 4),\n"
    "    (3, 9),\n"
    "    (4, 16),\n"
    "    (-2, 4),\n"
    "    (0, 0),\n"
    "])\n"
    "def test_square(input_val, expected):\n"
    "    assert input_val ** 2 == expected"
))
story.append(body("This generates six separate tests, each shown in test output with its values."))

story.append(section("Parametrize with IDs"))
story.append(code(
    "@pytest.mark.parametrize(\"username, is_valid\", [\n"
    "    (\"alice\", True),\n"
    "    (\"bob123\", True),\n"
    "    (\"\", False),\n"
    "    (\"a\" * 256, False),\n"
    "    (\"user@name\", False),\n"
    "], ids=[\"normal\", \"with_numbers\", \"empty\", \"too_long\", \"special_chars\"])\n"
    "def test_validate_username(username, is_valid):\n"
    "    assert validate(username) == is_valid"
))

story.append(section("Multiple Parametrize (Cartesian Product)"))
story.append(code(
    "@pytest.mark.parametrize(\"x\", [0, 1, 2])\n"
    "@pytest.mark.parametrize(\"y\", [10, 20])\n"
    "def test_multiply(x, y):\n"
    "    result = x * y\n"
    "    assert isinstance(result, int)\n"
    "# Generates 6 tests: (0,10), (0,20), (1,10), (1,20), (2,10), (2,20)"
))

story.append(section("Parametrized Fixtures"))
story.append(code(
    "@pytest.fixture(params=[\"sqlite\", \"postgres\", \"mysql\"])\n"
    "def database(request):\n"
    "    db = create_database(request.param)\n"
    "    yield db\n"
    "    db.drop()\n\n"
    "def test_insert(database):\n"
    "    # This test runs 3 times — once per database type\n"
    "    database.insert({\"key\": \"value\"})\n"
    "    assert database.count() == 1"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 10 — TESTING EXCEPTIONS
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 10: Testing Exceptions"))

story.append(section("pytest.raises"))
story.append(code(
    "import pytest\n\n"
    "def divide(a, b):\n"
    "    if b == 0:\n"
    "        raise ValueError(\"Cannot divide by zero\")\n"
    "    return a / b\n\n"
    "def test_divide_by_zero():\n"
    "    with pytest.raises(ValueError):\n"
    "        divide(10, 0)\n\n"
    "def test_divide_by_zero_message():\n"
    "    with pytest.raises(ValueError, match=\"Cannot divide by zero\"):\n"
    "        divide(10, 0)\n\n"
    "def test_exception_details():\n"
    "    with pytest.raises(ValueError) as exc_info:\n"
    "        divide(10, 0)\n"
    "    assert \"zero\" in str(exc_info.value)\n"
    "    assert exc_info.type is ValueError"
))

story.append(section("Testing That No Exception Is Raised"))
story.append(code(
    "def test_valid_division():\n"
    "    # If this raises, the test fails automatically\n"
    "    result = divide(10, 2)\n"
    "    assert result == 5.0"
))

story.append(section("Testing Multiple Exception Types"))
story.append(code(
    "def test_type_error():\n"
    "    with pytest.raises((TypeError, ValueError)):\n"
    "        divide(\"hello\", 2)"
))

story.append(section("unittest Style"))
story.append(code(
    "class TestDivide(unittest.TestCase):\n"
    "    def test_divide_by_zero(self):\n"
    "        with self.assertRaises(ValueError) as ctx:\n"
    "            divide(10, 0)\n"
    "        self.assertIn(\"zero\", str(ctx.exception))\n\n"
    "    def test_raises_shorthand(self):\n"
    "        self.assertRaises(ValueError, divide, 10, 0)"
))

story.append(section("Testing Warnings"))
story.append(code(
    "import warnings\n\n"
    "def old_function():\n"
    "    warnings.warn(\"Deprecated: use new_function()\", DeprecationWarning)\n\n"
    "def test_deprecation_warning():\n"
    "    with pytest.warns(DeprecationWarning, match=\"Deprecated\"):\n"
    "        old_function()"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 11 — MARKERS
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 11: Markers, Skipping & Expected Failures"))

story.append(section("Built-in Markers"))
story.append(code(
    "import pytest\n"
    "import sys\n\n"
    "# Skip unconditionally\n"
    "@pytest.mark.skip(reason=\"Not implemented yet\")\n"
    "def test_future_feature():\n"
    "    pass\n\n"
    "# Skip conditionally\n"
    "@pytest.mark.skipif(\n"
    "    sys.platform == \"win32\",\n"
    "    reason=\"Not supported on Windows\"\n"
    ")\n"
    "def test_unix_only():\n"
    "    pass\n\n"
    "# Expected failure — test is known to fail\n"
    "@pytest.mark.xfail(reason=\"Bug #1234 not fixed yet\")\n"
    "def test_known_bug():\n"
    "    assert broken_function() == 42\n\n"
    "# Strict xfail — fail if the test PASSES unexpectedly\n"
    "@pytest.mark.xfail(strict=True)\n"
    "def test_should_fail():\n"
    "    assert 1 == 2"
))

story.append(section("Custom Markers"))
story.append(code(
    "# pytest.ini or pyproject.toml\n"
    "# [tool.pytest.ini_options]\n"
    "# markers = [\n"
    "#     \"slow: marks tests as slow\",\n"
    "#     \"integration: marks integration tests\",\n"
    "# ]\n\n"
    "@pytest.mark.slow\n"
    "def test_large_dataset():\n"
    "    process_million_records()\n\n"
    "@pytest.mark.integration\n"
    "def test_api_endpoint():\n"
    "    response = call_real_api()"
))

story.append(section("Running Tests by Marker"))
story.append(code(
    "# Run only slow tests\n"
    "pytest -m slow\n\n"
    "# Run everything EXCEPT slow tests\n"
    "pytest -m \"not slow\"\n\n"
    "# Run slow OR integration tests\n"
    "pytest -m \"slow or integration\""
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 12 — COVERAGE
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 12: Test Coverage"))

story.append(body(
    "Coverage measures which lines of your code are actually executed by your tests. "
    "It helps identify untested code paths."
))

story.append(section("Setup"))
story.append(code(
    "pip install pytest-cov\n\n"
    "# Run tests with coverage\n"
    "pytest --cov=mypackage\n\n"
    "# With detailed report\n"
    "pytest --cov=mypackage --cov-report=term-missing\n\n"
    "# Generate HTML report (opens in browser)\n"
    "pytest --cov=mypackage --cov-report=html\n\n"
    "# Fail if coverage is below threshold\n"
    "pytest --cov=mypackage --cov-fail-under=80"
))

story.append(section("Reading Coverage Output"))
story.append(code(
    "---------- coverage: ... ----------\n"
    "Name                    Stmts   Miss  Cover   Missing\n"
    "-----------------------------------------------------\n"
    "mypackage/__init__.py       2      0   100%\n"
    "mypackage/core.py          45      3    93%   34-36\n"
    "mypackage/utils.py         20      8    60%   15-22\n"
    "-----------------------------------------------------\n"
    "TOTAL                      67     11    84%"
))
story.append(body(
    "<b>Stmts</b> = total statements, <b>Miss</b> = lines not executed, "
    "<b>Cover</b> = percentage covered, <b>Missing</b> = uncovered line numbers."
))

story.append(section("Configuration (pyproject.toml)"))
story.append(code(
    "[tool.pytest.ini_options]\n"
    "addopts = \"--cov=mypackage --cov-report=term-missing\"\n\n"
    "[tool.coverage.run]\n"
    "source = [\"mypackage\"]\n"
    "omit = [\"*/tests/*\", \"*/migrations/*\"]\n\n"
    "[tool.coverage.report]\n"
    "exclude_lines = [\n"
    "    \"pragma: no cover\",\n"
    "    \"if __name__ == .__main__.\",\n"
    "    \"if TYPE_CHECKING:\",\n"
    "]"
))

story.append(section("Excluding Lines from Coverage"))
story.append(code(
    "def debug_function():  # pragma: no cover\n"
    "    \"\"\"This function is excluded from coverage.\"\"\"\n"
    "    print(\"debugging...\")"
))

story.append(sp())
story.append(tip(
    "100% coverage doesn't mean 100% correct. Coverage tells you what code ran, "
    "not whether the assertions are meaningful. Aim for 80-90% coverage and focus "
    "on testing critical business logic."
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 13 — MONKEYPATCHING
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 13: Monkeypatching"))

story.append(body(
    "Monkeypatching dynamically modifies objects at runtime. pytest's built-in monkeypatch "
    "fixture is cleaner than unittest.mock for simple replacements."
))

story.append(section("Replacing Attributes"))
story.append(code(
    "# myapp/config.py\n"
    "API_URL = \"https://api.production.com\"\n\n\n"
    "# tests/test_config.py\n"
    "import myapp.config\n\n"
    "def test_with_test_api(monkeypatch):\n"
    "    monkeypatch.setattr(myapp.config, \"API_URL\", \"https://test.api.com\")\n"
    "    assert myapp.config.API_URL == \"https://test.api.com\"\n"
    "    # Original value is restored after the test"
))

story.append(section("Replacing Functions"))
story.append(code(
    "import os\n\n"
    "def test_fake_home_dir(monkeypatch):\n"
    "    monkeypatch.setattr(os.path, \"expanduser\", lambda x: \"/fake/home\")\n"
    "    assert os.path.expanduser(\"~\") == \"/fake/home\""
))

story.append(section("Environment Variables"))
story.append(code(
    "def test_with_env_var(monkeypatch):\n"
    "    monkeypatch.setenv(\"DATABASE_URL\", \"sqlite:///test.db\")\n"
    "    assert os.environ[\"DATABASE_URL\"] == \"sqlite:///test.db\"\n\n"
    "def test_without_env_var(monkeypatch):\n"
    "    monkeypatch.delenv(\"SECRET_KEY\", raising=False)\n"
    "    assert \"SECRET_KEY\" not in os.environ"
))

story.append(section("Replacing Dictionary Items"))
story.append(code(
    "def test_modify_dict(monkeypatch):\n"
    "    config = {\"debug\": False, \"port\": 8080}\n"
    "    monkeypatch.setitem(config, \"debug\", True)\n"
    "    assert config[\"debug\"] is True"
))

story.append(section("Monkeypatch vs Mock — When to Use Which"))
story.append(bullet("<b>monkeypatch</b> — Simple replacements: attributes, env vars, dict items."))
story.append(bullet("<b>Mock/patch</b> — When you need to assert calls, track arguments, or use side_effect."))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 14 — TESTING I/O
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 14: Testing I/O, Files & Environment"))

story.append(section("Temporary Files with tmp_path"))
story.append(code(
    "def test_write_and_read(tmp_path):\n"
    "    # tmp_path is a pathlib.Path to a unique temp directory\n"
    "    file = tmp_path / \"data.txt\"\n"
    "    file.write_text(\"hello world\")\n\n"
    "    assert file.read_text() == \"hello world\"\n"
    "    assert file.exists()\n"
    "    # Directory is cleaned up after the test session"
))

story.append(section("Temporary Directory for a Class"))
story.append(code(
    "@pytest.fixture\n"
    "def output_dir(tmp_path):\n"
    "    d = tmp_path / \"output\"\n"
    "    d.mkdir()\n"
    "    return d\n\n"
    "def test_generate_report(output_dir):\n"
    "    generate_report(output_dir / \"report.pdf\")\n"
    "    assert (output_dir / \"report.pdf\").exists()"
))

story.append(section("Capturing stdout and stderr"))
story.append(code(
    "def greet(name):\n"
    "    print(f\"Hello, {name}!\")\n\n"
    "def test_greet_output(capsys):\n"
    "    greet(\"Alice\")\n"
    "    captured = capsys.readouterr()\n"
    "    assert captured.out == \"Hello, Alice!\\n\"\n"
    "    assert captured.err == \"\"  # Nothing on stderr"
))

story.append(section("Capturing Logs"))
story.append(code(
    "import logging\n\n"
    "def process_item(item):\n"
    "    logging.info(f\"Processing {item}\")\n"
    "    if not item:\n"
    "        logging.warning(\"Empty item received\")\n\n"
    "def test_logging(caplog):\n"
    "    with caplog.at_level(logging.INFO):\n"
    "        process_item(\"\")\n\n"
    "    assert \"Processing\" in caplog.text\n"
    "    assert \"Empty item received\" in caplog.text\n"
    "    assert len(caplog.records) == 2\n"
    "    assert caplog.records[1].levelname == \"WARNING\""
))

story.append(section("Testing stdin Input"))
story.append(code(
    "def get_name():\n"
    "    return input(\"Enter your name: \")\n\n"
    "def test_get_name(monkeypatch):\n"
    "    monkeypatch.setattr(\"builtins.input\", lambda _: \"Alice\")\n"
    "    assert get_name() == \"Alice\""
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 15 — UNIT VS INTEGRATION VS E2E
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 15: Unit vs Integration vs End-to-End Tests"))

story.append(section("Unit Tests"))
story.append(body(
    "Test a single function or class in complete isolation. All dependencies are mocked. "
    "Fast, focused, deterministic."
))
story.append(code(
    "def test_calculate_discount():\n"
    "    # Pure function — no external dependencies\n"
    "    assert calculate_discount(100, 0.2) == 80.0\n"
    "    assert calculate_discount(50, 0.1) == 45.0"
))

story.append(section("Integration Tests"))
story.append(body(
    "Test that multiple components work together. May use real databases, file systems, "
    "or network calls (to test environments)."
))
story.append(code(
    "@pytest.mark.integration\n"
    "def test_create_and_fetch_user(test_db):\n"
    "    # Tests the full flow: service -> repository -> database\n"
    "    user_service = UserService(test_db)\n"
    "    user_service.create(\"Alice\", \"alice@test.com\")\n\n"
    "    user = user_service.get_by_email(\"alice@test.com\")\n"
    "    assert user.name == \"Alice\""
))

story.append(section("End-to-End Tests"))
story.append(body(
    "Test the complete system as a user would experience it. For web apps, this often means "
    "browser automation."
))
story.append(code(
    "# Using httpx/TestClient for API E2E\n"
    "from fastapi.testclient import TestClient\n"
    "from myapp import app\n\n"
    "client = TestClient(app)\n\n"
    "def test_full_user_flow():\n"
    "    # Register\n"
    "    r = client.post(\"/register\", json={...})\n"
    "    assert r.status_code == 201\n\n"
    "    # Login\n"
    "    r = client.post(\"/login\", json={...})\n"
    "    token = r.json()[\"token\"]\n\n"
    "    # Access protected resource\n"
    "    r = client.get(\"/profile\", headers={\"Authorization\": token})\n"
    "    assert r.status_code == 200"
))

story.append(section("How to Organize"))
story.append(code(
    "tests/\n"
    "    unit/\n"
    "        test_calculator.py\n"
    "        test_validators.py\n"
    "    integration/\n"
    "        test_user_service.py\n"
    "        test_payment_flow.py\n"
    "    e2e/\n"
    "        test_full_checkout.py"
))
story.append(body("Run them separately:"))
story.append(code(
    "pytest tests/unit                # Fast — run always\n"
    "pytest tests/integration         # Moderate — run before merging\n"
    "pytest tests/e2e                 # Slow — run in CI pipeline"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 16 — TEST DOUBLES
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 16: Test Doubles"))

story.append(body(
    "\"Test double\" is the general term for any object that stands in for a real dependency. "
    "There are several specific types:"
))

doubles_data = [
    ["Type", "Purpose", "Example"],
    ["Dummy", "Fills a required parameter\nbut is never used", "A placeholder object\npassed but not called"],
    ["Stub", "Returns pre-configured\nresponses", "A fake API that always\nreturns {\"status\": 200}"],
    ["Spy", "Records calls for\nlater verification", "Track how many times\na function was called"],
    ["Mock", "Pre-programmed with\nexpected calls/responses", "unittest.mock.Mock()"],
    ["Fake", "Working implementation\nbut simplified", "In-memory database\ninstead of PostgreSQL"],
]

t = Table(doubles_data, colWidths=[0.9*inch, 2*inch, 2.5*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), HexColor('#16213e')),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('GRID', (0,0), (-1,-1), 0.5, HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, HexColor('#f8f8f8')]),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
]))
story.append(t)

story.append(section("Examples"))
story.append(code(
    "# DUMMY — never actually used\n"
    "def test_create_report():\n"
    "    dummy_logger = None  # Not used by the code path we test\n"
    "    report = create_report(data, logger=dummy_logger)\n"
    "    assert report.title == \"Q1 Report\"\n\n\n"
    "# STUB — returns fixed data\n"
    "class StubUserRepo:\n"
    "    def get(self, user_id):\n"
    "        return User(id=user_id, name=\"Test User\")\n\n"
    "def test_with_stub():\n"
    "    service = UserService(repo=StubUserRepo())\n"
    "    assert service.get_name(1) == \"Test User\"\n\n\n"
    "# FAKE — simplified but working implementation\n"
    "class FakeEmailService:\n"
    "    def __init__(self):\n"
    "        self.sent = []\n\n"
    "    def send(self, to, subject, body):\n"
    "        self.sent.append({\"to\": to, \"subject\": subject})\n"
    "        return True\n\n"
    "def test_sends_welcome_email():\n"
    "    fake_email = FakeEmailService()\n"
    "    register_user(\"alice@test.com\", email_service=fake_email)\n"
    "    assert len(fake_email.sent) == 1\n"
    "    assert fake_email.sent[0][\"subject\"] == \"Welcome!\""
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 17 — ASYNC TESTING
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 17: Async Testing"))

story.append(body(
    "Testing async code requires a test runner that understands async/await. "
    "The pytest-asyncio plugin handles this."
))

story.append(section("Setup"))
story.append(code("pip install pytest-asyncio"))

story.append(section("Writing Async Tests"))
story.append(code(
    "import pytest\n"
    "import asyncio\n\n"
    "@pytest.mark.asyncio\n"
    "async def test_async_function():\n"
    "    result = await fetch_data()\n"
    "    assert result is not None\n\n"
    "@pytest.mark.asyncio\n"
    "async def test_async_with_timeout():\n"
    "    result = await asyncio.wait_for(\n"
    "        slow_operation(), timeout=5.0\n"
    "    )\n"
    "    assert result == \"done\""
))

story.append(section("Async Fixtures"))
story.append(code(
    "@pytest.fixture\n"
    "async def async_client():\n"
    "    client = AsyncClient()\n"
    "    await client.connect()\n"
    "    yield client\n"
    "    await client.disconnect()\n\n"
    "@pytest.mark.asyncio\n"
    "async def test_with_async_fixture(async_client):\n"
    "    response = await async_client.get(\"/health\")\n"
    "    assert response.status == 200"
))

story.append(section("Mocking Async Functions"))
story.append(code(
    "from unittest.mock import AsyncMock, patch\n\n"
    "@pytest.mark.asyncio\n"
    "async def test_mock_async():\n"
    "    mock_fetch = AsyncMock(return_value={\"data\": \"test\"})\n\n"
    "    with patch(\"myapp.api.fetch_data\", mock_fetch):\n"
    "        result = await process_data()\n\n"
    "    assert result == {\"data\": \"test\"}\n"
    "    mock_fetch.assert_awaited_once()"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 18 — TESTING CLI
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 18: Testing CLI Applications"))

story.append(section("Testing with Click"))
story.append(code(
    "import click\n"
    "from click.testing import CliRunner\n\n"
    "@click.command()\n"
    "@click.argument(\"name\")\n"
    "def greet(name):\n"
    "    click.echo(f\"Hello, {name}!\")\n\n"
    "def test_greet():\n"
    "    runner = CliRunner()\n"
    "    result = runner.invoke(greet, [\"Alice\"])\n"
    "    assert result.exit_code == 0\n"
    "    assert \"Hello, Alice!\" in result.output"
))

story.append(section("Testing with argparse"))
story.append(code(
    "import sys\n"
    "from io import StringIO\n\n"
    "def test_cli_help(monkeypatch):\n"
    "    monkeypatch.setattr(sys, \"argv\", [\"prog\", \"--help\"])\n"
    "    monkeypatch.setattr(sys, \"stdout\", StringIO())\n\n"
    "    with pytest.raises(SystemExit) as exc:\n"
    "        main()\n"
    "    assert exc.value.code == 0"
))

story.append(section("Testing subprocess Commands"))
story.append(code(
    "import subprocess\n\n"
    "def test_cli_as_subprocess():\n"
    "    result = subprocess.run(\n"
    "        [\"python\", \"-m\", \"myapp\", \"--version\"],\n"
    "        capture_output=True, text=True\n"
    "    )\n"
    "    assert result.returncode == 0\n"
    "    assert \"1.0.0\" in result.stdout"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 19 — TOX & NOX
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 19: tox & nox — Multi-Environment Testing"))

story.append(body(
    "tox and nox run your tests across multiple Python versions and configurations, "
    "ensuring your code works everywhere."
))

story.append(section("tox"))
story.append(code(
    "# tox.ini\n"
    "[tox]\n"
    "envlist = py39, py310, py311, py312\n\n"
    "[testenv]\n"
    "deps = pytest\n"
    "       pytest-cov\n"
    "commands = pytest --cov=mypackage {posargs}\n\n"
    "# Run tox\n"
    "pip install tox\n"
    "tox           # Run all environments\n"
    "tox -e py311  # Run only Python 3.11"
))

story.append(section("nox (Python-based alternative)"))
story.append(code(
    "# noxfile.py\n"
    "import nox\n\n"
    "@nox.session(python=[\"3.9\", \"3.10\", \"3.11\", \"3.12\"])\n"
    "def tests(session):\n"
    "    session.install(\"pytest\", \"pytest-cov\")\n"
    "    session.install(\".\")\n"
    "    session.run(\"pytest\", \"--cov=mypackage\")\n\n"
    "@nox.session\n"
    "def lint(session):\n"
    "    session.install(\"flake8\", \"black\")\n"
    "    session.run(\"flake8\", \"mypackage\")\n"
    "    session.run(\"black\", \"--check\", \"mypackage\")\n\n"
    "# Run nox\n"
    "pip install nox\n"
    "nox             # Run all sessions\n"
    "nox -s tests    # Run only the tests session"
))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 20 — BEST PRACTICES
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 20: Best Practices & Common Pitfalls"))

story.append(section("Best Practices"))

story.append(subsection("1. One Assertion Per Concept"))
story.append(code(
    "# BAD — testing too many things\n"
    "def test_user():\n"
    "    user = create_user(\"Alice\", 30)\n"
    "    assert user.name == \"Alice\"\n"
    "    assert user.age == 30\n"
    "    assert user.is_active\n"
    "    assert user.created_at is not None\n"
    "    assert len(user.permissions) == 0\n\n"
    "# BETTER — focused tests\n"
    "def test_user_has_correct_name():\n"
    "    user = create_user(\"Alice\", 30)\n"
    "    assert user.name == \"Alice\"\n\n"
    "def test_new_user_is_active():\n"
    "    user = create_user(\"Alice\", 30)\n"
    "    assert user.is_active"
))

story.append(subsection("2. Use Descriptive Test Names"))
story.append(code(
    "# BAD\n"
    "def test_calc(): ...\n"
    "def test_1(): ...\n\n"
    "# GOOD\n"
    "def test_discount_applies_20_percent_for_premium_users(): ...\n"
    "def test_login_fails_with_wrong_password(): ..."
))

story.append(subsection("3. Arrange-Act-Assert (AAA) Pattern"))
story.append(code(
    "def test_transfer_funds():\n"
    "    # ARRANGE — set up preconditions\n"
    "    sender = Account(balance=1000)\n"
    "    receiver = Account(balance=500)\n\n"
    "    # ACT — perform the action\n"
    "    transfer(sender, receiver, amount=200)\n\n"
    "    # ASSERT — verify the outcome\n"
    "    assert sender.balance == 800\n"
    "    assert receiver.balance == 700"
))

story.append(subsection("4. Don't Test Implementation Details"))
story.append(code(
    "# BAD — tests break when you refactor internals\n"
    "def test_sort_uses_quicksort():\n"
    "    assert sorter._algorithm == \"quicksort\"\n\n"
    "# GOOD — tests behavior, not implementation\n"
    "def test_sort_returns_ascending_order():\n"
    "    assert sort([3, 1, 2]) == [1, 2, 3]"
))

story.append(subsection("5. Keep Tests Independent"))
story.append(body(
    "Tests must not depend on each other or on execution order. Each test should set up "
    "its own state and clean up after itself."
))

story.append(sp())
story.append(section("Common Pitfalls"))
story.append(sp())
story.append(bullet("<b>Mutable default fixtures</b> — If a fixture returns a mutable object (list, dict), "
                     "tests can accidentally modify it. Use function scope or return a new copy."))
story.append(bullet("<b>Patching the wrong location</b> — Always patch where the name is looked up, "
                     "not where it's defined."))
story.append(bullet("<b>Over-mocking</b> — If you mock everything, you're only testing that your mocks "
                     "work. Let some real code run."))
story.append(bullet("<b>Flaky tests</b> — Tests that sometimes pass and sometimes fail due to timing, "
                     "order-dependence, or shared state. Fix these immediately."))
story.append(bullet("<b>Testing frameworks instead of your code</b> — Don't test that Django's ORM works. "
                     "Test YOUR business logic."))
story.append(bullet("<b>Ignoring test speed</b> — Slow test suites get run less often. Keep unit tests fast "
                     "(&lt;1 second each)."))

story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 21 — CHEAT SHEET
# ═══════════════════════════════════════════════════════════
story.append(title("Chapter 21: Quick Reference Cheat Sheet"))

story.append(section("pytest Commands"))
story.append(code(
    "pytest                          # Run all tests\n"
    "pytest test_file.py             # Run one file\n"
    "pytest test_file.py::test_func  # Run one test\n"
    "pytest -v                       # Verbose output\n"
    "pytest -x                       # Stop on first failure\n"
    "pytest -s                       # Show print output\n"
    "pytest -k \"keyword\"             # Filter by name\n"
    "pytest -m \"marker\"              # Filter by marker\n"
    "pytest --lf                     # Rerun last failures\n"
    "pytest --ff                     # Failures first\n"
    "pytest -n auto                  # Parallel (pytest-xdist)\n"
    "pytest --cov=pkg                # Coverage report\n"
    "pytest --tb=short               # Shorter tracebacks"
))

story.append(section("Essential Fixtures"))
story.append(code(
    "tmp_path        # Temporary directory (pathlib.Path)\n"
    "tmp_path_factory# Create multiple temp dirs\n"
    "capsys          # Capture stdout/stderr\n"
    "caplog          # Capture logging output\n"
    "monkeypatch     # Modify objects/env vars\n"
    "request         # Access fixture metadata"
))

story.append(section("Mock Quick Reference"))
story.append(code(
    "from unittest.mock import Mock, MagicMock, patch, AsyncMock\n\n"
    "m = Mock()                          # Basic mock\n"
    "m = MagicMock()                     # Mock with magic methods\n"
    "m = AsyncMock()                     # Mock for async functions\n"
    "m.method.return_value = 42          # Set return value\n"
    "m.method.side_effect = Exception()  # Raise on call\n"
    "m.method.side_effect = [1, 2, 3]    # Sequential returns\n\n"
    "# Verify calls\n"
    "m.method.assert_called_once()\n"
    "m.method.assert_called_with(arg1, key=val)\n"
    "m.method.assert_not_called()\n"
    "m.method.call_count                 # Number of calls\n"
    "m.method.call_args                  # Last call args\n"
    "m.method.call_args_list             # All call args"
))

story.append(section("Common Decorators"))
story.append(code(
    "@pytest.fixture                     # Define a fixture\n"
    "@pytest.fixture(scope=\"session\")    # Session-scoped fixture\n"
    "@pytest.fixture(autouse=True)       # Auto-applied fixture\n"
    "@pytest.mark.parametrize(...)       # Data-driven tests\n"
    "@pytest.mark.skip(reason=\"...\")     # Skip test\n"
    "@pytest.mark.skipif(cond)           # Conditional skip\n"
    "@pytest.mark.xfail                  # Expected failure\n"
    "@pytest.mark.asyncio                # Async test\n"
    "@patch(\"module.object\")             # Mock decorator"
))

story.append(section("pyproject.toml Configuration"))
story.append(code(
    "[tool.pytest.ini_options]\n"
    "testpaths = [\"tests\"]\n"
    "python_files = [\"test_*.py\"]\n"
    "python_functions = [\"test_*\"]\n"
    "addopts = \"-v --tb=short --strict-markers\"\n"
    "markers = [\n"
    "    \"slow: marks tests as slow\",\n"
    "    \"integration: integration tests\",\n"
    "]\n\n"
    "[tool.coverage.run]\n"
    "source = [\"mypackage\"]\n"
    "omit = [\"tests/*\"]"
))

story.append(Spacer(1, 0.5*inch))
story.append(hr())
story.append(Spacer(1, 12))
story.append(Paragraph(
    "End of Guide — Happy Testing!",
    ParagraphStyle('EndNote', parent=S['CoverSubtitle'], fontSize=13,
                   textColor=HexColor('#16213e'))
))


# ── BUILD PDF ──
doc.build(story)
print(f"PDF generated: {OUTPUT}")

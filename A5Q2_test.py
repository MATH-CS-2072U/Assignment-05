import os
import re
import sys
import subprocess
from pathlib import Path


def test_a5q2_runs_and_reports_correct_error():
    target = Path("A5Q2.py")
    assert target.exists(), "Missing required file: A5Q2.py"

    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"

    result = subprocess.run(
        [sys.executable, str(target)],
        capture_output=True,
        text=True,
        env=env,
        timeout=15,
    )

    if result.returncode != 0:
        raise AssertionError(
            "A5Q2.py crashed.\n"
            f"STDOUT:\n{result.stdout}\n\n"
            f"STDERR:\n{result.stderr}"
        )

    combined_output = result.stdout + "\n" + result.stderr

    match = re.search(
        r"Least squares error is\s+([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)",
        combined_output,
    )

    assert match is not None, (
        "Could not find the required printed line:\n"
        "'Least squares error is <number>.'\n\n"
        f"Actual output was:\n{combined_output}"
    )

    reported_error = float(match.group(1))
    expected_error = 2.4461974110032325e-01

    assert abs(reported_error - expected_error) < 1e-6, (
        f"Incorrect least squares error.\n"
        f"Expected about {expected_error:.12e}, got {reported_error:.12e}.\n\n"
        f"Full output:\n{combined_output}"
    )
"""Tests for templar from CLI, interactive, with an EE, check {{ readme }}."""
import pytest

from tests.integration._interactions import Command
from tests.integration._interactions import UiTestStep
from tests.integration._interactions import add_indices
from tests.integration._interactions import step_id

from .base import BaseClass


CLI = Command(subcommand="collections", execution_environment=True).join()

steps: tuple[UiTestStep, ...] = (
    UiTestStep(
        user_input=CLI,
        comment="ansible-navigator collections",
        present=["ansible.builtin", "ansible.posix"],
    ),
    UiTestStep(
        user_input=":f redhatinsights.insights",
        comment="filter collections",
        present=["redhatinsights.insights"],
    ),
    UiTestStep(
        user_input=":0",
        comment="select redhatinsights.insights",
    ),
    UiTestStep(user_input=":f", comment="unfiltered", present=["compliance"]),
    UiTestStep(user_input=":f compliance", comment="filter content", present=["compliance"]),
    UiTestStep(
        user_input=":0",
        comment="select compliance",
        present=["full_name: redhatinsights.insights.compliance"],
    ),
    UiTestStep(user_input=":{{ readme }}", comment="open readme", present=["OpenSCAP"]),
)

steps = add_indices(steps)


@pytest.mark.parametrize("step", steps, ids=step_id)
class Test(BaseClass):
    """Run the tests for templar from CLI, interactive, with an EE, check {{ readme }}."""

    UPDATE_FIXTURES = False

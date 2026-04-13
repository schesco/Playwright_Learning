# conftest.pyä+#
import os
import pytest


# Steuert Headless/Headed
@pytest.fixture(scope="session")
def browser_type_launch_args():
    running_in_ci = os.getenv("CI") == "true"
    return {"headless": running_in_ci}

# Steuert Videos & Traces
@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "record_video_dir": "videos",
    }
# Traces müssen pro Test gestartet werden
@pytest.fixture(scope="function", autouse=True)
def trace_on(page, context, request):
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    context.tracing.stop(path=f"traces/{request.node.name}.zip")

# Speichert Testergebnis (wichtig für Screenshots)
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        item.rep_call = call

# Screenshot bei Fehler
@pytest.fixture(scope="function", autouse=True)
def record_artifacts(page, request):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png")




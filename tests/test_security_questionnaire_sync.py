import pytest
from security_questionnaire_sync import SecurityQuestionnaireSync, SecurityQuestionnaire

def test_connect_to_api():
    sync = SecurityQuestionnaireSync("https://example.com/api", "api_key")
    assert sync.connect_to_api()

def test_sync_questionnaires():
    sync = SecurityQuestionnaireSync("https://example.com/api", "api_key")
    questionnaires = sync.sync_questionnaires()
    assert questionnaires is not None
    assert len(questionnaires) > 0

def test_handle_errors():
    sync = SecurityQuestionnaireSync("https://example.com/api", "api_key")
    error = Exception("Test error")
    sync.handle_errors(error)

def test_main():
    # Test main function
    import io
    import sys
    capturedOutput = io.StringIO()  # Create StringIO object
    sys.stdout = capturedOutput  # Redirect stdout
    from security_questionnaire_sync import main
    main()  # Call main function
    sys.stdout = sys.__stdout__  # Reset stdout
    assert capturedOutput.getvalue()  # Check if output is not empty

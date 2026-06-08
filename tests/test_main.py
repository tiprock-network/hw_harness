from src.main import hello_message, add_two_numbers

def test_hello_message():
    """This test checks if hello world has been printed out as is, in its lower case."""
    assert hello_message() == "hello world"

def test_add_two_numbers():
    """Test that adds two numbers returns correct sum and type."""
    #Test basic addition
    result = add_two_numbers(4, 6)
    assert isinstance(result, int), f"Expected int, got {type(result).__name__}"
    assert result == 10, f"Expected 10, got {result}"
    
    #Test negative number addition
    assert add_two_numbers(-10, -20) == -30, "Failed for negative numbers"
    
    # Test large numbers
    assert add_two_numbers(1000000, 2000000) == 3000000, "Failed for large numbers"
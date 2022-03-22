# Table 11-1: Assert Methods Available from the unittest Module
#
# Method                        Use
#
# assertEqual(a, b)             Verify that a == b
# assertNotEqual(a, b)          Verify that a != b
# assertTrue(x)                 Verify that x is True
# assertFalse(x)                Verify that x is False
# assertIn(item, list)          Verify that item is in list
# assertNotIn(item, list)       Verify that item is not in list


# A Class to Test
#
# Testing a class is similar to testing a function—much of your work 
# involves testing the behavior of the methods in the class. But there
# are a few differences, so let’s write a class to test. Consider a 
# class that helps administer anonymous surveys:

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.responses.append(new_response)
    
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


<<<<<<< HEAD
#!/usr/bin/python3
''' Defines unittest for console.py'''
import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestAirBnB_CloneConsole(unittest.TestCase):
    ''' Tests the AirBnB_clone console'''
    def test_prompt_present(self):
        '''Test if the prompt is displayed'''
        self.assertEqual("(hbnb)", HBNBCommand.prompt)

    def test_empty_line(self):
        '''Tests if line is empty'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())
    
    ''' Testing help messages of HBNB'''
    def test_help(self):
        ''' Tests if help prints available commands and how to use it'''
        help_message = ("Documented commands (type help <topic>):\n"
                        "========================================\n"
                        "EOF  help  quit")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help_message, output.getvalue().strip())

    def test_help_EOF(self):
        '''Test if help EOF print correct help message'''
        help_message = "exit the program, if end of file"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help_message, output.getvalue().strip())

    def test_help_quit(self):
        '''Test if help quit prints correct help message'''
        help_message = "quit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help_message, output.getvalue().strip())
    
    '''Testing commands'''
    def test_quit(self):
        '''Test if quit is typed in console'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))
    
    def test_EOF(self):
        '''Test if EOF is typed in console'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
        
    
if __name__ == "__main__":
    unittest.main()
=======
#!/usr/bin/python3
''' unittests fot console.py '''

import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand_prompt(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""
    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self):
        message = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(message, output.getvalue().strip())

    def test_help_EOF(self):
        message = "EOF (Ctrl+D) signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(message, output.getvalue().strip())

    def test_help(self):
        display = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(display, output.getvalue().strip())
#

class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
>>>>>>> db0e851ee1e39b4ac3c0695415d5af10df97e9e9

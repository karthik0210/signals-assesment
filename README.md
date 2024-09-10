Topic: Django Signals

Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
--->By default, Django signals are executed synchronously. This means the signal's receiver functions are executed in the same process as the action that triggers the signal.
Output : the signal_receiver function pauses for 5 seconds.


Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
---> Yes, by default, Django signals run in the same thread as the caller. To prove this, we can print out the thread ID of both the caller and the signal receiver.


Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
---> Yes, Django signals are executed in the same database transaction as the caller by default, meaning they can be rolled back if the transaction fails. This can be shown by triggering an error within a signal after a database change and seeing if the change is rolled back.


Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

-->The __init__ method initializes the length and width of the rectangle.
   The __iter__ method is implemented to allow iteration over the instance. It first yields the length as a dictionary and then the width.

**All Task are successfully completed**

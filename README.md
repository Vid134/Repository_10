1. Project Title :
Automation of Drag and Drop Operation Using Selenium WebDriver and PyTest with HTML Reporting

2. Objective of the Project:
The objective of this project is to automate the Drag and Drop functionality available on:
🔗 https://jqueryui.com/droppable/

Using:
Python
Selenium WebDriver
ActionChains
PyTest Framework
HTML Reporting via pytest-html
This project includes both Positive and Negative test cases.

Tools and Technology used:
Tool : Python 3,Selenium WebDriver,ActionChains,PyTest,pytest-html,ChromeDriver,webdriver-manager,PyCharm,GitHub

Purpose : Programming language,Browser automation,Drag-and-drop mouse actions,Test framework,HTML report generation,Automatically downloads driver,
IDE used for writing and running test scripts,Version control and code hosting


5. Test Scenarios
1 Positive Test Case – Successful Drag and Drop
ID and Test Case Description:
TC01 and Verify that the white box can be dragged and dropped into the yellow box

Expected Result:
Text inside yellow box should change to “Dropped!”



2 Negative Test Case – Drag Outside Target Area
ID and Test Case Description:
TC02 and Verify that dropping the white box outside the yellow box does NOT trigger â€œDropped!â€ text

Expected Result:
Text inside the yellow box should NOT change to “Dropped!”.

6. Test Steps (for both cases)
   
Steps for Positive Case:
Launch the browser.
Navigate to https://jqueryui.com/droppable/.
Switch to the iframe containing the drag-and-drop elements.
Identify the draggable element.
Identify the droppable element.
Perform drag_and_drop().
Validate text: "Dropped!".


Steps for Negative Case:
Launch the browser.
Navigate to the same website.
Switch to the iframe.
Locate draggable element.
Perform drag_and_drop_by_offset() with large offset (e.g., 300px).
Validate: text should not contain "Dropped".


 Conclusion:
This project successfully demonstrates:
✔ Automation of drag-and-drop operations

✔ How to design positive & negative test cases

✔ Usage of PyTest fixtures

✔ Generating HTML reports

✔ Uploading project to GitHub as a professional portfolio piece










































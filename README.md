# Google Auto-Suggest Tracker


**Google Auto-Suggest Tracker** is a simple Python script designed to fetch and display Google search suggestions based on a specified keyword. It leverages Google's search suggestion API and presents the results in a structured format on the terminal. This tool is ideal for developers, content creators, or anyone looking to explore trending search terms.

---

## How to Use the Tool
### **Prerequisites**
1. **Python 2.7**  
   This script is written for Python 2.7. If you are using Python 3, minor adjustments may be required.

2. **Required Libraries**  
   Ensure the following libraries are installed:
   - `requests`
   - `beautifulsoup4`
   
   Install them using pip:
   ```bash
   pip install requests beautifulsoup4
   ```

---

### **Usage Steps**
1. **Download or Clone the Script**  
   Save the script with the name `google_suggest_tracker.py`.

2. **Run the Tool**  
   Execute the script using the following command:
   ```bash
   python google_suggest_tracker.py <keyword>
   ```
   Replace `<keyword>` with the search term you want to track. For example:
   ```bash
   python google_suggest_tracker.py technology
   ```

3. **View Suggestions**  
   The tool will display Google’s search suggestions based on the keyword provided.

---

## Features of the Tool
1. **Real-Time Search Suggestions**  
   Fetches live search suggestions directly from Google's API.

2. **Clean and Organized Output**  
   Displays suggestions in a numbered list format in the terminal.

---
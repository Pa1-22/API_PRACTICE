import requests
from flask import Flask, render_template_string

# 1. Initialize the Flask application
app = Flask(__name__)

# --- API Configuration ---
API_URL = "https://jsonplaceholder.typicode.com/todos"

def get_todo_data():
    """Fetches the data from the fake API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        # Return an empty list or an error message if the API call fails
        print(f"Error fetching data: {e}")
        return [{"id": 0, "title": "API FAILED TO LOAD DATA", "completed": False}]


# 2. Define a route (URL path) for your browser
@app.route('/')
def display_todos():
    # Call the function to get the data
    todo_list = get_todo_data()
    
    # 3. Build the HTML output
    html_content = "<h1>API Data Display</h1>"
    html_content += "<p>Data retrieved from " + API_URL + "</p>"
    html_content += "<hr>"
    html_content += "<ul>"
    
    # Loop through the data and create list items for the browser
    for item in todo_list[:10]: # Display only the first 10 items for simplicity
        status = "✅" if item.get('completed') else "⏳"
        
        # Use HTML tags to format the output for the browser
        html_content += f"<li><strong>{status} ID: {item.get('id')}</strong> - {item.get('title')}</li>"
        
    html_content += "</ul>"
    
    # 4. Return the HTML to the browser
    return render_template_string(html_content)

# 5. Run the application
if __name__ == '__main__':
    # Setting debug=True restarts the server automatically on code changes
    app.run(debug=True)
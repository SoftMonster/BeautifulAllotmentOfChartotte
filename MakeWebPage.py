import os

# Specify the filename for the HTML output
output_filename = "index.html"

# Supported image extensions
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')

# Get the current directory
current_directory = os.getcwd()

# Create a list to hold image file paths
image_files = []

# Scan the current directory for image files
for filename in os.listdir(current_directory):
    if filename.lower().endswith(image_extensions):
        image_files.append(filename)

# Generate the HTML content
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Charlotte's Beautiful allotment</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        img {
            margin: 10px;
            max-width: 300px;
            max-height: 300px;
        }
    </style>
</head>
<body>
    <h1>Charlotte's Beautiful allotment</h1>
'''

# Add each image file to the HTML content
for image_file in image_files:
    html_content += f'<img src="{image_file}" alt="{image_file}"><br>\n'

# Close the HTML tags
html_content += '''
</body>
</html>
'''

# Write the HTML content to a file
with open(output_filename, 'w') as f:
    f.write(html_content)

print(f"HTML file '{output_filename}' has been created with {len(image_files)} images.")

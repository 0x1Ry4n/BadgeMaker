# PDF Generation from HTML Templates and CSV

This script allows you to generate PDFs from HTML templates and a CSV file containing the data. It uses the `pdfkit` library to convert the HTML templates into PDF documents.

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/TrilanCo/BadgeMaker.git

2. It is recommended to use a virtual environment to install the dependencies. Create a virtual environment using your preferred tool (e.g., virtualenv, conda), then activate the virtual environment.

3. Install the required dependencies from the requirements.txt file:

   ```shell
   pip install -r requirements.txt

4. Download and install the wkhtmltopdf library. You can find the installation files for your operating system at the following link: https://wkhtmltopdf.org/downloads.html. Make sure to update the path_to_wkhtmltopdf variable in the script (convert.py) with the correct path to the wkhtmltopdf executable.

## Usage

To generate PDFs from your HTML templates and CSV file, follow these steps:

1. Prepare your HTML templates and CSS files. Make sure to include placeholders (e.g., {name}, {job_title}) in the HTML templates that will be replaced with the corresponding values from the CSV file.

2. Create a CSV file with the data you want to populate in the templates. The CSV file should have a header row containing the field names (e.g., name, job_title) and subsequent rows containing the data for each entry.

3. Run the script with the following command:

   ```shell
   python convert.py --html template.html --css styles.css --csv data.csv --page_size A4 --output_dir /output

4. The script will generate PDF files for each entry in the CSV file, using the provided templates and data. The PDF files will be saved in the specified output directory (or the current working directory if not specified).

## Example

1. Create a HTML template with specified keys

   ```html 
   <!DOCTYPE html>
   <html>
      <head>
         <meta charset="utf-8">
         <title>Cracha - Frente</title>
      </head>

      <body>
         <br>
         <div class="badge">
            <div class="image">
                  <img src={img} alt="">
            </div>
            <div class="name">{name}</div>
            <div class="job-title">{job}</div>
         </div>
      </body>
   </html>
   
2. Create a CSS file for the template

   ```css
   body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100%;
   }

   .badge {
      width: 8.5cm;
      height: 5.4cm;
      margin: auto;
      border: 2px solid #333;
      border-radius: 10px;
      padding: 10px;
      text-align: center;
      background-color: #f9f9f9;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
   }

   .badge .image {
      width: 80px;
      height: 80px;
      margin: 0 auto 10px; 
      overflow: hidden;
      border-radius: 50%;
   }

   .badge .image img {
      width: 100%;
      height: 100%;
      object-fit: cover; 
      object-position: center; 
      border-radius: 50%;
   }

   .name {
      font-size: 20px;
      font-weight: bold;
      margin-bottom: 5px;
   }

   .job-title { 
      font-size: 16px;
      color: #888;
   }

3. Create a CSV file with wanted (name, job, img) keys and populate it

4. Finally, run the script with the following command:
   ```shell
   python convert.py --html <filename>.html --css <filename>.css --csv <filename>.csv --page_size A4 --output_dir /output

## Additional Notes
* If you encounter any issues with the PDF generation, ensure that the paths to the HTML templates, CSS files, and the wkhtmltopdf executable are correct.

* For more information on the available options and arguments, you can use the --help option:
   ```shell
   python convert.py --help

* Feel free to customize the HTML templates and CSS files to fit your specific requirements.

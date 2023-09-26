import argparse
import csv
import os
import sys
import pdfkit
import datetime

ZERO_MARGIN = '0.0in'
DEFAULT_PATH_TO_WKHTMLTOPDF = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'


def verify_files_existence(files):
    for file in files:
        if not os.path.isfile(file):
            print(f"File not found: {file}")
            return False
    return True


def verify_html_css_match(html_files, css_files):
    if len(html_files) != len(css_files):
        print("The amount of HTML and CSS files must be the same")
        return False
    return True


def generate_pdf_content(html_files, css_files, line):
    pdf_content = ""
    for i, (html_file, css_file) in enumerate(zip(html_files, css_files)):
        with open(html_file, 'r') as html_file:
            html_content = html_file.read()

        with open(css_file, 'r') as css_file:
            css_content = css_file.read()

        modified_html = html_content.format(**line)
        pdf_content += f'<style>{css_content}</style>\n{modified_html}'

        if i < len(html_files) - 1:
            pdf_content += '<div style="page-break-after:always;"></div>'  # Quebra de página

    return pdf_content


def generate_pdf(wkhtmltopdf_path, html_files, css_files, csv_file, page_size, page_width, page_height, output_dir=None):
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

    if not verify_files_existence(html_files + css_files + [csv_file]):
        return

    if not verify_html_css_match(html_files, css_files):
        return

    with open(csv_file, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        options = {
            'enable-local-file-access': None,
            'page-size': page_size,
            'page-width': f'{page_width}cm',
            'page-height': f'{page_height}cm',
            'margin-top': ZERO_MARGIN,
            'margin-right': ZERO_MARGIN,
            'margin-bottom': ZERO_MARGIN,
            'margin-left': ZERO_MARGIN,
            'no-outline': None
        }

        for line in csv_reader:
            pdf_content = generate_pdf_content(html_files, css_files, line)

            uniq_filename = str(datetime.datetime.now().date(
            )) + '_' + str(datetime.datetime.now().time()).replace(':', '.')

            pdf_name = f"badge_{uniq_filename}.pdf"
            if output_dir:
                pdf_name = os.path.join(output_dir, pdf_name)

            try:
                pdfkit.from_string(
                    input=pdf_content, output_path=pdf_name, configuration=config, options=options)
                print(f"PDF created: {pdf_name}")
            except Exception as e:
                print(f"Failed to create PDF: {str(e)}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate PDFs from HTML templates and CSV file')

    parser.add_argument('--html', nargs='+',
                        help='Paths to HTML template files', required=True)
    parser.add_argument('--css', nargs='+', help='Paths to CSS files', required=True)
    parser.add_argument('--csv', help='Path to the CSV file', required=True)
    parser.add_argument('--page_size', type=str, default='A4',
                        help='Page size. Example: A4, A6')
    parser.add_argument('--width', type=float, default=8.5,
                        help='Page width in cm')
    parser.add_argument('--height', type=float, default=5.4,
                        help='Page height in cm')
    parser.add_argument(
        '--output_dir', help='Output directory for the generated PDFs')
    parser.add_argument(
        '--wkhtmltopdf', default=DEFAULT_PATH_TO_WKHTMLTOPDF, help='Path to the wkhtmltopdf executable')

    args = parser.parse_args()

    html_files = args.html
    css_files = args.css
    csv_file = args.csv
    page_size = args.page_size
    page_width = args.width
    page_height = args.height
    output_dir = args.output_dir
    wkhtmltopdf_path = args.wkhtmltopdf

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        generate_pdf(wkhtmltopdf_path, html_files, css_files, csv_file,
                     page_size, page_width, page_height, output_dir)


if __name__ == '__main__':
    main()

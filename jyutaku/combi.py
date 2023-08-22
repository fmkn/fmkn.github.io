#output_file = "c[調査員番号]"
#
#with open(output_file, "w") as output:
#    for file_name in ["[調査区A].html", "[調査区B].html", "[調査区C].html"]:
#        with open(file_name, "r") as input_file:
#            output.write(input_file.read())

import csv

def combine_html(output_filename, input_filenames):
    with open(output_filename, "w") as output:
        for file_name in input_filenames:
            with open(file_name, "r") as input_file:
                output.write(input_file.read())

def main():
    with open("input.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Read the header row

        for row in reader:
            output_file = row[0]
            input_files = row[1:]
            input_files = [file_name for file_name in input_files if file_name]  # Remove empty cells
            combine_html(output_file, input_files)
            print(f"HTML files combined to {output_file} successfully!")

if __name__ == "__main__":
    main()

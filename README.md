# Subdomain Scanner

Subdomain Scanner is a Python tool that scans for subdomains using all possible combinations of alphanumeric characters. It sends a HEAD request to each subdomain to check if it's alive, and if so, records the HTTP response code.

## Usage

To use Subdomain Scanner, you need to have Python 3 installed. You also need to install the `requests` module by running the following command:



Once you have the dependencies installed, you can run the tool by executing the `sub.py` file. This will scan for all possible three-letter combinations of alphanumeric characters on the domain `example.com`, and write the results to a file called `subdomains.txt`. You can change the domain by editing the `subdomain` variable in the script.

## Output

The output of the tool is a text file called `subdomains.txt`, which contains a list of all alive subdomains and their HTTP response codes, in the format `<subdomain> (<response code>)`.

Note that scanning for subdomains in this way may be considered unethical or even illegal, depending on the circumstances. Make sure you have permission from the domain owner before using this tool.

## License

This tool is licensed under the MIT License. See the LICENSE file for details.

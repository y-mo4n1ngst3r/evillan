import json
import csv

def save_payloads(payloads, output_file, output_format):
    """
    Save payloads to a file in the specified format.
    :param payloads: List of tuples (payload, methods).
    :param output_file: Path to the output file.
    :param output_format: Output format (txt, json, csv, markdown).
    """
    if output_format == "txt":
        save_as_txt(payloads, output_file)
    elif output_format == "json":
        save_as_json(payloads, output_file)
    elif output_format == "csv":
        save_as_csv(payloads, output_file)
    elif output_format == "markdown":
        save_as_markdown(payloads, output_file)
    else:
        print("Unsupported format. Defaulting to plain text.")
        save_as_txt(payloads, output_file)

def save_as_txt(payloads, output_file):
    """Save payloads as plain text."""
    with open(output_file, "w") as file:
        for payload, methods in payloads:
            file.write(f"{payload}\n")
           # file.write(f"Methods: {', '.join(methods)}\n\n")
    print(f"Payloads saved to {output_file} (txt).")

def save_as_json(payloads, output_file):
    """Save payloads as JSON."""
    data = [{"payload": payload} for payload in payloads]
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Payloads saved to {output_file} (json).")

def save_as_csv(payloads, output_file):
    """Save payloads as CSV."""
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Payload"])
        for payload in payloads:
            writer.writerow([payload])
    print(f"Payloads saved to {output_file} (csv).")

def save_as_markdown(payloads, output_file):
    """Save payloads as Markdown."""
    with open(output_file, "w") as file:
        file.write("# Encoded Payloads\n\n")
        for payload, methods in payloads:
            file.write(f"## Payload\n")
            file.write(f"```\n{payload}\n```\n")
            #file.write(f"### Methods\n")
            #file.write(f"- {'\n- '.join(methods)}\n\n")
    print(f"Payloads saved to {output_file} (markdown).")

def extract_parameters(text):
    lines = text.split("\n")

    result = {}

    for line in lines:
        if "Jenkins Job" in line:
            result["job_name"] = line.split(":")[1].strip()

        if "Environment" in line:
            result["environment"] = line.split(":")[1].strip()

        if "Branch" in line:
            result["branch"] = line.split(":")[1].strip()

    return result


input_text = """
Jenkins Job: CustomerPortal_Build
Environment: UAT
Branch: main
"""

output = extract_parameters(input_text)


# print("Input text : ", input_text)
# print("Output text : ", output)

print(output)